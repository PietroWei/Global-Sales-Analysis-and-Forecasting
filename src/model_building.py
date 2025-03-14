from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib
import pandas as pd
import numpy as np
import os

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    print(f'Mean Absolute Error: {mae}')
    joblib.dump(model, 'models/sales_forecast_model.pkl')

if __name__ == "__main__":
    data = pd.read_csv('data/processed_train.csv')
    X = data.drop(columns=['Weekly_Sales'])
    y = data['Weekly_Sales']
    train_model(X, y)