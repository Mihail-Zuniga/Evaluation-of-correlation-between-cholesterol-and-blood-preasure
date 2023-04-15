#IMPORT OF LIBRARIES AND DATAFRAME
from scipy.signal import medfilt
from scipy import stats
import pandas as pd
import numpy as np

df = pd.read_csv('dataheart.csv')
print(len(df))
print(df)

# DEFINITION OF VARIABLES AND RANGES
df = df[(df.SEXO == 1)]
df = df[(df.EDAD >= 60)]
df = df[(df.EDAD <= 65)]
n1 = 'PRES'
n2 = 'COL'
n3 =  'EDAD'
df = df.drop(['GA'], axis = 1)
df = df.drop(['RER'], axis = 1)
df = df.drop(['TD'], axis = 1)
df = df.drop(['FCM'], axis = 1)
df = df.drop(['AIE'], axis = 1)
df = df.drop(['PicoA'], axis = 1)
df = df.drop(['MST'], axis = 1)
df = df.drop(['NVP'], axis = 1)
df = df.drop(['tal'], axis = 1)
df = df.drop(['CARIO'], axis = 1)
df = df.drop(['SEXO'], axis = 1)

print(len(df))
print(df)

#DEFINITION OF PERCENTILS (Removing outliers)
df = df[(df[n2] < np.percentile(df[n2].dropna(),95)) &
       (df[n2] > np.percentile(df[n2].dropna(),5))]
df = df[(df[n1] < np.percentile(df[n1].dropna(),95)) &
       (df[n1] > np.percentile(df[n1].dropna(),5))]

print(len(df))

## Finally the preprocessing has ended
df.to_csv('outputlbiolof.csv',index=False)
