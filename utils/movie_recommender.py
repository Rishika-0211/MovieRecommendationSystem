import pandas as pd

# Load the dataset
movies_df = pd.read_csv('data/movies_metadata.csv.zip', low_memory=False)

def recommend_movies(emotion):
    # Define genre mapping based on emotions
    genre_dict = {
        'happy': 'Comedy',
        'sad': 'Drama',
        'angry': 'Action',
        'fear': 'Horror',
        'surprise': 'Thriller',
        'neutral': 'Drama'
    }
    # Get genre for the detected emotion
    genre = genre_dict.get(emotion, 'Comedy')

    # Filter movies based on the genre
    recommended_movies = movies_df[movies_df['genres'].str.contains(genre, case=False, na=False)]
    
    # Remove duplicates and get top 5 movies
    movies_list = recommended_movies[['title']].drop_duplicates().head(5).to_dict(orient='records')
    return movies_list