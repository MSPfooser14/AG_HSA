import pandas as pd 
import numpy as np 
import csv
import os
import importsurveydata as impsd
import shutil

surv_CSVdir = os.listdir('C:\\Users\\Jairoc\\pyHome\\Ag_HSA\\databuild\\surveys\\headernormpassed\\')
surv_CSVs = []
for val in surv_CSVdir:
	x = val[-4:]
	if x == '.csv':
		surv_CSVs.append(val)
surveyDFs = []
for i, val in enumerate(surv_CSVs):
	surv_ID = str(i + 1)
	path = 'C:\\Users\\Jairoc\\pyHome\\Ag_HSA\\databuild\\surveys\\headernormpassed\\' + val
	SurveyDF = impsd.importsurveydata(path, surv_ID)
	surveyDFs.append(SurveyDF)

DFMerges = []
dfOmega = pd.concat([surveyDFs[0],surveyDFs[1]])
DFMerges.append(dfOmega)
sDFremain = surveyDFs[2:]

for val in sDFremain:
	dfm = pd.concat([DFMerges[-1], val])
	DFMerges.append(dfm)


DFMerges[-1].to_pickle('C:\\Users\\Jairoc\\pyHome\\Ag_HSA\\databuild\\pklmaster\\MasterDataFrame_AGHSA_V1.pkl')
print(DFMerges[-1])