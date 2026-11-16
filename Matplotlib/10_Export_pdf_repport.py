import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [30000, 35000, 32000, 45000, 50000, 60000]

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(
    months,
    sales,
    marker="o",
    linewidth=2,
    label="Monthly Sales"
)

# Find the highest sales value
max_sales = max(sales)
max_month = months[sales.index(max_sales)]

# Highlight the highest sales point
ax.scatter(
    max_month,
    max_sales,
    s=100,
    label="Highest Sales"
)

# Annotate the highest sales point
ax.annotate(
    f"Highest: ₹{max_sales:,}",
    xy=(max_month, max_sales),
    xytext=(-100, -35),
    textcoords="offset points",
    arrowprops={"arrowstyle": "->"},
    fontsize=10
)

ax.set_title("Monthly Sales Performance")
ax.set_xlabel("Month")
ax.set_ylabel("Sales (₹)")

ax.grid(True, linestyle="--", alpha=0.5)
ax.legend()

fig.tight_layout()

# Export to PDF
fig.savefig(
    "monthly_sales_report.pdf",
    format="pdf",
    bbox_inches="tight"
)

# Optional PNG export
fig.savefig(
    "monthly_sales_report.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()