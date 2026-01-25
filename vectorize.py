import os
import json
import chromadb
from chromadb.utils import embedding_functions

# --- SETUP ---
client = chromadb.PersistentClient(path="./chroma_db")

# Using BGE-Small (Optimized for technical retrieval)
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="BAAI/bge-small-en-v1.5"
)

client.delete_collection("onem2mKnowledge")
collection = client.get_or_create_collection(
    name="onem2mKnowledge", 
    embedding_function=embedding_func
)

def chunk_text(text, chunk_size=1000, overlap=100):
    """Slices text into overlapping parts for better context retention."""
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunk = text[i:i + chunk_size]
        if chunk:
            chunks.append(chunk)
    return chunks

def process_files(base_path): 
    # Valid extensions for folders (Dictionary .json is handled separately)
    valid_text_extensions = ('.md', '.py', '.ini', '.as')
    
    for root, _, files in os.walk(base_path):
        root_lower = root.lower()
        
        for file in files:
            file_path = os.path.join(root, file)
            
            # The Dictionary (Nested JSON) 
            if file == "onem2m_dictionary.json":
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    dict_docs, dict_metas, dict_ids = [], [], []
                    
                    # Flatten the nested JSON structure
                    for category, mappings in data.items():
                        for key, value in mappings.items():
                            # Create a descriptive string for the LLM
                            entry_text = f"Term: {key} | Category: {category} | Definition: {value}"
                            
                            dict_docs.append(entry_text)
                            dict_metas.append({
                                "source": file,
                                "type": "dictionary",
                                "category": category,
                                "key": key
                            })
                            dict_ids.append(f"dict_{category}_{key}")
                    
                    collection.upsert(
                        documents=dict_docs, 
                        metadatas=dict_metas, 
                        ids=dict_ids
                    )
                    print(f"Indexed Dictionary: {len(dict_docs)} terms")
                except Exception as e:
                    print(f"Error processing dictionary: {e}")

            # REGULAR CASE: Specs & Implementations
            elif file.lower().endswith(valid_text_extensions):
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    if not content.strip():
                        continue

                    # Labeling logic based on folder hierarchy
                    if "specifications" in root_lower:
                        doc_type = "specification"
                    elif "acme" in root_lower:
                        doc_type = "implementation_docs"
                    elif "acmecode" in root_lower:
                        doc_type = "implementation_code"
                    else:
                        doc_type = "general_info"

                    chunks = chunk_text(content)
                    documents, metadatas, ids = [], [], []
                    
                    for i, chunk in enumerate(chunks):
                        documents.append(chunk)
                        metadatas.append({
                            "source": file,
                            "path": file_path,
                            "category": os.path.basename(root),
                            "type": doc_type
                        })
                        ids.append(f"{file}_chunk_{i}")
                    
                    collection.upsert(
                        documents=documents,
                        metadatas=metadatas,
                        ids=ids
                    )
                    print(f"Indexed {file}: {len(chunks)} chunks ({doc_type})")
                except Exception as e:
                    print(f"Error processing {file}: {e}")

    print("\n LearnOneM2M Database Built Successfully!")

if __name__ == "__main__":
    # Ensure you are running this from the root where 'rawData' folder exists
    basePath = "rawData"
    if os.path.exists(basePath):
        process_files(basePath)
    else:
        print(f"Error: Folder '{basePath}' not found.")