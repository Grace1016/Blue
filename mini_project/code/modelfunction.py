#!/usr/bin/env python3
"""define some functions that can help for later NLLS model fitting"""
__author__ = 'Hongye Wang (hw2419@imperial.ac.uk)'
__version__ = '0.0.1'

# imports
import pandas as pd
import numpy as np
from scipy import constants
from lmfit import minimize, Parameters, report_fit

# set constants
e = np.exp(1)

def All_data(id,df):
    """this function is to create a dictionary to store all the data in population growth models"""

    all_data = {
        'ID' : id,
        'xVal'      : np.asarray(df.Time[df.ID == id]),
        'Log_yVal'  : np.asarray(df.Log_PopBio[df.ID == id]),
        'N0'        : df.N0[df.ID == id].iloc[0],  # starting values: B,E,El,Eh,Tl,Th
        'Nmax'      : df.Nmax[df.ID == id].iloc[0],
        'Rmax'      : df.Rmax[df.ID == id].iloc[0],
        'Tlag'      : df.Tlag[df.ID == id].iloc[0],
        'Tmax'      : df.Tmax[df.ID == id].iloc[0],
        'A'         : df.A[df.ID == id].iloc[0],
        'H0'        : df.H0[df.ID == id].iloc[0],
        'u'         : df.u[df.ID == id].iloc[0]
    }
    return all_data

# model_1 : classical_model
def classical_residuals(params, x, data):
    """returns residuals of classical_model with given parameters"""
    N0 = params['N0'].value
    Nmax  = params['Nmax'].value
    Rmax = params['Rmax'].value
    
    model = (N0*Nmax*(e**(Rmax*x)))/(
                   Nmax+N0*(e**(Rmax*x)-1))

    return model - data


# create a function to try to use lmfit to find the best fitted parameters in classical model
def try_classical_residuals(id,df, max_tries = 25):
    """Use non linear least square to fit for each curve in terms of classical model"""
    all_data = All_data(id,df) # get the used data for model fitting
    xVal = all_data['xVal'] 
    yVal = all_data['Log_yVal']

    # create a dictionary to store results 
    results = {'ID'      : all_data["ID"],
               'N0'      : all_data["N0"],
               'Nmax'    : all_data["Nmax"],
               'Rmax'    : all_data["Rmax"],
               'chisqr'  : [np.NaN],
               'RSS'     : [np.NaN],
               'TSS'     : [np.NaN],
               'Rsqrd'   : [np.NaN],
               'aic'     : [np.NaN],  # will test on each try for improvment
               'bic'     : [np.NaN]}

    trycount = 0
    while True: # use while loop, until the max tries is the last try, finding the best fitting parameters by comparing AIC
        trycount += 1

        if results["aic"] != [np.NaN] or trycount > max_tries:
                break
        try:
            # When first try, use estimated starting values
            if trycount == 1:
                params = Parameters()
                params.add('N0', value = all_data["N0"])
                params.add('Nmax', value = all_data["Nmax"])
                params.add('Rmax', value = all_data["Rmax"],min=0)

            # then the starting values are selected from the Range of [0,2*estimated_starting_values]
            else:
                params = Parameters()
                params.add('N0', value = all_data["N0"])                
                params.add('Rmax', value = np.random.uniform(0, all_data["Rmax"]*2), min = 0)
                params.add('Nmax', value = all_data["Nmax"])

            # use minimize function to get the best final parameters
            out = minimize(classical_residuals, params, args = (xVal,yVal))

            # Calculate Rsquared 
            RSS = sum(classical_residuals(out.params,xVal,yVal)**2)
            TSS = sum((yVal-np.mean(yVal))**2)
            Rsquared = 1 - (RSS/TSS)

            # Store results
            if results["aic"] == [np.NaN]:
                results = {'ID'   : [id],
                           'N0'      : [out.params["N0"].value],
                           'Nmax'       : [out.params["Nmax"].value],
                           'Rmax'      : [out.params["Rmax"].value],
                           'chisqr'  : [out.chisqr],
                           'RSS'     : RSS,
                           'TSS'     : TSS,
                           'Rsqrd'   : Rsquared,
                           'aic'     : [out.aic],
                           'bic'     : [out.bic]}

            continue

        # If not converge then go to next try
        except ValueError:
            continue

        # Convert results dictionary to dataframe
    results = pd.DataFrame(results)
    return results 



  # model_2 : Gompertz model  
