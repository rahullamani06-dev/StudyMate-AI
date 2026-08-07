"""
cleaner.py

Purpose:
--------
Clean extracted text before chunking.
"""

import re


class TextCleaner:
    """
    Cleans extracted document text.
    """

    def clean(self, text: str) -> str:
        """
        Clean extracted text.

        Args:
            text (str): Raw extracted text.

        Returns:
            str: Cleaned text.
        """

        # Replace multiple spaces/tabs with one space
        text = re.sub(r"[ \t]+", " ", text)

        # Replace 3 or more newlines with 2 newlines
        text = re.sub(r"\n{3,}", "\n\n", text)

        # Remove leading/trailing spaces
        text = text.strip()

        return text