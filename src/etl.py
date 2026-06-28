import pandas as pd

from config import RAW_DATA
from database import get_engine
from logger import logger

engine = get_engine()

files = {
    "sales": "train.csv",
    "stores": "stores.csv",
    "transactions": "transactions.csv",
    "oil": "oil.csv",
    "holidays": "holidays_events.csv"
}

for table, file in files.items():

    logger.info(f"Loading {file}")

    df = pd.read_csv(RAW_DATA / file)

    df.to_sql(
        table,
        engine,
        if_exists="append",
        index=False
    )

    logger.info(f"{table} loaded successfully.")