def gompertz_residuals(params, x, data):
    """returns residuals of gompertz_model with given parameters"""

    Tlag = params['Tlag'].value
    A = params['A'].value
    Rmax = params['Rmax'].value
    
    model = A*(e**(-e**((Rmax*e*(Tlag-x))/A)+1))

    return model - data


# create a function to try to use lmfit to find the best fitted parameters in classical model
def try_gompertz_residuals(id,df, max_tries = 25):
    """Use non linear least square to fit for each curve in terms of full gompertz model"""
    all_data = All_data(id,df) # get the used data for model fitting
    xVal = all_data['xVal'] 
    yVal = all_data['Log_yVal']

    # create a dictionary to store results 
    results = {'ID'      : all_data["ID"],
               'A'       : all_data["A"],
               'Tlag'    : all_data["Tlag"],
               'Rmax'    : all_data["Rmax"],
               'chisqr'  : [np.NaN],
               'RSS'     : [np.NaN],
               'TSS'     : [np.NaN],
               'Rsqrd'   : [np.NaN],
               'aic'     : [np.NaN],  # will test on each try for improvment
               'bic'     : [np.NaN]}

    trycount = 0
    while True: # use while loop, until the max tries is the last try, finding the best fitting parameters by comparing AIC
        trycount += 1

        if results["aic"] != [np.NaN] or trycount > max_tries:
                break
        try:
            # When first try, use estimated starting values
            if trycount == 1:
                params = Parameters()
                params.add('A', value = all_data["A"])
                params.add('Tlag', value = all_data["Tlag"],min=0)
                params.add('Rmax', value = all_data["Rmax"],min=0)

            # then the starting values are selected from the Range of [0,2*estimated_starting_values]
            else:
                params = Parameters()
                params.add('Tlag', value = np.random.uniform(0, all_data["Tlag"]*2), min = 0)
                params.add('A', value = all_data["A"])
                params.add('Rmax', value = np.random.uniform(0, all_data["Rmax"]*2), min = 0)

            # use minimize function to get the best final parameters
            out = minimize(gompertz_residuals, params, args = (xVal,yVal))

            # Calculate Rsquared 
            RSS = sum(gompertz_residuals(out.params,xVal,yVal)**2)
            TSS = sum((yVal-np.mean(yVal))**2)
            Rsquared = 1 - (RSS/TSS)

            # Store results
            if results["aic"] == [np.NaN]:
                results = {'ID'   : [id],
                           'A'       : [out.params["A"].value],
                           'Tlag'    : [out.params["Tlag"].value],
                           'Rmax'    : [out.params["Rmax"].value],
                           'chisqr'  : [out.chisqr],
                           'RSS'     : RSS,
                           'TSS'     : TSS,
                           'Rsqrd'   : Rsquared,
                           'aic'     : [out.aic],
                           'bic'     : [out.bic]}

            continue

        # If not converge then go to next try
        except ValueError:
            continue

        # Convert results dictionary to dataframe
    results = pd.DataFrame(results)
    return results



# model_3 : Baranyi model
def baranyi_residuals(params, x, data):
    """returns residuals of baranyi_model with given parameters"""
    N0 = params['N0'].value
    Nmax  = params['Nmax'].value
    Rmax = params['Rmax'].value
    H0 = params['H0'].value

    At = x+(1+Rmax)*(np.log((e**(-Rmax*x)+H0)/(1+H0)))
    model = N0+Rmax*At-(np.log(1+((e**(Rmax*At)+1)/e**(Nmax-N0))))

    return model - data


