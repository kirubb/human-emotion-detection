# 🎵 Human Emotion Detection with Music Recommendation
This project detects human emotions using a pre-trained .h5 model and recommends songs based on the detected mood. It utilizes Flask for the backend, integrates the Spotify API for music recommendations, and uses TensorFlow/Keras to load the emotion detection model.

## 🚀 Tech Stack

### 🎯 Backend
Flask – To create the web server and handle the API calls.
Spotify API – For fetching and recommending mood-based songs.
TensorFlow/Keras – To load the .h5 model for emotion detection.

### 🎯 Model Creation
OpenCV – For image processing and face detection.
NumPy – For numerical operations.
Pandas – For data manipulation.
Matplotlib – For visualization and model evaluation.
TensorFlow/Keras – For building and training the emotion detection model.

## 🛠️ Installation and Setup
### 1️⃣ Clone the Repository
First, clone the repository to your local machine:

git clone https://github.com/kirubb/human-emotion-detection.git
cd human-emotion-detection

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
Creating a virtual environment helps isolate the project dependencies:


#### For Windows
python -m venv venv
venv\Scripts\activate

#### For Linux/Mac
python3 -m venv venv
source venv/bin/activate

### 3️⃣ Install Dependencies
Install the required Python libraries:

pip install -r requirements.txt

## 🔥 Running the Application
Once the dependencies are installed, run the Flask server:

python app.py
The application will be available at:
👉 http://127.0.0.1:5000

## 🎧 How It Works
Emotion Detection:

The app uses a test image for emotion detection.
The .h5 model classifies the emotion (e.g., happy, sad, angry, etc.).
Music Recommendation:

Based on the detected emotion, the app uses the Spotify API to suggest mood-appropriate songs.


## Jupyter Notebook where training was done is added for reference
