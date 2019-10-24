#!/usr/bin/env python3

"""A python version of Vectorize1.R2"""

__author__ = 'Hongye Wang (hw2419@ic.ac.uk)'

import math
import numpy as np
import time

# loop
def stochrick(p0 = np.random.uniform(0.5,1.5,size=1000),r=1.2,K=1,sigma=0.2,numyears=100):
    N = np.ones((numyears,len(p0)))
    N[1,] = p0
    for pop in range(1,len(p0)):
        for yr in range(2,numyears):
            N[yr,pop] = N[yr-1,pop]*math.exp(r*(1-N[yr-1,pop]/K)+np.random.normal(0,sigma,1))
    return(N)

#vectorize
def stochrickvect(p0 = np.random.uniform(0.5,1.5,size=1000),r=1.2,K=1,sigma=0.2,numyears=100):
    N = np.ones((numyears,len(p0)))
    N[1,] = p0
    for yr in range(2,numyears):
        N[yr,] = N[yr-1,]*np.exp(r*(1-N[yr-1,]/K)+np.random.normal(0,sigma,1))
    return(N)

res2 = stochrickvect()
a = time.time()
res2 = stochrickvect()
b = time.time()
res2_time = b-a

print("Vectorized Stochastic Ricker takes:")
print(res2_time)
