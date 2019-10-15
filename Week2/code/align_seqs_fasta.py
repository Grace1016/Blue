#!/usr/bin/env python3
"""Match two sequences from different external files"""
__author__ = 'Hongye Wang (hw2419@ic.ac.uk)'

import sys
arg = sys.argv[1:]    # a list of filenames arguments

# default sequences
if arg == []:
    arg.append("../data/fasta/407228326.fasta")
    arg.append("../data/fasta/407228412.fasta")

f1 = arg[0]
f2 = arg[1]

# read sequences in files
seq1 = ""
with open(f1, "r") as f:
    next(f)
    for line in f.readlines():
        line = line.strip()
        seq1 += line
f.close()

seq2 = ""
with open(f2, "r") as f:
    next(f)
    for line in f.readlines():
        line = line.strip()
        seq2 += line
f.close()

# Assign the longer sequence s1, and the shorter to s2
# l1 is length of the longest, l2 that of the shortest

l1 = len(seq1)
l2 = len(seq2)
if l1 >= l2:
    s1 = seq1
    s2 = seq2
else:
    s1 = seq2
    s2 = seq1
    l1, l2 = l2, l1 # swap the two lengths

# A function that computes a score by returning the number of matches starting
# from arbitrary startpoint (chosen by user)
def calculate_score(s1, s2, l1, l2, startpoint):
    matched = "" # to hold string displaying alignements
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]: # if the bases match
                matched = matched + "*"
                score = score + 1
            else:
                matched = matched + "-"

    # some formatted output
    # print("." * startpoint + matched)           
    # print("." * startpoint + s2)
    # print(s1)
    # print(score) 
    # print(" ")

    return score

    # now try to find the best match (highest score) for the two sequences
my_best_align = None
my_best_score = -1

for i in range(l1): # Note that you just take the last alignment with the highest score
    z = calculate_score(s1, s2, l1, l2, i)
    if z > my_best_score:
        my_best_align = "." * i + s2 # think about what this is doing!
        my_best_score = z 

f = open('../Results/fasta_alignment.txt','w')
f.write(my_best_align + '\n' + s1 + '\n' + "Best score:" + str(my_best_score))
f.close()


