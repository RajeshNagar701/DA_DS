


import matplotlib.pyplot as plt

# 1. Monthly sales data
months = [
    "Jan", "Feb", "Mar", "Apr",
    "May", "Jun", "Jul", "Aug"
]

sales = [
    30000, 35000, 32000, 40000,
    45000, 42000, 55000, 60000
]

# 2. Calculate important values
max_sales = max(sales)
max_index = sales.index(max_sales)
max_month = months[max_index]

total_sales = sum(sales)
average_sales = total_sales / len(sales)

# 3. Create figure and axes
fig, ax = plt.subplots(figsize=(12, 6))

# 4. Plot monthly sales
ax.plot(
    months,
    sales,
    color="#1F4E79",
    linewidth=2.5,
    marker="o",
    markersize=7,
    label="Monthly Sales"
)

# 5. Highlight highest sales
ax.scatter(
    max_month,
    max_sales,
    color="#E74C3C",
    s=150,
    zorder=3,
    label="Highest Sales"
)

# 6. Add annotation and arrow  # display main point highlight for any this on o point
ax.annotate(
    f"Highest Sales\n{max_month}: ₹{max_sales:,}",
    xy=(max_month, max_sales),
    xytext=(-100, -65),
    textcoords="offset points",
    fontsize=11,
    fontweight="bold",
    color="#E74C3C",
    arrowprops=dict(
        arrowstyle="->",
        color="#E74C3C",
        linewidth=2
    ),
    bbox=dict(
        boxstyle="round,pad=0.4",
        facecolor="white",
        edgecolor="#E74C3C",
        alpha=0.95
    )
)

# 7. Add business summary text box
summary = (
    f"Total Sales: ₹{total_sales:,}\n"
    f"Average Sales: ₹{average_sales:,.0f}\n"
    f"Best Month: {max_month}"
)

ax.text(
    0.02,
    0.95,
    summary,
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment="top",
    bbox=dict(
        boxstyle="round,pad=0.5",
        facecolor="#EAF2F8",
        edgecolor="#1F4E79",
        alpha=0.95
    )
)

# 8. Customize title and axes
ax.set_title(
    "Monthly Sales Performance Report",
    fontsize=16,
    fontweight="bold",
    pad=15
)

ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Sales (₹)", fontsize=12)

# 9. Customize grid and legend
ax.grid(
    True,
    axis="y",
    linestyle="--",
    alpha=0.35
)

ax.legend(loc="upper right")

# 10. Set Y-axis limits to leave space for annotations
ax.set_ylim(0, max_sales * 1.25)

# 11. Improve layout
fig.tight_layout()

# 12. Save chart
fig.savefig(
    "highest_sales_annotation.png",
    dpi=300,
    bbox_inches="tight"
)

# 13. Display chart
plt.show()

# 14. Print business insights
print("MONTHLY SALES SUMMARY")
print("---------------------")
print("Highest Sales Month:", max_month)
print("Highest Sales:", f"₹{max_sales:,}")
print("Total Sales:", f"₹{total_sales:,}")
print("Average Sales:", f"₹{average_sales:,.2f}")