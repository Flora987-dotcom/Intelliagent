# IntelliAgent – A Multi-Agent AI System for Automated Task Assistance

## 📌 Project Description

IntelliAgent is a **multi-agent AI system** built using Large Language Models (LLMs) to automate and assist with complex tasks. Instead of a single chatbot, IntelliAgent uses **multiple specialized agents** that work together to plan, execute, evaluate, and refine results.

This project was created as part of a **Generative AI Capstone** and demonstrates real-world usage of:

- Multi-agent architecture
- Tool integration (including custom tools and MCP style discovery)
- Session and memory management
- Observability (logging, tracing, evaluation)
- Agent-to-Agent (A2A) communication
- Deployment readiness

---

## 🧠 Agents in the System

The system uses **three main AI agents**:

### 1. Planner Agent
- Understands the user’s task
- Breaks large problems into smaller steps
- Sends steps to the Tool Agent

### 2. Tool Agent
- Uses built-in and custom tools
- Performs actions like data processing, code execution, or analysis

### 3. Evaluator Agent
- Reviews the output
- Checks for correctness and relevance
- Sends final improved response to the user

➡️ This creates a **Sequential Multi-Agent Workflow**
---

## 💾 Memory & Context

The system uses:

- Short-term memory for current session
- Long-term memory for storing important user interactions
- InMemorySessionService for fast access
- Context compaction to remove unnecessary data

This helps the system **remember previous conversations** and deliver more personalized responses.

---

## 🛠️ Tools & Technologies

- Python
- LLM APIs (OpenAI-compatible)
- LangChain (optional)
- MCP-style Tool Integration
- Custom Tools (for data processing, text analysis, etc.)

---

## 👁️ Observability & Quality

To ensure high performance, the following are included:

- Logging of agent actions
- Tracing full workflow
- Task success tracking
- Evaluation scoring

This allows continuous monitoring and improvement.

---

## 🌐 Future Enhancements

- Add parallel agents
- Add long-term vector-based memory
- Deploy as a web application (Streamlit / Flask)
- Mobile app integration

---

## 🚀 How to Run the Project

1. Clone the repository
2. Install requirements
3. Run
