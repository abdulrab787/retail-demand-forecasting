import sys
sys.path.append("src")

import pandas as pd
from pathlib import Path

DATA = Path("data/processed")
df = pd.read_csv(DATA / "forecast_features.csv", parse_dates=["date"])

TARGET = "sales"
DROP_COLUMNS = ["id", "date", "sales"]

numeric_features = df.select_dtypes(include=["int64", "float64", "bool"]).columns.tolist()
numeric_features = [c for c in numeric_features if c not in DROP_COLUMNS]

X = df[numeric_features]

output_path = DATA / "model_features.csv"
X.to_csv(output_path, index=False)

print("Saved →", output_path)
print("Shape:", X.shape)
print("Columns:", len(X.columns))
