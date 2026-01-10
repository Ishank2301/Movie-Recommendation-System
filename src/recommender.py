import pickle
import difflib

def recommend(movie_title, top_n=5):
    # Load data internally
    with open("model/movies.pkl", "rb") as f:
        movies = pickle.load(f)

    with open("model/similarity.pkl", "rb") as f:
        similarity = pickle.load(f)

    # Fuzzy match for safety
    all_titles = movies["title"].tolist()
    close_matches = difflib.get_close_matches(movie_title, all_titles, n=1)

    if not close_matches:
        return []

    movie_title = close_matches[0]

    idx = movies[movies["title"] == movie_title].index[0]
    distances = similarity[idx]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1: top_n + 1]

    return [
    (movies.iloc[i[0]].title, round(i[1], 3))
    for i in movie_list
]

