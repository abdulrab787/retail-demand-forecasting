import os
import mlflow
import pandas as pd
import logging

logger = logging.getLogger(__name__)

class MLflowModelLoader:
    def __init__(self, model_name: str, stage: str = "Production"):
        self.model_name = model_name
        self.stage = stage

        # CI mode → use mock model
        if os.getenv("CI") == "true":
            logger.info("CI mode detected — using mock model instead of MLflow.")
            self.model = self._mock_model()
        else:
            logger.info(f"Loading MLflow model: {model_name} (stage: {stage})")
            self.model = self._load_mlflow_model()

    def _mock_model(self):
        class MockModel:
            def predict(self, df):
                return [123.45]  # Dummy prediction for CI
        return MockModel()

    def _load_mlflow_model(self):
        model_uri = f"models:/{self.model_name}/{self.stage}"
        logger.info(f"MLflow model URI: {model_uri}")
        return mlflow.pyfunc.load_model(model_uri)

    def predict(self, data: dict):
        df = pd.DataFrame([data])
        logger.info(f"Running prediction on: {data}")
        result = self.model.predict(df)[0]
        logger.info(f"Prediction output: {result}")
        return result
