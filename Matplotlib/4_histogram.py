"""
=> What Is a Histogram?

A histogram is a graph used to understand the distribution of numerical data.

It groups numerical values into intervals called bins and displays how many observations 
fall into each interval.

For range between 2 number / age 

"""

import matplotlib.pyplot as plt

# Customer age dataset
ages = [
    18, 22, 25, 29, 31, 35, 38, 42, 45, 48,
    21, 24, 27, 30, 33, 36, 40, 44, 47, 50,
    19, 23, 28, 32, 37, 41, 46, 52, 55, 60,
    26, 34, 39, 43, 49, 51, 29, 33, 36, 40,
    22, 25, 31, 35, 38, 45, 48, 54, 57, 62
]

# Create histogram
plt.figure(figsize=(10, 6))

plt.hist(
    ages,
    bins=5,  # how many bins want for (piller)
    edgecolor="black",
    alpha=0.5    # transparancy 
)

# Add title and axis labels
plt.title("Customer Age Distribution", fontsize=16)
plt.xlabel("Customer Age (Years)", fontsize=12)
plt.ylabel("Number of Customers", fontsize=12)

# Add grid
plt.grid(axis="y", alpha=0.3)

# Display chart
plt.tight_layout()
plt.show()