import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv("cyber_logs.csv")

# Ensure attack categories and protocol values are not null
df["attack_cat"].fillna("Unknown", inplace=True)

# Set Seaborn Style
sns.set(style="whitegrid")

# 📊 1. Attack Type Distribution
plt.figure(figsize=(12, 6))
attack_counts = df["attack_cat"].value_counts()

ax = sns.barplot(y=attack_counts.index, x=attack_counts.values, palette="viridis")
plt.title("📊 Attack Type Distribution", fontsize=14)
plt.xlabel("Count", fontsize=12)
plt.ylabel("Attack Category", fontsize=12)

for index, value in enumerate(attack_counts.values):
    plt.text(value + 100, index, f"{value / df.shape[0] * 100:.2f}%", va="center", fontsize=10)

plt.show()

# 📊 2. Protocol vs Attack Type
plt.figure(figsize=(14, 8))
top_protocols = df["proto"].value_counts().index[:10]
df_filtered = df[df["proto"].isin(top_protocols)]

ax = sns.histplot(data=df_filtered, y="proto", hue="attack_cat", multiple="stack", palette="magma")
plt.title("📡 Protocol vs Attack Type", fontsize=14)
plt.xlabel("Count", fontsize=12)
plt.ylabel("Protocol", fontsize=12)
plt.legend(title="Attack Category", loc="upper right", bbox_to_anchor=(1.3, 1))
plt.show()

# 📊 3. Top 10 Source Ports (Potential Entry Points)
plt.figure(figsize=(12, 6))
top_src_ports = df["sport"].value_counts().nlargest(10)

sns.barplot(x=top_src_ports.index, y=top_src_ports.values, palette="coolwarm")
plt.title("🔌 Top 10 Source Ports", fontsize=14)
plt.xlabel("Source Port", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.show()

# 📊 4. Top 10 Destination Ports (Targeted Services)
plt.figure(figsize=(12, 6))
top_dst_ports = df["dsport"].value_counts().nlargest(10)

sns.barplot(x=top_dst_ports.index, y=top_dst_ports.values, palette="coolwarm")
plt.title("🎯 Top 10 Destination Ports", fontsize=14)
plt.xlabel("Destination Port", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.show()

# 📊 5. Packet Count Analysis (Sent vs Received)
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x="attack_cat", y="spkts", palette="Blues")
plt.title("📦 Sent Packets Distribution by Attack Type", fontsize=14)
plt.xlabel("Attack Category", fontsize=12)
plt.ylabel("Sent Packets", fontsize=12)
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x="attack_cat", y="dpkts", palette="Oranges")
plt.title("📩 Received Packets Distribution by Attack Type", fontsize=14)
plt.xlabel("Attack Category", fontsize=12)
plt.ylabel("Received Packets", fontsize=12)
plt.xticks(rotation=45)
plt.show()

# 📊 6. State Distribution of Network Traffic
plt.figure(figsize=(12, 6))
sns.countplot(y=df["state"], order=df["state"].value_counts().index, palette="Set2")
plt.title("📊 State Distribution of Network Traffic", fontsize=14)
plt.xlabel("Count", fontsize=12)
plt.ylabel("State", fontsize=12)
plt.show()

# 📊 7. Correlation Heatmap (Feature Relationships)
plt.figure(figsize=(10, 8))
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns  # Select only numeric columns
corr_matrix = df[numeric_cols].corr()

sns.heatmap(corr_matrix, annot=False, cmap="coolwarm", linewidths=0.5)
plt.title("🔥 Feature Correlation Heatmap", fontsize=14)
plt.show()

# 📊 8. Time-Series Attack Trends (If 'timestamp' column exists)
if "timestamp" in df.columns:
    df["timestamp"] = pd.to_datetime(df["timestamp"])  # Convert to datetime
    df["date"] = df["timestamp"].dt.date  # Extract date for grouping

    attack_trends = df.groupby("date")["attack_cat"].value_counts().unstack().fillna(0)

    plt.figure(figsize=(14, 6))
    attack_trends.plot(kind="line", marker="o", colormap="tab10", figsize=(14, 6))
    plt.title("⏳ Time-Series Trend of Attacks", fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Attack Count", fontsize=12)
    plt.legend(title="Attack Category", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.grid()
    plt.show()
