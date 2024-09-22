import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=473ca318d9b1f71c3db3f8e28999d1fe&language=en-US".format(movie_id)
    data = requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    full_path="http://image.tmdb.org/t/p/w500/"+poster_path

    return full_path

#recommendation function

def recommend(movie):
    index=movies[movies['title'] == movie].index[0]
    distances=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])
    recommended_movies_name=[]
    recommended_movies_poster=[]

    for i in distances[1:6]:   #get top 5 movues
        movie_id=movies.iloc[i[0]]['movie_id']
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].title)
    return recommended_movies_name,recommended_movies_poster    



st.header("Movie Recommendation System")
movies = pickle.load(open('C:\\Users\\Admin\\IRWA_project\\artifacts\\movie_list.pkl', 'rb'))
similarity = pickle.load(open('C:\\Users\\Admin\\IRWA_project\\artifacts\\similarity.pkl', 'rb'))

movie_list=movies['title'].values
selected_movie=st.selectbox('Type or select a movie to get recommendation',
             movie_list
             
             
             )

#Creating a button for recommendation


if st.button('Show Recommendations'):
    recommended_movies_name,recommended_movies_poster=recommend(selected_movie)
    col1,col2,col3,col4,col5=st.columns(5)
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
    
    
    
    

