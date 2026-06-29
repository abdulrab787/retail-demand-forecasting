import pandas as pd

pred = pd.read_csv("data/processed/predictions.csv")
feat = pd.read_csv("data/processed/forecast_features.csv")

merged = pred.merge(
    feat[["date","store_nbr","family","onpromotion","transactions"]],
    on=["date","store_nbr","family"],
    how="left"
)

merged.to_csv("data/processed/dashboard_dataset.csv", index=False)
print("Dashboard dataset created → data/processed/dashboard_dataset.csv")
