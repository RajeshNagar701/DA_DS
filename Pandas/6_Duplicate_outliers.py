import pandas as pd

# Step 1: Create dataset
data = {
    "OrderID": [101, 102, 103, 104, 102, 105, 106, 107, 108, 109, 110],
    "Product": [
        "Mouse", "Keyboard", "Headphones", "Mouse",
        "Keyboard", "Monitor", "Keyboard", "Mouse",
        "Laptop", "Headphones", "Monitor"
    ],
    "Sales": [
        500, 600, 550, 700, 600,
        650, 620, 580, 50000, 590, 610
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Step 2: Detect duplicate rows
print("\nDuplicate Rows:")
print(df[df.duplicated()])

print("\nDuplicate Count:")
print(df.duplicated().sum())

# Step 3: Remove exact duplicate rows
df = df.drop_duplicates().reset_index(drop=True)

print("\nDataset After Removing Exact Duplicates:")
print(df)

# Step 4: Calculate IQR
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Step 5: Detect outliers
df["Outlier_Status"] = df["Sales"].apply(
    lambda x: "Outlier"
    if x < lower_bound or x > upper_bound
    else "Normal"
)

print("\nFinal Dataset:")
print(df)

# Step 6: Export report
df.to_csv("cleaned_sales_report.csv", index=False)

print("\nReport saved successfully!")