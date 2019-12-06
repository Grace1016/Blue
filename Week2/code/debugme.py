#!/usr/bin/env python3
""" use pdb function to debug bugs """
__author__=' Hongye Wang (hw2419@ic.ac.uk) '


def makeabug(x):
    y = x**4
    z = 0.
    import pdb; pdb.set_trace()
    y = y/z
    return y

makeabug(25)


