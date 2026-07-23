# 🤖 RAG Chatbot using Gemini & LangChain

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge\&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge\&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green?style=for-the-badge)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-blue?style=for-the-badge\&logo=google)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-purple?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

A Retrieval-Augmented Generation (RAG) chatbot that answers questions from uploaded PDF documents using **Google Gemini**, **LangChain**, and **ChromaDB**. Instead of relying only on the language model, the chatbot retrieves relevant information from the uploaded documents before generating responses, resulting in more accurate and context-aware answers.

Author: D V Shriram

Registration No: 23MIM10044

---

## 📌 Features

* 📄 Chat with PDF documents
* 🔍 Semantic search using vector embeddings
* 🤖 Google Gemini LLM integration
* 🧠 LangChain Retrieval-Augmented Generation (RAG)
* 💾 ChromaDB vector database
* ⚡ Fast document retrieval
* 🎨 Streamlit web interface
* 🔐 Environment variable support using `.env`

---

## 🛠 Tech Stack

* Python 3.12
* Streamlit
* LangChain
* Google Gemini API
* ChromaDB
* PyPDF
* Tiktoken
* Python-dotenv

---

## 📂 Project Structure

```text
RAG-Chatbot/
│
├── app.py                 # Streamlit application
├── ingest.py              # PDF ingestion & vector creation
├── data/                  # PDF documents
├── .chroma_db/            # Chroma vector database
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/RAG-Chatbot.git
cd RAG-Chatbot
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Gemini API

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## 📄 Add Documents

Place all PDF files inside the **data/** folder.

---

## 🧠 Create the Vector Database

```bash
python ingest.py
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💬 Example Questions

* Summarize the document.
* What are the key topics discussed?
* Explain Chapter 2.
* What conclusions are mentioned?
* Give me the important points from the report.

---

## 🚀 Future Improvements

* Multiple PDF upload
* Chat history
* Source citations
* Dark mode
* Export chat
* Conversation memory
* Hybrid search
* Docker support

---

## 👨‍💻 Author

**D. V. Shriram**
Student at VIT Bhopal University

GitHub: https://github.com/dvshriram-dvs

---

## ⭐ If you found this project useful

Please consider giving it a **Star ⭐** on GitHub.
