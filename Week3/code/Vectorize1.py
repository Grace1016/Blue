#!/usr/bin/env python3

"""A python version of Vectorize1.R which is compare the time consuming between loop and vectorize"""

__author__ = 'Hongye Wang (hw2419@ic.ac.uk)'

# import modules
import numpy as np
import time

Matrix = np.random.uniform(low=0,high=1,size=[1000,1000])
def SumALLElements(Matrix):
    ToT = 0
    for i in range(0,Matrix.shape[0]):
        for j in range(0,Matrix.shape[1]):
            ToT = ToT+Matrix[i,j]
    return ToT

a = time.time()
SumALLElements(Matrix)
b = time.time()
time1 = b-a
print("SUM ALL ELEMENTS In Loop takes:")
print(time1)

start = time.time()
np.sum(Matrix)
stop = time.time()
time2 = stop-start
print("Sum all elements by vectorize takes:")
print(time2)
