from modules.rag.embedder import EmbeddingGenerator

chunks = [
    "Artificial Intelligence is the simulation of human intelligence.",
    "Machine Learning is a subset of Artificial Intelligence.",
    "Deep Learning uses neural networks."
]

embedder = EmbeddingGenerator()

embeddings = embedder.generate(chunks)

print("Shape :", embeddings.shape)
print("First Vector Length :", len(embeddings[0]))