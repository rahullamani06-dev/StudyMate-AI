"""
app.py

StudyMate AI
------------

Main Streamlit application.

Workflow

1. Upload documents
2. Process documents
3. Generate embeddings
4. Create FAISS index
5. Ask questions
6. Generate summaries
7. Generate quizzes
8. Generate flashcards
"""

from pathlib import Path

import streamlit as st

from modules.rag.document_processor import DocumentProcessor
from modules.rag.embedder import EmbeddingGenerator
from modules.rag.vector_store import VectorStore
from modules.rag.metadata_manager import MetadataManager
from modules.rag.retriever import Retriever
from modules.rag.generator import Generator

# ----------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚",
    layout="wide"
)

st.title("📚 StudyMate AI")
st.caption("Intelligent Document Question Answering System")

# ----------------------------------------------------------
# DIRECTORIES
# ----------------------------------------------------------

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

VECTOR_DIR = Path("vector_store")
VECTOR_DIR.mkdir(exist_ok=True)

# ----------------------------------------------------------
# SESSION STATE
# ----------------------------------------------------------

if "processor" not in st.session_state:
    st.session_state.processor = DocumentProcessor()

if "embedder" not in st.session_state:
    st.session_state.embedder = EmbeddingGenerator()

if "vector_store" not in st.session_state:
    st.session_state.vector_store = VectorStore()

if "metadata_manager" not in st.session_state:
    st.session_state.metadata_manager = MetadataManager()

if "retriever" not in st.session_state:
    st.session_state.retriever = None

if "generator" not in st.session_state:
    st.session_state.generator = Generator()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "document_text" not in st.session_state:
    st.session_state.document_text = ""

if "document_chunks" not in st.session_state:
    st.session_state.document_chunks = []

# ----------------------------------------------------------
# SIDEBAR
# ----------------------------------------------------------

with st.sidebar:

    st.header("Upload Documents")

    uploaded_file = st.file_uploader(
        "Choose a document",
        type=[
            "pdf",
            "docx",
            "pptx",
            "txt"
        ]
    )

    process_button = st.button(
        "Process Document",
        use_container_width=True
    )
# ----------------------------------------------------------
# PROCESS DOCUMENT
# ----------------------------------------------------------

if process_button:

    if uploaded_file is None:
        st.warning("Please upload a document.")
        st.stop()

    file_path = UPLOAD_DIR / uploaded_file.name

    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    with st.spinner("Processing document..."):

        result = st.session_state.processor.process(file_path)

    document_text = result["text"]
    document_chunks = result["chunks"]

    st.session_state.document_text = document_text
    st.session_state.document_chunks = document_chunks

    st.success("Document processed successfully!")

    st.write(f"Words : {result['word_count']}")
    st.write(f"Characters : {result['character_count']}")
    st.write(f"Chunks : {result['chunk_count']}")

    # ------------------------------------------------------
    # Generate Embeddings
    # ------------------------------------------------------

    with st.spinner("Generating embeddings..."):

        embeddings = (
            st.session_state.embedder.generate(
                document_chunks
            )
        )

    # ------------------------------------------------------
    # Create FAISS Index
    # ------------------------------------------------------

    with st.spinner("Creating vector database..."):

        st.session_state.vector_store.create_index(
            embeddings
        )

        st.session_state.vector_store.save()
        st.session_state.vector_store.load()

    # ------------------------------------------------------
    # Save Metadata
    # ------------------------------------------------------

    st.session_state.metadata_manager.save(
        document_chunks,
        uploaded_file.name
    )

    st.success("Vector database created successfully.")
    st.balloons()

    # ------------------------------------------------------
    # Initialize Retriever
    # ------------------------------------------------------

    st.session_state.retriever = Retriever(
        vector_store=st.session_state.vector_store,
        metadata_manager=st.session_state.metadata_manager,
        embedder=st.session_state.embedder
    )
# ----------------------------------------------------------
# CHAT TAB
# ----------------------------------------------------------
# ----------------------------------------------------------
# TABS
# ----------------------------------------------------------

chat_tab, summary_tab, quiz_tab, flashcard_tab = st.tabs(
    [
        "💬 Chat",
        "📝 Summary",
        "🧠 Quiz",
        "📚 Flashcards"
    ]
)
with chat_tab:

    st.header("Ask Questions")

    question = st.text_input(
        "Ask a question about the uploaded document"
    )

    ask_button = st.button("Ask")


    if ask_button:

        if question.strip() == "":

            st.warning("Please enter a question.")

        else:

            with st.spinner("Searching document..."):

                context = st.session_state.retriever.retrieve_context(
                    question
                )


            


            if context == "":

                st.error(
                    "No relevant information found in the document."
                )

            else:

                answer = st.session_state.generator.generate_answer(
                    question,
                    context
                )

                st.subheader("Answer")

                st.write(answer)

                
# ----------------------------------------------------------
# SUMMARY TAB
# ----------------------------------------------------------

with summary_tab:

    st.header("📝 Document Summary")

    if st.session_state.document_text == "":

        st.info("Please upload and process a document first.")

    else:

        if st.button("Generate Summary"):

            with st.spinner("Generating summary..."):

                summary = (
                    st.session_state.generator.generate_summary(
                        st.session_state.document_text
                    )
                )

            st.write(summary)


# ----------------------------------------------------------
# QUIZ TAB
# ----------------------------------------------------------

with quiz_tab:

    st.header("🧠 Generate Quiz")

    if st.session_state.document_text == "":

        st.info("Please upload and process a document first.")

    else:

        if st.button("Generate Quiz"):

            with st.spinner("Generating quiz..."):

                quiz = (
                    st.session_state.generator.generate_quiz(
                        st.session_state.document_text,
                        number_of_questions=10
                    )
                )

            st.write(quiz)


# ----------------------------------------------------------
# FLASHCARD TAB
# ----------------------------------------------------------

with flashcard_tab:

    st.header("📚 Generate Flashcards")

    if st.session_state.document_text == "":

        st.info("Please upload and process a document first.")

    else:

        if st.button("Generate Flashcards"):

            with st.spinner("Generating flashcards..."):

                flashcards = (
                    st.session_state.generator.generate_flashcards(
                        st.session_state.document_text,
                        number_of_cards=10
                    )
                )

            st.write(flashcards)