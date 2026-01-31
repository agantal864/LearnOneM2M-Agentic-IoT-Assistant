import uuid
import requests
from typing import Annotated, Literal, Optional, Dict, Any
from typing_extensions import TypedDict
import operator
# langchain 
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.tools import tool
# chroma
import chromadb
from chromadb.utils import embedding_functions

from rank_bm25 import BM25Okapi
import re

from pydantic import BaseModel, Field, field_validator
from langgraph.graph import StateGraph, START, END
from langgraph.types import Send


CHROMA_PATH = "./chroma_db"
TS_COLLECTION = "oneM2MSpecsv3"
TR_COLLECTION = "oneM2MApiGuide"
DOCS_COLLECTION = "acmeDocs"
CODE_COLLECTION = "acmeCSEcode"

DEFAULT_BASE_URL = "http://localhost:5000/~/id-in/cse-in"
DEFAULT_ORIGIN = "CArt"

OllamaModel = ChatOllama(model="gpt-oss:20b", temperature=0)
# Initialize Chroma and embedding function
client = chromadb.PersistentClient(path=CHROMA_PATH)
embeddingFunc = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="nomic-ai/nomic-embed-text-v1.5", trust_remote_code=True)
codeembeddingFunc = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="jinaai/jina-embeddings-v2-base-code", trust_remote_code=True)
tsCollection = client.get_collection(name=TS_COLLECTION, embedding_function=embeddingFunc)
trCollection = client.get_collection(name=TR_COLLECTION, embedding_function=embeddingFunc)
docsCollection = client.get_collection(name=DOCS_COLLECTION, embedding_function=embeddingFunc)
codeCollection = client.get_collection(name=CODE_COLLECTION, embedding_function=codeembeddingFunc)


class AgentInput(TypedDict):
    """Simple input state for each subagent."""
    query: str

class AgentOutput(TypedDict):
    """Output from each subagent."""
    source: str
    result: str

class Classification(TypedDict):
    """A single routing decision: which agent to call with what query."""
    source: Literal["oneM2MStandards", "oneM2MACMEDocs", "oneM2MACMECodebase"]
    query: str

class RouterState(TypedDict):
    query: str
    classifications: list[Classification]
    results: Annotated[list[AgentOutput], operator.add]  # Reducer collects parallel results
    final_answer: str

class OneM2MRequestInput(BaseModel):
    method: Optional[str] = Field(default="GET", description="HTTP method (GET, POST, PUT, DELETE). Defaults to GET.")
    url: Optional[str] = Field(default=DEFAULT_BASE_URL, description="Target oneM2M resource URL. Defaults to IN-CSE base URL.")
    origin: Optional[str] = Field(default=DEFAULT_ORIGIN,description="X-M2M-Origin. Defaults to CArt.")
    resource_type: Optional[int] = Field(default=None, description="oneM2M resource type (ty). Inferred if missing.")
    payload: Optional[Dict[str, Any]] = Field(default=None, description="oneM2M JSON payload. Auto-generated if missing.")

    @field_validator("method")
    def normalize_method(cls, v):
        return v.upper()

