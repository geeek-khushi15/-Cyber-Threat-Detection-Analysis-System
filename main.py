import pandas as pd

# Load dataset
df = pd.read_csv("cyber_logs.csv")

print("✅ Data Loaded Successfully")
print(df.head())  # Display first 5 rows
print("\n📌 Columns:", df.columns.tolist())  # List of columns
print("\n🔹 Attack Category Counts:\n", df["attack_cat"].value_counts())  # Frequency of attack types
