import chromadb
from chromadb.utils import embedding_functions

# 1. Connect to your new database
client = chromadb.PersistentClient(path="../chroma_db")

# 2. Setup the SAME embedding function
embedding = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="BAAI/bge-small-en-v1.5"
)

# 3. Get the collection
collection = client.get_or_create_collection(
    name="onem2mKnowledge", 
    embedding_function=embedding
)

# Test a technical question
query = "What is ty?"

results = collection.query(
    query_texts=[query],
    # Find top 10 best matches
    n_results=10  
)

print(f"\n🔍 Query: {query}")
print("=" * 60)

for i in range(len(results['documents'][0])):
    source = results['metadatas'][0][i]['source']
    distance = results['distances'][0][i]
    content = results['documents'][0][i]
    
    print(f"MATCH {i+1} | Source: {source} | Distance: {distance:.4f}")
    print(f"Content snippet: {content[:300]}...") 
    print("-" * 60)