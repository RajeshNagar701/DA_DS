"""
Pandas is a fast, open-source Python library used for working with structured data sets. Built on top of NumPy, 
it provides tools for 
    cleaning, 
    transforming, and 
    analyzing tabular data like spreadsheets or SQL tables.

Pandas organizes data using two primary objects:
• Series. A one-dimensional labeled array capable of holding any data type. It acts like a single column in a spreadsheet.

• DataFrame. A two-dimensional labeled table with rows and columns. 
Different columns can hold different data types, such as numbers, text, or dates

"""


import pandas as pd

# Step 1: Create data manually
data = {
    "StudentID": [101, 102, 103, 104, 105],
    "Name": ["Raj", "Amit", "Neha", "Priya", "Karan"],
    "Age": [22, 23, 21, 22, 24],
    "Course": ["Python", "Java", "Python", "Data Science", "Java"],
    "Marks": [85, 90, 78, 95, 68]
}

# Step 2: Create DataFrame
df = pd.DataFrame(data)

# Step 3: Display complete data
print("Student Data:")
print(df)

# Step 4: Display first 3 records
print("\nFirst 3 Students:")
print(df.head(3))

# Step 5: Display column names
print("\nColumn Names:")
print(df.columns)

# Step 6: Display dimensions
print("\nShape:")
print(df.shape)

# Step 7: Display data types
print("\nData Types:")
print(df.dtypes)

# Step 8: Display summary statistics give all count mean std min max
print("\nStatistical Summary:")
print(df.describe())
