"""
document_processor.py

Purpose:
--------
Process uploaded documents.

Workflow:
1. Load document
2. Extract text
3. Clean text
4. Split text into chunks
"""

from pathlib import Path

from modules.loaders.pdf_loader import PDFLoader
from modules.loaders.docx_loader import DOCXLoader
from modules.loaders.ppt_loader import PPTLoader
from modules.loaders.txt_loader import TXTLoader

from modules.preprocessing.cleaner import TextCleaner
from modules.preprocessing.chunker import TextChunker


class DocumentProcessor:
    """
    Process uploaded documents for the RAG pipeline.
    """

    def __init__(self):

        self.cleaner = TextCleaner()

        self.chunker = TextChunker(
            chunk_size=400,
            overlap=80
        )

    def process(self, file_path):
        """
        Process an uploaded document.

        Args:
            file_path (Path): Path of uploaded document.

        Returns:
            dict
        """

        extension = Path(file_path).suffix.lower()

        # Select Loader

        if extension == ".pdf":
            loader = PDFLoader(file_path)

        elif extension == ".docx":
            loader = DOCXLoader(file_path)

        elif extension == ".pptx":
            loader = PPTLoader(file_path)

        elif extension == ".txt":
            loader = TXTLoader(file_path)

        else:
            raise ValueError(
                f"Unsupported document type: {extension}"
            )

        # Extract text

        raw_text = loader.extract_text()

        # Clean text

        clean_text = self.cleaner.clean(raw_text)

        # Chunk text

        chunks = self.chunker.split_text(clean_text)

        return {

            "text": clean_text,

            "chunks": chunks,

            "word_count": len(clean_text.split()),

            "character_count": len(clean_text),

            "chunk_count": len(chunks),

            "file_type": extension.replace(".", "").upper()

        }