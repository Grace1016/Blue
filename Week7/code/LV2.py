#!/usr/bin/env python3
"""This script is a improvement of LV1 which is integrating Lotka Volterra model and visualizing it."""

__author__ = 'Hongye Wang (hw2419@ic.ac.uk)'

import scipy as sc
import scipy.integrate as integrate
import matplotlib.pylab as p
import sys

def dCR_dt(pops, t=0):
    """define the model"""
    R = pops[0]
    C = pops[1]
    dRdt = r * R * (1 - R/K) - a * R * C 
    dCdt = -z * C + e * a * R * C
    
    return sc.array([dRdt, dCdt])
type(dCR_dt)


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
    a = 0.5
    z = 1.5
    e = 0.75
    K = 40

t = sc.linspace(0, 15,  1000)

R0 = 10
C0 = 5 
RC0 = sc.array([R0, C0])


pops, infodict = integrate.odeint(dCR_dt, RC0, t, full_output=True)
print(pops)
type(infodict)
infodict.keys()
infodict['message']

f1 = p.figure()
p.plot(t, pops[:,0], 'g-', label='Resource density') # Plot
p.plot(t, pops[:,1]  , 'b-', label='Consumer density')
p.grid()
p.legend(loc='best')
p.xlabel('Time')
p.ylabel('Population density')
textstr = ''
textstr += 'r='+str(r)+'\n'+'a='+str(a)+'\n'+'z='+str(z)+'\n'+'e='+str(e)+'\n'+'K='+str(K)
p.text(16.5,5,textstr,fontsize=12)
p.title('Consumer-Resource population dynamics')
#p.show()# To display the figure

f1.savefig('../result/LV2_model1.pdf') #Save figure

f2 = p.figure()
p.plot(pops[:,0], pops[:,1], 'r-')
p.grid()
p.yticks([2.5,5,7.5,10,12.5,15,17.5,20,22.5])
p.xticks([10,15,20,25,30,35,40])
p.text(35,17.5,textstr,fontsize=12)
p.xlabel('Resource density')
p.ylabel('Consumer density')
p.title('Consumer-Resource population dynamics')
#p.show()

f2.savefig('../result/LV2_model2.pdf')