class HybridRetriever:
    def __init__(self, collection, k=60):
        self.collection = collection
        self.k = k  # Constant for RRF
        
        # Load all data for BM25 and Metadata mapping
        data = self.collection.get()
        self.documents = data['documents']
        self.metadatas = data['metadatas']
        
        # Performance Optimization: O(1) lookup for metadata instead of O(N) .index()
        self.docToMetadata = {doc: meta for doc, meta in zip(self.documents, self.metadatas)}
        
        # Build Keyword Index (BM25)
        tokenizedCorpus = [self._tokenize(doc) for doc in self.documents]
        self.bm25 = BM25Okapi(tokenizedCorpus)

    def _tokenize(self, text):
        return re.sub(r'[^\w\s]', '', text.lower()).split()

    def search(self, query, nResults=5, filterDict=None):
        # 1. Semantic Search
        vectorResponse = self.collection.query(
            query_texts=[f"search_query: {query}"], 
            n_results=nResults * 3,
            where=filterDict
        )
        
        resultMap = {} # Stores {text: {"score": float, "metadata": dict}}

        # Process Vector Hits
        if vectorResponse['documents']:
            for rank, doc in enumerate(vectorResponse['documents'][0]):
                meta = vectorResponse['metadatas'][0][rank]
                if doc not in resultMap:
                    resultMap[doc] = {"score": 0, "metadata": meta}
                resultMap[doc]["score"] += 1 / (self.k + rank)
        
        # 2. Keyword Search
        tokenizedQuery = self._tokenize(query)
        bm25Docs = self.bm25.get_top_n(tokenizedQuery, self.documents, n=nResults * 3)

        # Process BM25 Hits
        for rank, doc in enumerate(bm25Docs):
            if doc not in resultMap:
                # Optimized lookup
                meta = self.docToMetadata.get(doc, {})
                resultMap[doc] = {"score": 0, "metadata": meta}
            resultMap[doc]["score"] += 1 / (self.k + rank)

        # 3. Sort by RRF Score and Format
        sortedResults = sorted(resultMap.items(), key=lambda x: x[1]['score'], reverse=True)
        
        finalStrings = []
        for doc, data in sortedResults[:nResults]:
            metaHeader = " | ".join([f"{k}: {v}" for k, v in data['metadata'].items()])
            finalStrings.append(f"[METADATA] {metaHeader}\n[CONTENT] {doc}")

        return finalStrings

# Global initialization
tsRetriever = HybridRetriever(tsCollection)
trRetriever = HybridRetriever(trCollection)
acmeDocsRetriever = HybridRetriever(docsCollection)
acmeCodebaseRetriever = HybridRetriever(codeCollection)

@tool
def searchOneM2MTs(query: str, sourceFilter: str = None) -> str:
    """
    Searches official oneM2M Technical Specifications (TS). 
    Use this for normative rules, mandatory attributes, and resource definitions.
    Optional: use sourceFilter (e.g., 'ts-0001') to narrow down documents.
    """
    fDict = {"source": {"$eq": sourceFilter}} if sourceFilter else None
    results = tsRetriever.search(query, nResults=5, filterDict=fDict)
    return "\n\n---\n\n".join(results)

@tool
def searchOneM2MTr(query: str) -> str:
    """
    Searches oneM2M Technical Reports (TR) and API Guides. 
    Use this for implementation examples, flow diagrams, and protocol bindings.
    """
    results = trRetriever.search(query, nResults=5)
    return "\n\n---\n\n".join(results)

@tool
def searchAcmeDocs(query: str) -> str:
    """
    Searches the ACME oneM2M CSE implementation documentation.
    Use this tool to answer questions about ACME oneM2M CSE implementation (e.g., configurations).
    """
    results = acmeDocsRetriever.search(query, nResults=3)
    return "\n\n---\n\n".join(results)

@tool 
def searchAcmeCodeBase(query: str) -> str:
    """Searches the ACME CSE source code for concrete implementations, function signatures, and class definitions.
    Use this to find specific examples of how features in OneM2M ACME CSE are implemented in Python."""
    results = acmeCodebaseRetriever.search(query, nResults=5)
    return "\n\n---\n\n".join(results)

