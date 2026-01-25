import chromadb
import requests
from pydantic import BaseModel, Field
from chromadb.utils import embedding_functions
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage, RemoveMessage
from langgraph.graph import MessagesState, StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode
import json
from typing import Literal

# --- 1. State Definition ---
class AgentState(MessagesState):
    summary: str
    context: str 

class OneM2MRequestSchema(BaseModel):
    # Removing long descriptions helps Llama 3.2 focus on the keys
    method: str = Field(description="GET, POST, PUT, or DELETE")
    url: str = Field(description="The target URL")
    origin: str = Field(description="The X-M2M-Origin ID")
    body: dict = Field(default=None, description="The oneM2M JSON body")

def router_intent(state: AgentState) -> Literal["retrieve", "professor"]:
    """TASK 5.2: Decides if we need the PDF Library or just the Professor."""
    last_msg = state["messages"][-1].content.lower()
    
    # If the user is giving a command or technical request, skip retrieval
    action_keywords = ["register", "create", "check", "post", "get", "delete", "server", "http", "call"]
    if any(kw in last_msg for kw in action_keywords):
        return "professor"
    return "retrieve"

# --- 2. Tool Definition ---
@tool(args_schema=OneM2MRequestSchema)
def execute_onem2m_request(method, url, origin, body=None):
    """
    Executes a real oneM2M REST request. 
    """
    method = method.upper()

    # 1. Handle stringified body if LLM sends it as a string
    if isinstance(body, str):
        try:
            body = json.loads(body)
        except:
            pass

    # 2. Extract 'ty' and SANITIZE body (Crucial for ACME)
    # ACME errors if 'ty' or 'description' are inside the JSON body
    target_ty = None
    if isinstance(body, dict):
        # Determine ty before we delete it from the body
        if "m2m:ae" in body:
            target_ty = 2
        else:
            target_ty = body.get("ty")
            
        # Remove non-oneM2M attributes that cause 400 errors
        body.pop("ty", None)
        body.pop("type", None)
        body.pop("description", None)

    print(f"\n[TOOL EXECUTION] {method} | URL: {url} | Origin: {origin}")
    
    # 3. Setup Base Headers
    headers = {
        "X-M2M-Origin": origin,
        "X-M2M-RI": "req_" + str(requests.utils.quote(url[-5:])),
        "X-M2M-RVI": "3",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    # 4. Handle Resource Type (ty) logic for POST headers
    if method == "POST" and target_ty:
        headers["Content-Type"] = f"application/json;ty={target_ty}"

    try:
        # Use requests.request to handle all methods cleanly
        response = requests.request(
            method=method, 
            url=url, 
            headers=headers, 
            json=body if method in ["POST", "PUT"] else None, 
            timeout=5
        )
        
        clean_body = response.text[:500] + "..." if len(response.text) > 500 else response.text
        return f"Status: {response.status_code}\nBody: {clean_body}"
    
    except Exception as e:
        return f"Connection Failed: {str(e)}"

# --- 3. Node Functions ---
def filter_node(state: AgentState):
    messages = state["messages"]
    if len(messages) > 20: 
        summary = state.get("summary", "")
        prompt = f"Summarize this oneM2M conversation: {summary}\n\nRecent context: {messages[:-5]}"
        response = llm.invoke(prompt)
        delete_messages = [RemoveMessage(id=m.id) for m in messages[:-5]]
        return {"summary": response.content, "messages": delete_messages}
    return {}

def retrieve_node(state: AgentState):
    last_msg = state["messages"][-1].content
    results = collection.query(query_texts=[last_msg], n_results=5)
    context = "\n".join(results['documents'][0])
    return {"context": context}

def professor_node(state: AgentState):
    summary = state.get("summary", "")
    context = state.get("context", "")
    messages = state["messages"]

    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a Senior oneM2M Expert.
            
            ### CORE RULES ###
            1. Use 'execute_onem2m_request' for ALL server tasks.
            2. For POST/PUT: The 'body' must ONLY contain the oneM2M resource key (e.g., {{"m2m:ae": ...}}).
            3. CRITICAL: Never include "type": "object" or "description" in your tool calls.
            4. If you call a tool, output ONLY the tool call. No preamble.

            ### EXAMPLES ###
            - Valid Body: {{"m2m:ae": {{"rn": "MyAE", "api": "N-001", "srv": ["3"]}}}}
            - Resource Type (ty): AE=2, Container=3, ContentInstance=4.

            KNOWLEDGE: {context}
            SUMMARY: {summary}"""),
        ("placeholder", "{messages}")
    ])
    chain = prompt | llm_with_tools
    result = chain.invoke({"summary": summary, "context": context, "messages": messages})
    return {"messages": [result]}

def should_continue(state: AgentState):
    messages = state["messages"]
    last_message = messages[-1]
    
    # Check if the model explicitly called a tool
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"
    
    # FALLBACK: If the LLM just wrote the JSON in text (common with smaller models)
    if "execute_onem2m_request" in last_message.content:
        print("\n[DEBUG] LLM mentioned tool in text but didn't trigger it. Check prompt.")
        
    return END

# --- 4. Setup & Graph Construction ---
client = chromadb.PersistentClient(path="./chroma_db")
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="BAAI/bge-small-en-v1.5")
collection = client.get_or_create_collection(name="onem2mKnowledge", embedding_function=embedding_func)

llm = ChatOllama(model="gpt-oss:20b", temperature=0)
tools = [execute_onem2m_request]
llm_with_tools = llm.bind_tools(tools)
tool_node = ToolNode(tools)

workflow = StateGraph(AgentState)
workflow.add_node("filter", filter_node)
workflow.add_node("retrieve", retrieve_node)
workflow.add_node("professor", professor_node)
workflow.add_node("tools", tool_node)

workflow.add_edge(START, "filter")

# Use conditional logic to skip retrieval for actions
workflow.add_conditional_edges(
    "filter", 
    router_intent, 
    {
        "retrieve": "retrieve", 
        "professor": "professor"
    }
)

workflow.add_edge("retrieve", "professor")
workflow.add_conditional_edges("professor", should_continue)
workflow.add_edge("tools", "professor")

checkpointer = MemorySaver()
professor_agent = workflow.compile(checkpointer=checkpointer)