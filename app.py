import streamlit as st
import requests
import pickle
from dotenv import load_dotenv
import os


load_dotenv() 

API_KEY=os.getenv('API_KEY')

movies=pickle.load(open('movie_list.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movie_list=movies['title'].values

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    list_movie=[]
    list_posters=[]
    for i in distances[1:11]:
        title=movies.iloc[i[0]].title
        id=movies.iloc[i[0]].movie_id
        list_movie.append(title)
        list_posters.append(fetch_poster(id))
    return list_movie,list_posters


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(movie_id,API_KEY)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
        


st.header("Movie Recommendation System!")
st.subheader("Enter the movie related to which you want recommendation.")

selected_movie=st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

st.text("The selected movie is: ")
st.text(selected_movie)


if st.button('Show Recommendations'):
 list_movie,list_poster=recommend(selected_movie)
 counter=0
 for i in range(2):
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(list_poster[counter])
        st.text(list_movie[counter])
        counter+=1
    with col2:
        st.image(list_poster[counter])
        st.text(list_movie[counter])
        counter+=1

    with col3:
        st.image(list_poster[counter])
        st.text(list_movie[counter])
        counter+=1
    with col4:
        st.image(list_poster[counter])
        st.text(list_movie[counter])
        counter+=1
    with col5:
        st.image(list_poster[counter])
        st.text(list_movie[counter])
        counter+=1
      
      

