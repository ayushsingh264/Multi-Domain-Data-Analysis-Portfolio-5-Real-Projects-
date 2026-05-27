import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load Dataset
house = pd.read_csv('data/house_prices.csv')

# Dataset Info
print(house.head())
print(house.info())

# Feature Selection
X = house[['Area', 'Bedrooms', 'Bathrooms']]
y = house['Price']

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Accuracy
mae = mean_absolute_error(y_test, predictions)
print('Mean Absolute Error:', mae)

# Visualization 1
plt.figure(figsize=(8,5))
sns.scatterplot(x=y_test, y=predictions)
plt.title('Actual vs Predicted Prices')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.show()

# Visualization 2
plt.figure(figsize=(8,5))
sns.histplot(house['Price'], kde=True)
plt.title('House Price Distribution')
plt.show()

# Visualization 3
plt.figure(figsize=(8,5))
sns.heatmap(house.corr(), annot=True)
plt.title('Correlation Heatmap')
plt.show()

# Insights
print('Area has strong impact on house prices.')
print('Linear Regression predicts prices effectively.')