#!/usr/bin/env python3
""" exercise of sys function and defining functions """
__author__='Hongye Wang (hw2419@ic.ac.uk)'

import sys

# What does each of foo_x do? 
def foo_1(x):
    """ calculate the square root of x """
    return x ** 0.5

def foo_2(x, y):
    """ compare the x and y, choose the bigger one """
    if x > y:
        return x
    return y

def foo_3(x, y, z):
    """ check if the given three number are in ascending order, if not exchange the value """
    if x > y:
        tmp = y
        y = x
        x = tmp
    if y > z:
        tmp = z
        z = y
        y = tmp
    return [x, y, z]

def foo_4(x):
    """ a loop to use all the numbers from a range of 1 to x+1 
        to multiply them together，x is given from input
    """
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result

def foo_5(x):
    """ a recursive function to calculate what foo_4 did """
    if x == 1:
        return 1
    return x * foo_5(x - 1)

def foo_6(x): 
    """ another way that use while loop to calculate what foo_4,foo_5 will do """
    facto = 1
    while x >= 1:
        facto = facto * x
        x = x - 1
    return facto

#test all of them above by a function similar to control_flow.py (if it is not imported by other script)
def main(argv):
    """ test every foo function """
    print(foo_1(27))
    print(foo_2(4,23))
    print(foo_3(3,1,7))
    print(foo_4(7))
    print(foo_5(10))
    print(foo_6(4))
    return 0

if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)