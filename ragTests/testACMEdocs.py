import chromadb
from chromadb.utils import embedding_functions

# --- Configuration ---
# IMPORTANT: Use the SAME settings as your ingestion script
CHROMA_PATH = "../chroma_db"
COLLECTION_NAME = "acmeDocs"
EMBEDDING_MODEL = "nomic-ai/nomic-embed-text-v1.5"

def runQueryTests():
    """Connects to ChromaDB and runs a series of test queries on the documentation."""
    print("Initializing ChromaDB client and connecting to the 'acmeDocs' collection...")
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
        print("Please ensure you have run the documentation ingestion script first and the collection exists.")
        return

    # Define a list of test queries relevant to the ACME documentation
    test_queries = [
        "how to setup certificates",
        "what is ACME script",
        "run ACME with docker",
        "raspberry pi installation",
        "how to contribute to the project"
    ]

    print("\n" + "="*50)
    print("Running documentation query tests...")
    print("="*50 + "\n")

    for query in test_queries:
        print(f"--- Query: '{query}' ---")
        
        # Perform the search
        results = collection.query(
            query_texts=[query],
            n_results=2  # Get the top 2 most relevant chunks
        )
        
        # Check if any results were found
        if not results['ids'][0]:
            print("No results found.\n")
            continue

        # Display the results
        for i in range(len(results['ids'][0])):
            doc_id = results['ids'][0][i]
            distance = results['distances'][0][i]
            metadata = results['metadatas'][0][i]
            document = results['documents'][0][i]
            
            print(f"\nResult {i+1}:")
            print(f"  - Distance: {distance:.4f}")
            print(f"  - Source: {metadata.get('source', 'N/A')}")
            # This is the key metadata for docs!
            print(f"  - Section: {metadata.get('Header 1', 'N/A')} > {metadata.get('Header 2', 'N/A')}")
            print("  - Text Snippet:")
            # Print just the first few lines for readability
            print("    " + "\n    ".join(document.splitlines()[:5]))
            if len(document.splitlines()) > 5:
                print("    ...")
        
        print("\n" + "-"*50 + "\n")


if __name__ == "__main__":
    runQueryTests()