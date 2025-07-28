import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

#Load Data
print("Loading dataset...")
df = pd.read_csv(
    "energy_data.csv", 
    sep=';', 
    low_memory=False, 
    na_values='?',
    parse_dates={'Datetime': ['Date', 'Time']},
    infer_datetime_format=True
)

#Preprocess
print("Preprocessing data...")
df.dropna(inplace=True)
df = df.set_index('Datetime')
df = df.astype('float64')

# Filter data for faster training 
df = df['2007-02-01':'2007-02-02']  # use 2 days of data

# Feature Engineering
print("Extracting time features...")
df['hour'] = df.index.hour
df['day'] = df.index.day
df['weekday'] = df.index.weekday
df['month'] = df.index.month

#Target and Features
target = 'Global_active_power'
features = ['hour', 'day', 'weekday', 'month']

X = df[features]
y = df[target]

#Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Training Models
print("Training Linear Regression model...")
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

print("Training Random Forest model...")
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

#Evaluation
def evaluate(y_true, y_pred, model_name):
    print(f"\n--- {model_name} ---")
    print(f"RMSE: {np.sqrt(mean_squared_error(y_true, y_pred)):.4f}")
    print(f"R^2 Score: {r2_score(y_true, y_pred):.4f}")

evaluate(y_test, y_pred_lr, "Linear Regression")
evaluate(y_test, y_pred_rf, "Random Forest")

#Visualization for Random Forest
plt.figure(figsize=(12, 5))
plt.plot(y_test.values[:200], label="Actual", linewidth=2)
plt.plot(y_pred_rf[:200], label="Predicted (RF)", linestyle='--')
plt.title("Energy Consumption Forecasting (First 200 samples)")
plt.xlabel("Time Index")
plt.ylabel("Global Active Power (kilowatts)")
plt.legend()
plt.tight_layout()
plt.show()


# Visualization for Linear Regression
plt.figure(figsize=(12, 5))
plt.plot(y_test.values[:200], label="Actual", linewidth=2)
plt.plot(y_pred_lr[:200], label="Predicted (Linear Regression)", linestyle='--', color='orange')
plt.title("Energy Consumption Forecasting (First 200 samples) - Linear Regression")
plt.xlabel("Time Index")
plt.ylabel("Global Active Power (kilowatts)")
plt.legend()
plt.tight_layout()
plt.show()

