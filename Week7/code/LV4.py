#!/usr/bin/env python3
"""This script is a discrete-time version of integrating Lotka Volterra model and visualizing it."""

__author__ = 'Hongye Wang (hw2419@ic.ac.uk)'

import scipy as sc
import scipy.stats as st
import scipy.integrate as integrate
import matplotlib.pylab as p
import sys

def CR_t(R0,C0,t=0):
    pops = sc.empty((t,2), dtype='float')#INITIATE
    pops[0,0] = R0
    pops[0,1] = C0
    c = st.norm.rvs(0,0.1)
    for i in range(1,t): # create population list at given  discrete time
        pops[i,0] = pops[i-1,0] * (1 + (r + c) * (1 - pops[i-1,0]/K) - a * pops[i-1,1] )
        pops[i,1] = pops[i-1,1] * (1 - z + e * a * pops[i-1,0])
        if pops[i,0] <= 0 or pops[i,1] <= 0: # make sure there is non-zero populations
            break
    return pops

if len(sys.argv) == 6:
# take arguments from command line
    r = float(sys.argv[1])
    a = float(sys.argv[2])
    z = float(sys.argv[3])
    e = float(sys.argv[4])
    K = float(sys.argv[5])
else:
# set default value    
    r = 1.
    a = 0.1
    z = 0.5
    e = 0.75
    K = 20

#set length of t (could be every second,minute,hour,day,month or year)
t = 60

# set initial populations
R0 = 10
C0 = 5 
populations = CR_t(R0,C0,t)

print("the final population values is:")
print(populations)



f1 = p.figure()
p.plot(range(t), populations[:,0], 'g-', label='Resource density') # Plot
p.plot(range(t), populations[:,1]  , 'b-', label='Consumer density')
p.grid()
p.legend(loc='best')
p.xlabel('Time')
p.ylabel('Population density')
textstr = ''
textstr += 'r='+str(r)+'\n'+'a='+str(a)+'\n'+'z='+str(z)+'\n'+'e='+str(e)+'\n'+'K='+str(K)
p.text(61.5,5,textstr,fontsize=12)
p.title('Consumer-Resource population dynamics')
# p.show()# To display the figure

f1.savefig('../result/LV4_model1.pdf') #Save figure

f2 = p.figure()
p.plot(populations[:,0], populations[:,1], 'r-')
p.grid()
p.yticks([2.5,5,7.5,10,12.5,15,17.5,20,22.5])
p.xticks([10,15,20,25,30,35,40])
p.text(35,17.5,textstr,fontsize=12)
p.xlabel('Resource density')
p.ylabel('Consumer density')
p.title('Consumer-Resource population dynamics')
# p.show()

f2.savefig('../result/LV4_model2.pdf')