# create a function to try to use lmfit to find the best fitted parameters in baranyi model
def try_baranyi_residuals(id,df, max_tries = 25):
    """Use non linear least square to fit for each curve in terms of baranyi model"""
    all_data = All_data(id,df) # get the used data for model fitting
    xVal = all_data['xVal'] 
    yVal = all_data['Log_yVal']

    # create a dictionary to store results 
    results = {'ID'      : all_data["ID"],
               'N0'      : all_data["N0"],
               'H0'      : all_data["H0"],
               'Nmax'    : all_data["Nmax"],
               'Rmax'    : all_data["Rmax"],
               'chisqr'  : [np.NaN],
               'RSS'     : [np.NaN],
               'TSS'     : [np.NaN],
               'Rsqrd'   : [np.NaN],
               'aic'     : [np.NaN],  # will test on each try for improvment
               'bic'     : [np.NaN]}

    trycount = 0
    while True: # use while loop, until the max tries is the last try, finding the best fitting parameters by comparing AIC
        trycount += 1

        if results["aic"] != [np.NaN] or trycount > max_tries:
                break
        try:
            # When first try, use estimated starting values
            if trycount == 1:
                params = Parameters()
                params.add('N0', value = all_data["N0"])
                params.add('Nmax', value = all_data["Nmax"])
                params.add('Rmax', value = all_data["Rmax"],min=0)
                params.add('H0', value = all_data["H0"],min=0)


            # then the starting values are selected from the Range of [0,2*estimated_starting_values]
            else:
                params = Parameters()
                params.add('N0', value = all_data["N0"])                
                params.add('Rmax', value = np.random.uniform(0, all_data["Rmax"]*2), min = 0)
                params.add('Nmax', value = all_data["Nmax"])
                params.add('H0', value = np.random.uniform(0, all_data["H0"]*2), min = 0)


            # use minimize function to get the best final parameters
            out = minimize(baranyi_residuals, params, args = (xVal,yVal))

            # Calculate Rsquared 
            RSS = sum(baranyi_residuals(out.params,xVal,yVal)**2)
            TSS = sum((yVal-np.mean(yVal))**2)
            Rsquared = 1 - (RSS/TSS)

            # Store results
            if results["aic"] == [np.NaN]:
                results = {'ID'      : [id],
                           'N0'      : [out.params["N0"].value],
                           'Nmax'    : [out.params["Nmax"].value],
                           'Rmax'    : [out.params["Rmax"].value],
                           'H0'      : [out.params["H0"].value],
                           'chisqr'  : [out.chisqr],
                           'RSS'     : RSS,
                           'TSS'     : TSS,
                           'Rsqrd'   : Rsquared,
                           'aic'     : [out.aic],
                           'bic'     : [out.bic]}

            continue

        # If not converge then go to next try
        except ValueError:
            continue

        # Convert results dictionary to dataframe
    results = pd.DataFrame(results)
    return results


    # model_4 : Buchanan model
def buchanan_residuals(params, x, data):
    """returns residuals of buchanan_model with given parameters"""
    N0 = params['N0'].value
    Nmax  = params['Nmax'].value
    u = params['u'].value
    Tlag = params['Tlag'].value

    model = (N0 +(x >= Tlag)*(x <= (Tlag +  (Nmax - N0) * np.log(10)/u)) *u* (x-Tlag)/np.log(10) +
            (x >= Tlag) * (x > (Tlag + (Nmax - N0) * np.log(10)/u)) * (Nmax - N0))
    return model-data

