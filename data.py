import pandas as pd

import seaborn as sns

# Example seaborn style
sns.set(style='whitegrid')


# Load the dataset
try:
    df = pd.read_csv('path_to_your_dataset.csv')
except FileNotFoundError:
    print("File not found. Please check the path.")

# Display the first few rows
print(df.head())

# Check data types and missing values
print(df.info())
print(df.isnull().sum())

# Display the first few rows
print(df.head())

# Check data types and missing values
print(df.info())
print(df.isnull().sum())

# Fill or drop missing values
df.fillna(method='ffill', inplace=True)  # Example to forward fill

# task 2
# Describe numerical columns
print(df.describe())

# Example grouping by species
grouped = df.groupby('species').mean()
print(grouped)

# Example observation
# "The average petal length of species A is higher than species B."

# task 3
import matplotlib.pyplot as plt

# Example: Time-series data
plt.figure(figsize=(10, 5))
plt.plot(df['date'], df['sales'], marker='o')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Average petal length per species
df.groupby('species')['petal_length'].mean().plot(kind='bar', color='skyblue')
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length')
plt.show()

# Histogram of petal length
plt.figure(figsize=(8, 5))
df['petal_length'].hist(bins=20, color='purple', alpha=0.7)
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
plt.show()

# Scatter plot 

plt.figure(figsize=(8, 5))
plt.scatter(df['sepal_length'], df['petal_length'], alpha=0.5)
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.show()

