"""
Ejercicio 1
"""
import numpy as np
import matplotlib.pyplot as mp
import random
import math


class GCL():

    def __init__(self, current = 0):
        self.current = current

    def random(self, seed):
        self.current = round(((1013904223 * seed) + 1664525) % (2 ^ 32))
        return self.current / (2^32)

    def next(self):
        number = self.random(self.current)
        return number

seed = 971981
generator = GCL(seed)
total_samples = 100000
numbers = []
for i in range(0, total_samples):
	numbers.append(generator.next())
    #print(generator.next())

mp.hist(numbers,100)
mp.savefig("1-hist.png")
