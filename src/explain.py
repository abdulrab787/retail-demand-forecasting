import sys
sys.path.append("src")

import matplotlib
matplotlib.use("Agg")   # Required for Windows

import shap
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure images folder exists
os.makedirs("images", exist_ok=True)

# Load Model
model = joblib.load("models/xgboost.pkl")

# Load Features (correct spelling!)
df = pd.read_csv("data/processed/forecast_features.csv", parse_dates=["date"])

# Select numeric features only (same as training)
DROP_COLUMNS = ["id", "date", "sales"]
numeric_features = df.select_dtypes(include=["int64", "float64", "bool"]).columns.tolist()
numeric_features = [c for c in numeric_features if c not in DROP_COLUMNS]

X = df[numeric_features]

# SHAP cannot handle millions of rows → sample
X_sample = X.sample(5000, random_state=42)

# SHAP Explainer
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_sample)

# SHAP Summary Plot
shap.summary_plot(shap_values, X_sample, show=False)
plt.savefig("images/shap_summary.png", dpi=300, bbox_inches="tight")
plt.close()

# SHAP Bar Plot
shap.summary_plot(shap_values, X_sample, plot_type="bar", show=False)
plt.savefig("images/shap_bar.png", dpi=300, bbox_inches="tight")
plt.close()

# SHAP Dependence Plots
important_features = [
    "lag_1",
    "lag_7",
    "rolling_mean_7",
    "transactions",
    "promotion_flag",
    "month"
]

for feature in important_features:
    shap.dependence_plot(feature, shap_values, X_sample, show=False)
    plt.savefig(f"images/shap_dependence_{feature}.png", dpi=300, bbox_inches="tight")
    plt.close()

print("SHAP analysis complete. Plots saved to images/")
