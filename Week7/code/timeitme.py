#!/usr/bin/env python3
"""This is a script to compare the time using by different ways,that is profiling"""

__author__ = 'Hongye Wang (hw2419@ic.ac.uk)'

##############################################################################
# loops vs. list comprehensions: which is faster?
##############################################################################

iters = 1000000

import timeit

from profileme import my_squares as my_squares_loops

from profileme2 import my_squares as my_squares_lc

# %timeit my_squares_loops(iters)
# %timeit my_squares_lc(iters)


##############################################################################
# loops vs. the join method for strings: which is faster?
##############################################################################

mystring = "my string"

from profileme import my_join as my_join_join

from profileme2 import my_join as my_join

# %timeit(my_join_join(iters, mystring))
# %timeit(my_join(iters, mystring)) 

import time
start = time.time()
my_squares_loops(iters)
print("my_squares_loops takes %f s to run." % (time.time() - start))

start = time.time()
my_squares_lc(iters)
print("my_squares_lc takes %f s to run." % (time.time() - start))

start = time.time()
my_join_join(iters,mystring)
print("my_join_join takes %f s to run" % (time.time() - start))

start = time.time()
my_join(iters,mystring)
print("my_join takes %f s to run" % (time.time() - start))
