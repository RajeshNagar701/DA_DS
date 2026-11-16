"""
Matplotlib

Matplotlib is a Python library used to create data visualizations.

It supports many chart types and provides detailed control over chart 
elements, including:

plot  : line graph   For : trend     Property : linewidth,linestyle,marker(o),color  


Titles and labels.
Axis limits and tick marks.
Colors and line styles.
Legends and grid lines.
Figure size and layout.
Multiple plots within a figure.

When Should You Use Matplotlib?

Use Matplotlib when:
You want precise control over chart elements.
You need custom plots or complex layouts.
You want to understand how Python charts work.
You need to customize labels, axes, annotations, and figure dimensions.

"""

import matplotlib.pyplot as plt

# Step 1: Prepare the data
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June"
]

sales = [10000, 15000, 12000, 20000, 25000, 22000]



#plt.plot(x,y,color,marker,linestyle,linewidth,markersiz,label)

# Step 2: Create the line chart
plt.plot(
    months,
    sales,
    color="blue",
    marker="o", #x
    linestyle="-", #-- ..
    linewidth=2,
    markersize=8,  # o size
    label="Monthly Sales"   # main heading
)

# Step 3: Add title
plt.title("Monthly Sales Trend - 2026")

# Step 4: Add axis labels
plt.xlabel("Month")
plt.ylabel("Sales (₹)")

# Step 5: Add grid
plt.grid(True, linestyle="--", alpha=0.5) # chart background boxes

# Step 6: Add legend
plt.legend()   # label in graph

# Step 7: Display the chart
plt.show()   