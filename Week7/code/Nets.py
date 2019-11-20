"""This script is to visualizes the QMEE CDT collaboration network"""

import csv
import pandas
import networkx as nx
import matplotlib.pyplot as p
import scipy as sc

# assign nodes and link from data file
nodes = pandas.read_csv('../Data/QMEE_Net_Mat_nodes.csv')
link = pandas.read_csv('../Data/QMEE_Net_Mat_edges.csv')

# rename the row name in dataframe
link = link.rename(index={0:'ICL',1:'UoR',2:'CEH',3:'ZSL',4:'CEFAS',5:'NonAc'})

# reset the dataframe to an edge list
edgels = link.stack().reset_index()

# reset the column name more meaningfully
edgels = edgels.rename(columns={'level_0':'Source', 'level_1':'Target', 0:'Weight'})

# delete the zero weight pair
edgels = edgels[edgels.Weight != 0]

# convert to tuple
edgels = edgels.apply(tuple, axis=1)

# create a circular layout
pos = nx.circular_layout(nodes["id"])

G = nx.Graph()
G.add_nodes_from(nodes["id"]) # add nodes

for (Source,Target,Weight) in edgels:
    G.add_weighted_edges_from(edgels,weight=Weight)

# plot and save
f = p.figure()

nx.draw_networkx(G,pos,node_size = 1000,node_color = ["r","r","g","g","g","b"])

p.legend(pandas.unique(nodes["Type"]),numpoints = 0.1,loc = 1,prop={'size':12})
# p.show()
f.savefig("../result/QMEE_py.svg")