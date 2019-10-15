#!/usr/bin/env python3
"""This is a script that converts a list to a dictionary"""
__author__=' Hongye Wang (hw2419@ic.ac.uk) '


taxa = [ ('Myotis lucifugus','Chiroptera'),
         ('Gerbillus henleyi','Rodentia',),
         ('Peromyscus crinitus', 'Rodentia'),
         ('Mus domesticus', 'Rodentia'),
         ('Cleithrionomys rutilus', 'Rodentia'),
         ('Microgale dobsoni', 'Afrosoricida'),
         ('Microgale talazaci', 'Afrosoricida'),
         ('Lyacon pictus', 'Carnivora'),
         ('Arctocephalus gazella', 'Carnivora'),
         ('Canis lupus', 'Carnivora'),
        ]

# Write a short python script to populate a dictionary called taxa_dic 
# derived from  taxa so that it maps order names to sets of taxa. 
# E.g. 'Chiroptera' : set(['Myotis lucifugus']) etc. 

# Creat a key set first
keys = set([x[1] for x in taxa])
taxa_dic = {}
for key in keys:
        for i in taxa:
                if i[1] == key:
                        taxa_dic.setdefault(key,set()).add(i[0])
print(taxa_dic)
