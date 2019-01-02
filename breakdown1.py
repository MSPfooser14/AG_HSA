import pandas as pd 
import numpy as np 
import csv
import matplotlib.pyplot as plt


file = 'C:\\Users\\Jairoc\\pyHome\\Ag_HSA\\databuild\\pklmaster\\MasterDataFrame_AGHSA_V1.pkl'
df = pd.read_pickle(file)

sID = str(1)

Q1gSex = df.loc['3']['Q1','R1'].groupby([pd.Grouper(level='Sex')]).value_counts()



fig1, ax1 = plt.subplots()
ax1.pie(Q1gSex['Female'], labels=Q1gSex['Female'].index.get_level_values(('Q1','R1')), autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

plt.show()