"""
 Area Chart

What Is an Area Chart?

An area chart is similar to a line chart, but the area below the line is filled with color.
It is useful for showing:
Sales trends over time.
Website traffic.
Revenue growth.
Contributions from different business categories.

Matplotlib provides:

plt.fill_between()

and:

plt.stackplot()

Use fill_between() to fill the area between a line and a baseline or another boundary. 
Use stackplot() to show cumulative contributions from multiple series.

"""

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [20000, 25000, 22000, 30000, 35000, 40000]

plt.figure(figsize=(10, 5))

plt.fill_between(
    months,
    sales,
    color="#00A6A6",
    alpha=0.4
)

plt.plot(
    months,
    sales,
    color="#1F4E79",
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales Growth")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")

plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()
plt.show()