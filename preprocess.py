import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("cyber_logs.csv")

# Convert categorical columns to numerical
cat_columns = ["proto", "service", "state", "attack_cat"]
encoder = LabelEncoder()
for col in cat_columns:
    df[col] = encoder.fit_transform(df[col])

# Save preprocessed data
df.to_csv("preprocessed_data.csv", index=False)
print("✅ Data Preprocessed and Saved as 'preprocessed_data.csv'")
