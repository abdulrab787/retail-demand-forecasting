import sys
sys.path.append("src")

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import joblib
from pathlib import Path

# Load model and data
model = joblib.load("models/xgboost.pkl")

DATA = Path("data/processed")
df = pd.read_csv(DATA / "forecast_features.csv", parse_dates=["date"])

TARGET = "sales"
DROP_COLUMNS = ["id", "date", "sales"]

numeric_features = df.select_dtypes(include=["int64", "float64", "bool"]).columns.tolist()
numeric_features = [c for c in numeric_features if c not in DROP_COLUMNS]

# Train/valid split
split_date = "2017-01-01"
train = df[df["date"] < split_date]
valid = df[df["date"] >= split_date]

X_valid = valid[numeric_features]
y_valid = valid[TARGET]

# Predictions
pred = model.predict(X_valid)

# Forecast Diagnostics
results = pd.DataFrame()
results["actual"] = y_valid.values
results["predicted"] = pred
results["residual"] = results["actual"] - results["predicted"]

# Store Error Metrics
store_error = (
    results
    .groupby(valid["store_nbr"])
    ["residual"]
    .mean()
)

plt.figure(figsize=(12,6))
store_error.plot(kind="bar")
plt.title("Average Forecast Error by Store")
plt.xlabel("Store Number")
plt.ylabel("Mean Residual (Actual - Predicted)")
plt.tight_layout()
plt.savefig("images/forecast_error_store.png", dpi=300)
plt.close()

# Product Family Error Metrics
family_error = (
    results
    .groupby(valid["family"])
    ["residual"]
    .mean()
)

plt.figure(figsize=(14,6))
family_error.sort_values().plot(kind="bar")
plt.title("Forecast Error by Product Family")
plt.xlabel("Family")
plt.ylabel("Mean Residual")
plt.tight_layout()
plt.savefig("images/forecast_error_family.png", dpi=300)
plt.close()

# Residual Distribution
plt.figure(figsize=(10,6))
plt.hist(results["residual"], bins=50, color="steelblue", edgecolor="black")
plt.title("Residual Distribution")
plt.xlabel("Residual")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("images/residual_distribution.png", dpi=300)
plt.close()

# Residual vs Prediction
plt.figure(figsize=(10,6))
plt.scatter(results["predicted"], results["residual"], alpha=0.3)
plt.title("Residual vs Predicted")
plt.xlabel("Predicted Sales")
plt.ylabel("Residual (Actual - Predicted)")
plt.axhline(0, color="red", linestyle="--")
plt.tight_layout()
plt.savefig("images/residual_vs_prediction.png", dpi=300)
plt.close()

#  Export Executive Power BI Dataset

export_df = valid.copy()

export_df["actual"] = results["actual"].values
export_df["predicted"] = results["predicted"].values
export_df["residual"] = results["residual"].values

export_df.to_csv("data/processed/predictions.csv", index=False)

print("Executive Power BI dataset saved → data/processed/predictions.csv")

print("Diagnostics complete. Plots saved to images/")
