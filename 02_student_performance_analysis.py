import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
students = pd.read_csv('data/student_performance.csv')

# Dataset Information
print(students.head())
print(students.info())

# Average Marks
print('Average Math Score:', students['math_score'].mean())
print('Average Reading Score:', students['reading_score'].mean())
print('Average Writing Score:', students['writing_score'].mean())

# Gender Analysis
gender_scores = students.groupby('gender')['math_score'].mean()
print(gender_scores)

# Visualization 1
plt.figure(figsize=(8,5))
sns.countplot(x='gender', data=students)
plt.title('Gender Distribution')
plt.show()

# Visualization 2
plt.figure(figsize=(8,5))
sns.scatterplot(x='reading_score', y='writing_score', data=students)
plt.title('Reading vs Writing Scores')
plt.show()

# Visualization 3
plt.figure(figsize=(8,5))
sns.heatmap(students.corr(), annot=True)
plt.title('Correlation Heatmap')
plt.show()

# Insights
print('Reading and writing scores are strongly correlated.')
print('Student performance differs across demographics.')

