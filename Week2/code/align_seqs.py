#!/usr/bin/env python3
""" This is a script to match two sequences """
__author__ = ' Hongye Wang (hw2419@ic.ac.uk) '

#read the data from sequence file
lines = []
f = open('../data/Sequences.txt','r')
for line in f.readlines():
    lines.append(line.strip('\n'))
f.close()

seq1 = lines[0]
seq2 = lines[1]

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
    """ match the two sequences from the startpoint, then store the matched score and matched pattern """
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
    print("." * startpoint + matched)           
    print("." * startpoint + s2)
    print(s1)
    print(score) 
    print(" ")

    return score

# Test the function with some example starting points:
# calculate_score(s1, s2, l1, l2, 0)
# calculate_score(s1, s2, l1, l2, 1)
# calculate_score(s1, s2, l1, l2, 5)

# now try to find the best match (highest score) for the two sequences
my_best_align = None
my_best_score = -1

for i in range(l1): # Note that you just take the last alignment with the highest score
    z = calculate_score(s1, s2, l1, l2, i)
    if z > my_best_score:
        my_best_align = "." * i + s2 # think about what this is doing!
        my_best_score = z 
#print(my_best_align)
#print(s1)
#print("Best score:", my_best_score)

#open a result .txt file and store the data into it
g = open(r'../Results/best_alignment_result.txt','w')
g.write("Best_alignment: " + my_best_align + '\n' + "Best_score: " + str(my_best_score))
g.close()