import pickle
import streamlit as st
import requests



st.header("Movie Recommender System")
movies = pickle.load(open('mvlist.pkl','rb'))
sim= pickle.load(open('similarity.pkl','rb'))


def recommend(movie):
    idx=movies[movies["title"]==movie].index[0]
    rec_movies=[]
    for i in sim[idx]:
        rec_movies.append(movies.loc[i[0]].title)
    return rec_movies


movie_list=movies["title"].values

selected_movie = st.selectbox("Select a movie from the dropdown",movie_list)


if st.button("Recommend"):
    rec_movies=recommend(selected_movie)
    for i in range(len(rec_movies)):
        st.text(rec_movies[i])
