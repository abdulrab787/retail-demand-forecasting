from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"

def test_predict():
    payload = {
        "store_nbr": 1,
        "family": "GROCERY I",
        "onpromotion": 0,
        "lag_1": 12.5,
        "lag_7": 10.2,
        "lag_14": 9.8,
        "lag_28": 8.7,
        "rolling_mean_7": 11.0,
        "rolling_mean_30": 10.5,
        "transactions": 150,
        "month": 7,
        "day_of_week": 3
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "forecast" in response.json()
