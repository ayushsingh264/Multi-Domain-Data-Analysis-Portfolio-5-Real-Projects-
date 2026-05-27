import pandas as pd


def load_dataset(path):
    df = pd.read_csv(path)
    return df


def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()
    return df


def dataset_info(df):
    print("Shape:", df.shape)
    print("Columns:")
    print(df.columns)
    print("Missing Values:")
    print(df.isnull().sum())

