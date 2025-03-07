import pandas as pd
import numpy as np

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(df):
    # Example preprocessing steps
    df['Date'] = pd.to_datetime(df['Date'])
    df.fillna(0, inplace=True)
    return df

if __name__ == "__main__":
    data = load_data('data/train.csv')
    processed_data = preprocess_data(data)
    processed_data.to_csv('data/processed_train.csv', index=False)