# **Forecast Diagnostics Report**

## **1. Overview**

This report summarizes diagnostic findings from the retail demand forecasting model.  
The analysis covers:

- Forecast error by store  
- Forecast error by product family  
- Residual distribution  
- Residual vs predicted  
- Business implications  
- Recommended improvements  

These diagnostics help identify systematic bias, volatility, and feature gaps.

---

## **2. Forecast Error by Store**

store‑level error chart shows clear patterns:

### **Key Findings**
- **Store 6** shows **consistent underprediction** (positive mean residuals).  
- Stores **2, 3, 4, 5, 7, and 8** show **consistent overprediction** (negative residuals).  
- Store‑level behavior is not uniform — each store has its own demand signature.

### **Business Interpretation**
- Store 6 may have unique demand drivers:  
  - Local events  
  - Higher traffic  
  - Stronger promotion response  
  - Stockout patterns  
- Other stores may have stable, predictable patterns.

### **Recommendation**
- Add **store‑specific features**:  
  - store_cluster  
  - store_avg_sales  
  - store_promotion_intensity  
- Consider **store‑level models** or **hierarchical forecasting**.


## **3. Forecast Error by Product Family**

family‑level error chart shows large variation across categories.

### **Key Findings**
- **Prepared Foods** → large negative residuals → model **overpredicts**.  
- **Players & Electronics** → large positive residuals → model **underpredicts**.  
- **Beverages** → high volatility → needs stronger seasonality and weather features.  
- **Dairy, Bakery, Produce** → moderate residuals → stable families.

### **Business Interpretation**
Different families behave differently:

- Electronics respond strongly to promotions.  
- Beverages respond to weather and seasonality.  
- Prepared Foods may have operational constraints (freshness, stockouts).  

### **Recommendation**
**family‑specific features**:

- Weather (temperature, rainfall)  
- Holiday × Family interactions  
- Promotion intensity per family  
- Family‑level seasonality (month × family)

## **4. Residual Distribution**

Your residual histogram shows:

### **Key Findings**
- Most residuals cluster tightly around zero.  
- Very few extreme errors.  
- Slight right‑skew → occasional underprediction on high‑volume days.

### **Business Interpretation**
The model is:

- Stable  
- Unbiased  
- Well‑calibrated  

The slight skew suggests:

- High‑volume days (holidays, promotions) need better feature engineering.

### **Recommendation**

- holiday_type  
- promotion_duration  
- promotion_ratio  
- rolling_mean_30  
- lag_28  


## **5. Residual vs Predicted**

### **Key Findings**
- Residuals are randomly scattered around zero.  
- No funnel shape → no heteroscedasticity.  
- No curved pattern → no major non‑linear gaps.  
- No systematic bias at high or low predicted values.

### **Business Interpretation**
The model generalizes well across:

- Low‑volume stores  
- High‑volume stores  
- All product families  

This is a sign of a strong forecasting model.

### **Recommendation**
Focus improvements on **specific families and stores**, not the entire model.

## **6. Combined Insights**

### ✔ Weekly seasonality is strong  
Lag features and rolling averages dominate SHAP importance.

### ✔ Promotions drive large spikes  
Promotion_flag and promotion_ratio are major contributors.

### ✔ Store traffic matters  
Transactions is one of the top features.

### ✔ Family‑level behavior varies  
Some families need additional engineered features.

### ✔ Model is stable and unbiased  
Residual distribution and scatter plot confirm this.

## **7. Recommended Enhancements**

### **Feature Engineering**
- Holiday interactions  
- Weather features  
- Promotion intensity  
- Store‑level embeddings  
- Family‑level seasonality  
- Rolling volatility features (rolling_std_7)

### **Modeling**
- Tune XGBoost further  
- Try CatBoost with categorical boosting  
- Consider LightGBM with monotonic constraints  
- Explore hierarchical forecasting (Store → Family → SKU)

### **Business**
- Investigate Store 6 operational patterns  
- Review Prepared Foods forecasting process  
- Improve promotion planning for Electronics and Beverages

