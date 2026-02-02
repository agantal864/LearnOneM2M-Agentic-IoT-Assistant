
# Regex
import re
# Langchain
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.tools import tool
# Chroma & embeddings
import chromadb
from chromadb.utils import embedding_functions
# Bm25
from rank_bm25 import BM25Okapi

CHROMA_PATH = "./chroma_db"
TS_COLLECTION = "oneM2MSpecsv3"
TR_COLLECTION = "oneM2MApiGuide"
DOCS_COLLECTION = "acmeDocs"
CODE_COLLECTION = "acmeCSEcode"

# Initialize Model, chromadB, and embeddings
agentModel = ChatOllama(model="gpt-oss:20b", temperature=0, repeat_penalty=1.2, top_k=10)
client = chromadb.PersistentClient(path=CHROMA_PATH)
nomicEmbedding = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="nomic-ai/nomic-embed-text-v1.5", trust_remote_code=True)
jinaEmbedding = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="jinaai/jina-embeddings-v2-base-code", trust_remote_code=True)

# Data Collections
tsCollection = client.get_collection(name = TS_COLLECTION, embedding_function=nomicEmbedding)
trCollection = client.get_collection(name = TR_COLLECTION, embedding_function=nomicEmbedding)
docsCollection = client.get_collection(name = DOCS_COLLECTION, embedding_function=nomicEmbedding)
codeCollection = client.get_collection(name= CODE_COLLECTION, embedding_function=jinaEmbedding)

# Retriever Logic
class HybridRetriever:
    def __init__(self, collection, k=60):
        self.collection = collection
        self.k = k
        data = self.collection.get()
        self.documents = data['documents']
        self.metadatas = data['metadatas']
        self.docToMetadata = {doc: meta for doc, meta in zip(self.documents, self.metadatas)}
        
        tokenizedCorpus = [self._tokenize(doc) for doc in self.documents]
        self.bm25 = BM25Okapi(tokenizedCorpus)

    def _tokenize(self, text):
        return re.sub(r'[^\w\s]', '', text.lower()).split()

    def search(self, query, nResults=5, filterDict=None):
        vectorResponse = self.collection.query(
            query_texts=[f"search_query: {query}"], 
            n_results=nResults * 3,
            where=filterDict
        )
        
        resultMap = {}
        if vectorResponse['documents']:
            for rank, doc in enumerate(vectorResponse['documents'][0]):
                meta = vectorResponse['metadatas'][0][rank]
                if doc not in resultMap:
                    resultMap[doc] = {"score": 0, "metadata": meta}
                resultMap[doc]["score"] += 1 / (self.k + rank)
        
        tokenizedQuery = self._tokenize(query)
        bm25Docs = self.bm25.get_top_n(tokenizedQuery, self.documents, n=nResults * 3)

        for rank, doc in enumerate(bm25Docs):
            if doc not in resultMap:
                meta = self.docToMetadata.get(doc, {})
                resultMap[doc] = {"score": 0, "metadata": meta}
            resultMap[doc]["score"] += 1 / (self.k + rank)

        sortedResults = sorted(resultMap.items(), key=lambda x: x[1]['score'], reverse=True)
        
        finalStrings = []
        for doc, data in sortedResults[:nResults]:
            metaHeader = " | ".join([f"{k}: {v}" for k, v in data['metadata'].items()])
            finalStrings.append(f"[METADATA] {metaHeader}\n[CONTENT] {doc}")
        return finalStrings
    

# Initialize Retrievers
tsRetriever = HybridRetriever(tsCollection)
trRetriever = HybridRetriever(trCollection)
acmeDocsRetriever = HybridRetriever(docsCollection)
acmeCodebaseRetriever = HybridRetriever(codeCollection)

# Tools
@tool
def searchOneM2MTs(query: str, sourceFilter: str = None) -> str:
    """Searches official oneM2M Technical Specifications (TS)."""
    fDict = {"source": {"$eq": sourceFilter}} if sourceFilter else None
    results = tsRetriever.search(query, nResults=5, filterDict=fDict)
    return "\n\n---\n\n".join(results)

@tool
def searchOneM2MTr(query: str) -> str:
    """Searches oneM2M Technical Reports (TR) (e.g., API Guides)."""
    results = trRetriever.search(query, nResults=5)
    return "\n\n---\n\n".join(results)

@tool
def searchAcmeDocs(query: str) -> str:
    """Searches the ACME oneM2M CSE implementation documentation (e.g., ACME configuration, setup & running, etc.)."""
    results = acmeDocsRetriever.search(query, nResults=3)
    return "\n\n---\n\n".join(results)

@tool 
def searchAcmeCodeBase(query: str) -> str:
    """Searches the ACME CSE source code for concrete implementations."""
    results = acmeCodebaseRetriever.search(query, nResults=5)
    return "\n\n---\n\n".join(results)

# Initialize Agents
oneM2MStandardsAgent = create_agent(
    agentModel,
    tools=[searchOneM2MTs, searchOneM2MTr],
    system_prompt="You are a oneM2M Standards Technical Expert."
)

acmeDocsAgent = create_agent(
    agentModel,
    tools=[searchAcmeDocs],
    system_prompt="You are a oneM2M ACME CSE expert."
)

acmeCodeAgent = create_agent(
    agentModel,
    tools=[searchAcmeCodeBase],
    system_prompt="You are a oneM2M ACME CSE developer."
)