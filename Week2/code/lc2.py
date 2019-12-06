#!/usr/bin/env python3
"""This is a script using two methods to find when the amount of rain in rainfall was greater than 100 and less than 50"""
__author__=' Hongye Wang (hw2419@ic.ac.uk) '


# Average UK Rainfall (mm) for 1910 by month
# http://www.metoffice.gov.uk/climate/uk/datasets
rainfall = (('JAN',111.4),
            ('FEB',126.1),
            ('MAR', 49.9),
            ('APR', 95.3),
            ('MAY', 71.8),
            ('JUN', 70.2),
            ('JUL', 97.1),
            ('AUG',140.2),
            ('SEP', 27.0),
            ('OCT', 89.4),
            ('NOV',128.4),
            ('DEC',142.2),
           )

# (1) Use a list comprehension to create a list of month,rainfall tuples where
# the amount of rain was greater than 100 mm.
greater_than_100 = [] # create a list for storing
for x in rainfall: 
    # store the month names and rainfall amount in the list
    if x[1] > 100:
       greater_than_100.append(x)
print("Displaying the results")
print("\nmonthes where the amount of rain was greater than 100 mm :" ,greater_than_100)

# using a list comprehension to sovle this problem
greater_than_100 = [ tuple for tuple in rainfall if tuple[1]>100]
print("Second method")
print ("\nmonthes where the amount of rain was greater than 100 mm :" ,greater_than_100)
 
# (2) Use a list comprehension to create a list of just month names where the
# amount of rain was less than 50 mm. 
less_than_50 = [] #creat a list for storing
for name in rainfall: 
    # store the month names and rainfall amount in the list
    if name[1] < 50:
        less_than_50.append(name[0])
print("\nDisplaying the results")
print("\nmothe names where the amount of rain was less than 50 mm :", less_than_50)

# using a list comprehension to sovle this problem
less_than_50 = [ name[0] for name in rainfall if name[1]<50]
print("\nSecond method")
print("\nmothe names where the amount of rain was less than 50 mm :", less_than_50)

# (3) Now do (1) and (2) using conventional loops (you can choose to do 
# this before 1 and 2 !). 


