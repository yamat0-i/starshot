import numpy as np
from scipy import integrate

import calc_gamma as g


# Sail mass
def calc_ms(rho, thickness, A):
    ms = rho * thickness * A
    return ms

# Sail parameter
rho = 5060 # MoS2 [kg/m^3]
thickness = 59e-9 # Sail thickness [m]
A = 10 # Sail area [m^2]
ms = calc_ms(rho, thickness, A)
print('ms: ', ms)

mp = 0.1e-3 # Payload mass [kg]
mt = ms + mp # Total mass [kg]
c = 3e8 # Light speed [m/s]

P = 10e9 # Laser power [W]
I = P / A # Laser intensity [W/m^2]



# R = 0.68 # Reflectance
fname = 'sweep_1.txt'
data = np.loadtxt(fname, delimiter=',', skiprows=3)

lam = data[439:671, 0]
R = data[439:671, 1]

# Set velocity
v_min = 0
v_f = 0.2 * c

v = np.linspace(v_min, v_f, len(lam))

def calc_momentum(mt, reflectance, gamma, v, c):
    gamma = g.calc_gamma(v, c)
    return (mt / reflectance) * (gamma * v / (1 - v/c)**2)

momentum = []

"""

energy, err = integrate.quad(momentum, v_min, v_f)

coef = c / (2 * I * A) # 1/force

D = coef * energy # Acceleration distance

print('D:', D)
print('error:', err)
"""