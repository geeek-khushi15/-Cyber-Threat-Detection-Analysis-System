import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report

# Load test data
df = pd.read_csv("preprocessed_data.csv")
X = df.drop(columns=["label"])  # Features
y = df["label"]  # Target

# Load trained model
model = joblib.load("models/random_forest.pkl")

# Make predictions
y_pred = model.predict(X)

# Evaluate
print("\n🔹 Accuracy:", accuracy_score(y, y_pred))
print("\n📌 Classification Report:\n", classification_report(y, y_pred))
