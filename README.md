# Retail Demand Forecasting

## Business Problem

Forecast daily product demand for multiple retail stores to optimize inventory and reduce stock-outs.

## Objectives

- SQL analytics
- Time-series forecasting
- Feature engineering
- Machine learning
- Explainable AI
- Power BI dashboard

## Tech Stack

- Python
- SQL
- Pandas
- Scikit-learn
- XGBoost
- Prophet
- SHAP
- Power BI

## Dataset

The project uses the Kaggle "Store Sales - Time Series Forecasting" dataset.

### Files

- train.csv
- test.csv
- stores.csv
- transactions.csv
- holidays_events.csv
- oil.csv

## Baseline Forecasting

Models evaluated:

- Naïve Forecast
- Linear Regression

Metrics:

- MAE
- RMSE
- RMSLE
- MAPE

The baseline establishes a benchmark before introducing advanced gradient boosting models.

## Forecasting Models

The project compares multiple machine learning models:

- Linear Regression
- XGBoost
- LightGBM
- CatBoost

Performance is evaluated using:

- MAE
- RMSE
- RMSLE
- MAPE

The best-performing model is selected for deployment.

### Business Goal

Forecast daily sales for every store and product family to optimize inventory planning.