import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=b51e8f05df464e0fae4d77bf6d811977".format(movie_id))
    data = response.json()
    print(data)
    return "http://image.tmdb.org/t/p/w500" + data ['poster_path']

def recommend(movie):
     movie_index = movies[movies['title']==movie].index[0]
     distance = similarity[movie_index]
     movies_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    
     recommend_movies = []
     recommended_movies_poster = []
     for i in movies_list:
         movie_id = movies.iloc[i[0]].movie_id
        
         recommend_movies.append( movies.iloc[i[0]].title)
          #fetch poster from api
         recommended_movies_poster.append(fetch_poster(movie_id))

     return recommend_movies, recommended_movies_poster


movies = pickle.load(open('movie.pkl','rb'))
movies_list = movies['title'].values 
similarity = pickle.load(open('similarity.pkl','rb'))  # Assuming you have this



st.title('Movie Recommender Systeam')

selected_movie_name = st.selectbox(
    "How would you like to be con",
    movies_list)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])




# import streamlit as st
# import pickle

# movies = pickle.load(open('movie.pkl','rb'))
# similarity = pickle.load(open('similarity.pkl','rb'))  # Assuming you have this

# movies_list = movies['title'].values

# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distance = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

#     recommended_movies = []
#     for i in movies_list:
#         recommended_movies.append(movies.iloc[i[0]].title)
    
#     return recommended_movies

# st.title('Movie Recommender System')

# selected_movie_name = st.selectbox(
#     "Select a movie to get recommendations:",
#     movies_list)

# if st.button('Recommend'):
#     recommendations = recommend(selected_movie_name)
#     for i in recommendations:
#         st.write(i)






# import pickle
# import streamlit as st
# import requests

# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path

# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_movie_names = []
#     recommended_movie_posters = []
#     for i in distances[1:6]:
#         # fetch the movie poster
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         recommended_movie_names.append(movies.iloc[i[0]].title)

#     return recommended_movie_names,recommended_movie_posters


# st.header('Movie Recommender System')
# movies = pickle.load(open('model/movie_list.pkl','rb'))
# similarity = pickle.load(open('model/similarity.pkl','rb'))

# movie_list = movies['title'].values
# selected_movie = st.selectbox(
#     "Type or select a movie from the dropdown",
#     movie_list
# )

# if st.button('Show Recommendation'):
#     recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
#     col1, col2, col3, col4, col5 = st.beta_columns(5)
#     with col1:
#         st.text(recommended_movie_names[0])
#         st.image(recommended_movie_posters[0])
#     with col2:
#         st.text(recommended_movie_names[1])
#         st.image(recommended_movie_posters[1])

#     with col3:
#         st.text(recommended_movie_names[2])
#         st.image(recommended_movie_posters[2])
#     with col4:
#         st.text(recommended_movie_names[3])
#         st.image(recommended_movie_posters[3])
#     with col5:
#         st.text(recommended_movie_names[4])
#         st.image(recommended_movie_posters[4])




