from pathlib import Path
import pandas as pd

RAW_DATA_PATH = Path("data/raw")


def load_csv(filename: str) -> pd.DataFrame:
    """Load a CSV file from the raw data directory."""
    file_path = RAW_DATA_PATH / filename
    return pd.read_csv(file_path)


if __name__ == "__main__":
    train = load_csv("train.csv")
    print(train.head())