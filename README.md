# Banking_rag_assistance
# 🏦 Banking RAG Assistance

An AI-powered Banking Assistant built using **Retrieval-Augmented Generation (RAG)** and **Large Language Models (LLMs)**. The system helps users get accurate answers to banking-related queries by retrieving relevant information from banking documents and generating context-aware responses.

## 📌 Project Overview

Banking RAG Assistance is designed to improve customer support by providing instant and reliable responses to banking questions. Instead of relying solely on a language model, the system retrieves relevant information from a knowledge base and then generates responses based on the retrieved content.

This approach ensures higher accuracy, reduced hallucinations, and better user experience.

## ✨ Features

* Intelligent banking chatbot
* Retrieval-Augmented Generation (RAG)
* Semantic document search
* Context-aware responses
* Banking FAQ assistance
* Loan and credit card information support
* Secure local LLM execution using Ollama
* User-friendly interface

## 🛠️ Technologies Used

* Python
* Retrieval-Augmented Generation (RAG)
* Large Language Models (LLMs)
* LangChain
* Transformers
* Ollama
* FAISS / ChromaDB
* Streamlit
* Embedding Models
* PyPDF2 / PDF Processing Libraries

## 🏗️ System Architecture

1. User submits a banking query.
2. Query is converted into embeddings.
3. Relevant documents are retrieved from the vector database.
4. Retrieved context is passed to the LLM.
5. LLM generates an accurate response.
6. Response is displayed to the user.

## 📂 Project Structure

```text
main_internship_project/
│
├── banking_rag_assistance/
│   │
│   ├── data/
│   │   └── banking_documents.pdf
│   │
│   ├── vector_db/
│   │
│   ├── src/
│   │   ├── document_loader.py
│   │   ├── embeddings.py
│   │   ├── retriever.py
│   │   ├── chatbot.py
│   │   └── rag_pipeline.py
│   │
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
│
└── venv/
    ├── Scripts/
    ├── Lib/
    ├── Include/
    └── pyvenv.cfg
```


## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/banking_rag_assistance.git
cd banking_rag_assistance
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open your browser and visit:

```text
http://localhost:8501
```

## 📊 Applications

* Banking Customer Support
* FAQ Automation
* Loan Information Assistance
* Credit Card Guidance
* Banking Policy Queries
* Internal Knowledge Management

## 🔮 Future Enhancements

* Multi-language support
* Voice-based interaction
* Real-time banking integration
* Personalized financial recommendations
* Advanced document analytics

## 🤝 Contributing

Contributions are welcome. Feel free to fork the repository and submit pull requests for improvements.

## 📜 License

This project is developed for educational and research purposes.

## 👩‍💻 Author

**Gokavalasa Sumanjali**

B.Tech Computer Science and Engineering

Artificial Intelligence & Machine Learning Enthusiast

