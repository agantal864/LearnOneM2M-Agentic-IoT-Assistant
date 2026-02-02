import chromadb
from chromadb.utils import embedding_functions

# --- Configuration ---
# Use the SAME settings as your ingestion script
CHROMA_PATH = "../chroma_db"
COLLECTION_NAME = "acmeCSEcode"
EMBEDDING_MODEL = "jinaai/jina-embeddings-v2-base-code"

def runQueryTests():
    """Connects to ChromaDB and runs a series of test queries."""
    print("Initializing ChromaDB client and connecting to collection...")
    try:
        client = chromadb.PersistentClient(path=CHROMA_PATH)
        embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name=EMBEDDING_MODEL, 
            trust_remote_code=True
        )
        collection = client.get_collection(name=COLLECTION_NAME, embedding_function=embedding_func)
        print(f"Successfully connected to collection: '{COLLECTION_NAME}'")
    except Exception as e:
        print(f"Error connecting to ChromaDB: {e}")
        print("Please ensure you have run the ingestion script first and the collection exists.")
        return

    # Define a list of test queries
    test_queries = [
        "Find the implementation logic for creating a 'cnt' resource and check for any specific name validation for 'rn' (resourceName)",
    ]

    print("\n" + "="*50)
    print("Running query tests...")
    print("="*50 + "\n")

    for query in test_queries:
        print(f"--- Query: '{query}' ---")
        
        # Perform the search
        # n_results specifies how many top matches to return
        results = collection.query(
            query_texts=[query],
            n_results=2  # Get the top 2 most relevant chunks
        )
        
        # Check if any results were found
        if not results['ids'][0]:
            print("No results found.\n")
            continue

        # Display the results
        # results['ids'], results['documents'], and results['metadatas'] are lists of lists
        # We only sent one query, so we access the first element [0]
        for i in range(len(results['ids'][0])):
            doc_id = results['ids'][0][i]
            distance = results['distances'][0][i]  # Lower distance means higher similarity
            metadata = results['metadatas'][0][i]
            document = results['documents'][0][i]
            
            print(f"\nResult {i+1}:")
            print(f"  - Distance: {distance:.4f}")
            print(f"  - Source: {metadata.get('source', 'N/A')}")
            print(f"  - Class: {metadata.get('class_name', 'N/A')}")
            print(f"  - Function: {metadata.get('function_name', 'N/A')}")
            print("  - Full Code Snippet:")
            # Print the ENTIRE document
            print("    " + "\n    ".join(document.splitlines()))
            print("-" * 20)
        
        print("\n" + "-"*50 + "\n")


if __name__ == "__main__":
    runQueryTests()