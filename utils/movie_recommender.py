import pandas as pd

movies_df = pd.read_csv('data/movies_metadata.csv.zip', low_memory=False)


def recommend_movies(emotion):
    genre_dict = {
        'happy': 'Comedy',
        'sad': 'Drama',
        'angry': 'Action',
        'fear': 'Horror',
        'surprise': 'Thriller',
        'neutral': 'Drama'
    }

    genre = genre_dict.get(emotion, 'Comedy')

    recommended_movies = movies_df[movies_df['genres'].str.contains(genre, case=False, na=False)].drop_duplicates(subset=['title'])
    
    base_url = "https://image.tmdb.org/t/p/w500"
    movies_list = recommended_movies[['title', 'poster_path']].head(5).to_dict(orient='records')

    for movie in movies_list:
        poster_path = movie.get('poster_path')

        if isinstance(poster_path, str) and poster_path.strip() and poster_path.lower() not in ['nan', 'none']:
            if not poster_path.startswith('/'):
                poster_path = '/' + poster_path  # Ensure the path starts with "/"
            movie['poster_url'] = f"{base_url}{poster_path}"
        else:
            movie['poster_url'] = 'https://via.placeholder.com/200x300'  # Default image

    return movies_list
