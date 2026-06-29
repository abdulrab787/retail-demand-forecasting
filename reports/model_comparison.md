# **Model Comparison Report**

This report summarizes the performance of all baseline and machine learning models trained for the Retail Demand Forecasting project.

---

## **📊 Model Performance Summary**

| Model             | RMSE        | MAE         | MAPE        | RMSLE       |
|------------------|-------------|-------------|-------------|-------------|
| Linear Regression | 365.86      | 106.97      | 978.06      | 1.18876     |
| **XGBoost**       | **250.91**  | **61.63**   | 209.46      | **0.66194** |
| LightGBM          | 254.28      | 67.15       | **191.76**  | 0.82729     |
| CatBoost          | 253.50      | 68.60       | 264.84      | 0.86378     |

---

## **🏆 Selected Production Model: XGBoost**

### **Reason for Selection**

XGBoost is selected as the production model because it demonstrates:

- **Lowest RMSE** → Best overall accuracy  
- **Lowest MAE** → Most stable error distribution  
- **Lowest RMSLE** → Best performance on skewed retail sales  
- **Consistent predictions** across stores and families  
- **Fast inference** suitable for real‑time or batch forecasting  
- **Strong feature importance interpretability**  

Although LightGBM achieved the lowest MAPE, XGBoost provides the best balance across *all* metrics, making it the most reliable model for production deployment.

---

## **📈 Visual Comparison**

Prediction plots saved in:

```
images/xgboost_prediction.png
images/lightgbm_prediction.png
images/catboost_prediction.png
images/linear_prediction.png
```

Feature importance plots saved in:

```
images/xgboost_feature_importance.png
images/lightgbm_feature_importance.png
images/catboost_feature_importance.png
```

---

## **📦 Saved Models**

All trained models are stored in:

```
models/linear.pkl
models/xgboost.pkl
models/lightgbm.pkl
models/catboost.pkl
models/xgboost_tuned.pkl   ← after tuning
