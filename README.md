# LearnOneM2M: Agentic IoT Assistant

An AI-powered autonomous agent designed to teach the **oneM2M IoT standard** by interacting with a live **ACME CSE (Common Service Entity)** server in real-time.

---

## Overview
LearnOneM2M bridges the gap between complex industrial IoT protocols and user-friendly AI. Built with **LangGraph**, it features a multi-agent state machine that can classify queries, perform parallel knowledge retrieval, execute oneM2M REST, and synthesize technical answers.


---

## Tech Stack
* **Orchestration Framework:** LangChain & LangGraph (State Machines with Fan-Out support)
* **LLM Models:** Ollama local models: Llama 3.1 (8B) for refining metadata during data chunking and vectorization. GPT-OSS 20B for multi-agent systems. 
* **Vector Database:** ChromaDB (Multi-collection: TS, TR, acmeDocs, acmeCode)
* **Embedding Models:** `nomic-ai/nomic-embed-text-v1.5` (Text) & `jinaai/jina-embeddings-v2-base-code` (Code)
* **Search Logic:** Hybrid Search (BM25 + Vector) with Reciprocal Rank Fusion (RRF)
* **oneM2M Server** [ACME CSE by Ankraft](https://github.com/ankraft/ACME-oneM2M-CSE)
* **Interface:** Streamlit (Ongoing)

---

## Key Features

### 1. Multi-Agent Orchestration (Fan-Out Pattern)
The app uses a `classifyNode` node to decompose user intent into sub-tasks. It can trigger three specialized agents in parallel:
* **oneM2MStandardsAgent:** Queries Technical Specifications (TS) and Technical Reports (TR).
* **acmeDocsAgent:** Focuses on implementation-specific behavior and configurations.
* **acmeCodeAgent:** Uses a specialized code-embedding model to retrieve Python snippets from the actual ACME CSE codebase.

### 2. Hybrid Retrieval System
The `HybridRetriever` class combines keyword matching (**BM25**) with semantic vector search. It uses **Reciprocal Rank Fusion (RRF)** to re-rank results, ensuring that both precise technical terms and general concepts are retrieved accurately.

### 3. Technical Architect Synthesis
A final `synthesize` node acts as a Technical Architect. It merges data from all sub-agents, resolves conflicts between standards and implementation.

### 4. Execute live oneM2M REST
The app enables the execution of a live oneM2M REST mapped to an http request. If the user requests for a live oneM2M request to an ACME CSE server, the agent executes the `oneM2MExecuteRest` tool

---

## Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/agantal864/LearnOneM2M-Agentic-IoT-Assistant.git](https://github.com/agantal864/LearnOneM2M-Agentic-IoT-Assistant.git)
   cd LearnOneM2M-Agentic-IoT-Assistant
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt or uv pip install -r requirements.txt
3. **Initialize Knowledge Base**
   ```bash
     # Ingest raw data
      python ingestSpecifications.py
      python ingestACMEDocs.py
      python ingestACMErepo.py

      # Process and Vectorize
      python processOneM2MSpecs.py
      python processTR.py
      python processAcmeDocs.py
      python processAcmeCode.py
4. **Run Agent**
   * **Learn oneM2M**
     ```bash
     python learnOneM2MAgent.py
     ```
   * **REST oneM2M**
     ```bash
     python restM2MAgent.py
     ```
