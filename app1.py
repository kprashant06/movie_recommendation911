import streamlit as st
import pickle
import pandas as pd


movies=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open("similarity.pkl",'rb'))

movies_list=movies['title'].values


def recommend(movie):
    movie_index=movies[movies["title"]==movie].index[0]

    distances=similarity[movie_index]

    movies_list=sorted(list(enumerate(distances)),reverse=True, key= lambda x :x [1])[1:6]

    recommended_movies=[]

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies
    

# movies_=pickle.load(open('movies.pkl','rb'))
# similarity=pickle.load(open("similarity.pkl",'rb'))

# movies_list=movies['title'].values

st.title('Movie recommendar system')

selected_movie_name =st.selectbox('how would you like to be contacted', movies_list)

if st.button('Recommend'):
    recommendation=recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)