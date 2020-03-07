#!/usr/bin/env python3
"""start NLLS model fitting"""
__author__ = 'Hongye Wang (hw2419@imperial.ac.uk)'
__version__ = '0.0.1'

#import
import pandas as pd
import sys
from datetime import datetime
from modelfunction import *

#set the maximum time for try
if len(sys.argv) > 4:
    max_time = sys.argv[2]
    print("Use given parameter: \nMax tries: {0}".format(max_time))
else:
    max_time = 30
    print("Use default parameter: \nMax tries: {0}".format(max_time))
    
start_time = datetime.now()

df = pd.read_csv("../data/start_val_data.csv") #read the data

#creat blank dataframe for store the results
cla_model_result = pd.DataFrame(data = None)
gom_model_result = pd.DataFrame(data = None)
bar_model_result = pd.DataFrame(data = None)
bucha_model_result = pd.DataFrame(data = None)
cubic_model_result = pd.DataFrame(data = None)

#run model fitting function 
print("Starting the NLLS model fitting now")
iterations = len(df.ID.unique())
print("\nModel_1.1: classical model")
for id in df["ID"].unique():
    cla_model_result = cla_model_result.append(try_classical_residuals(id,df,max_time))
failed = cla_model_result.aic.isnull().sum()
converged = iterations - failed
print("\n{0} of {1} curves converged.".format(converged,iterations))

print("\nModel_2.1: Gompertz model")
for id in df["ID"].unique():
    gom_model_result = gom_model_result.append(try_gompertz_residuals(id,df,max_time))
failed = gom_model_result.aic.isnull().sum()
converged = iterations - failed
print("\n{0} of {1} curves converged.".format(converged,iterations))

print("\nModel_3.1: Baranyi model")
for id in df["ID"].unique():
    bar_model_result = bar_model_result.append(try_baranyi_residuals(id,df,max_time))
failed = bar_model_result.aic.isnull().sum()
converged = iterations - failed
print("\n{0} of {1} curves converged.".format(converged,iterations))


print("\nModel_4: Buchanan model")
for id in df["ID"].unique():
    bucha_model_result = bucha_model_result.append(try_buchanan_residuals(id,df,max_time))
failed = bucha_model_result.aic.isnull().sum()
converged = iterations - failed
print("\n{0} of {1} curves converged.".format(converged,iterations))

print("\nModel_5: Cubic model")
for id in df["ID"].unique():
    cubic_model_result = cubic_model_result.append(try_cubic_residuals(id,df))
failed = cubic_model_result.aic.isnull().sum()
converged = iterations - failed
print("\n{0} of {1} curves converged.".format(converged,iterations))




print("\nsaving results")
cla_model_result.to_csv("../results/classical_model.csv")
gom_model_result.to_csv("../results/gompertz_model.csv")
bar_model_result.to_csv("../results/baranyi_model.csv")
bucha_model_result.to_csv("../results/buchanan_model.csv")
cubic_model_result.to_csv("../results/cubic_model.csv")

print("Time taken: ", datetime.now() - start_time)