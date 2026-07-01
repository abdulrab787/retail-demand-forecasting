# Model Overview

This document explains the structure of the Retail BI Forecasting Model.

---

## 🧩 Tables

### Date
- Full calendar
- Fiscal year logic
- Month, Quarter, Week
- Flags for YTD, MTD, WTD

### Stores
- Store ID
- Store Name
- Cluster
- Region

### Families
- Family ID
- Category
- Subcategory

### dashboard_dataset
- Sales
- Revenue
- Promotions
- Inventory
- Forecast values

---

## 🔗 Relationships

- Date[Date] → dashboard_dataset[Date]
- Stores[Store ID] → dashboard_dataset[Store ID]
- Families[Family ID] → dashboard_dataset[Family ID]

All relationships are **single-direction** for performance.

---

## 📁 Measures Table

Contains all business logic:

- Revenue
- Promotions
- Forecast accuracy
- Inventory risk
- KPIs
- Store performance

Organized into display folders for clarity.

---

## 🎨 Themes

- Ultra Dark Neon Theme v3
- Dark Glass Backgrounds
- Neon KPI Cards
- Neon Slicers
