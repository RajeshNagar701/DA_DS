# Complete Mini Project Code

# Create the following complete code in main.py.

import os
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------
# STEP 1: LOAD DATASET
# --------------------------------

df = pd.read_csv("Matplotlib\dataset\sales_data.csv")

# --------------------------------
# STEP 2: DATA CLEANING
# --------------------------------

df["Date"] = pd.to_datetime(df["Date"])

df = df.drop_duplicates()

df = df.dropna(
    subset=["Date", "Product", "Quantity", "Unit_Price"]
)

# --------------------------------
# STEP 3: CREATE REVENUE
# --------------------------------

df["Revenue"] = df["Quantity"] * df["Unit_Price"]

# --------------------------------
# STEP 4: BUSINESS ANALYSIS
# --------------------------------

total_revenue = df["Revenue"].sum()

total_quantity = df["Quantity"].sum()

total_transactions = len(df)

monthly_sales = df.groupby(
    df["Date"].dt.to_period("M")
)["Revenue"].sum()

product_sales = df.groupby(
    "Product"
)["Revenue"].sum().sort_values(ascending=False)

category_sales = df.groupby(
    "Category"
)["Revenue"].sum()

region_sales = df.groupby(
    "Region"
)["Revenue"].sum().sort_values(ascending=False)

highest_month = monthly_sales.idxmax()

highest_revenue = monthly_sales.max()

# --------------------------------
# STEP 5: CREATE DASHBOARD
# --------------------------------

fig, axes = plt.subplots(
    2, 2,
    figsize=(15, 10)
)

fig.suptitle(
    "BUSINESS SALES ANALYTICS DASHBOARD",
    fontsize=18,
    fontweight="bold"
)

# --------------------------------
# CHART 1: MONTHLY REVENUE
# --------------------------------

ax1 = axes[0, 0]

month_labels = monthly_sales.index.astype(str)

ax1.plot(
    month_labels,
    monthly_sales.values,
    marker="o",
    linewidth=2,
    label="Revenue"
)

max_index = monthly_sales.values.argmax()

ax1.scatter(
    month_labels[max_index],
    highest_revenue,
    s=100,
    label="Highest Revenue"
)

ax1.annotate(
    f"₹{highest_revenue:,.0f}",
    xy=(max_index, highest_revenue),
    xytext=(-15, 15),
    textcoords="offset points",
    arrowprops={"arrowstyle": "->"}
)

ax1.set_title("Monthly Revenue Trend")
ax1.set_xlabel("Month")
ax1.set_ylabel("Revenue (₹)")
ax1.tick_params(axis="x", rotation=30)
ax1.grid(True, alpha=0.3)
ax1.legend()

# --------------------------------
# CHART 2: PRODUCT-WISE REVENUE
# --------------------------------

ax2 = axes[0, 1]

ax2.bar(
    product_sales.index,
    product_sales.values
)

ax2.set_title("Product-wise Revenue")
ax2.set_xlabel("Product")
ax2.set_ylabel("Revenue (₹)")

ax2.tick_params(axis="x", rotation=20)

# --------------------------------
# CHART 3: CATEGORY DISTRIBUTION
# --------------------------------

ax3 = axes[1, 0]

ax3.pie(
    category_sales.values,
    labels=category_sales.index,
    autopct="%1.1f%%",
    startangle=90
)

ax3.set_title("Category-wise Revenue")

# --------------------------------
# CHART 4: REGION-WISE REVENUE
# --------------------------------

ax4 = axes[1, 1]

ax4.bar(
    region_sales.index,
    region_sales.values
)

ax4.set_title("Region-wise Revenue")
ax4.set_xlabel("Region")
ax4.set_ylabel("Revenue (₹)")

# --------------------------------
# STEP 6: KPI SUMMARY
# --------------------------------

kpi_text = (
    f"Total Revenue: ₹{total_revenue:,.0f}\n"
    f"Total Quantity Sold: {total_quantity:,}\n"
    f"Total Transactions: {total_transactions}\n"
    f"Highest Sales Month: {highest_month}\n"
    f"Highest Monthly Revenue: ₹{highest_revenue:,.0f}"
)

fig.text(
    0.5,
    0.01,
    kpi_text,
    ha="center",
    fontsize=11,
    bbox={
        "facecolor": "lightyellow",
        "edgecolor": "gray",
        "boxstyle": "round,pad=0.7"
    }
)

# --------------------------------
# STEP 7: DASHBOARD LAYOUT
# --------------------------------

plt.tight_layout(rect=[0, 0.13, 1, 0.94])

# --------------------------------
# STEP 8: EXPORT DASHBOARD
# --------------------------------

os.makedirs("output", exist_ok=True)

fig.savefig(
    "output/sales_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

fig.savefig(
    "output/sales_dashboard.pdf",
    bbox_inches="tight"
)

plt.show()

print("\nDASHBOARD GENERATED SUCCESSFULLY!")

print("Total Revenue:", total_revenue)
print("Total Quantity:", total_quantity)
print("Total Transactions:", total_transactions)
print("Highest Month:", highest_month)
print("Highest Revenue:", highest_revenue)