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

    "Revenue": [
        55000, 800, 15000, 1200, 65000,
        2500, 12000, 18000, 900, 45000
    ]
}

df = pd.DataFrame(data)

print("ORIGINAL DATASET")
print(df)


# STEP 2: Sort by revenue in descending order

sorted_df = df.sort_values(
    by="Revenue",
    ascending=False
)

print("\nSORTED BY REVENUE")
print(sorted_df)


# STEP 3: Select the top five customers

top_five = sorted_df.head(5)

print("\nTOP FIVE CUSTOMERS")
print(top_five)


# STEP 4: Reset the index

top_five = top_five.reset_index(drop=True)

print("\nTOP FIVE WITH RESET INDEX")
print(top_five)


# STEP 5: Arrange columns in the required order

final_report = top_five.reindex(
    columns=["CustomerID", "Customer", "Revenue", "City"]
)

print("\nFINAL CUSTOMER REVENUE REPORT")
print(final_report)


# STEP 6: Export the final report

final_report.to_csv(
    "top_customers.csv",
    index=False
)

print("\nReport exported successfully!")