import os
import chromadb
from chromadb.utils import embedding_functions
from langchain_core.documents import Document
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter


DOCS_DIR = "rawData/implementations/acme"

def processMarkdownDocs(rootDir):
    """Walks a directory, processes all .md files, and returns a list of Document objects."""
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
    # Adjusted chunk size for prose/text
    textSplitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)

    print(f"Starting to process documentation in: {rootDir}\n")
    for subdir, _, files in os.walk(rootDir):
        for fileName in files:
            if fileName.endswith(".md"):
                filePath = os.path.join(subdir, fileName)
                relativePath = os.path.relpath(filePath, rootDir)
                print(f"--- Processing {relativePath} ---")

                try:
                    with open(filePath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Split by headers first to get context
                    mdHeaderSplits = markdownSplitter.split_text(content)
                    
                    # Then split each section into smaller chunks
                    for parentDoc in mdHeaderSplits:
                        childChunks = textSplitter.split_text(parentDoc.page_content)
                        for chunk in childChunks:
                            # Create a stable and unique ID
                            safeIdPrefix = relativePath.replace(os.sep, '_')
                            docId = f"{safeIdPrefix}_chunk_{globalChunkIndex}" # <-- USE GLOBAL COUNTER
                            globalChunkIndex += 1
                            
                            # Assemble final metadata
                            metadata = {
                                "source": relativePath,
                                "filename": fileName,
                                "directory": os.path.basename(subdir),
                                "language": "markdown",
                                # Unpack the header metadata from the markdown splitter
                                **parentDoc.metadata 
                            }

                            doc = Document(page_content=chunk, metadata=metadata)
                            allDocsWithIds.append((docId, doc))

                except Exception as e:
                    print(f"  FAILED to process {relativePath}. Error: {e}. Skipping.")
                    continue

    return allDocsWithIds

if __name__ == "__main__":
    # Process the documentation
    docsWithIds = processMarkdownDocs(DOCS_DIR)

    if not docsWithIds:
        print("\nNo markdown documents were processed. Exiting.")
    else:
        print(f"\n" + "="*50)
        print(f"Documentation processing complete. Found {len(docsWithIds)} chunks.")
        print("="*50)

        # Initialize ChromaDB
        print("\nConnecting to ChromaDB...")
        collectionName = "acmeDocs"
        client = chromadb.PersistentClient(path="./chroma_db")
        embeddingFunc = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="nomic-ai/nomic-embed-text-v1.5", trust_remote_code=True)
        collection = client.get_or_create_collection(name=collectionName, embedding_function=embeddingFunc)

        # Prepare data for upsert
        ids = [item[0] for item in docsWithIds]
        documents = [f"search_document: {item[1].page_content}" for item in docsWithIds]
        metadatas = [item[1].metadata for item in docsWithIds]

        # Upsert to ChromaDB
        print(f"Upserting {len(documents)} documents to collection '{collectionName}'...")
        collection.upsert(
            ids=ids,
            documents=documents,
            metadatas=metadatas
        )
        
        print(f"Successfully upserted documents to '{collectionName}'.")
        print("Documentation ingestion is complete.")
        print("="*50)