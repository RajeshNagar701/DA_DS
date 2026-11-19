import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
"""
pip install  seaborn

1. numpy ------> array   
2. pandas ---> data cleaning 
3. matplotlib ---> basic chart plot  
4. seaborn ---> statistical chart plot

what is  difference between  matplotlib and seaborn ??

            matplotlib               seaborn
1.    use for  basic charts        use  for statistical charts
2.    more  coding                 less coding
3.    independent                  built  on 
4.    highly  customizable         less customizable
"""

df= pd.read_csv("seaborn/customer_sales.csv")

"""month_wise = df.groupby('Month')['Sales'].sum()

plt.figure(figsize=(10,5))
sns.lineplot(
    x=month_wise.index,
    y=month_wise.values,
    marker='o',
    palette="Set1",
    label="Sales"
)
plt.title("Monthly Sales")
plt.show()
"""

# line plot  : 
"""
sns.set_style("darkgrid")
sns.set_style("dark")
sns.lineplot(data =df, x="Month", y="Sales",hue="Gender",palette="Set1",markers="o",errorbar=None)
plt.show()
"""

# two level charts :
"""

Axes level charts  : 
Relational plots:   ;line
    sns.scatterplot()
    sns.lineplot()

Distribution plots:   like histogram
    sns.histplot()
    sns.kdeplot()
    
    sns.ecdfplot()
    sns.rugplot()

Categorical plots:     bar chart
    sns.boxplot()
    sns.barplot()
    sns.countplot()
    
    sns.violinplot()
    sns.stripplot()
    sns.swarmplot()
    sns.pointplot()

Regression plots:     line chart with regression line
    sns.regplot()

Matrix plots:         find co relation between 2 or more numericle value
    sns.heatmap()
    
    
    
figure level charts:

Relational plots:
    sns.relplot() → wraps scatterplot() / lineplot()

Distribution plots:
    sns.displot() → wraps histplot(), kdeplot(), ecdfplot()
    sns.jointplot() → combines scatter + marginal histograms
    sns.pairplot() → grid of pairwise plots

Categorical plots:

    sns.catplot() → wraps boxplot(), violinplot(), barplot(), countplot(), stripplot(), swarmplot()

Regression plots:
    sns.lmplot() → wraps regplot() with faceting


"""

#scatterplot
sns.scatterplot(
    data=df,
    x="Age",
    y="Sales",
    hue="Gender",
    alpha=0.5,
    edgecolor="black",
   
)

plt.show()