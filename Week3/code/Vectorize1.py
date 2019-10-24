#!/usr/bin/env python3

"""A python version of Vectorize1.R"""

__author__ = 'Hongye Wang (hw2419@ic.ac.uk)'

# import modules
import numpy as np
import time

M = np.random.uniform(low=0,high=1,size=[1000,1000])
def SumALLElements(M):
    ToT = 0
    for i in range(0,M.shape[0]):
        for j in range(0,M.shape[1]):
            ToT = ToT+M[i,j]
    return ToT

a = time.time()
SumALLElements(M)
b = time.time()
time1 = b-a
print("SUM ALL ELEMENTS In Loop takes:")
print(time1)

c = time.time()
np.sum(M)
d = time.time()
time2 = d-c
print("Sum all elements by vectorize takes:")
print(time2)