# create a function to try to use lmfit to find the best fitted parameters in buchanan model
def try_buchanan_residuals(id,df, max_tries = 25):
    """Use non linear least square to fit for each curve in terms of buchanan model"""
    all_data = All_data(id,df) # get the used data for model fitting
    xVal = all_data['xVal'] 
    yVal = all_data['Log_yVal']

    # create a dictionary to store results 
    results = {'ID'      : all_data["ID"],
               'N0'      : all_data["N0"],
               'Tlag'    : all_data["Tlag"],
               'Nmax'    : all_data["Nmax"],
               'u'       : all_data["u"],
               'chisqr'  : [np.NaN],
               'RSS'     : [np.NaN],
               'TSS'     : [np.NaN],
               'Rsqrd'   : [np.NaN],
               'aic'     : [np.NaN],  # will test on each try for improvment
               'bic'     : [np.NaN]}

    trycount = 0
    while True: # use while loop, until the max tries is the last try, finding the best fitting parameters by comparing AIC
        trycount += 1

        if results["aic"] != [np.NaN] or trycount > max_tries:
                break
        try:
            # When first try, use estimated starting values
            if trycount == 1:
                params = Parameters()
                params.add('N0', value = all_data["N0"])
                params.add('Nmax', value = all_data["Nmax"])
                params.add('u', value = all_data["u"],min=0)
                params.add('Tlag', value = all_data["Tlag"],min=0)



            # then the starting values are selected from the Range of [0,2*estimated_starting_values]
            else:
                params = Parameters()
                params.add('N0', value = all_data["N0"])                
                params.add('u', value = np.random.uniform(0, all_data["u"]*2), min = 0)
                params.add('Nmax', value = all_data["Nmax"])
                params.add('Tlag', value = np.random.uniform(0, all_data["Tlag"]*2), min = 0)
    


            # use minimize function to get the best final parameters
            out = minimize(buchanan_residuals, params, args = (xVal,yVal))

            # Calculate Rsquared 
            RSS = sum(buchanan_residuals(out.params,xVal,yVal)**2)
            TSS = sum((yVal-np.mean(yVal))**2)
            Rsquared = 1 - (RSS/TSS)

            # Store results
            if results["aic"] == [np.NaN]:
                results = {'ID'      : [id],
                           'N0'      : [out.params["N0"].value],
                           'Nmax'    : [out.params["Nmax"].value],
                           'u'    : [out.params["u"].value],
                           'Tlag'    : [out.params["Tlag"].value],
                           'chisqr'  : [out.chisqr],
                           'RSS'     : RSS,
                           'TSS'     : TSS,
                           'Rsqrd'   : Rsquared,
                           'aic'     : [out.aic],
                           'bic'     : [out.bic]}

            continue

        # If not converge then go to next try
        except ValueError:
            continue

        # Convert results dictionary to dataframe
    results = pd.DataFrame(results)
    return results


# define a function to store data for cubic model
def cubic_data(id,df):
    """returns in a dictionary including x,y and estimated starting values"""

    cubic_dt = {
        'ID': id,
        'xVal' : np.asarray(df.Time[df.ID == id]),
        'Log_yVal'  : np.asarray(df.Log_PopBio[df.ID == id]),        
        'a'    : 0.,
        'b'    : 0.,
        'c'    : 0.,
        'd'    : 0.
    }
    return cubic_dt

#cubic residuals
def cubic_residuals(params, x, data):
    """returns residuals of data and model"""

    a = params['a'].value
    b = params['b'].value
    c = params['c'].value
    d = params['d'].value

    model = a + b*x + c*x**2 + d*x**3

    return model - data



#try fit cubic model
def try_cubic_residuals(id,df):
    cubic_dt = cubic_data(id,df) # extract data
    xVal = cubic_dt["xVal"]
    yVal = cubic_dt["Log_yVal"]

    results = {'ID'  : cubic_dt["ID"],
               'a'      : cubic_dt["a"],
               'b'      : cubic_dt["b"],
               'c'      : cubic_dt["c"],
               'd'      : cubic_dt["d"],
               'chisqr' : [np.NaN],
               'RSS'    : [np.NaN],
               'TSS'    : [np.NaN],
               'Rsqrd'  : [np.NaN],
               'aic'    : [np.NaN],  # will test on each try for improvment
               'bic'    : [np.NaN]}

    # add parameters
    params = Parameters()
    params.add('a', value = cubic_dt["a"])
    params.add('b', value = cubic_dt["b"])
    params.add('c', value = cubic_dt["c"])
    params.add('d', value = cubic_dt["d"])

    # minimize
    out = minimize(cubic_residuals, params, args = (xVal, yVal))

    RSS = sum(cubic_residuals(out.params, xVal, yVal)**2)
    TSS = sum((yVal-np.mean(yVal))**2)
    Rsquared = 1 - (RSS/TSS)

    # save output in res convert to dataframe and return
    results = {'ID'   : [id],
                'a'      : [out.params["a"].value],
                'b'      : [out.params["b"].value],
                'c'      : [out.params["c"].value],
                'd'      : [out.params["d"].value],
                'chisqr' : [out.chisqr],
                'RSS'    : RSS,
                'TSS'    : TSS,
                'Rsqrd'  : Rsquared,
                'aic'    : [out.aic],
                'bic'    : [out.bic]}

    results = pd.DataFrame(results)

    return results
    



