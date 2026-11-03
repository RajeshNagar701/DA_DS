
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

# Step 8: Display summary statistics
print("\nStatistical Summary:")
print(df.describe())
