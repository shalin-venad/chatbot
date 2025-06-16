#🧠 Simple Python Chatbot using Ollama and LangChain
A minimal command-line chatbot built with LangChain and Ollama that runs locally using open-source LLMs like llama3.

## ✨ Features
Local LLM chat with no API key needed

Supports conversation history

Simple CLI interface

Built with Python, LangChain, and Ollama

## 📦 Requirements
Python 3.9+

Ollama installed and running

An Ollama model pulled (e.g. llama3:8b or llama3:1b)

## 🚀 Installation
1. Clone the repository
```bash
git clone https://github.com/shalin-venad/chatbot.git
cd chatbot
```
2. Set up a virtual environment
 ```python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
3. Install dependencies
```
   pip install -r requirements.txt
```
4. Pull a model
```
   ollama pull llama3.2:1b
```
5. Run the chatbot
```
python3 main.py
```

