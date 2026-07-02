<p align="center">
  <img src="https://github.com/abdulrab787/retail-demand-forecasting/actions/workflows/ci.yml/badge.svg" alt="CI Status">
  <img src="https://img.shields.io/badge/Python-3.11-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-Production-green.svg" alt="FastAPI">
  <img src="https://img.shields.io/badge/MLflow-Model%20Registry-orange.svg" alt="MLflow">
  <img src="https://img.shields.io/badge/Docker-Ready-blue.svg" alt="Docker">
  <img src="https://img.shields.io/badge/Postgres-Database-blue.svg" alt="Postgres">
  <img src="https://img.shields.io/badge/PowerBI-Dashboard-yellow.svg" alt="Power BI">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>


# 📘 **Retail Demand Forecasting — End‑to‑End MLOps Project**

An end‑to‑end **Retail Demand Forecasting System** built using:

- **Python (FastAPI, MLflow, SHAP, CatBoost, LightGBM, XGBoost)**
- **Postgres SQL (Star Schema)**
- **Docker + Docker Compose**
- **GitHub Actions CI**
- **Power BI Dashboard**
- **MLflow Tracking + Model Registry**
- **Production‑grade Logging & Environment Variables**

This project demonstrates a complete **MLOps workflow** from raw data → ETL → feature engineering → model training → experiment tracking → model registry → API deployment → monitoring.

---

# 🏗️ **Architecture Overview**
```mermaid
flowchart TD
    A[Raw Data (Kaggle)] --> B[ETL Pipeline (Python + SQL)]
    B --> C[Feature Store (Postgres)]
    C --> D[Model Training (CatBoost, LightGBM, XGBoost)]
    D --> E[MLflow Tracking + Model Registry]
    E --> F[FastAPI Prediction Service]
    F --> G[Docker Deployment (API + DB)]
    G --> H[Power BI Dashboard]

```
                ┌──────────────────────────┐
                │        Raw Data          │
                └──────────────┬───────────┘
                               ▼
                    ┌──────────────────┐
                    │       ETL        │
                    │  (Python + SQL)  │
                    └──────────┬───────┘
                               ▼
                    ┌──────────────────┐
                    │  Feature Store   │
                    │ (Postgres SQL)   │
                    └──────────┬───────┘
                               ▼
                    ┌──────────────────┐
                    │   Model Training │
                    │ (CatBoost, LGBM) │
                    └──────────┬───────┘
                               ▼
                    ┌──────────────────┐
                    │   MLflow Tracking│
                    │   + Model Registry│
                    └──────────┬────────┘
                               ▼
                    ┌──────────────────┐
                    │   FastAPI        │
                    │   Prediction API │
                    └──────────┬────────┘
                               ▼
                    ┌──────────────────┐
                    │ Docker Compose   │
                    │ API + Postgres   │
                    └──────────┬────────┘
                               ▼
                    ┌──────────────────┐
                    │ Power BI Reports │
                    └──────────────────┘
