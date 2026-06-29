import sys
sys.path.append("src")

from pathlib import Path
import pandas as pd

DATA = Path("data/processed")
df = pd.read_csv(DATA / "forecast_features.csv")

print(df.shape)
print(df.head())

# Select Features
TARGET = "sales"
DROP_COLUMNS = ["id", "date", "sales"]

# Select numeric features only
numeric_features = df.select_dtypes(include=["int64", "float64", "bool"]).columns.tolist()
numeric_features = [col for col in numeric_features if col not in DROP_COLUMNS]

# Time-Based Train/Validation Split
split_date = "2017-01-01"

train = df[df["date"] < split_date]
valid = df[df["date"] >= split_date]

X_train = train[numeric_features]
X_valid = valid[numeric_features]

y_train = train[TARGET]
y_valid = valid[TARGET]

# Naïve Forecast
from evaluation import evaluate

naive_pred = valid["lag_1"]
metrics_naive = evaluate(y_valid, naive_pred)
print("Naive Forecast Metrics:", metrics_naive)

# Linear Regression
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

pred = model.predict(X_valid)

metrics_lr = evaluate(y_valid, pred)
print("Linear Regression Metrics:", metrics_lr)

# Visualization — Actual vs Predicted
from visualization import plot_predictions
plot_predictions(y_valid, pred)

# Feature Importance (Linear Regression)
import matplotlib.pyplot as plt
import pandas as pd

importance = pd.DataFrame({
    "Feature": X_train.columns,
    "Coefficient": model.coef_
})

top20 = importance.reindex(
    importance.Coefficient.abs().sort_values(ascending=False).index
).head(20)

plt.figure(figsize=(10,6))
plt.barh(top20["Feature"], top20["Coefficient"])
plt.title("Linear Regression Feature Importance")
plt.xlabel("Coefficient")
plt.gca().invert_yaxis()
plt.show()

# Save Baseline Model
import joblib
joblib.dump(model, "models/baseline.pkl")
print("Saved baseline model → models/baseline.pkl")

# Save Metrics
import json

baseline_metrics = {
    "naive": metrics_naive,
    "linear_regression": metrics_lr
}

with open("models/metrics.json", "w") as f:
    json.dump(baseline_metrics, f, indent=4)

print("Saved baseline metrics → models/metrics.json")
