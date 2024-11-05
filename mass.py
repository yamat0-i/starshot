import numpy as np

def slab(rho, thickness, A):
    ms = rho * thickness * A
    return ms

def phc_holl(rho, thickness, A, diameter, ratio):
    # unit cell size
    x = ratio * diameter
    y = np.sqrt(3) * x
    A_unit = x * y - (np.pi * (diameter/2)**2) * 2

    ms = rho * A_unit * (A/(x*y)) * thickness
    return ms

if __name__ == '__main__':
    rho = 5060 # MoS2 [kg/m^3]
    thickness = 59e-9 # Sail thickness [m]
    A = 10 # Sail area [m^2]
    holl_diameter = 490e-9 
    print(phc_holl(rho, thickness, A, holl_diameter))

