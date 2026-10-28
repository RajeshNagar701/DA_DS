import pandas as pd

# Step 1: Create customer data
customers = pd.DataFrame({
    "CustomerID": [1, 2, 3, 4, 6],
    "CustomerName": ["Raj", "Amit", "Neha", "Priya", "Karan"],
    "City": [
        "Ahmedabad", "Surat", "Vadodara",
        "Rajkot", "Ahmedabad"
    ]
})

# Step 2: Create order data
orders = pd.DataFrame({
    "OrderID": [101, 102, 103, 104, 105, 106],
    "CustomerID": [1, 2, 1, 5, 6, 2],
    "Amount": [5000, 3000, 2000, 7000, 4500, 1500]
})

# Step 3: Merge customers and orders
report = pd.merge(
    customers,
    orders,
    on="CustomerID",
    how="outer",
    indicator=True,
    validate="one_to_many"
)

print("\nCOMPLETE CUSTOMER AND ORDER REPORT")
print(report)

# Step 4: Calculate total amount by customer
customer_totals = (
    report.groupby(
        ["CustomerID", "CustomerName"],
        dropna=False
    )["Amount"]
    .sum(min_count=1)
    .reset_index()
)

print("\nTOTAL AMOUNT BY CUSTOMER")
print(customer_totals)

# Step 5: Find customers without orders
customers_without_orders = report[
    report["_merge"] == "left_only"
]

print("\nCUSTOMERS WITHOUT ORDERS")
print(customers_without_orders)

# Step 6: Find orders without customer details
orders_without_customers = report[
    report["_merge"] == "right_only"
]

print("\nORDERS WITHOUT CUSTOMER DETAILS")
print(orders_without_customers)

# Step 7: Export reports
report.to_csv("complete_customer_order_report.csv", index=False)

customer_totals.to_csv("customer_totals.csv", index=False)

print("\nReports exported successfully!")