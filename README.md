# 📊 Sales & Revenue Analysis Dashboard

> **Data Analytics Internship Project** — Interactive dashboard to analyze sales performance, revenue trends, and business KPIs.

---

## 🗂️ Project Structure

```
Sales_Revenue_Analysis/
│
├── 📁 data/
│   ├── sales_data.csv          ← Main dataset (120 records, 2024)
│   └── README.md
│
├── 📁 logs/
│   ├── data_cleaning_log.txt   ← Data processing log
│   ├── analysis_log.txt        ← Analysis execution log
│   └── README.md
│
├── 📁 notebooks/
│   └── Sales_Analysis.ipynb    ← Full Jupyter Notebook analysis
│
├── 📁 scripts/
│   ├── sales_analysis.py       ← Python analysis script
│   └── README.md
│
├── 📁 dashboard/
│   └── Sales_Dashboard.html    ← Interactive HTML dashboard
│
├── 📁 images/
│   ├── monthly_revenue_trend.png
│   ├── category_revenue.png
│   ├── region_sales.png
│   ├── top_products.png
│   ├── quarterly_segment.png
│   └── README.md
│
├── 📁 project/
│   └── PROJECT_REPORT.md       ← Full project report
│
└── 📄 README.md                ← You are here
```

---

## 🎯 Objective

Build a complete sales analytics solution to:
- **Track KPIs** — Total Revenue, Profit, Orders, Avg Order Value
- **Identify trends** — Monthly, Quarterly, Seasonal patterns
- **Compare performance** — By Product, Category, Region, Customer Segment
- **Visualize insights** — Through charts and an interactive dashboard

---

## 📦 Dataset

**File:** `data/sales_data.csv`
**Records:** 120 transactions | **Year:** 2024 | **Products:** 30+

Columns: `Order_ID`, `Product`, `Category`, `Region`, `Sales_Amount`, `Profit`, `Quantity`, `Discount`, `Order_Date`, `Customer_Segment`

---

## 📊 Key KPIs

| Metric | Value |
|--------|-------|
| 💰 Total Revenue | ₹5.48 Crore |
| 📈 Total Profit | ₹1.09 Crore |
| 🛒 Total Orders | 120 |
| 📦 Units Sold | 2,847 |
| 💡 Profit Margin | 20.0% |
| 🏆 Top Category | Electronics |
| 🌍 Top Region | North |

---

## 🔍 Key Insights

- 📱 **Electronics** accounts for ~72% of total revenue
- 🗓️ **Q4 (Oct–Dec)** is the strongest quarter — ₹1.97 Cr
- 🥇 **Laptop Pro** is the best-selling product
- 🌍 **North** region leads in revenue across all categories
- 🏢 **Corporate** segment drives the highest revenue
- 📅 **December** recorded peak single-month sales

---

## 🚀 How to Run

### Python Script
```bash
pip install pandas numpy matplotlib seaborn
python scripts/sales_analysis.py
```

### Jupyter Notebook
```bash
pip install jupyter pandas numpy matplotlib seaborn
jupyter notebook notebooks/Sales_Analysis.ipynb
```

### Interactive Dashboard
```
Open dashboard/Sales_Dashboard.html in any browser — no installation needed!
```

---

## 🛠️ Tools & Technologies

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![HTML](https://img.shields.io/badge/HTML-Dashboard-red)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)

| Tool | Use |
|------|-----|
| Python | Core analysis language |
| Pandas | Data cleaning & aggregation |
| Matplotlib / Seaborn | Chart generation |
| Jupyter Notebook | Interactive analysis |
| HTML + Chart.js | Web dashboard |

---

## 📁 Expected Outcomes

✅ Data cleaning and preprocessing  
✅ KPI calculation (Revenue, Profit, Orders)  
✅ Monthly and quarterly trend analysis  
✅ Category, Region, and Product performance comparison  
✅ Customer segment analysis  
✅ Interactive HTML dashboard  
✅ Reusable Python script  

---

## 🔮 Future Work

- Add forecasting models (ARIMA / Prophet)
- Real-time data integration via APIs
- Advanced customer RFM segmentation
- Power BI version of the dashboard

---

## 👩‍💻 Author

**Aakriti Mathur**
B.Tech Computer Science Engineering | Data Analytics Intern

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black)](https://github.com/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/)

---

*⭐ If you found this project helpful, please give it a star!*
