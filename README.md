# learnOneM2M: Agentic IoT Assistant

An AI-powered autonomous agent designed to teach the **oneM2M IoT standard** while interacting with a live **acmeCse (Common Service Entity)** server in real-time.

---

## overview
learnOneM2M bridges the gap between complex industrial IoT protocols and user-friendly AI. Built with **langGraph**, it features a sophisticated multi-agent state machine that can classify queries, perform parallel knowledge retrieval, and synthesize technical answers.



---

## techStack
* **orchestrationFramework:** langChain & langGraph (State Machines with Fan-Out support)
* **llmModels:** ollama local models: llama3.1 (8B) / llama3.2
* **vectorDatabase:** chromaDb (Multi-collection: TS, TR, acmeDocs, acmeCode)
* **embeddingModels:** `nomic-ai/nomic-embed-text-v1.5` (Text) & `jinaai/jina-embeddings-v2-base-code` (Code)
* **searchLogic:** hybridSearch (BM25 + Vector) with Reciprocal Rank Fusion (RRF)
* **interface:** streamlit

---

## keyFeatures

### 1. multiAgentOrchestration (Fan-Out Pattern)
The system uses a `classify_query` node to decompose user intent into sub-tasks. It can trigger three specialized agents in parallel:
* **oneM2MStandardsAgent:** Queries Technical Specifications (TS) and Technical Reports (TR).
* **acmeDocsAgent:** Focuses on implementation-specific behavior and configurations.
* **acmeCodeAgent:** Uses a specialized code-embedding model to retrieve Python snippets from the actual acmeCse codebase.

### 2. hybridRetrievalSystem
The `HybridRetriever` class combines keyword matching (**BM25**) with semantic vector search. It uses **Reciprocal Rank Fusion (RRF)** to re-rank results, ensuring that both precise technical terms and general concepts are retrieved accurately.

### 3. technicalArchitectSynthesis
A final `synthesize` node acts as a Technical Architect. It merges data from all sub-agents, resolves conflicts between standards and implementation, and enforces oneM2M `camelCase` naming conventions for attributes.

---

## installationAndSetup

1. **cloneTheRepository:**
   ```bash
   git clone [https://github.com/agantal864/LearnOneM2M-Agentic-IoT-Assistant.git](https://github.com/agantal864/LearnOneM2M-Agentic-IoT-Assistant.git)
   cd LearnOneM2M-Agentic-IoT-Assistant
