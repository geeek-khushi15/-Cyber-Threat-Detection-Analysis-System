import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Ensure the 'models' directory exists
os.makedirs("models", exist_ok=True)

# Load preprocessed data
df = pd.read_csv("preprocessed_data.csv")

# Split into features & labels
X = df.drop(columns=["label"])  # Features
y = df["label"]  # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "models/random_forest.pkl")
print("✅ Model Trained & Saved in 'models/random_forest.pkl'!")

# Evaluate
y_pred = model.predict(X_test)
print("\n🔹 Accuracy:", accuracy_score(y_test, y_pred))
print("\n📌 Classification Report:\n", classification_report(y_test, y_pred))
