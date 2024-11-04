import numpy as np

import calc_gamma as g

c = 3e8

def doppler_shift(lam, v, c):
    nu = lam2nu(lam)
    gamma = g.calc_gamma(v, c)
    nu_shift =  nu / (np.sqrt(gamma) * (1 + v/c))
    lam_shift = nu2lam(nu_shift)
    return lam_shift

def lam2nu(lam):
    nu = c / lam
    return nu

def nu2lam(nu):
    lam = c / nu
    return lam

if __name__ == '__main__':
    v = np.linspace(0, 0.2*c, 50)
    lam = 1e-6
    lam_shift = doppler_shift(lam=lam, v=v, c=c)
    print(lam_shift)
