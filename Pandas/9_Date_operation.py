import pandas as pd

# Step 1: Create sample sales data
data = {
    "OrderID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Product": [
        "Laptop", "Mouse", "Keyboard", "Monitor",
        "Headphones", "Laptop", "Mouse", "Monitor"
    ],
    "OrderDate": [
        "2026-01-05", "2026-01-15",
        "2026-02-10", "2026-02-20",
        "2026-03-10", "2026-03-25",
        "2026-04-05", "2026-04-15"
    ],
    "Quantity": [2, 5, 3, 2, 4, 1, 10, 3],
    "Price": [50000, 500, 1500, 12000, 2000, 50000, 500, 12000]
}

df = pd.DataFrame(data)

# Step 2: Convert OrderDate into datetime
df["OrderDate"] = pd.to_datetime(
    df["OrderDate"],
    errors="coerce"
)

# Step 3: Calculate total sales
df["TotalSales"] = df["Quantity"] * df["Price"]

# Step 4: Extract date components
df["Year"] = df["OrderDate"].dt.year
df["Month"] = df["OrderDate"].dt.month
df["MonthName"] = df["OrderDate"].dt.month_name()
df["Day"] = df["OrderDate"].dt.day
df["Weekday"] = df["OrderDate"].dt.day_name()

# Step 5: Display complete data
print("\nCOMPLETE SALES DATA")
print(df)

# Step 6: Filter February and March 2026
start_date = "2026-02-01"
end_date = "2026-03-31"

period_sales = df[
    df["OrderDate"].between(start_date, end_date)
]

print("\nFEBRUARY-MARCH SALES")
print(period_sales[["OrderID", "Product", "OrderDate", "TotalSales"]])

# Step 7: Calculate total sales
print("\nTOTAL SALES:", df["TotalSales"].sum())

# Step 8: Calculate monthly sales
monthly_sales = (
    df.groupby(df["OrderDate"].dt.to_period("M"))["TotalSales"]
    .sum()
)

print("\nMONTHLY SALES")
print(monthly_sales)

# Step 9: Find the highest-sales order
highest_order = df.loc[df["TotalSales"].idxmax()]

print("\nHIGHEST-SALES ORDER")
print(highest_order)

# Step 10: Export the final report
df.to_csv("sales_date_report.csv", index=False)

print("\nReport exported successfully!")