import os
# Schema
from pydantic import BaseModel, Field
from typing import List
# Langchain
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document
# Langchain text splitter
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
# Chroma DB and embeddings
import chromadb
from chromadb.utils import embedding_functions

MODEL = "llama3.1:latest" 

summaryPrompt = ChatPromptTemplate.from_template(
    "You are an expert technical writer. Summarize the following text from a technical specification. "
    "The summary must be concise, factual, and retain key technical terms, acronyms, and mappings. "
    "Do not add any information that is not present in the text.\n\n"
    "TEXT:\n{parentText}\n\n"
    "SUMMARY:"
)

keywordPrompt = ChatPromptTemplate.from_template(
    "Extract a list of the most important technical terms, acronyms, parameter names, and resource types from the following text. "
    "TEXT:\n{chunkText}\n\n"
    "KEYWORDS:"
)

# Structured LLM output Schema
class KeywordMetadata(BaseModel):
    keywords: List[str] = Field(..., description="Important technical terms, acronyms, parameter names, and resource types")

class ParentSummaryMetadata(BaseModel):
    summary: str =  Field(..., description="Summarized parent text")

# Initialize LLM with model config
def initialize_llm_and_chains(model: str):
    """Initializes the LLM and structured output chains once."""
    
    # Initialize LLM
    llm = ChatOllama(model=model, temperature=0, num_predict=4096, num_ctx=8192)
    keywordsLlmStructuredOutput = llm.with_structured_output(KeywordMetadata)
    parentSummaryLlmStructuredOutput = llm.with_structured_output(ParentSummaryMetadata)
    
    # Chain prompts with their corresponding structured output schema
    summaryChain = summaryPrompt | parentSummaryLlmStructuredOutput
    keywordChain = keywordPrompt | keywordsLlmStructuredOutput
    
    return summaryChain, keywordChain

def textSplitAndRefine(filePath, summaryChain, keywordChain):
    """Split markdown text by headers + Refining with LLM"""

    # Read .md file
    with open(filePath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Markdown header text splitting
    headersToSplitOn = [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3")]
    markdownSplitter = MarkdownHeaderTextSplitter(headers_to_split_on=headersToSplitOn)
    # Markdown splitter 
    mdHeaderSplits = markdownSplitter.split_text(content)
    #  Recursive Splitter for smaller chunks
    textSplitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=200)
    # Do recursive chunking for child chunks for every parent chunk (parentDoc)
    
    # Chunks processing and refining metadata with llm
    finalSplits = []
    globalChunkIndex = 0
    for parentDoc in mdHeaderSplits:
        # Used to generate parent summary metadata for every child chunk using the model
        try:
            if len(parentDoc.page_content) > 100:
                parentSummary = summaryChain.invoke({"parentText": parentDoc.page_content})
            else:
                parentSummary = ParentSummaryMetadata(summary=parentDoc.page_content)
        except Exception as e:
            print(f"Could not generate summary for {parentDoc.metadata}: {e}")
            parentSummary = ParentSummaryMetadata(summary="")
        # Split the parent document into smaller recursive chunks
        childChunks = textSplitter.split_text(parentDoc.page_content)
        # Refine child chunks
        for chunk in childChunks:
            try:
                # Used to generate keywords metadata for every child chunk using the model
                keywords = keywordChain.invoke({"chunkText": chunk})
            except Exception as e:
                print(f"Could not generate keywords for a chunk in {parentDoc.metadata}: {e}")
                keywords = KeywordMetadata(keywords=[])
            # add unique id for every child chunks (used for upserting to chroma collections)
            docId = f"{os.path.basename(filePath)}_chunk_{globalChunkIndex}"
            globalChunkIndex += 1
            # Append the two new metadata along with the current metadata
            finalDoc = Document(
                page_content=chunk,
                metadata= {
                    # Unpack original metadata
                    **parentDoc.metadata,  
                    "parentSummary": parentSummary.summary,
                    "keywords": ", ".join(keywords.keywords),
                    "source": os.path.basename(filePath)
                }
            )
            finalSplits.append((docId, finalDoc))
    print(f"Created {len(finalSplits)} enriched chunks using model {MODEL}.")
    return finalSplits

if __name__ == "__main__":
    specificationsDir = "rawData/specifications"
    
    # Initialize LLM and chains
    summaryChain, keywordChain = initialize_llm_and_chains(MODEL)

    # Initialize Chroma db and embedding function
    oneM2Mspecs = "oneM2MSpecsv3"
    client = chromadb.PersistentClient(path="./chroma_db")
    # Using nomic-embed-text (Optimized for technical retrieval)
    embeddingFunc = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="nomic-ai/nomic-embed-text-v1.5", trust_remote_code=True)
    
    files = [f for f in os.listdir(specificationsDir) if f.endswith('.md')]
    print(f"Found {len(files)} files to process.")

    # Batch Processing
    specsCollection = []
    for fileName in files:
        fullPath = os.path.join(specificationsDir, fileName)
        print(f"\n--- Processing {fileName} ---")
        try:
            refinedData = textSplitAndRefine(fullPath, summaryChain, keywordChain)
            specsCollection.extend(refinedData)
        except Exception as e:
            # Catch file-specific errors without stopping the whole batch
            print(f"FAILED to process {fileName}. Error: {e}. Skipping to next file.")
            continue
    
        print("\n" + "="*50)
        print(f"Batch processing complete.")
        print(f"Total enriched chunks created across all files: {len(specsCollection)}")
        print("="*50)

    if specsCollection:
        try:
            client.delete_collection(oneM2Mspecs)
        except:
            pass

        print("\nEmbedding and indexing documents into vector store...")
        collection = client.get_or_create_collection(name=oneM2Mspecs, embedding_function=embeddingFunc)

        print(f"Vectorizing data and saving to {collection} collection")

        uniqueSpecs = {}
        for docId, docObj in specsCollection:
            uniqueSpecs[docId] = docObj

        print(f"Total unique chunks to upload: {len(uniqueSpecs)}")

        # initialize unique ids, documents, and metadatas to be inserted to chromadB
        ids = list(uniqueSpecs.keys())
        documents = [f"search_document: {doc.page_content}" for doc in uniqueSpecs.values()]
        metadatas = [doc.metadata for doc in uniqueSpecs.values()]

        # 3. Upsert in batches
        batchSize = 100 
        for i in range(0, len(ids), batchSize):
            collection.upsert(
                documents=documents[i : i + batchSize],
                metadatas=metadatas[i : i + batchSize],
                ids=ids[i : i + batchSize]
            )
            print(f"Upserted batch {i//batchSize + 1}...")

    print(f"Successfully added {len(documents)} documents to the collection.")
    print("="*50)