import numpy as np
from values import Values
from xysums import xValues, xyValues

def order(n): #el orden es el order del polinomio de Taylor a evaluar
    w = np.zeros((n + 1, n + 1))
    i = 0
    while i < len(w):
        j = 0
        while j < len(w[0]):
            print([i, j])
            j = j + 1
        i = i + 1

order(1)