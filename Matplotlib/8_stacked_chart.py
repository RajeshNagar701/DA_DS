"""
What Is a Stacked Bar Chart?

A stacked bar chart displays multiple data series in a single bar. Each series occupies a separate section of the bar.

It helps us understand:

Total sales for each month.

Sales contributed by individual products.

How different categories contribute to the overall total.

"""

# import matplotlib.pyplot as plt

# months = ["Jan", "Feb", "Mar", "Apr"]

# laptop = [20000, 25000, 30000, 28000]
# mobile = [30000, 35000, 40000, 45000]
# tablet = [15000, 18000, 20000, 22000]

# plt.figure(figsize=(10, 6))

# plt.bar(months, laptop, label="Laptop")
# plt.bar(months, mobile, bottom=laptop, label="Mobile")

# bottom_tablet = [
#     laptop[i] + mobile[i]
#     for i in range(len(months))
# ]

# plt.bar(
#     months,
#     tablet,
#     bottom=bottom_tablet,
#     label="Tablet"
# )

# plt.title("Monthly Product Sales", fontsize=16)
# plt.xlabel("Month")
# plt.ylabel("Sales (₹)")

# plt.legend()
# plt.grid(axis="y", linestyle="--", alpha=0.4)

# plt.tight_layout()
# plt.show()



"""

Monthly Performance Stacked Chart — Complete Demo

Business Scenario

A retail company wants to analyze monthly revenue from three departments:

Electronics
Clothing
Home Appliances

Management wants to see:
Each department's monthly contribution.
Total monthly revenue.
The change in overall performance over time.

"""



import matplotlib.pyplot as plt
import pandas as pd

# 1. Create the dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Electronics": [50000, 55000, 60000, 65000, 70000, 80000],
    "Clothing": [30000, 32000, 35000, 38000, 42000, 45000],
    "Home Appliances": [20000, 22000, 25000, 28000, 30000, 35000]
}

df = pd.DataFrame(data)

# 2. Calculate total monthly revenue
df["Total Revenue"] = (
    df["Electronics"]
    + df["Clothing"]
    + df["Home Appliances"]
)

# 3. Define corporate colors
colors = ["#1F4E79", "#00A6A6", "#F39C12"]

# 4. Create figure and axes
fig, ax = plt.subplots(figsize=(12, 7))

# 5. Draw stacked bars
ax.bar(
    df["Month"],
    df["Electronics"],
    label="Electronics",
    color=colors[0]
)

ax.bar(
    df["Month"],
    df["Clothing"],
    bottom=df["Electronics"],
    label="Clothing",
    color=colors[1]
)

ax.bar(
    df["Month"],
    df["Home Appliances"],
    bottom=df["Electronics"] + df["Clothing"],
    label="Home Appliances",
    color=colors[2]
)

# 6. Add total revenue labels above each bar
for i, total in enumerate(df["Total Revenue"]):
    ax.text(
        i,
        total + 3000,
        f"₹{total / 1000:.0f}K",
        ha="center",
        fontsize=9,
        fontweight="bold"
    )

# 7. Customize the chart
ax.set_title(
    "Monthly Revenue Performance by Department",
    fontsize=16,
    fontweight="bold",
    pad=15
)

ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Revenue (₹)", fontsize=12)

ax.grid(
    True,
    axis="y",
    linestyle="--",
    alpha=0.3
)

ax.legend(title="Department", loc="upper left")

# 8. Improve spacing
fig.tight_layout()

# 9. Save the chart
fig.savefig(
    "monthly_performance_stacked.png",
    dpi=300,
    bbox_inches="tight"
)

# 10. Display the chart
plt.show()

# 11. Display the totals
print(df[["Month", "Total Revenue"]])