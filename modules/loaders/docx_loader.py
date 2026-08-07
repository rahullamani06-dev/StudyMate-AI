"""
docx_loader.py

Purpose:
--------
Extract text from Microsoft Word (.docx) files.

Author: Rahul I Lamani
Project: StudyMate AI
"""

from pathlib import Path
from docx import Document


class DOCXLoader:
    """
    A class to load and extract text from DOCX files.
    """

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def extract_text(self) -> str:
        """
        Extract text from a DOCX document.

        Returns:
            str: Complete extracted text.
        """

        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")

        try:
            document = Document(self.file_path)

            extracted_text = []

            for paragraph in document.paragraphs:
                text = paragraph.text.strip()

                if text:
                    extracted_text.append(text)

            return "\n".join(extracted_text)

        except Exception as error:
            raise Exception(f"Error reading DOCX file: {error}")