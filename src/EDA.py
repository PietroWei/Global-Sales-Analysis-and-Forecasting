import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('../data/processed_train.csv')

# Plot sales trends
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x='Date', y='Weekly_Sales')
plt.title('Weekly Sales Trends')
plt.show()

# Additional EDA steps...