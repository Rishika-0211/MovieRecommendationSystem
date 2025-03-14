from flask import Flask, render_template, request
from utils.emotion_detector import detect_emotion
from utils.movie_recommender import recommend_movies

app = Flask(_name_)

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
    
    file.save("uploaded_image.jpg")  
    emotion = detect_emotion("uploaded_image.jpg")
    movies = recommend_movies(emotion)
    
    return render_template('index.html', emotion=emotion, movies=movies)

if _name_ == '_main_':
    app.run(debug=True)