import pandas as pd

# STEP 1: Create the dataset

data = {
    "CustomerID": [101, 102, 103, 104, 105,
                   106, 107, 108, 109, 110],

    "Customer": [
        "Raj", "Amit", "Neha", "Priya", "Karan",
        "Riya", "Jay", "Pooja", "Rahul", "Sneha"
    ],

    "City": [
        "Ahmedabad", "Surat", "Vadodara", "Ahmedabad",
        "Rajkot", "Surat", "Vadodara", "Ahmedabad",
        "Rajkot", "Surat"
    ],

    "Age": [25, 30, 28, 35, 40, 22, 32, 27, 29, 31],

    "Product": [
        "Laptop", "Mouse", "Mobile", "Keyboard", "Laptop",
        "Headphones", "Monitor", "Mobile", "Mouse", "Laptop"
    ],

    "Revenue": [
        55000, 800, 15000, 1200, 65000,
        2500, 12000, 18000, 900, 45000
    ]
}

df = pd.DataFrame(data)


# STEP 2: Display the complete dataset

print("\n1. COMPLETE CUSTOMER DATASET")
print(df)


# STEP 3: Select specific columns

print("\n2. CUSTOMER NAMES AND REVENUE")
print(df[["Customer", "Revenue"]])


# STEP 4: Select a row using loc

print("\n3. CUSTOMER AT INDEX 0")
print(df.loc[0])


# STEP 5: Select a row using iloc

print("\n4. THIRD CUSTOMER BY POSITION")
print(df.iloc[2])


# STEP 6: Filter revenue greater than 10000

print("\n5. CUSTOMERS WITH REVENUE > 10000")

high_revenue = df[df["Revenue"] > 10000]

print(high_revenue)


# STEP 7: Filter high-revenue customers in Ahmedabad

print("\n6. HIGH-REVENUE CUSTOMERS IN AHMEDABAD")

ahmedabad_customers = df[
    (df["Revenue"] > 10000) &
    (df["City"] == "Ahmedabad")
]

print(ahmedabad_customers)


# STEP 8: Filter revenue between 10000 and 50000

print("\n7. REVENUE BETWEEN 10000 AND 50000")

revenue_range = df[df["Revenue"].between(10000, 50000)]

print(revenue_range)


# STEP 9: Filter using query()

print("\n8. CUSTOMERS WITH REVENUE > 10000 USING QUERY")

query_result = df.query("Revenue > 10000")

print(query_result)


# STEP 10: Select customers from Surat or Vadodara

print("\n9. CUSTOMERS FROM SURAT OR VADODARA")

selected_cities = df[
    df["City"].isin(["Surat", "Vadodara"])
]

print(selected_cities)


# STEP 11: Find the top 3 customers by revenue

print("\n10. TOP 3 CUSTOMERS BY REVENUE")

top_customers = df.sort_values(
    "Revenue",
    ascending=False
).head(3)

print(top_customers[["Customer", "City", "Revenue"]])


# STEP 12: Combine city and revenue conditions

print("\n11. HIGH-REVENUE CUSTOMERS FROM SURAT OR VADODARA")

final_result = df[
    (df["City"].isin(["Surat", "Vadodara"])) &
    (df["Revenue"] > 10000)
]

print(final_result[["Customer", "City", "Revenue"]])


# STEP 13: Count high-revenue customers

print("\n12. NUMBER OF HIGH-REVENUE CUSTOMERS")

print(len(high_revenue))


# STEP 14: Calculate total revenue from high-revenue customers

print("\n13. TOTAL REVENUE FROM HIGH-REVENUE CUSTOMERS")

print(high_revenue["Revenue"].sum())