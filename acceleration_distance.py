import numpy as np
from scipy import integrate

import lorentz as l
import doppler as d


c = 3e8 # Light speed [m/s]

# Sail mass
def calc_ms(rho, thickness, A):
    ms = rho * thickness * A
    return ms

# Sail parameter
rho = 5060 # MoS2 [kg/m^3]
thickness = 59e-9 # Sail thickness [m]
A = 10 # Sail area [m^2]
ms = calc_ms(rho, thickness, A)

mp = 0.1e-3 # Payload mass [kg]
mt = ms + mp # Total mass [kg]

P = 10e9 # Laser power [W]
I = P / A # Laser intensity [W/m^2]

# Load data
fname = 'sweepver3_7.txt'
data = np.loadtxt(fname, delimiter=',', skiprows=3)

lam_data = data[:, 0]
R_data = -data[:, 1]

lam_0 = 1e-6
lam_f = 1.22 * lam_0

i_0 = np.abs(lam_data-lam_0).argmin() # Index of lam_0
i_f = np.abs(lam_data-lam_f).argmin() # Index of lam_f

lam = lam_data[i_f:i_0]
R = R_data[i_f:i_0]

def calc_r_shift(v):
    lam_shift = d.doppler_shift(lam=lam_0, v=v, c=c)
    i_shift = np.abs(lam-lam_shift).argmin()
    R_shift = R[i_shift]
    return R_shift

# Set velocity
v_0 = 0
v_f = 0.2 * c
dv = (v_f - v_0) / len(lam)

def calc_momentum(mt, reflectance, v, c):
    gamma = l.loretzfactor(v, c)
    return (mt / reflectance) * (gamma * v / (1 - v/c)**2)

# integrate
s = 0
for i in range(1, len(lam)):
    v1 = v_0 + dv * i
    reflectance = calc_r_shift(v1)
    f1 = calc_momentum(mt=mt, reflectance=reflectance, v=v1, c=c)
    s += dv * f1

coef = c / (2 * I * A) # 1/force
D = coef * s # Acceleration distance

print('D[m]: {:e}'.format(D))
