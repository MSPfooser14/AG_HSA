import pandas as pd 
import numpy as np 
import csv
import os
import headnorm
import calendar
import shutil

#importing survey data from user entered filename/path
file = input('Enter filename: ')
path = 'C:\\Users\\Jairoc\\pyHome\\Ag_HSA\\databuild\\surveys\\headernormpassed\\'
f = open(path + file)
reader_f = csv.reader(f)
#analyzing filename for location, nation, and survey type (pre or post)
fname = file.split("-")
loct = fname[0].strip()
nat = fname[1].strip()
styp = fname[-1].split(".")[0].strip()
pklname = file[:-4] + 'DF_pkl'
#lines 1&2 are header data
h1 = next(reader_f)
h2 = next(reader_f)
#normalized question headers
h1n, h2n = headnorm.normheader(h1)

#lines 3+ are respondent data
Resp_data = []
for row in reader_f:
	Resp_data.append(row)
#extracting index data from each respondent into a list of tuples
index_tup = []
for i in range(len(Resp_data)):
	#respondent index parameters
	RiP = []
	x = Resp_data[i]
	y = Resp_data[0]
	age = x[9]
	sex = (x[10] + x[11]).strip()
	year = x[2].split()[0].split("/")[2]
	monthnum = y[2].split()[0].split("/")[0]
	month = calendar.month_abbr[int(monthnum)]
	RiP.append(year)
	RiP.append(nat)
	RiP.append(loct)
	RiP.append(month)
	RiP.append(styp)
	RiP.append(sex)
	RiP.append(age)
	RiP = tuple(RiP)
	index_tup.append(RiP)
#creating multi index from tuples
index1 = pd.MultiIndex.from_tuples(index_tup)
#creating an array of respondent answers (specific to this survey format)
#number of responses for particular survey
Q_len = []
for val in h1n:
	if val != '':
		Q_len.append(1)
offset = (len(h1n) - len(Q_len))

QSer_list = []
for val in range(len(Q_len)):
	Qx = []
	for i in range(len(Resp_data)):
		x = Resp_data[i]
		y = x[val+offset]
		Qx.append(y)
	QxSer = pd.Series(Qx, index=index1)
	QSer_list.append(QxSer)

col_idx = []
for i in range(len(Q_len)):
	t = []
	x = h1n[i+offset]
	y = h2n[i+offset]
	t.append(x)
	t.append(y)
	t = tuple(t)
	col_idx.append(t)


#creating dictionary where keys are column index tuples and associated data are answer lists
QSer_dict = {}
for i, val in enumerate(QSer_list):
	x = col_idx[i]
	QSer_dict[x] = val

MasterDF = pd.DataFrame(QSer_dict)
MasterDF = MasterDF.sort_index()
MasterDF = MasterDF.sort_index(axis=1)
MasterDF.index.names = ['Year', 'Nat.', 'Loc.', 'Mo.', 'Type', 'Sex', 'Age']
path1 = 'C:\\Users\\Jairoc\\pyHome\\Ag_HSA\\databuild\\pklsurvey\\'
MasterDF.to_pickle(path1 + pklname + '.pkl')

print(MasterDF)

f.close()
srcfile = path + file
destdir = 'C:\\Users\\Jairoc\\pyHome\\Ag_HSA\\databuild\\surveys\\headernormpassed\\imported\\'
shutil.move(srcfile, destdir)