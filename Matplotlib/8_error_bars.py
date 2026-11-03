"""
 Error Bars

What Are Error Bars?

Error bars represent uncertainty, variability, or a range around a measured or estimated value.

They are commonly used in:

Scientific experiments.
Survey results.
Product testing.
Performance comparisons.
Business analysis where uncertainty has been measured.

Matplotlib provides:

plt.errorbar()

"""

import matplotlib.pyplot as plt

regions = ["North", "South", "East", "West"]

delivery_time = [35, 40, 32, 45]
errors = [3, 4, 2, 5]

plt.figure(figsize=(9, 5))

plt.errorbar(
    regions,
    delivery_time,
    yerr=errors,
    fmt="o",
    color="#1F4E79",
    ecolor="#F39C12",
    capsize=6,
    markersize=7,
    linewidth=2
)

plt.title("Average Delivery Time by Region")
plt.xlabel("Region")
plt.ylabel("Delivery Time (minutes)")

plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()
plt.show()