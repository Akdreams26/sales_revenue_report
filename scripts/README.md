# Scripts Folder

This folder contains all Python scripts used for data analysis and visualization.

## Files

| File | Description |
|------|-------------|
| `sales_analysis.py` | Main analysis script — runs full pipeline |

## How to Run

```bash
# Install dependencies
pip install pandas numpy matplotlib seaborn

# Run the script
cd scripts
python sales_analysis.py
```

## What It Does
1. Loads `data/sales_data.csv`
2. Cleans and processes data
3. Calculates KPIs (Revenue, Profit, Orders)
4. Generates and saves 4 charts to `/images/`
5. Prints key business insights
