"""
retriever.py

Retrieve relevant document chunks
from FAISS vector database.
"""


class Retriever:

    def __init__(
        self,
        vector_store,
        metadata_manager,
        embedder
    ):

        self.vector_store = vector_store
        self.metadata_manager = metadata_manager
        self.embedder = embedder


    def retrieve(
        self,
        query,
        top_k=3
    ):

        query_embedding = self.embedder.generate(
            [query]
        )


        scores, indices = self.vector_store.search(
            query_embedding,
            top_k
        )


        metadata = self.metadata_manager.load()


        results = []


        for score, index in zip(
            scores[0],
            indices[0]
        ):

            if index == -1:
                continue


            item = metadata[index]

            results.append(
                {
                    "text": item["text"],
                    "score": float(score)
                }
            )


        return results



    def retrieve_context(
        self,
        query
    ):

        results = self.retrieve(
            query,
            top_k=3
        )


        if not results:
            return ""


        # highest similarity first
        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )


        # combine only best 2 chunks
        context = ""

        for item in results[:2]:

            context += item["text"] + "\n\n"


        return context[:1200]