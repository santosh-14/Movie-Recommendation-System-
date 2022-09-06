import pickle
import streamlit as st
import requests



st.header("Movie Recommender System")
movies = pickle.load(open('mv_list.pkl','rb'))
sim= pickle.load(open('sim1.pkl','rb'))


def recommend(movie):
    idx=movies[movies["title"] == movie].index[0]
    dist=sorted(list(enumerate(sim[idx])),reverse=True, key = lambda x:x[1])
    rec_movies = []
    for i in dist[1:6]:
        rec_movies.append(movies.loc[i[0]].title)
    return rec_movies


movie_list=movies["title"].values

selected_movie = st.selectbox("Select a movie from the dropdown",movie_list)


if st.button("Recommend"):
    rec_movies=recommend(selected_movie)
    col1,col2,col3,col4,col5= st.beta_columns(5)
    with col1:
        st.text(rec_movies[0])
    with col2:
        st.text(rec_movies[1])
    with col3:
        st.text(rec_movies[2])
    with col4:
        st.text(rec_movies[3])
    with col5:
        st.text(rec_movies[4])
