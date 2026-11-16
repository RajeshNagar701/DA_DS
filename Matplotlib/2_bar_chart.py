"""

Bar Charts (Vertical + Horizontal)

1. Learning Objectives
By the end of this session, students will be able to:

Create vertical bar charts using plt.bar().
Create horizontal bar charts using plt.barh().

2. What Is a Bar Chart?
A bar chart is a data visualization that uses rectangular bars to compare values 
across different categories.


plt.bar()   vertical , 
plt.barh()  horizontal 

    property : 
         x ,y , linewidth ,edgeclr 

"""


# =======================  Vertical Revenue Chart ================================

import matplotlib.pyplot as plt

# Step 1: Prepare the data
regions = [
    "Ahmedabad",
    "Surat",
    "Vadodara",
    "Rajkot",
    "Mumbai"
]

revenue = [150000, 120000, 180000, 100000, 220000]

# Step 2: Create the vertical bar chart
bars = plt.bar(
    regions,
    revenue,
    color="skyblue",
    width=0.6,
    edgecolor="red",
    align="center"
)

# Step 3: Add values to the bars
plt.bar_label(bars, padding=2, fontsize=7)

# Step 4: Add title and axis labels
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue (₹)")

# Step 5: Improve layout
plt.tight_layout()   

# Step 6: Display the chart
plt.show()


#===============  Horizontal Revenue Chart ===============================

# import matplotlib.pyplot as plt

# # Step 1: Prepare the data
# regions = [
#     "Ahmedabad",
#     "Surat",
#     "Vadodara",
#     "Rajkot",
#     "Mumbai"
# ]

# revenue = [150000, 120000, 180000, 100000, 220000]

# # Step 2: Create the horizontal bar chart
# bars = plt.barh(
#     regions,
#     revenue,
#     color="lightgreen",
#     height=0.6
# )

# # Step 3: Add values to the bars
# plt.bar_label(bars, padding=5)

# # Step 4: Add title and labels
# plt.title("Revenue by Region")
# plt.xlabel("Revenue (₹)")
# plt.ylabel("Region")

# # Step 5: Adjust the layout
# plt.tight_layout()

# # Step 6: Display the chart
# plt.show()

