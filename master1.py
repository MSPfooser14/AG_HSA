import pandas as pd 
import numpy as np 
import csv
import shutil

file = input('Enter filename: ')
path = 'C:\\Users\\Jairoc\\pyHome\\Ag_HSA\\databuild\\pklsurvey\\'
df = pd.read_pickle(path + file)

print(df)

df.to_pickle('C:\\Users\\Jairoc\\pyHome\\Ag_HSA\\databuild\\pklmaster\\MasterDataFrame_AGHSA_V1.pkl')

srcfile = path + file
destdir = 'C:\\Users\\Jairoc\\pyHome\\Ag_HSA\\databuild\\pklsurvey\\merged_to_master\\'
shutil.move(srcfile, destdir)