import calc_gamma as g

c = 3e8

def doppler_shift(nu, v, c):
    nu_shift =  nu / (g.calc_gamma(v, c) * (1 - v/c))
    return nu_shift

def lam2nu(lam):
    nu = c / lam
    return nu

def nu2lam(nu):
    lam = c / nu
    return lam

