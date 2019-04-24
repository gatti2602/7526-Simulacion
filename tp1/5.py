"""
Ejercicio 5 
"""
import numpy as np
import matplotlib.pyplot as mp
import random
import collections

class GCL():
	def __init__(self, seed = 0):
		self.current = seed

	def random(self):
		self.current = round(((1013904223 * self.current) + 1664525) % (2**32))
		return self.current / (2**32)

	def next(self):
		number = self.random()
		return number


def empiric(a):
	if a<=0.4:
		return 1
	elif a<= 0.7:
		return 2
	elif a <= 0.82:
		return 3
	elif a <= 0.92:
		return 4
	else:
		return 5

seed = 93152 * 0.15 + 93570 * 0.25 + 99722 * 0.6
generator = GCL(seed)
total_samples = 100000
numbers = []
for i in range(0, total_samples):
	numbers.append(empiric(generator.next()))

cant = collections.Counter(numbers)
print(cant)  

mp.hist(numbers,5)
mp.savefig("5-hist.png")