import pandas as pd
import numpy as np

# Step 1: Create the dataset
data = {
    "OrderID": [101, 102, 103, 104, 105],
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
    "Quantity": [2, 5, 3, 2, 4],
    "Price": [50000, 500, 1500, 12000, 2000]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Step 2: Calculate total sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

# Step 3: Calculate discount (10%)
df["Discount"] = df["Total_Sales"] * 0.10

# Step 4: Calculate final sales
df["Final_Sales"] = df["Total_Sales"] - df["Discount"]

# Step 5: Convert product names to uppercase
df["Product_Upper"] = df["Product"].apply(str.upper)

# Step 6: Categorize sales
conditions = [
    df["Final_Sales"] >= 50000,
    df["Final_Sales"] >= 10000
]

choices = ["High", "Medium"]

df["Sales_Category"] = np.select(
    conditions,
    choices,
    default="Low"
)

# Step 7: Display the transformed dataset
print("\nTransformed Dataset:")
print(df)

# Step 8: Export the result
df.to_csv("transformed_sales.csv", index=False)

print("\nTransformed sales report saved successfully!")