# app/schemas.py
from pydantic import BaseModel


class PredictionInput(BaseModel):
    store_nbr: int
    family: str
    onpromotion: int

    lag_1: float
    lag_7: float
    lag_14: float
    lag_28: float

    rolling_mean_7: float
    rolling_mean_30: float

    transactions: int

    month: int
    day_of_week: int
