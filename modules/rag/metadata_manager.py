"""
metadata_manager.py

Purpose
-------
Store and load metadata for every document chunk.
"""

import pickle
from pathlib import Path


class MetadataManager:
    """
    Handles saving and loading metadata.
    """

    def __init__(self):

        self.save_path = Path("vector_store/metadata.pkl")

    # ---------------------------------------------------------
    # Save metadata
    # ---------------------------------------------------------

    def save(
        self,
        chunks,
        source_name,
    ):

        metadata = []

        for chunk_id, chunk in enumerate(chunks):

            metadata.append(
                {
                    "chunk_id": chunk_id,
                    "source": source_name,
                    "text": chunk,
                }
            )

        self.save_path.parent.mkdir(
            exist_ok=True
        )

        with open(
            self.save_path,
            "wb",
        ) as file:

            pickle.dump(
                metadata,
                file,
            )

    # ---------------------------------------------------------
    # Load metadata
    # ---------------------------------------------------------

    def load(self):

        if not self.save_path.exists():
            return []

        with open(
            self.save_path,
            "rb",
        ) as file:

            return pickle.load(file)

    # ---------------------------------------------------------
    # Number of chunks
    # ---------------------------------------------------------

    def total_chunks(self):

        metadata = self.load()

        return len(metadata)

    # ---------------------------------------------------------
    # Get chunk text
    # ---------------------------------------------------------

    def get_chunk_text(
        self,
        index,
    ):

        metadata = self.load()

        if index >= len(metadata):
            return None

        return metadata[index]["text"]

    # ---------------------------------------------------------
    # Get source
    # ---------------------------------------------------------

    def get_source(
        self,
        index,
    ):

        metadata = self.load()

        if index >= len(metadata):
            return None

        return metadata[index]["source"]