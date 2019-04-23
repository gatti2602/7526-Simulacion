"""
Ejercicio 7
"""
import numpy as np
import matplotlib.pyplot as mp
import random
import math
from mpl_toolkits import mplot3d

class GCL():

    def __init__(self, current = 0):
        self.current = current

    def random(self, seed):
        self.current = round(((1013904223 * seed) + 1664525) % (2 ^ 32))
        return self.current / (2^32)

    def next(self):
        number = self.random(self.current)
        return number

seed = 97198
generator = GCL(seed)
total_samples = 1000
xNumbers = []
yNumbers = []
for i in range(0, total_samples):
    xNumbers.append(generator.next())
    yNumbers.append(generator.next())
    mp.scatter(xNumbers, yNumbers)

mp.savefig("7_spectral_2D.png")

fig = mp.figure()
ax = mp.axes(projection = '3d')
xNumbers2 = []
yNumbers2 = []
zNumbers = []
for i in range(0, total_samples):
    xNumbers2.append(generator.next())
    yNumbers2.append(generator.next())
    zNumbers.append(generator.next())
    ax.scatter3D(xNumbers2, yNumbers2, zNumbers)

fig.savefig("7_spectral_3D.png")
