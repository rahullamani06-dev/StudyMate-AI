"""
chunker.py

Purpose:
--------
Split text into overlapping chunks based on words.
"""

from typing import List


class TextChunker:

    def __init__(self, chunk_size=150, overlap=30):
        """
        chunk_size : number of words
        overlap    : number of overlapping words
        """
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split_text(self, text: str) -> List[str]:

        words = text.split()

        chunks = []

        start = 0

        while start < len(words):

            end = start + self.chunk_size

            chunk = " ".join(words[start:end])

            chunks.append(chunk)

            start += self.chunk_size - self.overlap

        return chunks