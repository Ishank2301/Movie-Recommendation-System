import requests
import os

API_KEY = "AMDB_API_KEY"
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE = "https://image.tmdb.org/t/p/w500"

def fetch_poster(movie_title):
    url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": API_KEY,
        "query": movie_title
    }

    response = requests.get(url, params=params).json()
    results = response.get("results")

    if results and results[0].get("poster_path"):
        return IMAGE_BASE + results[0]["poster_path"]

    return None
