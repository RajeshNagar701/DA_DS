"""
 Time Series Charts

What Is Time Series Data?

Time series data contains observations recorded over time.

Examples include:

Daily website visitors.
Monthly revenue.
Hourly temperatures.
Quarterly profits.
Annual population.

A line chart is commonly used because the order of time periods matters.

"""

import matplotlib.pyplot as plt
import pandas as pd

dates = pd.date_range(
    start="2026-01-01",
    periods=6,
    freq="MS"
)

sales = [45000, 52000, 48000, 65000, 72000, 85000]

plt.figure(figsize=(11, 5))

plt.plot(
    dates,
    sales,
    color="#1F4E79",
    marker="o",
    linewidth=2.5
)

plt.title("Monthly Sales Time Series")
plt.xlabel("Date")
plt.ylabel("Sales (₹)")

plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()