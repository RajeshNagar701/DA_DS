# import numpy as np
# import matplotlib.pyplot as plt

# advertising = np.array([10, 15, 20, 25, 30, 35])
# sales = np.array([25, 32, 38, 45, 52, 58])

# # Calculate regression coefficients
# slope, intercept = np.polyfit(advertising, sales, 1)

# # Generate X values for the fitted line
# x_line = np.linspace(advertising.min(), advertising.max(), 100)

# # Calculate predicted Y values
# y_line = slope * x_line + intercept

# # Plot observations and fitted line
# plt.scatter(advertising, sales, label="Actual Sales")
# plt.plot(x_line, y_line, color="red", label="Regression Line")

# plt.title("Advertising Spend vs Sales")
# plt.xlabel("Advertising Spend (₹ thousands)")
# plt.ylabel("Sales (₹ thousands)")

# plt.legend()
# plt.grid(True, alpha=0.3)

# plt.show()


"""
Complete Demo: Advertising Spend vs Sales

Business Scenario

A company wants to understand the relationship between its advertising budget and sales.

The company has recorded advertising expenditure and sales for ten illustrative observations.

The objective is to visualize the relationship and fit a regression line using NumPy.

"""

import matplotlib.pyplot as plt
import numpy as np

# Advertising expenditure in thousands of rupees
advertising = np.array([
    5, 10, 15, 20, 25,
    30, 35, 40, 45, 50
])

# Sales in thousands of rupees
sales = np.array([
    12, 18, 25, 29, 37,
    42, 48, 54, 61, 65
])

# Calculate linear regression coefficients
slope, intercept = np.polyfit(advertising, sales, 1) # if x change the how much % y cahnge 

# Generate points for the fitted line
x_line = np.linspace(
    advertising.min(),
    advertising.max(),
    100
)

# Calculate predicted sales
y_line = slope * x_line + intercept

# Create the chart
plt.figure(figsize=(10, 6))

# Plot actual observations   o for scatter
plt.scatter(
    advertising,
    sales,
    color="blue",
    s=80,
    label="Actual Sales"
)

# Plot regression line
plt.plot(
    x_line,
    y_line,
    color="red",
    linewidth=2,
    label="Linear Regression Line"
)

# Add labels and title
plt.title("Advertising Spend vs Sales", fontsize=16)
plt.xlabel("Advertising Spend (₹ thousands)", fontsize=12)
plt.ylabel("Sales (₹ thousands)", fontsize=12)

# Display the regression equation's coefficients
plt.text(
    7,
    60,
    f"Slope: {slope:.2f}\nIntercept: {intercept:.2f}",
    fontsize=10
)

plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.show()

# Print regression coefficients
print("Slope:", round(slope, 2))
print("Intercept:", round(intercept, 2))