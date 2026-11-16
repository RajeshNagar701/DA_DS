# Save One Chart in Four Formats

import matplotlib.pyplot as plt

products = ["Laptop", "Mobile", "Tablet", "Monitor"]
revenue = [120000, 180000, 90000, 75000]

plt.figure(figsize=(9, 5))

plt.bar(products, revenue)

plt.title("Product Revenue Report")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")

plt.tight_layout()

plt.savefig("product_revenue.png", dpi=300)
plt.savefig("product_revenue.jpg", dpi=300)
plt.savefig("product_revenue.svg")
plt.savefig("product_revenue.pdf")

plt.show()