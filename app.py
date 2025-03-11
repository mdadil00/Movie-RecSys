import pickle
import streamlit as st
import requests
import numpy as np

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=7e88b788f5026f7eda4c47e41f949043&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path



def recommend(movie_name):
    index = np.where(pt.index == movie_name)[0][0]  # Find movie index
    similar_items = sorted(
        list(enumerate(similarity[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:6]  # Get top 5 recommendations

    recommended_movies = []
    recommended_posters = []

    for i in similar_items:
        movie_title = pt.index[i[0]]
        movie_id = movies[movies['title'] == movie_title]['id'].values[0]  # Get movie ID

        recommended_movies.append(movie_title)
        recommended_posters.append(fetch_poster(movie_id))  # Fetch movie poster

    return recommended_movies, recommended_posters

st.header('Movie Recommender System')
movies = pickle.load(open('movies_list.pkl','rb'))
similarity = pickle.load(open('similarity_score.pkl','rb'))
pt = pickle.load(open('pt.pkl', 'rb'))  # Load the pivot table

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendations'):
    names, posters = recommend(selected_movie)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])

print("App Similarity Matrix Shape:", similarity.shape)
print("App Movies Shape:", movies.shape)
