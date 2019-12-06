#!/usr/bin/env python3
__author__ = 'Hongye Wang (hw2419@ic.ac.uk)'


import scipy as sc
import scipy.integrate as integrate
def dCR_dt(pops, t=0):
    R = pops[0]
    C = pops[1]
    dRdt = r * R - a * R * C 
    dCdt = -z * C + e * a * R * C
    return sc.array([dRdt, dCdt])

r = 1
a = 0.1
z = 1.5
e = 0.75
t = sc.linspace(0,15,1000)
R0 = 10
C0 = 5
RC0 = sc.array([R0,C0])
pops,infodict = integrate.odeint(dCR_dt,RC0,t,full_output = True)

##plotting
import matplotlib.pylab as p
f1 =  p.figure()
p.plot(pops[:,0], pops[:,1],  'r-')
p.grid()
p.yticks([2.5,5,7.5,10,12.5,15,17.5,20,22.5])
p.xticks([10,15,20,25,30,35,40])
p.legend(loc  = 'best')
p.xlabel('Resource density')
p.ylabel('Consumer density')
p.title('Consumer-Resource population dynamics')
p.show()

f1.savefig('../result/LV1_model.pdf')