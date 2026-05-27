import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
stocks = pd.read_csv('data/stock_market.csv')

# Dataset Overview
print(stocks.head())
print(stocks.info())

# Daily Returns
stocks['Daily_Return'] = stocks['Close'].pct_change()

# Visualization 1
plt.figure(figsize=(10,5))
sns.lineplot(x='Date', y='Close', data=stocks)
plt.title('Stock Closing Prices')
plt.xticks(rotation=45)
plt.show()

# Visualization 2
plt.figure(figsize=(10,5))
sns.histplot(stocks['Daily_Return'].dropna(), kde=True)
plt.title('Daily Return Distribution')
plt.show()

# Visualization 3
plt.figure(figsize=(8,5))
sns.boxplot(x=stocks['Daily_Return'].dropna())
plt.title('Stock Return Outliers')
plt.show()

# Insights
print('Stock market shows volatility in daily returns.')
print('Long-term trends can help investment decisions.')