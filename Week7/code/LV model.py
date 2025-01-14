import scipy  as sc
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

## plotting
import matplotlib.pylab as p
f1 = p.figure() #open an empty figure object
p.plot(t, pops[:,0], 'g-', label='Resource density') # Plot 
p.plot(t, pops[:,1]  , 'b-', label='Consumer density')
p.grid()
p.legend(loc='best')
p.xlabel('Time')
p.ylabel('Population density')
p.title('Consumer-Resource population dynamics')
p.show()# To display the figure

f1.savefig('../result/LV_model.pdf') #Save figure as a pdf
