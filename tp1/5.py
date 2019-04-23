"""
Ejercicio 5 
"""
import numpy as np
import matplotlib.pyplot as mp
import random

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

total_samples = 100000
numbers = []
for i in range(0, total_samples):
	numbers.append(empiric(random.uniform(0,1)))

mp.hist(numbers,5)
mp.savefig("5-hist.png")