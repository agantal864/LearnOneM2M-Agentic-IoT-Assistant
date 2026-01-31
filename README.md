# LearnOneM2M: Agentic IoT Assistant

An AI-powered autonomous agent designed to teach the **oneM2M IoT standard** while interacting with a live **ACME CSE (Common Service Entity)** server in real-time.

---

##  Overview
LearnOneM2M bridges the gap between complex industrial IoT protocols and user-friendly AI. Built with **LangGraph**, it features a multi-node state machine that can:

* **Educate:** Answer technical questions using a RAG pipeline powered by **ChromaDB**.
* **Execute:** Perform live REST operations (POST, GET, PUT, DELETE) on an ACME oneM2M server.
* **Route:** Automatically distinguish between "Theory" requests and "Action" commands using an intent-based router.

---

##  Tech Stack
* **Framework:** LangChain & LangGraph (State Machines)
* **LLM:** GPT-OSS / Llama 3.1 (8B) / Llama 3.2 (via Ollama)
* **Database:** ChromaDB (Vector Store for RAG)
* **IoT Protocol:** oneM2M (ACME CSE Implementation)
* **Interface:** Streamlit

---

##  Key Features

### 1. Intent-Based Routing (Level 3 Agent)
The agent uses a conditional logic gate to determine if a user needs documentation (Retrieval) or server interaction (Tools). This reduces token noise and increases execution accuracy.

### 2. Protocol-Aware Tooling
Includes a custom-built `execute_onem2m_request` tool that:
* Handles strict oneM2M header requirements (`X-M2M-Origin`, `X-M2M-RI`, `X-M2M-RVI`).
* Sanitizes JSON bodies to comply with primitive content constraints (Single-root key validation).
* Automatically manages Content-Type headers for different resource types (`ty`).

### 3. Dynamic Memory & Summarization
Utilizes a `filter_node` to manage long-term conversation history, generating summaries to maintain context without exceeding LLM token limits.

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/agantal864/LearnOneM2M-Agentic-IoT-Assistant.git](https://github.com/agantal864/LearnOneM2M-Agentic-IoT-Assistant.git)
   cd LearnOneM2M-Agentic-IoT-Assistant

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   
3. **Initialize Knowledge Base:**
   ```bash
   python ingestSpecifications.py
   python ingestACMEDocs.py
   python ingestACMErepo.py
   python processOneM2MSpecs.py
   python processTR.py
   python processAcmeDocs.py
   python processAcmeCode.py
   
4. **Run the Agent:**
   ```bash
   streamlit run app.py

Note: This project is currently a Work in Progress. I am actively refactoring the agent logic and expanding the oneM2M documentation.
