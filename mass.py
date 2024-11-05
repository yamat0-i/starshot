import numpy as np

def slab(rho, thickness, A):
    ms = rho * thickness * A
    return ms

def phc_holl(rho, thickness, A, radius, ratio):
    # unit cell size
    x_unit = ratio * 2 * radius
    y_unit = np.sqrt(3) * x_unit
    A_unit = x_unit * y_unit - (np.pi * radius**2) * 2

    num = A / (x_unit * y_unit)
    ms = rho * A_unit * num * thickness
    return ms

if __name__ == '__main__':
    rho = 5060 # MoS2 [kg/m^3]
    thickness = 59e-9 # Sail thickness [m]
    A = 10 # Sail area [m^2]
    hole_radius = 490e-9 
    print(phc_holl(rho, thickness, A, hole_radius))

