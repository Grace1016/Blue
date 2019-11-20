#!/usr/bin/env python3
"""This script shows how to profile the code."""

__author__ = 'Hongye Wang (hw2419@ic.ac.uk)'

def my_squares(iters):
    out = [i **2 for i in range(iters)]
    return out

def my_join(iters,string):
    out = ''
    for i in range(iters):
        out += ", " + string
    return out

def run_my_func(x,y):
    print(x,y)
    my_squares(x)
    my_join(x,y)
    return 0

run_my_func(10000000,"MY string")