"""
=============================================================
  Sales & Revenue Analysis Dashboard - Python Script
  Author  : Aakriti Kumari | B.Tech CSE Student
  Project : Data Analytics Internship
=============================================================
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────
DATA_PATH   = '../data/sales_data.csv'
OUTPUT_PATH = '../images/'
os.makedirs(OUTPUT_PATH, exist_ok=True)

sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 12
COLORS = ['#2196F3', '#FF9800', '#4CAF50', '#E91E63']

# ─────────────────────────────────────────────
# 1. LOAD DATA
# ─────────────────────────────────────────────
def load_data(path):
    df = pd.read_csv(path)
    df['Order_Date']   = pd.to_datetime(df['Order_Date'])
    df['Month']        = df['Order_Date'].dt.month
    df['Month_Name']   = df['Order_Date'].dt.strftime('%b')
    df['Quarter']      = df['Order_Date'].dt.quarter.map({1:'Q1',2:'Q2',3:'Q3',4:'Q4'})
    df['Year']         = df['Order_Date'].dt.year
    df['Profit_Margin']= (df['Profit'] / df['Sales_Amount'] * 100).round(2)
    print(f"✅ Data loaded: {df.shape[0]} rows × {df.shape[1]} columns")
    return df

# ─────────────────────────────────────────────
# 2. PRINT KPIs
# ─────────────────────────────────────────────
def print_kpis(df):
    print("\n" + "=" * 50)
    print("         📊 KEY PERFORMANCE INDICATORS")
    print("=" * 50)
    print(f"  Total Revenue     : ₹{df['Sales_Amount'].sum():>15,.0f}")
    print(f"  Total Profit      : ₹{df['Profit'].sum():>15,.0f}")
    print(f"  Total Orders      : {df['Order_ID'].nunique():>16,}")
    print(f"  Total Units Sold  : {df['Quantity'].sum():>16,}")
    print(f"  Avg Order Value   : ₹{df['Sales_Amount'].mean():>15,.0f}")
    print(f"  Avg Profit Margin : {df['Profit_Margin'].mean():>15.1f}%")
    print("=" * 50)

# ─────────────────────────────────────────────
# 3. PLOT MONTHLY TREND
# ─────────────────────────────────────────────
def plot_monthly_trend(df):
    month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    monthly = df.groupby('Month_Name')[['Sales_Amount','Profit']].sum().reindex(month_order)

    fig, ax = plt.subplots()
    ax.plot(monthly.index, monthly['Sales_Amount'], marker='o', lw=2.5,
            color='#2196F3', label='Revenue', markersize=8)
    ax.plot(monthly.index, monthly['Profit'], marker='s', lw=2.5,
            color='#4CAF50', label='Profit', markersize=8)
    ax.fill_between(monthly.index, monthly['Sales_Amount'], alpha=0.1, color='#2196F3')
    ax.set_title('Monthly Revenue & Profit Trend (2024)', fontsize=15, fontweight='bold')
    ax.set_xlabel('Month'); ax.set_ylabel('Amount (INR)')
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x,_: f'₹{x/1e5:.1f}L'))
    ax.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_PATH + 'monthly_revenue_trend.png', dpi=150, bbox_inches='tight')
    plt.show()
    print(f"  Peak month: {monthly['Sales_Amount'].idxmax()}")

# ─────────────────────────────────────────────
# 4. PLOT CATEGORY REVENUE
# ─────────────────────────────────────────────
def plot_category(df):
    cat = df.groupby('Category')['Sales_Amount'].sum().sort_values(ascending=False)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    bars = ax1.bar(cat.index, cat.values, color=COLORS[:len(cat)], edgecolor='white')
    for b, v in zip(bars, cat.values):
        ax1.text(b.get_x()+b.get_width()/2, b.get_height()+30000,
                 f'₹{v/1e5:.1f}L', ha='center', fontweight='bold')
    ax1.set_title('Revenue by Category', fontsize=14, fontweight='bold')
    ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x,_: f'₹{x/1e5:.0f}L'))

    ax2.pie(cat.values, labels=cat.index, autopct='%1.1f%%',
            colors=COLORS[:len(cat)], startangle=90)
    ax2.set_title('Category Share (%)', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(OUTPUT_PATH + 'category_revenue.png', dpi=150, bbox_inches='tight')
    plt.show()

# ─────────────────────────────────────────────
# 5. PLOT REGION SALES
# ─────────────────────────────────────────────
def plot_region(df):
    region = df.groupby('Region')[['Sales_Amount','Profit']].sum().sort_values('Sales_Amount', ascending=True)
    fig, ax = plt.subplots()
    y = range(len(region))
    ax.barh(y, region['Sales_Amount'], height=0.4, color='#2196F3', label='Revenue')
    ax.barh([i+0.4 for i in y], region['Profit'], height=0.4, color='#4CAF50', label='Profit')
    ax.set_yticks([i+0.2 for i in y]); ax.set_yticklabels(region.index)
    ax.set_title('Revenue & Profit by Region', fontsize=14, fontweight='bold')
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x,_: f'₹{x/1e5:.0f}L'))
    ax.legend(); plt.tight_layout()
    plt.savefig(OUTPUT_PATH + 'region_sales.png', dpi=150, bbox_inches='tight')
    plt.show()

# ─────────────────────────────────────────────
# 6. PLOT TOP PRODUCTS
# ─────────────────────────────────────────────
def plot_top_products(df):
    top = df.groupby('Product')['Sales_Amount'].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots()
    c = plt.cm.Blues(np.linspace(0.4, 0.9, len(top)))[::-1]
    bars = ax.bar(top.index, top.values, color=c)
    for b, v in zip(bars, top.values):
        ax.text(b.get_x()+b.get_width()/2, b.get_height()+15000,
                f'₹{v/1e5:.1f}L', ha='center', fontsize=9, fontweight='bold')
    ax.set_title('Top 10 Products by Revenue', fontsize=14, fontweight='bold')
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x,_: f'₹{x/1e5:.0f}L'))
    plt.xticks(rotation=45, ha='right'); plt.tight_layout()
    plt.savefig(OUTPUT_PATH + 'top_products.png', dpi=150, bbox_inches='tight')
    plt.show()

# ─────────────────────────────────────────────
# 7. PRINT INSIGHTS
# ─────────────────────────────────────────────
def print_insights(df):
    print("\n" + "=" * 55)
    print("         🔍 KEY BUSINESS INSIGHTS")
    print("=" * 55)
    print(f"  1. Top Category   : {df.groupby('Category')['Sales_Amount'].sum().idxmax()}")
    print(f"  2. Top Region     : {df.groupby('Region')['Sales_Amount'].sum().idxmax()}")
    print(f"  3. Best Product   : {df.groupby('Product')['Sales_Amount'].sum().idxmax()}")
    print(f"  4. Best Month     : {df.groupby('Month_Name')['Sales_Amount'].sum().idxmax()}")
    print(f"  5. Best Quarter   : {df.groupby('Quarter')['Sales_Amount'].sum().idxmax()}")
    print(f"  6. Top Segment    : {df.groupby('Customer_Segment')['Sales_Amount'].sum().idxmax()}")
    print(f"  7. Profit Margin  : {(df['Profit'].sum()/df['Sales_Amount'].sum()*100):.1f}%")
    print("=" * 55)

# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
if __name__ == '__main__':
    print("\n🚀 Starting Sales Analysis...\n")
    df = load_data(DATA_PATH)
    print_kpis(df)
    print("\n📊 Generating charts...")
    plot_monthly_trend(df)
    plot_category(df)
    plot_region(df)
    plot_top_products(df)
    print_insights(df)
    print("\n✅ Analysis complete! Charts saved to /images/")
