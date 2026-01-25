import os
import json
import uuid
import time
from langchain_ollama import ChatOllama
from langchain_text_splitters import MarkdownHeaderTextSplitter
import chromadb
from chromadb.utils import embedding_functions

# --- CONFIGURATION ---
CHROMA_PATH = "./chroma_db"
COLLECTION_NAME = "onem2m_specs"
MODEL_NAME = "llama3.2" 

VALID_TYPES = [
    "concept", "resource_type_info", "short_names", 
    "mandatory_attributes", "optional_attributes", 
    "procedures", "behavior", "constraints", 
    "security", "relationship", "example_payload"
]

# --- SETUP CHROMA ---
client = chromadb.PersistentClient(path=CHROMA_PATH)
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="BAAI/bge-small-en-v1.5"
)
spec_coll = client.get_or_create_collection(COLLECTION_NAME, embedding_function=embedding_func)

# JSON format enforcement is key for llama3.2
llm = ChatOllama(model=MODEL_NAME, temperature=0)

def refine_section_with_llm(text_content, metadata):
    """Passes a markdown section to the LLM to extract Q&A chunks."""
    if len(text_content.strip()) < 30:
        return []

    prompt = f"""
        You are a technical oneM2M expert. Analyze this section from the HTTP Protocol Binding spec: {metadata}
        
        TASK:
        Extract facts and turn them into Question/Answer pairs. 
        Each chunk must be one of these types: {VALID_TYPES}.

        REQUIREMENTS:
        - If the text is just a table of contents or references, return an empty list: []
        - If you find technical rules (e.g., "X-M2M-RI header is mandatory"), create a chunk.
        - Respond ONLY with a valid JSON list of objects.

        EXAMPLE FORMAT:
        [
            {{"q": "How is the Request-ID mapped in HTTP?", "a": "The Request-ID is mapped to the X-M2M-RI header.", "type": "mandatory_attributes"}}
        ]

        TEXT TO ANALYZE:
        {text_content}
        """
    try:
        response_msg = llm.invoke(prompt)
        content = response_msg.content.strip()
        
        if not content:
            return []

        # Find the JSON boundaries
        start = content.find('[')
        end = content.rfind(']') + 1
        
        if start == -1 or end == 0:
            return []

        data = json.loads(content[start:end])
        return data if isinstance(data, list) else []
    except Exception as e:
        print(f"  ⚠️ Skipping section {metadata} due to parsing error: {e}")
        return []

def run_refinery_pipeline(file_path):
    print(f"--- Starting Refinery for {file_path} ---")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    headers = [("#", "H1"), ("##", "H2"), ("###", "H3")]
    splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers)
    sections = splitter.split_text(content)
    
    refined_output = []
    staging_file = f"refined_{os.path.basename(file_path)}.json"

    for i, section in enumerate(sections):
        meta_label = section.metadata if section.metadata else "General"
        print(f"Processing Section {i+1}/{len(sections)}: {meta_label}")
        
        chunks = refine_section_with_llm(section.page_content, meta_label)
        
        if isinstance(chunks, list):
            for chunk in chunks:
                # 🛡️ THE FIX: Guard against non-dictionary items (like stray ints)
                if isinstance(chunk, dict) and all(k in chunk for k in ("q", "a", "type")):
                    chunk['source'] = os.path.basename(file_path)
                    chunk['section_meta'] = str(meta_label)
                    refined_output.append(chunk)
        
        # Periodic "Save Progress" to avoid total data loss on crash
        if i % 5 == 0:
            with open(staging_file, 'w', encoding='utf-8') as f:
                json.dump(refined_output, f, indent=2)

    with open(staging_file, 'w', encoding='utf-8') as f:
        json.dump(refined_output, f, indent=2)
    
    print(f"--- Refinement Complete. Saved {len(refined_output)} chunks to {staging_file} ---")
    return staging_file

def load_to_chroma(json_file):
    """Loads the refined JSON into ChromaDB."""
    if not json_file or not os.path.exists(json_file):
        return

    print(f"--- Loading {json_file} into ChromaDB ---")
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if not data:
        print("No valid data found to load.")
        return

    docs, metas, ids = [], [], []
    
    for item in data:
        docs.append(item['a']) 
        metas.append({
            "question": item['q'],
            "chunkType": item['type'],
            "source": item['source'],
            "hierarchy": item.get('section_meta', '')
        })
        ids.append(str(uuid.uuid4()))
    
    # Split into smaller batches for ChromaDB stability
    batch_size = 100
    for i in range(0, len(docs), batch_size):
        spec_coll.upsert(
            documents=docs[i:i + batch_size],
            metadatas=metas[i:i + batch_size],
            ids=ids[i:i + batch_size]
        )
        
    print(f"Successfully loaded {len(docs)} high-quality chunks.")

if __name__ == "__main__":
    target_spec = "rawData/specifications/TS-0009-HTTP_Protocol_Binding-V3_9_1(cl).md"
    
    if os.path.exists(target_spec):
        staging_path = run_refinery_pipeline(target_spec)
        load_to_chroma(staging_path)
    else:
        print(f"Error: {target_spec} not found.")