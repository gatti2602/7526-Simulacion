"""
Ejercicio 2 
"""
import numpy as np
import matplotlib.pyplot as mp
import random

class GCL():
	def __init__(self, seed = 0):
		self.current = seed

	def random(self):
		self.current = round(((1013904223 * self.current) + 1664525) % (2**32))
		return self.current / (2**32)

	def next(self):
		number = self.random()
		return number

def inverse(a):
	lamb = 20
	result = (-1/lamb) * np.log(1-a)
	return result

seed = 93152 * 0.15 + 93570 * 0.25 + 99722 * 0.6
generator = GCL(seed)

total_samples = 100000
numbers = []
for i in range(0, total_samples):
	numbers.append(inverse(generator.next()))

l = np.array(numbers)
print("Media obtenida: ", round(l.mean(), 4))
print("Varianza obtenida: ", round(l.var(), 4))

mp.hist(numbers,100)
mp.savefig("2-hist.png")