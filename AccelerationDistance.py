import numpy as np
from scipy import integrate


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

R = 0.68 # Reflectance

v = 0.1 * c
gamma = 1 / np.sqrt(1 - v**2 / c**2)

def momentum(x):
    return (mt / R) * (gamma * v / (1 - v/c)**2)

v_min = 0
v_f = 0.2 * c

energy, err = integrate.quad(momentum, v_min, v_f)

coef = c / (2 * I * A) # 1/force

D = coef * energy # Acceleration distance

print('D:', D)
print('error:', err)
