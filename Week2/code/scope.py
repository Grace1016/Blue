#!/usr/bin/env python3
""" this script helps us better understand the difference between global and local variable """
__author__='Hongye Wang (hw2419@ic.ac.uk)'


## Try this first
_a_global = 10

def a_function():
    """ see the difference between global and local value """
    _a_global = 5
    _a_local = 4
    print("Inside the function, the value is ", _a_global)
    print("Inside the function, the value is ", _a_local)
    return None

a_function()

print("Outside the function, the value is ", _a_global)


## Now try this

_a_global = 10

def a_function():
    """ see if a global outside the function """
    global _a_global
    _a_global = 5
    _a_local = 4
    print("Inside the function, the value is ", _a_global)
    print("Inside the function, the value is ", _a_local)
    return None

a_function()
print("Outside the function, the value is", _a_global)