@tool(args_schema=OneM2MRequestInput)
def oneM2MExecuteRest(method: str, url: str, origin: str, resource_type: int = None, payload: dict = None):
    """
    Executes a real-time oneM2M REST call. Use this ONLY after 
    the parameters have been validated against the standards.
    """
    headers = {
        "X-M2M-Origin": origin,
        "X-M2M-RI": "req_" + str(uuid.uuid4()),
        "X-M2M-RVI": "3",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    # logic specifically for oneM2M POST
    if method.upper() == "POST":
        headers["Content-Type"] = f"application/json;ty={resource_type}" 

    try:
        response = requests.request(
            method=method.upper(), 
            url=url, 
            headers=headers, 
            json=payload, 
            timeout=10
        )
        return {
            "statusCode": response.status_code,
            "body": response.json() if response.status_code != 204 else "Success (No Content)",
            "usedHeaders": headers
        }
    except Exception as e:
        return f"executionError: {str(e)}"


oneM2MStandardsAgent = create_agent(
    OllamaModel,
    tools=[searchOneM2MTs, searchOneM2MTr],
    system_prompt=(
        """You are a oneM2M Standards Technical Expert.
        Answer questions about technical specifications and technical reports of the oneM2M standard.
        """
    )
)

acmeDocsAgent = create_agent(
    OllamaModel,
    tools=[searchAcmeDocs],
    system_prompt=(
        """You are a oneM2M ACME CSE expert.
        Answer questions about documentations related to the oneM2M ACME CSE implementation. 
        """
    )
)

acmeCodeAgent = create_agent(
    OllamaModel,
    tools=[searchAcmeCodeBase],
    system_prompt=(
        """ You are a oneM2M ACME CSE developer.
        Provide a python code related to how oneM2M ACME CSE implements its core functionality.
        """
    )
)

class ClassificationResult(BaseModel):  
    """Result of classifying a user query into agent-specific sub-questions."""
    classifications: list[Classification] = Field(
        description="List of agents to invoke with their targeted sub-questions"
    )

def classify_query(state: RouterState) -> dict:
    """Classify query and determine which agents to invoke."""
    structured_llm = OllamaModel.with_structured_output(ClassificationResult)  

    result = structured_llm.invoke([
        {
            "role": "system",
            "content": """Analyze this query and determine which knowledge bases to consult.
            For each relevant source, generate a targeted sub-question optimized for that source.

            Available sources:
            - oneM2MStandards: Consult for normative rules, technical specifications (TS), and technical reports (TR). 
            Use for questions about mandatory attributes, resource definitions (e.g., <container>, <AE>), and standard protocol flows.
            
            - oneM2MACMEDocs: Consult for the ACME CSE implementation documentation. 
            Use for questions about ACME CSE-specific behavior and its configuration.
            
            - oneM2MACMECodebase: Consult for the actual Python source code of the ACME CSE. 
            Use for questions requiring concrete implementation details, function signatures, class definitions, and Python code examples of how oneM2M features are built in ACME. You can infer from the code on how to implement the user request.


            Return ONLY the sources that are relevant to the query. Each source should have
            a targeted sub-question optimized for that specific knowledge domain.

            MANDATORY PROTOCOL:
            1. If the user asks for code examples, you MUST invoke oneM2MACMEDocs for ACME configuration, invoke oneM2MACMECodebase to infer from the codebase, and invoke oneM2MStandards for validation.
            2. Treat the query as multi-part: Part A (Standard definition), Part B (ACME implementation)."""
        },
        {"role": "user", "content": state["query"]}
    ])

    return {"classifications": result.classifications}

def route_to_agents(state: RouterState) -> list[Send]:
    """Fan out to agents based on classifications."""
    return [
        Send(c["source"], {"query": c["query"]})  
        for c in state["classifications"]
    ]

def query_standards(state: AgentInput) -> dict:
    """Query the oneM2MStandards agent."""
    result = oneM2MStandardsAgent.invoke({
        "messages": [{"role": "user", "content": state["query"]}]  
    })
    return {"results": [{"source": "oneM2MStandards", "result": result["messages"][-1].content}]}

def query_docs(state: AgentInput) -> dict:
    """Query the acmeDocs agent."""
    result = acmeDocsAgent.invoke({
        "messages": [{"role": "user", "content": state["query"]}]  
    })
    print("test query_docs: ", result)
    return {"results": [{"source": "oneM2MACMEDocs", "result": result["messages"][-1].content}]}

def query_codebase(state: AgentInput) -> dict:
    """Query the acmeCode agent."""
    result = acmeCodeAgent.invoke({
        "messages": [{"role": "user", "content": state["query"]}]  
    })
    print("test query_docs: ", result)
    return {"results": [{"source": "oneM2MACMECodebase", "result": result["messages"][-1].content}]}

def createoneM2MRest(state: RouterState) -> dict:
    """
    Synthesizes research into a proposed JSON payload and parameters.
    Does NOT execute the REST call yet.
    """
    structuredLlm = OllamaModel.with_structured_output(OneM2MRequestInput)
    researchFindings = "\n".join([r['result'] for r in state["results"]])
    
    # LLM builds the ideal request based on findings
    prompt = f"""
    USER INTENT: {state['query']}
    KNOWLEDGE CONTEXT:
    {researchFindings}  
    TASK:
    Generate the precise oneM2M HTTP parameters. You must follow these protocol rules:
    1. OPERATION MAPPING:
        - If creating: Use POST, define 'resource_type' (ty), and wrap payload in 'm2m:<shortName>'.
        - If fetching: Use GET. No payload.
        - If updating: Use PUT. Payload should only contain attributes being changed.
        - If deleting: Use DELETE. No payload.
    2. TARGETING (To):
        - Use the structured path: '{DEFAULT_BASE_URL}'.
        - If the user targets a specific sub-resource, append the 'rn' (resourceName) to the URL.
    3. RESOURCE IDENTIFICATION:
        - Match the 'ty' (int) and 'm2m root key' based on Standards (e.g., AE=2, Container=3, ContentInstance=4, Subscription=23).
    4. ATTRIBUTE VALIDATION:
        - Use 'camelCase' for all attributes (e.g., 'resourceName', 'maxNrOfInstances').
        - Include mandatory attributes found in research (e.g., 'api' and 'rr' for AE; 'pc' for notifications).
    Generate the OneM2MRequestInput now.
    """
    proposedParams = structuredLlm.invoke(prompt)
    # Return the proposal to the results list
    return {"results": [{"source": "proposalEngine", "result": proposedParams.model_dump()}]}

def validateOneM2MRest(state: RouterState) -> dict:
    # 1. Retrieve the actual data dictionary
    proposal = next((r['result'] for r in state["results"] if r['source'] == "proposalEngine"), None)
    
    if not proposal:
        return {"results": [{"source": "executionEngine", "result": "Error: No proposal generated."}]}

    # 2. Context from research
    context = "\n".join([r['result'] for r in state["results"] if r['source'] not in ["proposalEngine", "executionEngine"]])

    # 3. Dynamic Validation
    validationPrompt = f"""
        You are a oneM2M ACME CSE Protocol Validator. 
        Verify the Proposed Request: {proposal}
        Against the discovered Research Findings: {context}

        VALIDATION RULES:
        1. MANDATORY ATTRIBUTES: Identify the resource type (ty) from the proposal. 
        Cross-reference with the Research Findings to ensure all mandatory attributes 
        for that specific type are present in the payload.
        2. ROOT KEY MATCH: Ensure the JSON root key (e.g., m2m:ae, m2m:cnt, m2m:sub) 
        matches the resource type (ty) indicated in the headers.
        3. HIERARCHY: Ensure the parent resource in the URL can logically host the 
        child resource being created.
        4. ADDRESSING: The URL must follow the ACME structured format: ~/id-in/cse-in/

        If all rules are met, respond 'VALID'.
        If any are missing, respond 'REJECTED: [Specific oneM2M attribute or rule violated]'.
        """
    validationResponse = OllamaModel.invoke(validationPrompt).content

    if "REJECTED" in validationResponse.upper():
        # This triggers the loopback in continueExecution
        return {"results": [{"source": "executionEngine", "result": validationResponse}]}

    # 4. Validated -> Execute
    # We pass the dictionary directly to the tool
    executionResult = oneM2MExecuteRest.invoke(proposal) 

    return {"results": [{"source": "executionEngine", "result": str(executionResult)}]}

def continueExecution(state: RouterState) -> Literal["execute_action", "synthesize"]:
    """
    Checks the last result in the state. If it contains a rejection,
    it sends the agent back to the drawing board.
    """
    lastResult = state["results"][-1]["result"]
    if "REJECTED" in lastResult or "Error" in lastResult:
        # You might want to limit the number of retries to avoid infinite loops
        return "createoneM2MRest"
    return "synthesize"

def synthesizeResults(state: RouterState) -> dict:
    """Consolidates validation steps and execution results into a step-by-step report."""

    if not state["results"]:
        return {"final_answer": "No information or execution results were gathered."}

    # Format results for synthesis
    formattedResults = []
    for r in state["results"]:
        sourceName = r['source'].replace("oneM2M", "").title()
        formattedResults.append(f"### Findings from {sourceName}:\n{r['result']}")
    synthesisPrompt = [
            {
                "role": "system",
                "content": f"""You are a Technical Architect reporting on a oneM2M operation.
                Query: "{state['query']}"

                YOUR TASK:
                1. Summarize the validation steps (what the Standards, ACME Docs, and ACME Codebase agents found).
                2. Present the final execution result from the 'ExecutionEngine'.
                3. Provide the specific Python code or JSON payload used for the successful call.
                
                STRUCTURE YOUR RESPONSE AS FOLLOWS:
                ## 1. Validation Phase
                Explain what rules were checked (e.g., mandatory attributes for the resource type).
                
                ## 2. Execution Phase
                Detail the HTTP method, URL, Payload, and the outcome (Status Code).
                
                ## 3. Steps Taken
                Use a numbered list to show the logic: 
                1. Identified resource type.
                2. Verified headers.
                3. Constructed payload.
                4. Executed REST call.

                STYLE:
                - Use camelCase for all oneM2M attributes.
                - Use Markdown code blocks for JSON/Python.
                """
            },
            {"role": "user", "content": "\n\n".join(formattedResults)}
        ]
    finalResponse = OllamaModel.invoke(synthesisPrompt)
    return {"final_answer": finalResponse.content}

workflow = (
    StateGraph(RouterState)
    .add_node("classify", classify_query)
    .add_node("oneM2MStandards", query_standards)
    .add_node("oneM2MACMEDocs", query_docs)
    .add_node("oneM2MACMECodebase", query_codebase)
    .add_node("createoneM2MRest", createoneM2MRest)
    .add_node("validateOneM2MRest", validateOneM2MRest)
    .add_node("synthesize", synthesizeResults)

    .add_edge(START, "classify")
    .add_conditional_edges("classify", route_to_agents, ["oneM2MStandards", "oneM2MACMEDocs", "oneM2MACMECodebase"])
    .add_edge(["oneM2MStandards", "oneM2MACMEDocs", "oneM2MACMECodebase"], "createoneM2MRest")
    .add_edge("createoneM2MRest", "validateOneM2MRest")
    .add_conditional_edges(
        "validateOneM2MRest", 
        continueExecution, 
        {
            "createoneM2MRest": "createoneM2MRest", # Loop back to fix errors
            "synthesize": "synthesize"           # Proceed to final report
        }
    )
    .add_edge("synthesize", END)
    .compile()
)

result = workflow.invoke({
    "query": "Create an AE with api = Nzis"
})

print("Original query:", result["query"])
print("\nClassifications:")
for c in result["classifications"]:
    print(f"  {c['source']}: {c['query']}")
print("\n" + "=" * 60 + "\n")
print("Final Answer:")
print(result["final_answer"])


