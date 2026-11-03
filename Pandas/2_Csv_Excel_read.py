import pandas as pd
import os

# STEP 1: Create the case study dataset

data = {
    "OrderID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Product": [
        "Laptop", "Mouse", "Keyboard", "Monitor", "Headphones",
        "Laptop", "Mouse", "Monitor", "Keyboard", "Headphones"
    ],
    "Category": [
        "Electronics", "Accessories", "Accessories", "Electronics",
        "Accessories", "Electronics", "Accessories", "Electronics",
        "Accessories", "Accessories"
    ],
    "Quantity": [2, 5, 3, 2, 4, 1, 10, 3, 6, 2],
    "Price": [50000, 500, 1500, 12000, 2000,
              50000, 500, 12000, 1500, 2000],
    "Region": [
        "West", "East", "West", "North", "South",
        "East", "West", "South", "North", "East"
    ]
}

df = pd.DataFrame(data)

print("ORIGINAL DATASET")
print(df)


# STEP 2: Create an output folder

os.makedirs("output", exist_ok=True)


# STEP 3: Export to CSV

df.to_csv("output/sales.csv", index=False)

print("\nCSV file exported successfully!")


# STEP 4: Export to Excel

df.to_excel(
    "output/sales.xlsx",
    sheet_name="SalesData",
    index=False
)

print("Excel file exported successfully!")


# STEP 5: Read the CSV file

csv_df = pd.read_csv("output/sales.csv")

print("\nDATA LOADED FROM CSV")
print(csv_df)


# STEP 6: Read the Excel file

excel_df = pd.read_excel(
    "output/sales.xlsx",
    sheet_name="SalesData"
)

print("\nDATA LOADED FROM EXCEL")
print(excel_df)


# STEP 7: Display the first five rows

print("\nFIRST FIVE ROWS")
print(csv_df.head())


# STEP 8: Display the last three rows

print("\nLAST THREE ROWS")
print(csv_df.tail(3))


# STEP 9: Display dataset information

print("\nDATASET INFORMATION")
csv_df.info()


# STEP 10: Display statistical summary

print("\nSTATISTICAL SUMMARY")
print(csv_df.describe())


# STEP 11: Display dataset dimensions

print("\nDATASET SHAPE")
print(csv_df.shape)


# STEP 12: Display column names

print("\nCOLUMN NAMES")
print(csv_df.columns.tolist())