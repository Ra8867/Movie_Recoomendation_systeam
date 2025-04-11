🎬 Movie Recommendation System
This is a content-based and similarity-based Movie Recommendation System built with Python, Pandas, and Streamlit. It recommends movies based on a selected movie using a precomputed similarity matrix.

📌 Features
🔍 Recommend top 5 similar movies based on selected movie
📊 Uses cosine similarity for recommendations
🧠 Model trained on movie metadata (titles, genres, etc.)
🌐 Simple web interface using Streamlit
💾 Data stored and loaded using Pickle
🚀 How it Works
Load preprocessed movie data (movie.pkl)
Load precomputed similarity matrix (similarity.pkl)
When a user selects a movie, find similar movies using cosine similarity
Display top 5 recommended titles on the web app
📦 Requirements
Install dependencies from requirements.txt:

pip install -r requirements.txt
