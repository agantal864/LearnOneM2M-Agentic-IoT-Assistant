from typing import Annotated, Literal
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

from pydantic import BaseModel, Field
from langgraph.graph import StateGraph, START, END
from langgraph.types import Send

CHROMA_PATH = "./chroma_db"
OllamaModel = ChatOllama(model="llama3.1:latest", temperature=0)
TS_COLLECTION = "oneM2MSpecsv3"
TR_COLLECTION = "oneM2MApiGuide"
DOCS_COLLECTION = "acmeDocs"
CODE_COLLECTION = "acmeCSEcode"

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
    Use this tool to answer questions about ACME oneM2M CSE implementation (e.g., CSE behavior, configuration, supported oneM2M features, limitations, defaults, etc.).
    """
    results = acmeDocsRetriever.search(query, nResults=3)
    return "\n\n---\n\n".join(results)

@tool 
def searchAcmeCodeBase(query: str) -> str:
    """Searches the ACME CSE source code for concrete implementations, function signatures, and class definitions.
    Use this to find specific examples of how features in OneM2M ACME CSE are implemented in Python."""
    results = acmeCodebaseRetriever.search(query, nResults=5)
    return "\n\n---\n\n".join(results)

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
            Use for questions about CSE-specific behavior, configuration settings, supported features, limitations, and default values in the ACME environment.
            
            - oneM2MACMECodebase: Consult for the actual Python source code of the ACME CSE. 
            Use for questions requiring concrete implementation details, function signatures, class definitions, and Python code examples of how oneM2M features are built in ACME.


            Return ONLY the sources that are relevant to the query. Each source should have
            a targeted sub-question optimized for that specific knowledge domain.

            MANDATORY PROTOCOL:
            1. If the user asks 'how to do X in ACME', you MUST invoke BOTH oneM2MStandards AND oneM2MACMEDocs.
            2. If the user asks for code examples, you MUST invoke oneM2MACMECodebase.
            3. Treat the query as multi-part: Part A (Standard definition), Part B (ACME implementation)."""
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

def synthesize_results(state: RouterState) -> dict:
    """Combine results from all agents into a coherent answer."""
    if not state["results"]:
        return {"final_answer": "No results found from any knowledge source."}

    # Format results for synthesis
    formatted = [
        f"**From {r['source'].title()}:**\n{r['result']}"
        for r in state["results"]
    ]

    synthesis_response = OllamaModel.invoke([
        {
            "role": "system",
            "content": f"""You are a Technical Architect synthesizing information for the query: "{state['query']}"

            GOALS:
            1. Consolidate standard definitions (from oneM2M) with implementation details (from ACME).
            2. If Python code or JSON examples are provided, include them in proper Markdown code blocks.
            3. Use clear headings (e.g., ## Standard Definition, ## ACME Implementation).
            4. If there is a conflict between the standard and the implementation, highlight it as a 'Note'.
            
            STYLE:
            - Professional, concise, and scannable.
            - Use camelCase for attribute names as per oneM2M convention.
            """
        },
        {"role": "user", "content": "\n\n".join(formatted)}
    ])

    return {"final_answer": synthesis_response.content}

workflow = (
    StateGraph(RouterState)
    .add_node("classify", classify_query)
    .add_node("oneM2MStandards", query_standards)
    .add_node("oneM2MACMEDocs", query_docs)
    .add_node("oneM2MACMECodebase", query_codebase)
    .add_node("synthesize", synthesize_results)
    .add_edge(START, "classify")
    .add_conditional_edges("classify", route_to_agents, ["oneM2MStandards", "oneM2MACMEDocs", "oneM2MACMECodebase"])
    .add_edge("oneM2MStandards", "synthesize")
    .add_edge("oneM2MACMEDocs", "synthesize")
    .add_edge("oneM2MACMECodebase", "synthesize")
    .add_edge("synthesize", END)
    .compile()
)

result = workflow.invoke({
    "query": "What is a container in oneM2M? how do i create one in ACME?"
})

print("Original query:", result["query"])
print("\nClassifications:")
for c in result["classifications"]:
    print(f"  {c['source']}: {c['query']}")
print("\n" + "=" * 60 + "\n")
print("Final Answer:")
print(result["final_answer"])


