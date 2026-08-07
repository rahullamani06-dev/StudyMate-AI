"""
txt_loader.py

Purpose:
--------
Extract text from plain text (.txt) files.

Author: Rahul I Lamani
Project: StudyMate AI
"""

from pathlib import Path


class TXTLoader:
    """
    A class to load and extract text from TXT files.
    """

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def extract_text(self) -> str:

        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return file.read()

        except Exception as error:
            raise Exception(f"Error reading TXT file: {error}")