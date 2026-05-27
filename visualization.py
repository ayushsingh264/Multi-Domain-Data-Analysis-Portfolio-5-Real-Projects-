
import matplotlib.pyplot as plt
import seaborn as sns


def bar_chart(df, x, y, title):
    plt.figure(figsize=(10,5))
    sns.barplot(x=x, y=y, data=df)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.show()


def line_chart(df, x, y, title):
    plt.figure(figsize=(10,5))
    sns.lineplot(x=x, y=y, data=df)
    plt.title(title)
    plt.show()


def heatmap(df, title):
    plt.figure(figsize=(10,6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title(title)
    plt.show()