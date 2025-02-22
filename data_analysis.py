import pandas as pd

def analyze_attacks(df):
    """Analyzes attack categories in the dataset."""
    try:
        # ✅ Use "attack_cat" instead of "attack_type"
        attack_counts = df["attack_cat"].value_counts()
        
        print("\n📌 Most Frequent Attack Types:")
        print(attack_counts)
        
        return attack_counts
    except KeyError:
        print("❌ Error: 'attack_cat' column not found in the dataset.")
        return None
