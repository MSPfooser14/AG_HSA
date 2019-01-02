import pandas as pd 
import numpy as np 
import csv


file = 'MasterDataFrame_AGHSA_V1.pkl'
path = 'C:\\Users\\Jairoc\\pyHome\\Ag_HSA\\databuild\\pklmaster\\'
df = pd.read_pickle(path + file)

#gives you specific survey by filtering for sID on index level=0
Q1gSex = df.loc['3']['Q1','R1'].groupby([pd.Grouper(level='Sex')]).value_counts()

print(Q1gSex['Female'])

print(Q1gSex.index.get_level_values(('Q1','R1'))[0])

#def filtbyindex():
#	yr = str(input('Filter by Year: '))
#	nat = str(input('Filter by Nation: '))
#	loc = str(input('Filter by Location: '))
#	mo = str(input('Filter by Month: '))
#	styp = str(input('Filter by Pre/Post: '))


#note !!!! sex and age should be removed from mulitindex and treated the same as questions/answers
#index level information should have to do with filtering for specific surveys... ex. year, nat, loc, month and survey type