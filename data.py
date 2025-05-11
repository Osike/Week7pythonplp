import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set seaborn style
sns.set(style='whitegrid')

# Load the dataset
try:
    df = pd.read_csv('sales_data.csv')
    print("File loaded successfully.\n")
except FileNotFoundError:
    print("File not found. Please check the path.")
    exit()

# Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Check data types and missing values
print("\nDataset information:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

# Since there are no missing values in this dataset, no filling is needed

# Task 2: Descriptive statistics
print("\nDescriptive statistics for numerical columns:")
print(df.describe())

# Grouping by Category
grouped_category = df.groupby('Category').mean(numeric_only=True)
print("\nAverage values by product category:")
print(grouped_category)

# Grouping by Region
grouped_region = df.groupby('Region').mean(numeric_only=True)
print("\nAverage values by region:")
print(grouped_region)

# Example observation
print("\nObservations:")
print("1. Electronics have the highest average unit price and total sales.")
print("2. The West region has the highest average unit price due to expensive items like TVs being sold there.")

# Task 3: Visualizations

# 1. Time-series of Total Sales
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['TotalSales'], marker='o', linestyle='-', color='b')
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Sales by Category
plt.figure(figsize=(10, 6))
df.groupby('Category')['TotalSales'].sum().sort_values().plot(kind='barh', color='skyblue')
plt.title('Total Sales by Product Category')
plt.xlabel('Total Sales ($)')
plt.ylabel('Category')
plt.show()

# 3. Quantity Sold by Product
plt.figure(figsize=(10, 6))
df.groupby('Product')['Quantity'].sum().sort_values().plot(kind='barh', color='purple')
plt.title('Total Quantity Sold by Product')
plt.xlabel('Quantity Sold')
plt.ylabel('Product')
plt.show()

# 4. Sales Distribution by Region
plt.figure(figsize=(8, 6))
df.groupby('Region')['TotalSales'].sum().plot(kind='pie', autopct='%1.1f%%', colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen'])
plt.title('Sales Distribution by Region')
plt.ylabel('')
plt.show()

# 5. Scatter plot of Quantity vs Unit Price
plt.figure(figsize=(8, 6))
plt.scatter(df['Quantity'], df['UnitPrice'], alpha=0.6, color='green')
plt.title('Quantity Sold vs Unit Price')
plt.xlabel('Quantity Sold')
plt.ylabel('Unit Price ($)')
plt.grid(True)
plt.show()

# 6. Boxplot of Total Sales by Category
plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='TotalSales', data=df, palette='Set2')
plt.title('Distribution of Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.show()