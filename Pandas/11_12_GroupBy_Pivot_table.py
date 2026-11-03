import pandas as pd

# Step 1: Create dataset
data = {
    "OrderID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Product": [
        "Laptop", "Mouse", "Laptop", "Keyboard",
        "Mouse", "Laptop", "Keyboard", "Mouse"
    ],
    "Category": [
        "Electronics", "Accessories", "Electronics",
        "Accessories", "Accessories", "Electronics",
        "Accessories", "Accessories"
    ],
    "City": [
        "Ahmedabad", "Surat", "Ahmedabad", "Vadodara",
        "Ahmedabad", "Surat", "Surat", "Vadodara"
    ],
    "Quantity": [2, 5, 1, 3, 4, 2, 2, 6],
    "Sales": [100000, 2500, 50000, 4500, 2000, 100000, 3000, 3000]
}

df = pd.DataFrame(data)

# Step 2: Product-wise summary
product_report = df.groupby("Product").agg(
    Total_Sales=("Sales", "sum"),
    Average_Sales=("Sales", "mean"),
    Total_Quantity=("Quantity", "sum"),
    Order_Count=("OrderID", "count")
).reset_index()

print("\nPRODUCT REPORT")
print(product_report)

# Step 3: City-wise summary
city_report = df.groupby("City").agg(
    Total_Sales=("Sales", "sum"),
    Total_Quantity=("Quantity", "sum"),
    Order_Count=("OrderID", "count")
).reset_index()

print("\nCITY REPORT")
print(city_report)

# Step 4: Category-wise summary
category_report = df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Average_Sales=("Sales", "mean"),
    Order_Count=("OrderID", "count")
).reset_index()

print("\nCATEGORY REPORT")
print(category_report)

# Step 5: Top-performing products
top_products = product_report.sort_values(
    by="Total_Sales",
    ascending=False
)

print("\nTOP PRODUCTS")
print(top_products)

# Step 6: Product vs city pivot table
pivot_report = pd.pivot_table(
    df,
    values="Sales",
    index="Product",
    columns="City",
    aggfunc="sum",
    fill_value=0,
    margins=True,
    margins_name="Grand Total"
)

print("\nPRODUCT-CITY PIVOT REPORT")
print(pivot_report)

# Step 7: Export reports
product_report.to_csv("product_report.csv", index=False)
city_report.to_csv("city_report.csv", index=False)
category_report.to_csv("category_report.csv", index=False)
top_products.to_csv("top_products.csv", index=False)
pivot_report.to_csv("product_city_pivot.csv")

print("\nAll reports exported successfully!")