```

---

# 📊 **Dataset Description**

Dataset: **Corporación Favorita Grocery Sales Forecasting (Kaggle)**  
Granularity: Daily sales per store per product family  
Key fields:

- `store_nbr`
- `family`
- `sales`
- `onpromotion`
- `transactions`
- `date`

Time range: **2013–2017**

---

# 🧱 **SQL Star Schema**

```md
```mermaid
erDiagram
    SALES_FACT {
        int date_key
        int store_key
        int item_key
        float sales
        int onpromotion
        int transactions
    }

    STORES_DIM {
        int store_key
        int store_nbr
        string city
        string state
        int cluster
    }

    ITEMS_DIM {
        int item_key
        string family
        int class
        bool perishable
    }

    CALENDAR_DIM {
        int date_key
        date date
        int day_of_week
        int month
        int year
        bool holiday_flag
    }

    SALES_FACT ||--|| STORES_DIM : "store_key"
    SALES_FACT ||--|| ITEMS_DIM : "item_key"
    SALES_FACT ||--|| CALENDAR_DIM : "date_key"

### **Fact Table: `sales_fact`**
- `date_key`
- `store_key`
- `item_key`
- `sales`
- `onpromotion`
- `transactions`

### **Dimension Tables**
#### `stores_dim`
- `store_key`
- `store_nbr`
- `city`
- `state`
- `cluster`

#### `items_dim`
- `item_key`
- `family`
- `class`
- `perishable`

#### `calendar_dim`
- `date_key`
- `date`
- `day_of_week`
- `month`
- `year`
- `holiday_flag`

---

# 🔄 **ETL Workflow**
```md
```mermaid
flowchart LR
    A[Raw CSV Files] --> B[Staging Layer]
    B --> C[Cleaning & Validation]
    C --> D[Feature Engineering]
    D --> E[Postgres Fact & Dimension Tables]

### **1. Raw → Staging**
- Load CSVs
- Normalize column names
- Convert date formats

### **2. Cleaning**
- Handle missing values
- Remove outliers
- Merge transactions

### **3. Transformations**
- Create lag features
- Create rolling windows
- Encode categorical variables
- Join dimension tables

### **4. Load into Postgres**
- Fact + dimension tables
- Indexes for fast querying

---

# 🧪 **Feature Engineering**

| Feature | Description |
|--------|-------------|
| `lag_1` | Sales 1 day ago |
| `lag_7` | Sales 7 days ago |
| `lag_14` | Sales 14 days ago |
| `rolling_mean_7` | 7‑day moving average |
| `rolling_mean_30` | 30‑day moving average |
| `onpromotion` | Promotion flag |
| `transactions` | Store traffic |
| `month` | Calendar month |
| `day_of_week` | Calendar weekday |

---

# 🤖 **Model Training & Comparison**

Models trained:

- **CatBoost**
- **LightGBM**
- **XGBoost**
- **Linear Regression**

Metrics stored in:

```
models/metrics.csv
```

### **Logged Metrics (MLflow)**

- MAE  
- RMSE  
- MAPE  
- RMSLE  
- Training time  
- Feature importance  

---

# 🔍 **SHAP Explainability**

SHAP plots generated:

- Summary plot  
- Bar plot  
- Dependence plots  

Insights:

- Lag features dominate prediction  
- Promotions significantly increase demand  
- Transactions correlate strongly with sales  

---

# ⚡ **FastAPI Prediction Service**

Endpoints:

### `GET /`
Health check

### `POST /predict`
Predict next‑day demand using MLflow model registry.

FastAPI loads:

```
models:/retail_forecasting_model/Production
```

CI uses a mock model for stability.

---

# 🐳 **Docker Usage**

### **Build & Run**

```
docker compose up --build
```

Services:

- `api` → FastAPI
- `postgres` → Database

---

# 📈 **MLflow Tracking & Model Registry**

Screenshots include:

- Experiment runs  
- Metrics  
- Artifacts  
- Registered models  
- Production model  

MLflow UI runs at:

```
http://127.0.0.1:5000
```



# 🧪 **GitHub Actions CI**

Badge:

```
![CI](https://github.com/<Abdurrab787>/<repo>/actions/workflows/ci.yml/badge.svg)
```

CI pipeline:

- Install dependencies  
- Run tests  
- Use mock MLflow model  
- Validate FastAPI endpoints  

---

# 📊 **Power BI Dashboard**

Includes:

- Store‑level forecasting  
- Family‑level trends  
- Promotions impact  
- Seasonal patterns  
- Drill‑through pages  

---

# 🛠️ **Project Structure**

retail-demand-forecasting/
│
├── app/
│   ├── main.py
│   ├── predictor.py
│   ├── logging_config.py

├── src/
│   ├── train.py
│   ├── etl.py
│   ├── features.py

├── tests/
│   ├── test_api.py
│
├── models/
│   ├── metrics.csv
│   ├── catboost.pkl

├── data/
├── database/
├── notebooks/
├── powerbi/
├── reports/

├── images/
│   ├── xgboost_prediction.png
│   ├── lightgbm_prediction.png
├── tests/
├── .github/

├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── LICENSE

# 🚀 **Future Improvements**

- Hyperparameter tuning (Optuna)
- Model monitoring (Prometheus + Grafana)
- Drift detection (Evidently AI)
- Batch inference pipeline
- Real‑time streaming (Kafka)
- Kubernetes deployment
- Feature Store (Feast)
- Automated retraining pipeline

# 📝 **License**

MIT License
