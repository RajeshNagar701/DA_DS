import  seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# box  plot  : outlier means in sale one value drastic changes 

# df=pd.read_csv("Seaborn_lib/transactions.csv")

# sns.boxplot(x=df["Transaction_Amount"])
           
# plt.show() 

# manually  calculate the  outlier  : IQR :  -----> HW 

# violin  plot  :

# df=pd.read_csv("Seaborn_lib/transactions.csv")
# sns.violinplot(x=df["Transaction_Amount"],
#                hue=df["Transaction_Type"]
#                )
# plt.show()


# compare -----> using axes  box vs violin  plot  :

# pairplot  :  4 chart many chart in one chart (sub plot)

# df=pd.read_csv("Seaborn_lib/customer_data.csv")

# # sns.pairplot(data=df[['Age','Annual_Income','Spending_Score']],
#             #  hue=df['Customer_Segment']
#             #  )
# sns.pairplot(df,
#              hue='Customer_Segment',
#              vars=['Age','Annual_Income','Spending_Score'],
#              kind='reg'
#              )

# plt.show()