import pandas as pd
import numpy as np
from config import RAW_DATA
from pathlib import Path

# Load Dataset
sales = pd.read_csv(RAW_DATA / "train.csv", parse_dates=["date"])
stores = pd.read_csv(RAW_DATA / "stores.csv")
holidays = pd.read_csv(RAW_DATA / "holidays_events.csv", parse_dates=["date"])
transactions = pd.read_csv(RAW_DATA / "transactions.csv", parse_dates=["date"])

# Merge Datasets
df = sales.merge(stores, on="store_nbr", how="left")
df = df.merge(transactions, on=["date", "store_nbr"], how="left")
df = df.merge(holidays, on="date", how="left")

# Calendar Features
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
df["day_of_week"] = df["date"].dt.dayofweek
df["week_of_year"] = df["date"].dt.isocalendar().week.astype(int)
df["quarter"] = df["date"].dt.quarter
df["is_weekend"] = (df["day_of_week"] >= 5).astype(int)

# Lag Features
df = df.sort_values(["store_nbr", "family", "date"])
df["lag_1"] = df.groupby(["store_nbr", "family"])["sales"].shift(1)
df["lag_7"] = df.groupby(["store_nbr", "family"])["sales"].shift(7)
df["lag_14"] = df.groupby(["store_nbr", "family"])["sales"].shift(14)
df["lag_28"] = df.groupby(["store_nbr", "family"])["sales"].shift(28)

# Rolling Features
df["rolling_mean_7"] = df.groupby(["store_nbr", "family"])["sales"].transform(lambda x: x.shift(1).rolling(7).mean())
df["rolling_std_7"] = df.groupby(["store_nbr", "family"])["sales"].transform(lambda x: x.shift(1).rolling(7).std())
df["rolling_mean_30"] = df.groupby(["store_nbr", "family"])["sales"].transform(lambda x: x.shift(1).rolling(30).mean())

# Promotion Features
df["promotion_flag"] = (df["onpromotion"] > 0).astype(int)
df["promotion_ratio"] = df["onpromotion"] / (df["onpromotion"] + 1)

#Holiday Features
holidays = holidays.rename(columns={
    "type": "holiday_type",
    "locale": "holiday_locale",
    "locale_name": "holiday_locale_name",
    "description": "holiday_description",
    "transferred": "holiday_transferred"
})

df = df.merge(holidays, on="date", how="left")

df["is_holiday"] = (df["holiday_type"].notna()).astype(int)
df = pd.get_dummies(df, columns=["holiday_type"], dummy_na=True)

# Store Features
store_avg = df.groupby("store_nbr")["sales"].mean()
df["store_avg_sales"] = df["store_nbr"].map(store_avg)

family_avg = df.groupby("family")["sales"].mean()
df["family_avg_sales"] = df["family"].map(family_avg)


# Handle missing values safely by dtype
num_cols = df.select_dtypes(include=["float64", "int64"]).columns
df[num_cols] = df[num_cols].fillna(0)

# String columns → fill with empty string
str_cols = df.select_dtypes(include=["string", "object"]).columns
df[str_cols] = df[str_cols].fillna("")

# Boolean columns → fill with False
bool_cols = df.select_dtypes(include=["bool"]).columns
df[bool_cols] = df[bool_cols].fillna(False)


print("RUNNING CORRECT FILE")

# Save Output
OUTPUT = RAW_DATA.parent.parent / "data" / "processed"
OUTPUT.mkdir(exist_ok=True)

df.to_csv(OUTPUT / "forecast_features.csv", index=False)

