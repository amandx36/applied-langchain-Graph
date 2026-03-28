#  Ollama Chatbot (LangChain + TinyLlama)

A lightweight terminal-based chatbot built using **LangChain** and **Ollama**, powered by the `tinyllama` model.  
Designed to run locally with minimal resources while maintaining conversational context.

---

##  Features

- ⚡ Runs fully **offline (local LLM via Ollama)**
- Maintains **chat history (context-aware replies)**
-  **CLI-based chatbot**
- **low-end systems (TinyLlama)**

---

##  Requirements

- Python 3.8+
- Ollama installed
- Internet (only for first-time model download)

---

## ⚙️ Setup & Installation

### 1️⃣ Install Ollama

Visit: https://ollama.com

Then pull the TinyLlama model:

```bash
ollama pull tinyllama