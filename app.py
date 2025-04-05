import pickle
import streamlit as st
import requests

import requests

def fetch(movie_id):
    api_key = "6bbc90fa0e7d5c39b2b2e35fb0217e29"  
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if 'poster_path' in data and data['poster_path']:  
            poster_path = data['poster_path']
            full_image_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
            return full_image_url
        else:
            return "https://via.placeholder.com/500x750?text=No+Image+Available"  
    else:
        print(f"Error: {response.status_code}, {response.text}")  
        return None  
      

def recommend(movie):
    index = movies[movies['title'] == movie ].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])
    recommended_movies_name = [] 
    recommended_movies_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_name.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch(movie_id))
    return recommended_movies_name,recommended_movies_poster    

st.header("Movies Recommendation System Using Machine Learning")
movies = pickle.load(open("movielist.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))
movieslist = movies["title"].values
selectedmovie = st.selectbox(
    "Type a movie to get recommendation",movieslist
) 

if st.button("Show Recommendation"):
    recommended_movies_name,recommended_movies_poster = recommend(selectedmovie)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(recommended_movies_name[0])
        st.image(recommended_movies_poster[0])

    with col2:
        st.text(recommended_movies_name[1])
        st.image(recommended_movies_poster[1])  

    with col3:
        st.text(recommended_movies_name[2])
        st.image(recommended_movies_poster[2])  

    with col4:
        st.text(recommended_movies_name[3])
        st.image(recommended_movies_poster[3]) 

    with col5:
        st.text(recommended_movies_name[4])
        st.image(recommended_movies_poster[4])           