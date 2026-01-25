from dataclasses import dataclass

import chromadb
from chromadb.utils import embedding_functions

from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.agents.middleware import dynamic_prompt, ModelRequest


# @dataclass
# class Context:
#     userLevel: str 

# @dynamic_prompt
# def dynamic_prompt(request: ModelRequest) -> str: 
#     userLevel = request.runtime.context.userLevel


#  Setup ChromaDB Connection 
client = chromadb.PersistentClient(path="./chroma_db")
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="BAAI/bge-small-en-v1.5"
)
collection = client.get_or_create_collection(
    name="onem2mKnowledge", 
    embedding_function=embedding_func
)

# Retriever Tool
@tool('retrieve_onem2m_info', description='Searches the oneM2M dictionary, technical specifications, ACME documentations, and ACME implementation code.')
def retrieve_onem2m_info(query: str) -> str:
    results = collection.query(query_texts=[query], n_results=10)
    formatted_results = []
    for i in range(len(results['documents'][0])):
        content = results['documents'][0][i]
        meta = results['metadatas'][0][i]
        
        # Extract metadata from the vectorized logic
        source = meta.get('source', 'Unknown')
        dtype = meta.get('type', 'general')
        cat = meta.get('category', 'misc')
        
        # Build a structured string for the LLM to read
        formatted_results.append(
            f"--- DATA BLOCK {i+1} ---\n"
            f"TYPE: {dtype}\n"
            f"CATEGORY: {cat}\n"
            f"SOURCE: {source}\n"
            f"CONTENT: {content}"
        )
    
    return "\n\n".join(formatted_results)

prompt = """ You are LearnOneM2M, a specialized AI tutor for the oneM2M IoT standard.
    Your goal is to explain concepts by combining theory (Specifications) with examples (code).

    Rules for your response:
    1. Check for 'dictionary' type blocks first to provide a concise definition.
    2. Use 'specification' type blocks to explain formal rules and technical attributes.
    3. Use 'implementation_docs' type blocks to explain ACME implementation documentation
    5. The 'implementation_code' type blocks is the ACME CSE implementation codebase. So when you provide ONEM2M REST code examples, try to infer the logic or reverse engineer from the 'implementation_code' type blocks 
    7. Cite your sources clearly at the end of each section (e.g., 'Source: TS-0001' or 'Source: AE.py').

    CRITICAL RULES: 
    1. If a specific data type (like implementation_code) is missing from the search results,
    simply state that you don't have a code example available rather than making one up.
    """

model = ChatOllama(model="gpt-oss:20b", temperature=0)

oneM2MAgent = create_agent(
    model,
    tools=[retrieve_onem2m_info],
    system_prompt=prompt,
)

result = oneM2MAgent.invoke(
    {"messages": [{"role": "user", "content": "How do I implement an AE?"}]}
)
for i, msg in enumerate(result["messages"]):
    msg.pretty_print()