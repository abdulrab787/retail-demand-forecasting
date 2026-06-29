import sys
sys.path.append("src")

import joblib
import pandas as pd
from pathlib import Path

from feature_engineering import build_features  # if you have this
# or from preprocessing import preprocess

MODEL_PATH = Path("models/xgboost.pkl")
DATA_PATH = Path("data/processed/forecast_features.csv")

def load_model():
    return joblib.load(MODEL_PATH)

def load_data():
    df = pd.read_csv(DATA_PATH, parse_dates=["date"])
    return df

def run_inference(df):
    # here you’d select numeric_features same as in train.py
    DROP_COLUMNS = ["id", "date", "sales"]
    numeric_features = df.select_dtypes(include=["int64", "float64", "bool"]).columns.tolist()
    numeric_features = [c for c in numeric_features if c not in DROP_COLUMNS]

    X = df[numeric_features]

    model = load_model()
    preds = model.predict(X)
    return preds

if __name__ == "__main__":
    df = load_data()
    preds = run_inference(df)
    print("Inference complete. Sample predictions:", preds[:10])
