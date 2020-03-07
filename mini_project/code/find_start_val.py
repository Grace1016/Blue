#!/usr/bin/env python3
"""Find starting values for all the parameters"""
__author__ = 'Hongye Wang (hw2419@imperial.ac.uk)'
__version__ = '0.0.1'

#import
import pandas as pd
import scipy as sc
import matplotlib.pylab as pl
import seaborn as sns
import numpy as np
from scipy import stats
import math
import warnings

warnings.filterwarnings("ignore")

#read the csv data
data = pd.read_csv("../data/modified_data.csv") 
data.drop('Unnamed: 0',axis=1,inplace=True) #drop useless columns

#creat function to find tne starting values
def cal_start_value(curve_subset): #define a function to calculate the starting values of each parameter
    curve = curve_subset.sort_values('Time') # sort the curve data by "time"
    end = curve.shape[0] #calculate the number of data in each subset
    curve = curve.reset_index(drop=True) #reset the index 
    rmax = 0 #give Rmax an initial value
    e = np.exp(1)
    for i in range(end-4):
        Nmax = curve['PopBio'].max()#Nmax is the carrying capacity, here I make Nmax equal to the maximum popbio
        nmax = curve['Log_PopBio'].max() #nmax is the maximum log_PopBio
        tmax = curve[curve['PopBio']==curve['PopBio'].max()].iat[0,1] #Tmax is the time at which Nmax is reached. 
        N0 = curve.at[0,"PopBio"]#N0 is the initial population size
        n0 = curve.at[0,"Log_PopBio"] #n0 is the loged initial population size
        a = np.log(Nmax/N0) #A is the asymptote 
        data_subset = curve.loc[i:i+3] #choose four points as a group from initial point in the time order
        x = data_subset['Time']
        y = data_subset['Log_PopBio']
        line = stats.linregress(x,y) #draw lines among every four points to find the maximum slope which can represent Rmax( the maximum growth rate)
        if line[0] > rmax :
            rmax = line[0] #use the max slope to take place of Rmax
            tlag = -line[1]/line[0] #tlag is the x-intercept
            h0 = 1/(e**(tlag*rmax)-1)
            u = (nmax-n0)/(tmax-tlag)
            curve_subset['Rmax'] = rmax #add new columns to the dataframe, which are will be needed in model fitting
            curve_subset['Tlag'] = tlag
            curve_subset['Nmax'] = nmax
            curve_subset['Tmax'] = tmax
            curve_subset['N0'] = n0
            curve_subset['A'] = a
            curve_subset['H0'] = h0
            curve_subset["u"] = u
    return(curve_subset)

data = data.groupby("ID").apply(cal_start_value) #divide the whole data into subsets according to ID, and then apply the function
data #check the data
data.to_csv('../data/start_val_data.csv')
