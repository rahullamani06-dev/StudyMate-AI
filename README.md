# 📚 StudyMate AI

## Intelligent Document Question Answering System using RAG

StudyMate AI is an AI-powered learning assistant that allows users to upload documents and interact with them using Natural Language Processing.

The system uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from uploaded documents and generate answers, summaries, quizzes, and flashcards.

---

## 🚀 Features

### 📄 Document Processing
- Upload PDF, DOCX, PPTX, and TXT documents
- Extract text from documents
- Split documents into meaningful chunks
- Generate embeddings for semantic search

### 💬 Question Answering
- Ask questions based on uploaded documents
- Retrieve relevant document information using FAISS vector search
- Generate AI-based answers using FLAN-T5

### 📝 Document Summarization
- Generate concise summaries from uploaded documents

### 🧠 Quiz Generation
- Automatically generate study questions from document content

### 📚 Flashcard Generation
- Create flashcards for quick revision and learning

---

# 🏗️ System Architecture

```
                User
                 |
                 ↓
        Upload Document
                 |
                 ↓
       Document Processing
                 |
                 ↓
        Text Chunking
                 |
                 ↓
    Sentence Transformer Embeddings
                 |
                 ↓
          FAISS Vector Store
                 |
                 ↓
            Retriever
                 |
                 ↓
        FLAN-T5 Generator
                 |
                 ↓
 Answers | Summaries | Quiz | Flashcards
```

---

# 🛠️ Technology Stack

## Programming Language
- Python

## Frontend
- Streamlit

## AI / NLP
- Hugging Face Transformers
- FLAN-T5
- Sentence Transformers

## Vector Database
- FAISS (Facebook AI Similarity Search)

## Document Processing
- PyMuPDF
- python-docx
- python-pptx

---

# 📂 Project Structure

```
StudyMate_AI/

│── app.py
│── requirements.txt
│── README.md
│
├── modules/
│   └── rag/
│       ├── document_processor.py
│       ├── embedder.py
│       ├── retriever.py
│       ├── generator.py
│       ├── vector_store.py
│       └── metadata_manager.py
│
├── data/
│   └── uploads/
│
└── vector_store/
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/rahullamani06-dev/StudyMate-AI.git
```

## 2. Navigate to Project Folder

```bash
cd StudyMate-AI
```

## 3. Create Virtual Environment

```bash
python -m venv .venv
```

## 4. Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Run Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 🔄 Workflow

1. Upload a document
2. Extract document text
3. Split text into chunks
4. Generate embeddings
5. Store embeddings in FAISS
6. Retrieve relevant information
7. Generate AI response

---

# 🎯 Project Objective

The objective of StudyMate AI is to create an intelligent document assistant that helps students understand and learn from large documents efficiently using Artificial Intelligence and Retrieval-Augmented Generation.

---

# 👨‍💻 Contributors

**Rahul I Lamani**

---

# 🔮 Future Improvements

- Multi-document conversation support
- Better source citation display
- Voice-based interaction
- Cloud deployment
- User authentication
- Improved quiz and flashcard formatting

---

# 📌 License

This project is developed for educational purposes.