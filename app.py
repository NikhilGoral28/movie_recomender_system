from flask import Flask, render_template, request
import pickle
import requests

app = Flask(__name__)

# Load data
final_movies = pickle.load(open("model/final_movies.pkl", "rb"))
cosine_similarity = pickle.load(open("model/cosine_sim.pkl", "rb"))

# Preprocessing
final_movies['title_lower'] = final_movies['title'].str.lower().str.strip()

from urllib.parse import quote


def fetch_poster(title):
    api_key = '54100729'
    title_encoded = quote(title)
    
    # First try exact match
    url = f"http://www.omdbapi.com/?t={title_encoded}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    
    if data.get("Response") == "True" and data.get("Poster") != "N/A":
        return data["Poster"]
    
    # Fallback: use search and take the first result
    search_url = f"http://www.omdbapi.com/?s={title_encoded}&apikey={api_key}"
    search_response = requests.get(search_url).json()
    
    if search_response.get("Response") == "True":
        first_match = search_response["Search"][0]
        imdb_id = first_match["imdbID"]
        
        # Get full details using imdbID
        movie_url = f"http://www.omdbapi.com/?i={imdb_id}&apikey={api_key}"
        movie_data = requests.get(movie_url).json()
        
        if movie_data.get("Poster") and movie_data["Poster"] != "N/A":
            return movie_data["Poster"]
    
    # Final fallback image
    return "https://via.placeholder.com/200x300?text=No+Image"



"""
def fetch_poster(title):
    OMDb_API ='54100729'
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDb_API}"
    response = requests.get(url)
    data = response.json()
    if 'Poster' in data and data['Poster'] != 'N/A':
        return data['Poster']
    else:
        return "https://via.placeholder.com/200x300?text=No+Image"
    
"""



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_name = request.form.get('movie_name').strip().lower()

    if movie_name not in final_movies['title_lower'].values:
        return render_template('index.html', error="Movie not found. Please try another one.")

    movie_index = final_movies[final_movies['title_lower'] == movie_name].index[0]
    similar_movies = list(enumerate(cosine_similarity[movie_index]))
    sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:11]

    recommended_movies = []
    for i in sorted_similar_movies:
        movie_data = final_movies.iloc[i[0]].to_dict()
        movie_data['poster'] = fetch_poster(movie_data['title'])
        recommended_movies.append(movie_data)


    return render_template('index.html', movies=recommended_movies, movie_name=final_movies.iloc[movie_index]['title'])

if __name__ == '__main__':
    app.run(debug=True)
