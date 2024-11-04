def calc_gamma(v, c):
    return 1 / (1 - (v**2 / c**2))

# Test
if __name__ == '__main__':
    c = 3e8
    v = 0.1*c
    print(calc_gamma(v, c))
