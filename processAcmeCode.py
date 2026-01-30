import os
import ast
import chromadb
from chromadb.utils import embedding_functions
from langchain_core.documents import Document
from langchain_text_splitters import PythonCodeTextSplitter


CODE_DIR = "rawData/implementations/acmeCode"

def extractMetadataFromChunk(codeChunk):
    """ Parses a Python code chunk to extract class and function names."""
    try:
        tree = ast.parse(codeChunk)
        className = None
        functionName = None

        for node in ast.walk(tree):
            # We are looking for top-level definitions within this chunk
            if isinstance(node, ast.ClassDef):
                className = node.name
                # If we find a class, we can stop looking for a top-level function
                break 
            elif isinstance(node, ast.FunctionDef) and not functionName:
                functionName = node.name
        
        return {
            "class_name": className, # Keep metadata keys consistent for DB queries
            "function_name": functionName,
        }
    except (SyntaxError, ValueError):
        # The chunk might not be valid Python on its own (e.g., it's just a part of a function)
        return {
            "class_name": None,
            "function_name": None,
        }

def processCodebase(rootDir):
    """Walks a directory, processes all .py files, and returns a list of Document objects."""

    allDocsWithIds = []
    splitter = PythonCodeTextSplitter(chunk_size=1000, chunk_overlap=100)

    print(f"Starting to process codebase in: {rootDir}\n")
    for subdir, _, files in os.walk(rootDir):
        for fileName in files:
            if fileName.endswith(".py"):
                filePath = os.path.join(subdir, fileName)
                relativePath = os.path.relpath(filePath, rootDir)
                print(f"--- Processing {relativePath} ---")

                try:
                    with open(filePath, 'r', encoding='utf-8') as f:
                        codeContent = f.read()
                    
                    # Split the code into logical chunks
                    chunks = splitter.split_text(codeContent)

                    for i, chunk in enumerate(chunks):
                        # Extract rich metadata using AST
                        astMetadata = extractMetadataFromChunk(chunk)
                        
                        # Create a stable and unique ID
                        safeIdPrefix = relativePath.replace(os.sep, '_')
                        docId = f"{safeIdPrefix}_chunk_{i}"

                        # Assemble final metadata
                        metadata = {
                            "source": relativePath,
                            "filename": fileName,
                            "directory": os.path.basename(subdir),
                            "language": "python",
                            **astMetadata # Unpack className and functionName
                        }

                        doc = Document(page_content=chunk, metadata=metadata)
                        allDocsWithIds.append((docId, doc))

                except Exception as e:
                    print(f"  FAILED to process {relativePath}. Error: {e}. Skipping.")
                    continue

    return allDocsWithIds

if __name__ == "__main__":
    # Process the codebase
    docsWithIds = processCodebase(CODE_DIR)

    if not docsWithIds:
        print("\nNo Python documents were processed. Exiting.")
    else:
        print(f"\n" + "="*50)
        print(f"Code processing complete. Found {len(docsWithIds)} code chunks.")
        print("="*50)

        # Initialize ChromaDB
        collectionName = "acmeCSEcode"
        print("\nConnecting to ChromaDB...")
        client = chromadb.PersistentClient(path="./chroma_db")
        embeddingFunc = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="jinaai/jina-embeddings-v2-base-code", trust_remote_code=True)
        collection = client.get_or_create_collection(name=collectionName, embedding_function=embeddingFunc)

        # Prepare data for upsert
        ids = [item[0] for item in docsWithIds]
        documents = [item[1].page_content for item in docsWithIds]
        metadatas = [item[1].metadata for item in docsWithIds]

        # Upsert to ChromaDB
        print(f"Upserting {len(documents)} documents to collection '{collectionName}'...")
        collection.upsert(
            ids=ids,
            documents=documents,
            metadatas=metadatas
        )
        
        print(f"Successfully upserted documents to '{collectionName}'.")
        print("Code ingestion is complete.")
        print("="*50)