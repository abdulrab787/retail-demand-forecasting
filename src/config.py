from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data
RAW_DATA = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA = PROJECT_ROOT / "data" / "processed"

# Models
MODEL_PATH = PROJECT_ROOT / "models"

# Database
DB_USER = "postgres"
DB_PASSWORD = "Abdur123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "retail_forecasting"

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)