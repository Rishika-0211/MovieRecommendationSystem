from deepface import DeepFace

def detect_emotion(image_path):
    results = DeepFace.analyze(img_path=image_path, actions=['emotion'])

    if isinstance(results, list):
       
        dominant_emotion = results[0]['dominant_emotion']
    else:
        
        dominant_emotion = results['dominant_emotion']
    
    return dominant_emotion