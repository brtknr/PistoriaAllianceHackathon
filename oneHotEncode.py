from sklearn import preprocessing
import pandas as pd
import numpy as np
import sys

df = pd.read_csv('f-02.tsv',delimiter='\t')

ec = preprocessing.LabelEncoder()
df['OldAANumeric'] = ec.fit_transform(df.OldAA)
df['NewAANumeric'] = ec.fit_transform(df.NewAA)

ec = preprocessing.OneHotEncoder()
nf = pd.DataFrame(ec.fit_transform(df[['OldAANumeric','NewAANumeric']]).todense(),dtype=int)

nf['PhredC'] = (df.PhredC - df.PhredC.min())/(df.PhredC.max()-df.PhredC.min())
nf['ClinSigSimple'] = df['ClinSigSimple']
nf.to_csv('ohe-aminos-normed-PhredC-02.csv')

zeros = nf.ClinSigSimple==0
ones = nf.ClinSigSimple==1

nf[zeros]
nf[ones]