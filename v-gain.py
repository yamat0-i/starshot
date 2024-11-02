# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 16:25:12 2022

@author: yuu42
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 14:29:00 2022

@author: marks
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 13:11:37 2018

@author: mark
"""

# Implement the classical cavity "QED" model of Novotny 
# from his paper "Strong coupling, energy splitting, and level crossings: A classical
# perspective", Am. J. Phys. 78 1199 (2010)
#
# In this case, we show the Purcell regime, where the electron oscillation decays at a rate close 
# to the cavity decay rate.

from scipy.integrate import ode
import matplotlib.pyplot as pl
import numpy as np

def a(z):
    # m = 6.28*10**(-19)
    # p = 1.0*10**(-3)
    # c = 3.0*10**8
    # q = 400*10**(-9)
    # r = 25*10**(-9)
    
    rho_Au = 1200 # Au density [kg / m^3]
    r = 5e-9 # Radius of gold nanoparticle [m]
    m = 4 / 3 * r**3 * rho_Au *np.pi # Mass of particle
    P0 = 1e-3 # Optical power [W]
    c = 2.99e8 # Speed of light [m / s]
    lam = 400e-9 # Wavelength [nm]
    
    om0 = 10* lam # Beam waist
    zR = np.pi * om0**2 / lam # Rayleigh length
    om = om0 * np.sqrt(1 + (z / zR)**2) # Beam waist at position z
    I0 = P0 / (np.pi * om0**2) # Intensity at beam waist
    #I = I0 * (om0 / om)**2 * np.exp(-2 * r**2 / (om**2)) # Intensity at particle radius
    P = I0 * np.pi * r**2 # Approximate power of beam within particle radius
    
    acc = 2 * P / (m * c)
    
    return acc

# Define the right hand side (RHS) of the differential equation 
# used to model the coupled oscillators.
def RHS(t, u, p):
    # u = [z,
    #      v]
    # z = u[0]
    # v = u[1]
    


    f = [u[1],
         a(u[0])]
    
    return f

# Parameters


# Set up integrator for complex values
r = ode(RHS, jac=None).set_integrator('vode', method='bdf')

# Initial conditions
u0 = [0.0, 0.0]
r.set_initial_value(u0, t=0.0).set_f_params(0)

print("Here")
# Set up variables to hold the output
u = []
t = []

# Define intergration parameters
T = 3000 # Total time in arb. units
dt = T / 1000 # Time step at which to sample the dynamics

# Perform the integration to numerically solve the D.E.s
while r.successful() and r.t <= T:
    r.integrate(r.t + dt)
    u.append(r.y)
    t.append(r.t)

# Display results
u = np.array(u)
pl.figure(1)
pl.clf()
pl.plot(t,np.real(u[:,0]) * 1e3,'r-', label = "z")
#pl.plot(t,np.real(u[:,1]),'b-', label = "v")
pl.xticks(fontsize=16)
pl.yticks(fontsize=16)
pl.xlabel("t (s)",fontsize=18)
pl.ylabel("z (mm)",fontsize=18)
#pl.title("gamma = %1.2f, kappa = %1.2f, g = %1.2f"%(gamma,kappa,g),fontsize=18)
pl.tight_layout()
pl.legend()

pl.figure(2)
pl.clf()
#pl.plot(t,np.real(u[:,0]),'r-', label = "z")
pl.plot(t,np.real(u[:,1]),'b-', label = "v")
pl.xticks(fontsize=16)
pl.yticks(fontsize=16)
pl.xlabel("t (s)",fontsize=18)
pl.ylabel("v (m/s)",fontsize=18)
#pl.title("gamma = %1.2f, kappa = %1.2f, g = %1.2f"%(gamma,kappa,g),fontsize=18)
pl.tight_layout()
pl.legend()

pl.figure(3)
pl.clf()
z = np.linspace(0,10e-6,100)
pl.plot(z * 1e6,a(z),'r')
pl.xlabel("Distance from beam waist (um)")
pl.ylabel("Acceleration (m / s^2)")
pl.show()
