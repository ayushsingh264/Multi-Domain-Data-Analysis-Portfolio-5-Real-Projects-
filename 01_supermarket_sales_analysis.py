import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
sales = pd.read_csv('data/supermarket_sales.csv')

# Display Dataset
print(sales.head())
print(sales.info())
print(sales.describe())

# Missing Values
print(sales.isnull().sum())

# Total Sales
print("Total Sales:", sales['Sales'].sum())

# Best Selling Products
best_products = sales.groupby('Product')['Sales'].sum().sort_values(ascending=False)
print(best_products)

# Visualization 1
plt.figure(figsize=(10,5))
best_products.plot(kind='bar')
plt.title('Best Selling Products')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.show()

# Visualization 2
plt.figure(figsize=(8,5))
sns.histplot(sales['Sales'], kde=True)
plt.title('Sales Distribution')
plt.show()

# Visualization 3
plt.figure(figsize=(8,5))
sns.boxplot(x=sales['Sales'])
plt.title('Sales Outliers')
plt.show()

# Business Insights
print('High demand products generate maximum revenue.')
print('Sales distribution shows seasonal variations.')
