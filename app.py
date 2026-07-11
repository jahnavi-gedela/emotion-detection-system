import json
from datetime import datetime
import os
from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model/emotion_model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

def save_history(emotion):
    """Save emotion prediction to history.json"""
    history_file = "data/history.json"
    
    # Load existing history or create new list
    if os.path.exists(history_file):
        with open(history_file, "r") as f:
            history = json.load(f)
    else:
        history = []
    
    # Add new entry
    entry = {
        "emotion": emotion,
        "timestamp": datetime.now().isoformat()
    }
    history.append(entry)
    
    # Save updated history
    with open(history_file, "w") as f:
        json.dump(history, f, indent=4)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.form["text"]
    text_vector = vectorizer.transform([text])

    emotion = model.predict(text_vector)[0]
    probs = model.predict_proba(text_vector)[0]
    labels = model.classes_

    emotion_scores = dict(zip(labels, probs))

    save_history(emotion)   # 👈 THIS LINE IS MUST
    quotes = {
        "happy": "Keep spreading your positive energy 🌞",
        "sad": "This moment will pass. You are strong 💙",
        "stress": "Breathe. One step at a time 🌿",
        "angry": "Pause. Calmness is power 🌱",
        "calm": "Peace looks good on you ✨"
    }

    responses = {
        "happy": f"You're radiating joy! {quotes['happy']}",
        "sad": f"It's okay to feel down sometimes. {quotes['sad']}",
        "stress": f"Take a deep breath. {quotes['stress']}",
        "angry": f"Channel that energy positively. {quotes['angry']}",
        "calm": f"Embrace the tranquility. {quotes['calm']}"
    }

    return jsonify({
        "emotion": emotion,
        "message": responses[emotion],
        "quote": quotes[emotion],
        "scores": emotion_scores
    })





@app.route("/clear_history", methods=["POST"])
def clear_history():
    with open("data/history.json", "w") as f:
        json.dump([], f)
    return jsonify({"status": "cleared"})


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
