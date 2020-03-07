#!/usr/bin/env python3
"""This script is to modify the original database, make it available in model fitting"""
__author__ = 'Hongye Wang (hw2419@imperial.ac.uk)'
__version__ = '0.0.1'



#import
import pandas as pd
import scipy as sc
import matplotlib.pylab as pl
import numpy as np
import warnings
warnings.filterwarnings("ignore")
## read and load the data
data = pd.read_csv("../data/LogisticGrowthData.csv")
print("Loaded {} columns.".format(len(data.columns.values)))
pd.read_csv("../data/LogisticGrowthMetaData.csv")

#set unique ID
data.insert(0, "ID", data.Species + "_" + data.Temp.map(str) + "_" + data.Medium + "_" + data.Citation + "_" + data.Rep.map(str))
#remove the uncommon data
data = data[data['Time']  > 0 ]
data = data[data['PopBio']  > 0 ]
#delet the subset with data less than 5
df = data.groupby(['ID']).filter(lambda x: len(x) > 4)
#make the ID start from number 1 and drop the unnesessary columns
df['ID'] = pd.factorize(df['ID'])[0] + 1
df.drop(['X','Temp','Time_units','PopBio_units','Rep','Medium'],axis=1,inplace=True)
#creat a new column to store the logged population size
df['Log_PopBio'] = np.log(df['PopBio'])
#print data frame
df
#output the data frame as a csv file
df.to_csv('../data/modified_data.csv')


