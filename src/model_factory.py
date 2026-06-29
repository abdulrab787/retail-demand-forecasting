from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor

def get_model(name):
    if name == "linear":
        return LinearRegression()

    elif name == "xgboost":
        return XGBRegressor(
            n_estimators=500,
            learning_rate=0.05,
            max_depth=8,
            subsample=0.8,
            colsample_bytree=0.8,
            random_state=42
        )

    elif name == "lightgbm":
        return LGBMRegressor(
            n_estimators=500,
            learning_rate=0.05,
            max_depth=8,
            random_state=42
        )

    elif name == "catboost":
        return CatBoostRegressor(
            iterations=500,
            learning_rate=0.05,
            depth=8,
            verbose=False,
            random_seed=42
        )

    else:
        raise ValueError(f"Unknown model: {name}")
