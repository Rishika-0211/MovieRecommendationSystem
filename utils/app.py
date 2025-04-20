from flask import Flask, render_template, request
import os
from utils.emotion_detector import detect_emotion
from utils.movie_recommender import recommend_movies

app = Flask(_name_)

UPLOAD_FOLDER = 'static/uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the folder exists

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    
    file_path = os.path.join(UPLOAD_FOLDER, "uploaded_image.jpg")
    file.save(file_path)  

    emotion = detect_emotion(file_path)  # Detect emotion from the image
    movies = recommend_movies(emotion)   # Get movie recommendations

    return render_template('index.html', emotion=emotion, movies=[m['title'] for m in movies])


if _name_ == '_main_':
    app.run(debug=True)