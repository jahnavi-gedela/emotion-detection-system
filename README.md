# 😊 EmoVerse - Emotion Detection System

## Overview

EmoVerse is a Machine Learning and Flask-based web application that predicts human emotions from text input using Natural Language Processing (NLP). The application analyzes the user's text and identifies the corresponding emotion using a trained machine learning model.

## Features

- Detects emotions from user text
- Machine Learning based prediction
- Flask web application
- Clean and responsive user interface
- Uses NLP for text preprocessing
- Stores trained model for fast prediction

## Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML
- CSS
- JavaScript
- Joblib

## Machine Learning

- Text Preprocessing
- TF-IDF Vectorization
- Emotion Classification Model

## Project Structure

emotion-detection-system/
│
├── data/
│   └── history.json
│
├── dataset/
│   └── emotions.csv
│
├── model/
│   ├── emotion_model.pkl
│   └── vectorizer.pkl
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore

## Installation

Install the required libraries:

pip install -r requirements.txt

## Run the Application

Train the model:

python train_model.py

Run the Flask application:

python app.py

Open your browser and visit:

http://127.0.0.1:5000

## Output

- Predicts the emotion from the given text.
- Uses the trained machine learning model.
- Displays the detected emotion through a simple web interface.

## Future Enhancements

- User Login System
- Emotion History Dashboard
- Voice Emotion Detection
- Deep Learning Model
- Deploy the application online

## Author

Jahnavi Gedela

GitHub:
https://github.com/jahnavi-gedela
