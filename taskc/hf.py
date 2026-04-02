# task_c.py

# Task C - Vectorization with Hugging Face
# Model used: intfloat/e5-small-v2
# This code loads a small embedding model, embeds example sentences,
# and performs similarity search using cosine similarity.

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load embedding model from Hugging Face
# intfloat/e5-small-v2 is lightweight, fast, and good for semantic search
model = SentenceTransformer("intfloat/e5-small-v2")

# Example sentences
# These can also be extracted from a PDF
sentences = [
    "Machine learning helps computers learn patterns from data.",
    "Deep learning is a subset of machine learning that uses neural networks.",
    "Natural language processing allows computers to understand human language.",
    "Computer vision helps machines identify objects in images and videos.",
    "Artificial intelligence is a broad field that includes machine learning and deep learning."
]

# Query sentence
query = "What is deep learning?"

# Check if query is empty
if query.strip() == "":
    print("Query cannot be empty")
    exit()

# e5 models work best with prefixes
# Use 'passage:' for stored text
# Use 'query:' for search input
passages = []

for sentence in sentences:
    passages.append("passage: " + sentence)

query_text = "query: " + query

# Generate embeddings
sentence_embeddings = model.encode(passages)
query_embedding = model.encode([query_text])

# Calculate cosine similarity
scores = cosine_similarity(query_embedding, sentence_embeddings)

# Convert scores to simple list
similarity_scores = scores[0]

# Print all similarity scores
print("\nQuery:", query)
print("\nSimilarity Scores:\n")

for i in range(len(sentences)):
    print("Sentence", i + 1, ":", sentences[i])
    print("Score:", round(similarity_scores[i], 4))
    print()

# Find best matching sentence
best_index = np.argmax(similarity_scores)

print("Best Match:")
print(sentences[best_index])
print("Best Score:", round(similarity_scores[best_index], 4))