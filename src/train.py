import sys
sys.path.append("src")

from pathlib import Path
import pandas as pd
import joblib
from evaluation import evaluate
from model_factory import get_model
import matplotlib.pyplot as plt
from visualization import plot_predictions

DATA = Path("data/processed")
df = pd.read_csv(DATA / "forecast_features.csv", parse_dates=["date"])

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

# Train All Models

results = {}

for name in ["linear", "xgboost", "lightgbm", "catboost"]:
    print(f"\nTraining {name}...")

    model = get_model(name)
    model.fit(X_train, y_train)

    pred = model.predict(X_valid)

    metrics = evaluate(y_valid, pred)
    results[name] = metrics


# Save model
    joblib.dump(model, f"models/{name}.pkl")
    print(f"Saved {name} → models/{name}.pkl")

    # Save prediction plot
    plot_predictions(y_valid, pred)
    plt.savefig(f"images/{name}_prediction.png")
    plt.close()

    # Save feature importance (tree models only)
    if hasattr(model, "feature_importances_"):
        importance = pd.DataFrame({
            "Feature": X_train.columns,
            "Importance": model.feature_importances_
        }).sort_values("Importance", ascending=False)

        importance.to_csv(f"models/{name}_feature_importance.csv", index=False)
        print(f"Saved {name} feature importance → models/{name}_feature_importance.csv")

#Save Metrics Comparison

comparison = pd.DataFrame(results).T
comparison.to_csv("models/metrics.csv", index=True)

print("\nSaved model comparison → models/metrics.csv")
print("\nTraining complete.")