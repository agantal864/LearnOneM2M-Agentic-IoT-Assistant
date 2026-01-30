import os
import chromadb
from chromadb.utils import embedding_functions
from langchain_core.documents import Document
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter


API_GUIDE_FILE = "rawData/specifications/tr/TR-0051-oneM2M_API_guide-V3_0_0.md"

def processApiGuideSimple(filePath):
    """Processes a single API guide markdown file quickly, without LLM calls."""
    with open(filePath, 'r', encoding='utf-8') as f:
        content = f.read()

    allDocsWithIds = []
    globalChunkIndex = 0

    # Headers to split on for metadata
    headersToSplitOn = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
        ("####", "Header 4"),
    ]
    markdownSplitter = MarkdownHeaderTextSplitter(headers_to_split_on=headersToSplitOn)
    textSplitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)

    print(f"Starting to process API guide: {os.path.basename(filePath)}\n")
    
    # Split by headers first to get context
    mdHeaderSplits = markdownSplitter.split_text(content)
    
    # Then split each section into smaller chunks
    for parentDoc in mdHeaderSplits:
        childChunks = textSplitter.split_text(parentDoc.page_content)
        for chunk in childChunks:
            # Create a stable and unique ID
            safeIdPrefix = os.path.basename(filePath).replace('.', '_')
            docId = f"{safeIdPrefix}_chunk_{globalChunkIndex}"
            globalChunkIndex += 1
            
            # Assemble final metadata
            metadata = {
                "source": os.path.basename(filePath),
                "language": "markdown",
                # Unpack the header metadata from the markdown splitter
                **parentDoc.metadata 
            }

            doc = Document(page_content=chunk, metadata=metadata)
            allDocsWithIds.append((docId, doc))
            
    return allDocsWithIds

if __name__ == "__main__":
    # Process the single API guide file
    docsWithIds = processApiGuideSimple(API_GUIDE_FILE)

    if not docsWithIds:
        print("\nNo documents were processed. Exiting.")
    else:
        print(f"\n" + "="*50)
        print(f"API Guide processing complete. Found {len(docsWithIds)} chunks.")
        print("="*50)


        # Initialize ChromaDB              
        print("\nConnecting to ChromaDB...")
        collectioName = "oneM2MApiGuide"
        client = chromadb.PersistentClient(path="./chroma_db")
        embeddingFunc = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="nomic-ai/nomic-embed-text-v1.5", 
            trust_remote_code=True
        )
        collection = client.get_or_create_collection(name=collectioName, embedding_function=embeddingFunc)

        # Prepare data for upsert
        ids = [item[0] for item in docsWithIds]
        documents = [item[1].page_content for item in docsWithIds]
        metadatas = [item[1].metadata for item in docsWithIds]

        # Upsert to ChromaDB
        print(f"Upserting {len(documents)} documents to collection '{collectioName}'...")
        collection.upsert(
            ids=ids,
            documents=documents,
            metadatas=metadatas
        )
        
        print(f"Successfully upserted documents to '{collectioName}'.")
        print("API Guide ingestion is complete.")
        print("="*50)