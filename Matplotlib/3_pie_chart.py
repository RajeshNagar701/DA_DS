"""
Pie Chart & Donut Chart in Matplotlib
In this session, you will learn how to create pie charts and donut charts using 
Python Matplotlib, display percentages, highlight individual segments, and visualize 
market share.

By the end of this session, students will be able to:

Create pie charts using plt.pie().

Display percentages using autopct.

Separate pie chart segments using explode.

Customize colors, labels, and chart rotation.

Create donut charts using wedgeprops.

Add text inside a donut chart.

Build a practical market share visualization.

Interpret business data using pie and donut charts.

2. What Is a Pie Chart?

A pie chart is a circular chart divided into slices. Each slice represents a 
category's proportion of the total.

Important: Pie charts work best when there are only a few categories and all slices 
represent parts of the same meaningful total.

"""


#Complete Pie Chart

# import matplotlib.pyplot as plt

# products = ["Laptop", "Mobile", "Tablet", "Monitor"]
# sales = [40, 30, 20, 10]

# colors = ["#3498DB", "#E67E22", "#2ECC71", "#E74C3C"]
# explode = [0.08, 0, 0, 0]

# plt.figure(figsize=(8, 6))

# plt.pie(
#     sales,
#     labels=products,
#     colors=colors,
#     autopct="%1.1f%%",
#     explode=explode,
#     startangle=90,
#     shadow=False,
#     wedgeprops={"edgecolor": "white", "linewidth": 2}
# )

# plt.title("Product Sales Distribution", fontsize=15)

# plt.show()




#Exaple 2

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

# Step 2: Define colors
colors = [
    "#3498DB",
    "#E67E22",
    "#2ECC71",
    "#E74C3C",
    "#9B59B6"
]

# Step 3: Highlight Company A
explode = [0.08, 0, 0, 0, 0]

# Step 4: Create the pie chart
plt.figure(figsize=(9, 7))

plt.pie(
    market_share,
    labels=companies,
    colors=colors,
    autopct="%1.1f%%",
    explode=explode,
    startangle=90,
    wedgeprops={"edgecolor": "white", "linewidth": 2}
)

# Step 5: Add the title
plt.title("Technology Market Share", fontsize=16)

# Step 6: Display the chart
plt.show()