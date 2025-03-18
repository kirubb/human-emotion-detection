# emotion_detector.py
import numpy as np
import cv2
from tensorflow.keras.models import load_model


class EmotionDetector:
    def __init__(self, model_path):
        self.model = load_model(model_path)
        # FER2013 emotion labels
        self.emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
        # Load the face detector
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def preprocess_image(self, image_path):
        # Read image
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) == 0:
            # If no face detected, process the entire image
            face_img = cv2.resize(gray, (64, 64))  # Changed from 48,48 to 64,64
        else:
            # Process the first detected face
            x, y, w, h = faces[0]
            face_img = gray[y:y + h, x:x + w]
            face_img = cv2.resize(face_img, (64, 64))  # Changed from 48,48 to 64,64

        # Normalize and reshape for the model
        face_img = face_img.astype("float") / 255.0
        face_img = np.expand_dims(face_img, axis=-1)  # Add channel dimension
        face_img = np.expand_dims(face_img, axis=0)  # Add batch dimension

        return face_img
    def predict(self, image_path):
        preprocessed_image = self.preprocess_image(image_path)
        predictions = self.model.predict(preprocessed_image)
        emotion_index = np.argmax(predictions[0])

        return self.emotions[emotion_index]