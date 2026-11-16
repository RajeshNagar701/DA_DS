
"""
pip install  seaborn

1. numpy ------> array   
2. pandas ---> data cleaning 
3. matplotlib ---> basic plot  
4. seaborn ---> statistical plot

what is  difference between  matplotlib and seaborn ??

            matplotlib               seaborn
1.    use for  basic charts        use  for statistical charts
2.    more  coding                 less coding
3.    independent                  built  on 
4.    highly  customizable         less customizable
"""


#Axes-Level Functions
import seaborn as sns
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [20000, 25000, 22000, 30000, 35000]

sns.lineplot(
    x=months,
    y=sales,
    marker="o"
)

plt.title("Monthly Sales")
plt.show()