import numpy as np


def load_data(fname):
    data = np.loadtxt(fname)
    R_data = data[:, 1]
