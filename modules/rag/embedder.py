"""
embedder.py

Generate embeddings for text chunks using
SentenceTransformer (all-MiniLM-L6-v2).
"""

from sentence_transformers import SentenceTransformer
import numpy as np


class EmbeddingGenerator:
    """
    Generates embeddings for document chunks.
    """

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def generate(self, chunks):
        """
        Generate embeddings.

        Args:
            chunks (list): List of text chunks.

        Returns:
            numpy.ndarray
        """

        embeddings = self.model.encode(
            chunks,
            convert_to_numpy=True,
            normalize_embeddings=True,
            show_progress_bar=True
        )

        return np.array(embeddings)