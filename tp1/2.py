"""
Ejercicio 2 
"""
import numpy as np
import matplotlib.pyplot as mp
import random

def inverse(a):
	lamb = 20
	result = (-1/lamb) * np.log(1-a)
	return result

total_samples = 100000
numbers = []
for i in range(0, total_samples):
	numbers.append(inverse(random.uniform(0,1)))

l = np.array(numbers)
print("Media obtenida: ", round(l.mean(), 4))
print("Varianza obtenida: ", round(l.var(), 4))

mp.hist(numbers,100)
mp.savefig("2-hist.png")