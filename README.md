# Walmart Store Sales Analysis and Forecasting

## Description
This project focuses on analyzing Walmart store sales and forecasting future sales using machine learning techniques. Using the "Walmart Recruiting - Store Sales Forecasting" dataset available on Kaggle, we will explore sales trends, identify key factors influencing sales, and build predictive models to improve business decision-making.

## Dataset
The dataset used in this project is available on Kaggle: [Walmart Recruiting - Store Sales Forecasting](https://www.kaggle.com/competitions/walmart-recruiting-store-sales-forecasting). It is recommended to download the dataset and upload it to the project directory on GitHub.

## Project Structure
- `data/`: Contains the dataset.
- `notebooks/`: Contains Jupyter notebooks for analysis and modeling.
- `src/`: Contains source code for data preprocessing, model building, and evaluation.
- `README.md`: This file.

## Requirements
- Python 3.x
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn

## Instructions
1. Download the dataset from Kaggle and upload it to the `data/` directory.
2. Run the Jupyter notebooks in the `notebooks/` directory for exploratory data analysis and model building.
3. Use the code in the `src/` directory for data preprocessing and model evaluation.

## Algorithms and Evaluation
In this project, we use the following machine learning algorithms to forecast Walmart store sales:

1. **Linear Regression**: A simple linear approach to model the relationship between the dependent variable (sales) and one or more independent variables.
2. **Random Forest Regressor**: An ensemble learning method that operates by constructing multiple decision trees during training and outputting the mean prediction of the individual trees.

### Evaluation Metrics
To evaluate the performance of our models, we use the following metrics:

- **Mean Absolute Error (MAE)**: Measures the average magnitude of the errors in a set of predictions, without considering their direction.
- **Mean Squared Error (MSE)**: Measures the average of the squares of the errors, giving more weight to larger errors.
- **Root Mean Squared Error (RMSE)**: The square root of the mean squared error, providing an error metric in the same units as the target variable.
- **R-squared (R2 Score)**: Represents the proportion of the variance for the dependent variable that's explained by the independent variables in the model.

## Author
Pietro Gazzi

## License
This project is licensed under the MIT License. See the LICENSE file for more details.