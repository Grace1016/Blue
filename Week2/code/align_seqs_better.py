#!/usr/bin/env python3
"""Match two sequences and output all the best alignments"""
__author__ = 'Hongye Wang (hw2419@ic.ac.uk)'

import pickle

# use two simple sequences as examples
seq2 = "ATCGCCGGATTACGGG"
seq1 = "CAATTCGGAT"

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
    """ match the two sequences from the startpoint, then store the matched score and matched pattern"""
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

# Test the function with some example starting points:
# calculate_score(s1, s2, l1, l2, 0)
# calculate_score(s1, s2, l1, l2, 1)
# calculate_score(s1, s2, l1, l2, 5)

# now try to find the best match (highest score) for the two sequences
my_best_align = None
my_best_score = -1
best_align_num = 0 # count the number of best alignments

f = open('../sandbox/pickle.p', 'wb') # storing all best alignments in a file 'pickle.p'
for i in range(l1): 
    z = calculate_score(s1, s2, l1, l2, i)
    if z >= my_best_score:
        best_align_num += 1
        my_best_align = "." * i + s2 # think about what this is doing!(second sequence showed from the startpoint)
        my_best_score = z 
        pickle.dump(my_best_align, f, 0)
f.close()

# output all the best results in All_best_Aligment.txt
f = open('../sandbox/pickle.p','rb')
all_best_seq = open('../Results/All_best_Alignment.txt', 'w')

for i in range(best_align_num):
    all_best_seq.write(pickle.load(f) + '\n' + s1 + '\n' + "Best score:" + str(my_best_score) + '\n' + '\n')
f.close()
all_best_seq.close() 
