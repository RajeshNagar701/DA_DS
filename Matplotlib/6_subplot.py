
# 4 charts by subplot()
# too many charts in 1 chart 
 



# task 1 Subplot
 
# import matplotlib.pyplot as plt

# months = ["Jan", "Feb", "Mar", "Apr"]
# sales = [100, 120, 140, 160]
# expenses = [50, 65, 70, 90]
# profit = [50, 55, 70, 70]
# customers = [200, 230, 250, 290]

# plt.figure(figsize=(10, 7))

# plt.subplot(2, 2, 1)     # 2 row , 2 column , 1 indxe graph
# plt.plot(months, sales, marker="o")   # plot measn line  /
# plt.title("Sales")

# plt.subplot(2, 2, 2)    # 2 row , 2 column , 2 indxe graph
# plt.bar(months, expenses)  # bar measn bar chart  |||
# plt.title("Expenses")

# plt.subplot(2, 2, 3)    # 2 row , 2 column , 3 indxe graph
# plt.plot(months, profit, marker="s")
# plt.title("Profit")

# plt.subplot(2, 2, 4)     # 2 row , 2 column , 4 indxe graph
# plt.bar(months, customers)
# plt.title("Customers")

# plt.tight_layout()
# plt.show()

"""

Business Scenario

A retail company wants to analyze its performance across five months.
The management team wants to compare:
Monthly sales trends.
Monthly expenses.
Monthly profit.
Customer counts.

We can display all four visualizations in one figure
"""

# task 2 axislevel chart

import matplotlib.pyplot as plt

# Dataset
months = ["Jan", "Feb", "Mar", "Apr", "May"]

sales = [100, 120, 140, 130, 160]
expenses = [60, 70, 85, 80, 95]
profit = [40, 50, 55, 50, 65]
customers = [200, 230, 250, 240, 290]

# Create a 2 x 2 figure
fig, ax = plt.subplots(2, 2, figsize=(12, 8))  # 2 rows , 2 column , 12*8 box

# 1. Sales trend
ax[0, 0].plot(months, sales, marker="o")
ax[0, 0].set_title("Monthly Sales")
ax[0, 0].set_xlabel("Month")
ax[0, 0].set_ylabel("Sales")
ax[0, 0].grid(True, alpha=0.3)

# 2. Expenses
ax[0, 1].bar(months, expenses)
ax[0, 1].set_title("Monthly Expenses")
ax[0, 1].set_xlabel("Month")
ax[0, 1].set_ylabel("Expenses")
ax[0, 1].grid(axis="y", alpha=0.3)

# 3. Profit
ax[1, 0].plot(months, profit, marker="s")
ax[1, 0].set_title("Monthly Profit")
ax[1, 0].set_xlabel("Month")
ax[1, 0].set_ylabel("Profit")
ax[1, 0].grid(True, alpha=0.3)

# 4. Customer count
ax[1, 1].bar(months, customers)
ax[1, 1].set_title("Monthly Customers")
ax[1, 1].set_xlabel("Month")
ax[1, 1].set_ylabel("Number of Customers")
ax[1, 1].grid(axis="y", alpha=0.3)

# Overall figure title
fig.suptitle("Retail Business Performance Dashboard", fontsize=16)

# Adjust layout
fig.tight_layout(rect=[0, 0, 1, 0.95])

# Display the dashboard
plt.show()