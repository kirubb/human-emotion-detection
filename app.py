from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
from emotion_detector import EmotionDetector
from spotify_recommender import SpotifyRecommender

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Create upload folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize our emotion detector with the trained model
emotion_detector = EmotionDetector('best_emotion_model.h5')

# Initialize the Spotify recommender
spotify_recommender = SpotifyRecommender()


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/detect', methods=['POST'])
def detect_emotion():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Detect emotion in the image
        emotion = emotion_detector.predict(filepath)

        # Get song recommendation based on emotion
        song = spotify_recommender.get_recommendation(emotion)

        return render_template('result.html',
                               emotion=emotion,
                               song=song,
                               image_path=f"uploads/{filename}")  # ✅ Fixed path

    return jsonify({'error': 'Invalid file type'})


if __name__ == '__main__':
    app.run(debug=True)
