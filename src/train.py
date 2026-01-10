import os
import pickle
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Paths
DATA_PATH = "dataset/movies (2).csv"
MODEL_DIR = "model"

os.makedirs(MODEL_DIR, exist_ok=True)


# Training function
def train():
    print("📥 Loading dataset...")
    movies = pd.read_csv("D:\Ai ml\Projects_ALL\movie-recommender-system-tmdb-dataset-main\dataset\movies (2).csv")



# Feature engineering
    print("🧩 Creating tags...")
    movies["tags"] = (
        movies["overview"].fillna("") + " " +
        movies["genres"].fillna("") + " " +
        movies["keywords"].fillna("") + " " +
        movies["cast"].fillna("") + " " +
        movies["crew"].fillna("")
    )

    movies = movies[["title", "tags"]]

# BERT Embeddings
    print("🧠 Generating BERT embeddings...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    embeddings = model.encode(
        movies["tags"].tolist(),
        show_progress_bar=True
    )


# Similarity matrix
    print("📐 Computing cosine similarity...")
    similarity = cosine_similarity(embeddings)


# Save artifacts
    pickle.dump(movies, open(os.path.join(MODEL_DIR, "movies.pkl"), "wb"))
    pickle.dump(similarity, open(os.path.join(MODEL_DIR, "similarity.pkl"), "wb"))

    print("✅ BERT-based model training complete.")
    print(f"📁 Saved to `{MODEL_DIR}/`")



if __name__ == "__main__":
    train()
