import chromadb
from chromadb.utils import embedding_functions
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# 1. Connect to your local Vector Database
client = chromadb.PersistentClient(path="./chroma_db")
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="BAAI/bge-small-en-v1.5"
)
collection = client.get_or_create_collection(name="onem2mKnowledge", embedding_function=embedding_func)

# 2. Setup Ollama with Llama 3.2
# We set temperature to 0 for maximum coding accuracy (no "creativity")
llm = ChatOllama(model="llama3.2", temperature=0)

def ask_agent(query):
    # Retrieve the top 10 most relevant chunks from your oneM2M files
    results = collection.query(query_texts=[query], n_results=10)
    context = "\n".join(results['documents'][0])
    
    # 3. The "Strict Developer" Prompt
    # This forces the LLM to follow the oneM2M XSD rules found in your TS files
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a Senior oneM2M Protocol Engineer. 
        Your task is to provide valid, executable Python code for a student.
        
        CRITICAL RULES:
        - Resource Type (ty): Registration of an AE MUST use 'ty': 2.
        - JSON Structure: Attributes like 'rn' (Resource Name) and 'api' (App ID) must stay INSIDE the 'm2m:ae' dictionary.
        - Headers: Only use standard oneM2M headers: 'X-M2M-Origin', 'X-M2M-RI', 'Content-Type'.
        - URL: The endpoint should be the CSE's base path (e.g., http://localhost:8080/cse-in).
        
        If the provided context contains specific examples from 'testAE.py' or 'oneM2MRecipes.md', prioritize that syntax.
        
        CONTEXT:
        {context}"""),
        ("human", "{question}")
    ])

    # Build the chain
    chain = prompt | llm
    response = chain.invoke({"context": context, "question": query})
    return response.content

# --- EXECUTION ---
query = "Professor, don't use the internal 'acme' library. Write a standard Python script using 'import requests' that an external developer would use. I want to see the exact URL, the headers, and the JSON for registering 'MyWeatherApp' to a CSE running at localhost:8080."
print(f"🚀 Querying the oneM2M Knowledge Base...")
print("-" * 30)

answer = ask_agent(query)

print("\n🤖 AUTHORITATIVE RESPONSE:")
print(answer)