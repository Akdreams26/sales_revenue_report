# 📊 Sales & Revenue Analysis Dashboard
## Project Report — Data Analytics Internship

---

## Project Title
**Sales & Revenue Analysis Dashboard**

## One-Line Summary
Interactive dashboard to analyze sales performance, revenue trends, and business KPIs across products, regions, and customer segments for the year 2024.

---

## Overview

This project analyzes a synthetic retail sales dataset to identify revenue trends, top-performing products, regional sales patterns, and business growth opportunities using visual analytics and Python-based data analysis.

The project delivers:
- A cleaned, structured dataset (120 sales records)
- A Python analysis script and Jupyter Notebook
- 5 visualization charts (PNG)
- An interactive HTML dashboard

---

## Problem Statement

Businesses often struggle to track sales performance across multiple dimensions (product, region, time, customer segment) and identify specific areas for improvement. This project provides a centralized analytical view of key sales metrics to support data-driven decision-making.

**Core Questions Answered:**
1. Which product category drives the most revenue?
2. Which region has the highest sales growth?
3. What are the seasonal/monthly sales trends?
4. Which products are top performers?
5. How does profit margin vary across categories?

---

## Dataset Description

**File:** `data/sales_data.csv`
**Records:** 120 orders | **Period:** January–December 2024

| Column | Type | Description |
|--------|------|-------------|
| Order_ID | Integer | Unique order identifier |
| Product | String | Product name |
| Category | String | Electronics / Furniture / Stationery |
| Region | String | North / South / East / West |
| Sales_Amount | Float | Revenue in INR |
| Profit | Float | Profit in INR |
| Quantity | Integer | Units sold |
| Discount | Float | Discount rate applied |
| Order_Date | Date | Date of transaction |
| Customer_Segment | String | Corporate / Home Office / Retail |

---

## Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python 3.10 | Core programming language |
| Pandas | Data cleaning & manipulation |
| NumPy | Numerical calculations |
| Matplotlib | Static chart generation |
| Seaborn | Enhanced visualizations |
| Jupyter Notebook | Interactive analysis |
| HTML + Chart.js | Interactive dashboard |
| Power BI / Excel | (Optional) BI dashboard |

---

## Methodology

### 1. Data Cleaning
- Converted `Order_Date` from string to datetime
- Verified zero null values and zero duplicates
- Extracted derived columns: Month, Quarter, Year
- Calculated `Profit_Margin = (Profit / Sales_Amount) × 100`

### 2. KPI Calculation
| KPI | Value |
|-----|-------|
| Total Revenue | ₹5.48 Crore |
| Total Profit | ₹1.09 Crore |
| Total Orders | 120 |
| Total Units Sold | 2,847 |
| Avg Order Value | ₹45,686 |
| Avg Profit Margin | 20.0% |

### 3. Trend Analysis
- Monthly revenue trend plotted (Jan–Dec 2024)
- Q4 identified as peak quarter
- December recorded highest single-month revenue

### 4. Data Visualization
Five charts generated and saved as PNG files.

---

## Key Insights

1. **Electronics dominates** — contributed ~72% of total revenue
2. **North region** recorded the highest total revenue
3. **Q4 (Oct–Dec)** was the strongest quarter with ₹1.97 Cr revenue
4. **Laptop Pro** is the single highest-revenue product
5. **Corporate segment** contributes the most to revenue vs. Retail and Home Office
6. **Stationery** has the lowest revenue but highest volume of units sold
7. **20% consistent profit margin** across all categories

---

## Dashboard / Output

Open `dashboard/Sales_Dashboard.html` in any browser for the interactive version.

Charts available in the `images/` folder.

---

## How to Run This Project

### Option A — Python Script
```bash
pip install pandas numpy matplotlib seaborn
python scripts/sales_analysis.py
```

### Option B — Jupyter Notebook
```bash
pip install jupyter pandas numpy matplotlib seaborn
jupyter notebook notebooks/Sales_Analysis.ipynb
```

### Option C — Interactive Dashboard
```
Open dashboard/Sales_Dashboard.html in any web browser
```

### Option D — Power BI
```
1. Open Power BI Desktop
2. Get Data → CSV → select data/sales_data.csv
3. Build visuals using Category, Region, Month, and Sales_Amount columns
```

---

## Results & Conclusion

The project successfully delivers a complete sales analytics solution that provides clear, actionable insights into sales performance for 2024. The analysis confirms that Electronics is the primary revenue driver, Q4 shows seasonal peak demand, and the North region outperforms others.

The dashboard supports data-driven decision-making by making KPIs and trends instantly visible.

---

## Future Work

1. **Forecasting** — Implement ARIMA or Prophet models for next-quarter revenue prediction
2. **Real-time integration** — Connect to live POS or ERP database via APIs
3. **Customer Analytics** — RFM (Recency, Frequency, Monetary) segmentation
4. **Anomaly Detection** — Flag unusual sales dips or spikes automatically
5. **Power BI Enhancement** — Add drill-through reports and slicer filters

---

## Author & Contact

**Name:** Aakriti Mathur
**Degree:** B.Tech Computer Science Engineering
**Role:** Data Analytics Intern
**GitHub:** [Your GitHub Profile URL]
**LinkedIn:** [Your LinkedIn URL]
**Email:** [Your Email]

---

*This project was completed as part of a Data Analytics Internship in 2024.*
