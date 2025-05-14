import pickle
import streamlit as st
import pandas as pd
import requests

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    
    for i in distances[1:6]:  # Exclude the movie itself
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names


st.header('Movie Recommender System')

# Load data
movies = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('s.pkl', 'rb'))

# Movie list for the dropdown
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Initialize recommended_movie_names
recommended_movie_names = []

# Only show recommendations when the button is clicked
if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)

# Display the recommended movies after the button is clicked
for movie in recommended_movie_names:
    st.write(movie)
