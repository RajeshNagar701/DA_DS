
import pandas as pd

# =====================================
# TASK 1: Create Monthly Sales DataFrames
# =====================================

jan = pd.DataFrame({
    "OrderID": [101, 102, 103, 104],
    "Product": ["Laptop", "Mouse", "Keyboard", "Laptop"],
    "City": ["Ahmedabad", "Surat", "Ahmedabad", "Vadodara"],
    "Sales": [50000, 2000, 3000, 55000]
})

feb = pd.DataFrame({
    "OrderID": [105, 106, 107, 108],
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "City": ["Surat", "Ahmedabad", "Vadodara", "Surat"],
    "Sales": [60000, 2500, 3500, 15000]
})


# =====================================
# TASK 2: Combine DataFrames using concat()
# =====================================

sales = pd.concat(
    [jan, feb],
    keys=["January", "February"],
    names=["Month", "OriginalIndex"]
).reset_index(level="Month")

print("\nCOMBINED SALES DATA")
print(sales)


# =====================================
# TASK 3: Calculate Total Sales by Product
# =====================================

product_sales = sales.groupby("Product")["Sales"].sum()

print("\nTOTAL SALES BY PRODUCT")
print(product_sales)


# =====================================
# TASK 4: Create a Pivot Table
# =====================================

pivot_report = sales.pivot_table(
    index="Product",
    columns="Month",
    values="Sales",
    aggfunc="sum",
    fill_value=0
)

print("\nPRODUCT-WISE MONTHLY SALES")
print(pivot_report)


# =====================================
# TASK 5: Convert Wide Data to Long using melt()
# =====================================

long_report = pivot_report.reset_index().melt(
    id_vars="Product",
    var_name="Month",
    value_name="Sales"
)

print("\nLONG-FORMAT SALES REPORT")
print(long_report)


# =====================================
# TASK 6: Convert Long Data to Wide using pivot()
# =====================================

wide_report = long_report.pivot(
    index="Product",
    columns="Month",
    values="Sales"
)

print("\nWIDE-FORMAT SALES REPORT")
print(wide_report)


# =====================================
# TASK 7: Use stack()
# =====================================

stacked_report = pivot_report.stack()

print("\nSTACKED SALES REPORT")
print(stacked_report)


# =====================================
# TASK 8: Use unstack()
# =====================================

unstacked_report = stacked_report.unstack()

print("\nUNSTACKED SALES REPORT")
print(unstacked_report)


# =====================================
# TASK 9: Use explode()
# =====================================

orders = pd.DataFrame({
    "OrderID": [201, 202, 203],
    "Customer": ["Amit", "Neha", "Raj"],
    "Products": [
        ["Laptop", "Mouse"],
        ["Keyboard", "Mouse", "Monitor"],
        ["Laptop", "Keyboard"]
    ]
})

exploded_orders = orders.explode(
    "Products",
    ignore_index=True
)

print("\nEXPLODED ORDER DETAILS")
print(exploded_orders)


# =====================================
# TASK 10: Export Reports to CSV
# =====================================

sales.to_csv("combined_sales.csv", index=False)

pivot_report.to_csv("monthly_sales_report.csv")

long_report.to_csv("long_sales_report.csv", index=False)

exploded_orders.to_csv("exploded_orders.csv", index=False)

print("\nAll reports exported successfully!")
