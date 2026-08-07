"""
vector_store.py

Purpose:
--------
Manage the FAISS vector database.

Functions:
1. Create FAISS index
2. Add embeddings
3. Save index
4. Load index
5. Search similar chunks
"""

from pathlib import Path

import faiss
import numpy as np


class VectorStore:
    """
    Handles all FAISS operations.
    """

    def __init__(self):

        self.index = None

    def create_index(self, embeddings):
        """
        Create a new FAISS index.

        Args:
            embeddings (numpy.ndarray)
        """

        dimension = embeddings.shape[1]

        # Inner Product Index
        self.index = faiss.IndexFlatIP(dimension)

        self.index.add(
            embeddings.astype(np.float32)
        )

    def add_embeddings(self, embeddings):
        """
        Add new embeddings to an existing index.
        """

        if self.index is None:
            raise ValueError("FAISS index has not been created.")

        self.index.add(
            embeddings.astype(np.float32)
        )

    def save(self, path="vector_store/index.faiss"):
        """
        Save FAISS index.
        """

        Path("vector_store").mkdir(exist_ok=True)

        faiss.write_index(
            self.index,
            path
        )

    def load(self, path="vector_store/index.faiss"):
        """
        Load FAISS index.
        """

        self.index = faiss.read_index(path)

    def search(self, query_embedding, top_k=3):
        """
        Search similar vectors.

        Returns:
            scores
            indices
        """

        if self.index is None:
            raise ValueError("FAISS index not loaded.")

        scores, indices = self.index.search(
            query_embedding.astype(np.float32),
            top_k
        )

        return scores, indices

    def total_vectors(self):
        """
        Return total vectors stored.
        """

        if self.index is None:
            return 0

        return self.index.ntotal