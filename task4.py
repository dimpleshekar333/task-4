import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
file_path=r"C:\Users\Dimple.S\Downloads\data (1).csv"
df = pd.read_csv(file_path)

# Drop the empty column
df = df.drop(columns=["Unnamed: 32"], errors="ignore")

# Basic info
print("Shape of dataset:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nMissing values:\n", df.isnull().sum())
print("\nClass distribution:\n", df["diagnosis"].value_counts())

# Statistical summary
print("\nStatistical summary:\n", df.describe())

# Visualization: count of diagnoses
sns.countplot(x="diagnosis", data=df)
plt.title("Diagnosis Distribution (Benign vs Malignant)")
plt.show()

# Correlation heatmap
plt.figure(figsize=(12,8))
sns.heatmap(df.corr(), cmap="coolwarm")
plt.title("Correlation Heatmap of Features")
plt.show()