import streamlit as st
import pickle
from src.recommender import recommend
from src.tmdb import fetch_poster

# Page config
st.set_page_config(
    page_title="🎬 Movie Recommender System",
    page_icon="🎥",
    layout="centered",
)

# Load data (cached)
@st.cache_data
def load_movies():
    with open("model/movies.pkl", "rb") as f:
        return pickle.load(f)

movies = load_movies()

# UI Header
st.markdown(
    """
    <h1 style='text-align: center;'>🎬 Movie Recommender System</h1>
    <p style='text-align: center; color: gray;'>
        Content-Based Recommendation.
    </p>
    """,
    unsafe_allow_html=True,
)

st.divider()

# Movie selection
selected_movie = st.selectbox(
    "🎥 Select a movie you like",
    movies["title"].values,
    index=None,
    placeholder="Start typing a movie name...",
)

# SAFE initialization
recommendations = []

# Recommendation button
if st.button("🔍 Recommend Movies", use_container_width=True):

    if selected_movie is None:
        st.warning("Please select a movie first.")
    else:
        with st.spinner("Finding similar movies... 🍿"):
            recommendations = recommend(selected_movie)

# Display recommendations
if recommendations:
    st.success(f"Top recommendations based on **{selected_movie}**")

    cols = st.columns(len(recommendations))

    for col, (movie, score) in zip(cols, recommendations):
        with col:
            poster = fetch_poster(movie)
            if poster:
                st.image(poster, use_container_width=True)
            st.markdown(f"**{movie}**  \nSimilarity: `{score:.2f}`")


# Sidebar
st.sidebar.header("ℹ️ About")

st.sidebar.markdown(
    """
    **Model**
    - Content-Based Filtering
    - BERT Embeddings
    - Cosine Similarity

    **Dataset**
    - TMDB Movies Dataset

    **Tech Stack**
    - Python
    - Sentence Transformers
    - Streamlit
    """
)
