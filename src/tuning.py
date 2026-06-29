import sys
sys.path.append("src")

import pandas as pd
from pathlib import Path
from sklearn.model_selection import RandomizedSearchCV
from model_factory import get_model

DATA = Path("data/processed")
df = pd.read_csv(DATA / "forecast_features.csv", parse_dates=["date"])

TARGET = "sales"
DROP_COLUMNS = ["id", "date", "sales"]

numeric_features = df.select_dtypes(include=["int64", "float64", "bool"]).columns.tolist()
numeric_features = [c for c in numeric_features if c not in DROP_COLUMNS]

split_date = "2017-01-01"
train = df[df["date"] < split_date]
valid = df[df["date"] >= split_date]

X_train = train[numeric_features]
y_train = train[TARGET]

param_grid = {
    "max_depth": [4, 6, 8, 10],
    "learning_rate": [0.01, 0.03, 0.05, 0.1],
    "n_estimators": [300, 500, 800],
    "subsample": [0.7, 0.8, 0.9]
}

search = RandomizedSearchCV(
    estimator=get_model("xgboost"),
    param_distributions=param_grid,
    n_iter=12,
    scoring="neg_root_mean_squared_error",
    cv=3,
    random_state=42,
    n_jobs=-1
)
print("\nRunning hyperparameter tuning for XGBoost...")
search.fit(X_train, y_train)

best_model = search.best_estimator_
print("\nBest Parameters Found:")
print(search.best_params_)

#Save Tuned Model
import joblib
joblib.dump(best_model, "models/xgboost_tuned.pkl")
print("\nSaved tuned model → models/xgboost_tuned.pkl")