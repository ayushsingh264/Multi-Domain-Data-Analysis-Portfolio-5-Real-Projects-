
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
covid = pd.read_csv('data/covid_data.csv')

# Dataset Overview
print(covid.head())
print(covid.info())

# Total Cases
print('Total Cases:', covid['Confirmed'].sum())
print('Total Deaths:', covid['Deaths'].sum())

# Visualization 1
plt.figure(figsize=(10,5))
sns.lineplot(x='Date', y='Confirmed', data=covid)
plt.title('COVID Confirmed Cases Over Time')
plt.xticks(rotation=45)
plt.show()

# Visualization 2
plt.figure(figsize=(10,5))
sns.lineplot(x='Date', y='Deaths', data=covid)
plt.title('COVID Death Cases Over Time')
plt.xticks(rotation=45)
plt.show()

# Visualization 3
plt.figure(figsize=(8,5))
sns.boxplot(x=covid['Confirmed'])
plt.title('Confirmed Cases Distribution')
plt.show()

# Insights
print('COVID cases increased rapidly during outbreak periods.')
print('Deaths are positively correlated with confirmed cases.')