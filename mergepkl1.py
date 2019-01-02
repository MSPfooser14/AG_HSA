import pandas as pd 
import numpy as np 
import csv
import shutil

file = input('Enter filename: ')
path = 'C:\\Users\\Jairoc\\pyHome\\Ag_HSA\\databuild\\pklsurvey\\'
df_new = pd.read_pickle(path + file)
df_legacy = pd.read_pickle('C:\\Users\\Jairoc\\pyHome\\Ag_HSA\\databuild\\pklmaster\\MasterDataFrame_AGHSA_V1.pkl')
print(df_new)
print(df_legacy)

df3 = pd.concat([df_new,df_legacy])
print(df3)
print(df3.columns)

srcfile = path + file
destdir = 'C:\\Users\\Jairoc\\pyHome\\Ag_HSA\\databuild\\pklsurvey\\merged_to_master\\'


user_conf = input('Confirm merge? (y/n): ')
if user_conf == 'y':
	df3.to_pickle('C:\\Users\\Jairoc\\pyHome\\Ag_HSA\\databuild\\pklmaster\\MasterDataFrame_AGHSA_V1.pkl')
	shutil.move(srcfile, destdir)