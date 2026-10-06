import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("data.csv")
print("--- Initial Data Summary ---")
print(df.info())


# A. Handled Missing Values
if 'Calories' in df.columns:
    df['Calories'] = df['Calories'].fillna(df['Calories'].median())

df = df.dropna(subset=['Date'])
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date']) 

# B. Filter Rows
filtered_df = df[(df['Duration'] >= 30) & (df['Duration'] <= 120)].copy()

# C. Create New Columns
filtered_df['Pulse_Intensity_Ratio'] = (filtered_df['Pulse'] / filtered_df['Maxpulse']) * 100

print("\n--- Cleaned Data Preview ---")
print(filtered_df.head())

# ==========================================
# PART 2: DATA VISUALIZATION
# ==========================================
sns.set_theme(style="whitegrid")

# Plot 1: Histogram
plt.figure(figsize=(8, 4))
sns.histplot(filtered_df['Calories'], kde=True, color='salmon', bins=10)
plt.title('Distribution of Calories Burned', fontsize=14, fontweight='bold')
plt.xlabel('Calories')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Plot 2: Scatter Plot
plt.figure(figsize=(8, 5))
sns.scatterplot(data=filtered_df, x='Duration', y='Calories', hue='Pulse', palette='flare', s=100)
plt.title('Workout Duration vs Calories Burned', fontsize=14, fontweight='bold')
plt.xlabel('Duration (Minutes)')
plt.ylabel('Calories')
plt.tight_layout()
plt.show()

# Plot 3: Bar Plot
filtered_df['Date_Str'] = filtered_df['Date'].dt.strftime('%d-%b')
plt.figure(figsize=(12, 6))
sns.barplot(data=filtered_df, x='Date_Str', y='Maxpulse', color='royalblue')
plt.title('Daily Maximum Pulse Trend', fontsize=14, fontweight='bold')
plt.xlabel('Date')
plt.ylabel('Max Pulse')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()