from fastapi import FastAPI
from app.logging_config import setup_logging
from app.predictor import MLflowModelLoader
import logging

# Initialize logging
setup_logging()
logger = logging.getLogger(__name__)

# Initialize FastAPI
app = FastAPI(
    title="Retail Demand Forecast API",
    version="1.0.0"
)

# Load MLflow model (Production stage)
model = MLflowModelLoader(model_name="retail_forecasting_model")

@app.get("/")
def home():
    logger.info("Home endpoint called")
    return {"message": "Retail Forecasting API is running"}

@app.post("/predict")
def predict(payload: dict):
    logger.info(f"Prediction request received: {payload}")
    prediction = model.predict(payload)
    logger.info(f"Prediction result: {prediction}")
    return {"prediction": prediction}
