import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
data = pd.read_csv("dataset/emotions.csv")

X = data["text"]
y = data["emotion"]

# Convert text to numbers
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression()
model.fit(X_vectorized, y)

# Save model & vectorizer
pickle.dump(model, open("model/emotion_model.pkl", "wb"))
pickle.dump(vectorizer, open("model/vectorizer.pkl", "wb"))

print("✅ Model trained successfully!")
