# 📊 Walmart Store Sales Analysis and Forecasting

![Walmart Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Walmart_logo.svg/1200px-Walmart_logo.svg.png)

## 📝 Description
This project focuses on analyzing Walmart store sales and forecasting future sales using machine learning techniques. Using the "Walmart Recruiting - Store Sales Forecasting" dataset available on Kaggle, we will explore sales trends, identify key factors influencing sales, and build predictive models to improve business decision-making.

## 📂 Dataset
The dataset used in this project is available on Kaggle: [Walmart Recruiting - Store Sales Forecasting](https://www.kaggle.com/competitions/walmart-recruiting-store-sales-forecasting). It is recommended to download the dataset and upload it to the project directory on GitHub.

## 🗂️ Project Structure
```
├── 📁 data/               # Contains the dataset
├── 📁 notebooks/          # Contains Jupyter notebooks for analysis and modeling
├── 📁 src/                # Contains source code for data preprocessing, model building, and evaluation
└── 📄 README.md           # This file
```

## 📦 Requirements
- Python 3.x
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- XGBoost
- CatBoost

## 🚀 Instructions
1. **Download the dataset** from Kaggle and upload it to the `data/` directory.
2. **Run the Jupyter notebooks** in the `notebooks/` directory for exploratory data analysis and model building.
3. **Use the code** in the `src/` directory for data preprocessing and model evaluation.

## 🤖 Algorithms and Evaluation
In this project, we use the following machine learning algorithms to forecast Walmart store sales:

1. **Linear Regression**: A simple linear approach to model the relationship between the dependent variable (sales) and one or more independent variables.
2. **Random Forest Regressor**: An ensemble learning method that operates by constructing multiple decision trees during training and outputting the mean prediction of the individual trees.
3. **Gradient Boosting Regressor**: An ensemble technique that builds models sequentially, each new model correcting errors made by the previous ones.
4. **Extra Trees Regressor**: An ensemble method that fits multiple randomized decision trees and averages their predictions.
5. **XGBoost Regressor**: An optimized gradient boosting library designed to be highly efficient and flexible.
6. **CatBoost Regressor**: A gradient boosting algorithm that handles categorical features automatically and efficiently.
7. **Stacking Regressor**: An ensemble learning technique that combines multiple regression models via a meta-regressor.

### 📈 Evaluation Metrics
To evaluate the performance of our models, we use the following metrics:

- **Mean Absolute Error (MAE)**: Measures the average magnitude of the errors in a set of predictions, without considering their direction.
- **Mean Squared Error (MSE)**: Measures the average of the squares of the errors, giving more weight to larger errors.
- **Root Mean Squared Error (RMSE)**: The square root of the mean squared error, providing an error metric in the same units as the target variable.
- **R-squared (R2 Score)**: Represents the proportion of the variance for the dependent variable that's explained by the independent variables in the model.

### Hyperparameter Tuning
To improve the performance of the Extra Trees Regressor, we performed hyperparameter tuning using Grid Search with 5-fold cross-validation. The parameter grid included variations in the number of estimators, maximum depth, and minimum samples required to split an internal node.

The best parameters found were:
- `n_estimators`: 100
- `max_depth`: 15
- `min_samples_split`: 5

This tuning process helped in optimizing the model's performance by finding the best combination of hyperparameters.

## 📊 Results and Conclusion

### Results
The table below summarizes the R2 scores obtained from different models used in this project:

| Model                     | R2 Score |
|---------------------------|----------|
| Linear Regression         | 0.0486   |
| Random Forest Regressor   | 0.7459   |
| Gradient Boosting Regressor | 0.6941 |
| Extra Trees Regressor     | 0.8539   |
| XGBoost Regressor         | 0.7388   |
| CatBoost Regressor        | 0.7800   |

### Conclusion
From the results, it is evident that the **Extra Trees Regressor** performed the best in terms of R2 score, followed by the **Random Forest Regressor** and **CatBoost Regressor**. These models are capable of capturing complex patterns in the data due to their ensemble nature and ability to handle non-linear relationships.

- **Extra Trees Regressor**: This model achieved the highest R2 score, indicating its effectiveness in capturing the variance in the data. Its ability to average multiple randomized decision trees contributes to its high accuracy.
- **Random Forest Regressor**: This model also performed well, leveraging the power of multiple decision trees to improve prediction accuracy.
- **CatBoost Regressor**: This model is specifically designed to handle categorical features efficiently, making it suitable for this dataset.

The linear regression model, while simple and interpretable, did not perform as well as the ensemble methods due to its inability to capture non-linear relationships in the data.

Overall, the use of advanced ensemble techniques and hyperparameter tuning significantly improved the forecasting accuracy, making them the preferred choice for this project.

## 📚 Cited Articles
Here are some articles related to the algorithms used in this project:

1. **Linear Regression**:
   - Seber, G. A. F., & Lee, A. J. (2012). Linear Regression Analysis (Vol. 936). John Wiley & Sons.

2. **Random Forest Regressor**:
   - Breiman, L. (2001). Random forests. Machine Learning, 45(1), 5-32.

3. **Gradient Boosting Regressor**:
   - Friedman, J. H. (2001). Greedy function approximation: A gradient boosting machine. Annals of Statistics, 1189-1232.

4. **Extra Trees Regressor**:
   - Geurts, P., Ernst, D., & Wehenkel, L. (2006). Extremely randomized trees. Machine Learning, 63(1), 3-42.

5. **XGBoost Regressor**:
   - Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. In Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 785-794).

6. **CatBoost Regressor**:
   - Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A. V., & Gulin, A. (2018). CatBoost: unbiased boosting with categorical features. In Advances in Neural Information Processing Systems (pp. 6638-6648).

7. **Stacking Regressor**:
   - Wolpert, D. H. (1992). Stacked generalization. Neural Networks, 5(2), 241-259.

## 👤 Author
Pietro Gazzi

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for more details.

