import pandas as pd
import numpy as np

# Step 1: Create the dataset
data = {
    "OrderID": [101, 102, 103, 104, 105, 106, 107],
    "Product": [
        "Laptop", "Mouse", "Keyboard", "Monitor",
        "Headphones", "Laptop", "Mouse"
    ],
    "Quantity": [2, 5, np.nan, 3, 4, 1, np.nan],
    "Price": [50000, 500, 1500, np.nan, 2000, 50000, 500],
    "Region": [
        "West", "East", "NA", "North",
        np.nan, "West", "South"
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Step 2: Check missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Step 3: Replace the placeholder "NA"
df["Region"] = df["Region"].replace("NA", pd.NA)

# Step 4: Fill Quantity using median
df["Quantity"] = df["Quantity"].fillna(
    df["Quantity"].median()
)

# Step 5: Fill Price using mean
df["Price"] = df["Price"].fillna(
    df["Price"].mean()
)

# Step 6: Fill Region using a descriptive label
df["Region"] = df["Region"].fillna("Unknown")

# Step 7: Verify missing values
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Step 8: Display cleaned dataset
print("\nCleaned Dataset:")
print(df)

# Step 9: Export to CSV
df.to_csv("cleaned_sales.csv", index=False)

print("\nCleaned dataset saved successfully!")