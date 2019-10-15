#!/usr/bin/env python3
""" use ipdb function to debug bugs """
__author__=' Hongye Wang (hw2419@ic.ac.uk) '


def makeabug(x):
    y = x**4
    z = 0.
    import ipdb; ipdb.set_trace()
    y = y/z
    return y

makeabug(25)


