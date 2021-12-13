import numpy as np
from values import Values
from syssolver import Solver
import matplotlib.pyplot as plt

def Graph(n):
    t = np.arange(Values()[0][0], Values()[0][-1], 0.2)
    p = 0
    i = 0
    while i <= n: p = p + Solver(n)[i]*(t**i); i = i + 1
    plt.plot(Values()[0], Values()[1], 'bo', label="Data")
    plt.plot(t, p, 'k', label="{}th degree polynomial".format(n))
    plt.legend()
    plt.savefig('{}th degree'.format(n))
    

'''
Test area
Graph(199)
'''

Graph(70)

