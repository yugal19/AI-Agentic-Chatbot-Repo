# 🤖 AI-Agentic-Chatbot

AI-Agentic-Chatbot is an intelligent chatbot system that allows users to query and ask questions using the power of large language models. It is enhanced with **Tavily search**, which enables real-time information retrieval from the internet to give accurate, up-to-date answers.

---

## ✨ Features

- 💬 Natural Language Question Answering  
- 🌐 Real-time Web Search via **Tavily** API  
- 🧠 LLM-Powered Agentic Behavior  
- 🔌 FastAPI Backend + Streamlit Frontend  
- ⚙️ Easy to run locally with virtual environment support  

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-Agentic-Chatbot.git
cd AI-Agentic-Chatbot



python -m venv venv
# Activate (use one of the below depending on OS)
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt


uvicorn main:app --reload


streamlit run frontend.py


📦 Tech Stack
Python

FastAPI – for backend APIs

Streamlit – for frontend UI

Tavily API – for real-time search

LLM – Agent-based conversational intelligence




