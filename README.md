# Agentic Student Assistant 🎓🤖

An autonomous, local conversational agent designed to instantly process and resolve complex student administrative queries. Built entirely on open-source, local models to ensure zero external API latency and maximum data privacy.

## 🚀 Overview
This project demonstrates application-layer AI engineering by binding deterministic Python functions to a local Large Language Model (LLM). Instead of relying on standard text generation (which is prone to hallucination on mathematical queries), the model dynamically selects and executes custom tools to calculate fees, check attendance eligibility, and retrieve academic records from a mock database.

## 🧠 Architecture & Features
* **Local Tool-Calling:** Utilizes a custom `AgentExecutor` pipeline to give the LLM access to deterministic calculation tools.
* **Zero Hallucination Mathematics:** Offloads calculations (e.g., Attendance %, Library Fines, Hostel Fees) to native Python scripts, guaranteeing 100% accurate outputs.
* **Dynamic Data Retrieval:** Integrates a student information tool to parse dictionary-based records dynamically based on user prompts.
* **Context-Aware Dialog:** Employs structured system prompts to maintain persona consistency and concise delivery.

## 🛠️ Tech Stack
* **Framework:** LangChain (`create_tool_calling_agent`, `AgentExecutor`)
* **Local LLM Engine:** Ollama 
* **Model:** Qwen 2.5 (3B parameters)
* **Language:** Python 3.x

## 💻 Quick Start
1. Ensure [Ollama](https://ollama.com/) is installed and running on your machine.
2. Pull the required model:
   ```bash
   ollama run qwen2.5:3b
3. Install dependencies:
4. ```bash
   pip install langchain langchain-core langchain-ollama langchain-classic
5. Run the agent:
   ```bash
   python main.py
