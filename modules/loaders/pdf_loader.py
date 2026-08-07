"""
pdf_loader.py

Purpose:
--------
This module extracts text from PDF documents using PyMuPDF.

Author: Rahul I Lamani
Project: StudyMate AI
"""

import fitz  # PyMuPDF
from pathlib import Path


class PDFLoader:
    """
    A class to load and extract text from PDF files.
    """

    def __init__(self, file_path: str):
        """
        Initialize the PDF loader.

        Args:
            file_path (str): Path to the PDF file.
        """
        self.file_path = Path(file_path)

    def extract_text(self) -> str:
        """
        Extract text from all pages of the PDF.

        Returns:
            str: Complete extracted text.
        """
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")

        extracted_text = []

        try:
            pdf_document = fitz.open(self.file_path)

            for page in pdf_document:
                text = page.get_text()

                if text.strip():
                    extracted_text.append(text)

            pdf_document.close()

            return "\n".join(extracted_text)

        except Exception as error:
            raise Exception(f"Error reading PDF: {error}")