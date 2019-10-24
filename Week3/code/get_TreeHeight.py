#!/usr/bin/env python3
"""This function calculates heights of trees given distance of each tree
 from its base and angle to its top, using  the trigonometric formula"""

__author__ = 'Hongye Wang (hw2419@ic.ac.uk)'

# height = distance * tan(radians)
#
# ARGUMENTS
# degrees:   The angle of elevation of tree
# distance:  The distance from base of tree (e.g., meters)
#
# OUTPUT
# The heights of the tree, same units as "distance"
import sys
import csv
import os
import math

def TreeHeight(degrees,distance):
  radians = degrees * math.pi / 180
  height = distance * math.tan(radians)
  return (height)

# import data and takes the file name from command line 
mydata = []
with open(sys.argv[1],"r") as f:
    for line in csv.reader(f):
        mydata.append(line)
f.close()

#set arguments and calculate the height of trees
mydata[0].append("Tree.Height.m")
for i in range(1,len(mydata)):
    mydata[i].append(TreeHeight(float(mydata[i][2]),float(mydata[i][1]))) 

#Result <- data.frame(mydata,Tree.Height.m) # combine treeheight with other datas of trees
#output <- head(Result,2) # cat first 2 datas in results

# output as request
with open("../result/"+os.path.splitext(os.path.basename(sys.argv[1]))[0]+"_treeheights.csv","w") as g:
    for line in mydata:
        csv.writer(g).writerow(line)
g.close()
