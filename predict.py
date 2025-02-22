import pandas as pd
import joblib

# Load the trained model
model = joblib.load("models/random_forest.pkl")

# Load new data for prediction
new_data = pd.read_csv("new_logs.csv")  # Replace with actual input data file

# Ensure features match the training dataset
features = [col for col in new_data.columns if col not in ["attack_cat", "label"]]
X_new = new_data[features]

# Make predictions
predictions = model.predict(X_new)

# Add predictions to the dataset
new_data["Predicted_Label"] = predictions
new_data["Prediction_Result"] = new_data["Predicted_Label"].apply(lambda x: "Attack" if x == 1 else "Normal")

# Save the results
new_data.to_csv("predicted_results.csv", index=False)

print("✅ Prediction completed. Results saved in 'predicted_results.csv'.")
