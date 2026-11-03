"""
Corporate-Styled Sales Chart — Complete Practical Demo

Business Scenario

A company wants a professional monthly sales chart for a management presentation.
The chart should include:
Corporate colors
A suitable figure size
Clear titles and labels
Custom line styles and markers
A highlighted highest-sales month
Subtle grid lines
A legend
An image file for the presentation
Complete Python Code

"""

import matplotlib.pyplot as plt

# 1. Business data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = [45000, 52000, 48000, 65000, 72000, 85000]

# 2. Corporate color
corporate_blue = "#1F4E79"
highlight_color = "#F39C12"

# 3. Create the figure and axes
fig, ax = plt.subplots(figsize=(12, 6), dpi=100)

# 4. Draw the sales line
ax.plot(
    months,
    sales,
    color=corporate_blue,
    linewidth=3,
    linestyle="-",
    marker="o",
    markersize=8,
    markerfacecolor="white",
    markeredgecolor=corporate_blue,
    markeredgewidth=2,
    label="Monthly Sales"
)

# 5. Identify the highest-sales month
max_index = sales.index(max(sales))

# 6. Highlight the highest-sales point
ax.scatter(
    months[max_index],
    sales[max_index],
    color=highlight_color,
    s=150,
    zorder=3,
    label="Highest Sales"
)

# 7. Add an annotation
ax.annotate(
    f"Peak: ₹{sales[max_index]:,}",
    xy=(months[max_index], sales[max_index]),
    xytext=(-65, -35),
    textcoords="offset points",
    fontsize=11,
    fontweight="bold",
    arrowprops={
        "arrowstyle": "->",
        "color": highlight_color
    }
)

# 8. Customize the title
ax.set_title(
    "Monthly Sales Performance",
    fontsize=18,
    fontweight="bold",
    pad=18
)

# 9. Customize axis labels
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Sales (₹)", fontsize=12)

# 10. Customize grid lines
ax.grid(
    True,
    axis="y",
    linestyle="--",
    linewidth=0.7,
    alpha=0.4
)

# 11. Customize tick labels
ax.tick_params(axis="both", labelsize=10)

# 12. Customize the legend
ax.legend(frameon=False, loc="upper left")

# 13. Improve spacing
fig.tight_layout()

# 14. Save the chart
fig.savefig(
    "corporate_sales_chart.png",
    dpi=300,
    bbox_inches="tight"
)

# 15. Display the chart
plt.show()