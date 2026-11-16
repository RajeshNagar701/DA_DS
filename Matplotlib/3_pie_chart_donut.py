"""



What Is a Donut Chart?

A donut chart is a pie chart with a hole in the center.

It displays proportions in a similar way to a pie chart but leaves an 
empty space in the middle.

Example : 4 state & state by sales percentage


Donut charts are often used for:
Market share visualization.
Product contribution.
Budget allocation.
Revenue distribution.
Customer segmentation.


What is different from the pie chart?

The most important difference is:
wedgeprops={"width": 0.4}
This creates the hole in the center.
We then add:
plt.text(0, 0, "Market\nShare", ha="center", va="center")

This places a label in the center.

"""


import matplotlib.pyplot as plt

# Step 1: Prepare the data
companies = [
    "Company A",
    "Company B",
    "Company C",
    "Company D",
    "Company E"
]

market_share = [35, 25, 20, 12, 8]

colors = [
    "#3498DB",
    "#E67E22",
    "#2ECC71",
    "#E74C3C",
    "#9B59B6"
]

# Step 2: Create the donut chart
plt.figure(figsize=(9, 7))

plt.pie(
    market_share,
    labels=companies,
    colors=colors,
    autopct="%1.1f%%",
    startangle=90,
    wedgeprops={"width": 0.4, "edgecolor": "white", "linewidth": 2}
)

# Step 3: Add text in the center
plt.text(
    0,
    0,
    "Market\nShare",
    ha="center",
    va="center",
    fontsize=16,
    fontweight="bold"
)

# Step 4: Add the title
plt.title("Technology Market Share — Donut Chart", fontsize=15)

# Step 5: Display the chart
plt.show()