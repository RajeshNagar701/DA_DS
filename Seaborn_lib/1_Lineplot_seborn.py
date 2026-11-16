import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create DataFrame
data = {
    "Month": [
        "Jan", "Feb", "Mar",
        "Apr", "May", "Jun"
    ],
    "Sales": [
        25000, 30000, 28000,
        40000, 45000, 55000
    ]
}

df = pd.DataFrame(data)

# Apply Seaborn theme
sns.set_theme(
    style="whitegrid",
    context="notebook",
    palette="deep"
)

# Create line chart
sns.lineplot(
    data=df,
    x="Month",
    y="Sales",
    marker="o",
    linewidth=2
)

# Customize chart using Matplotlib
plt.title(
    "Monthly Sales Performance",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Month")
plt.ylabel("Sales (₹)")

plt.tight_layout()

plt.show()

# Code Explanation

# Create a Pandas DataFrame containing monthly sales.

# Apply the Seaborn whitegrid theme.

# Use sns.lineplot() to create the chart.

# Add markers to highlight individual values.

# Customize the title and axis labels using Matplotlib.

# Display the chart using plt.show().