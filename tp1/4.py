"""
Ejercicio 4
"""
import numpy as np
import matplotlib.pyplot as mp
import scipy.stats as st
import random
import math

def p(x):
    return st.norm.pdf(x, loc = 40, scale = 6)

def q(x):
    return st.norm.pdf(x, loc = 35, scale = 8)


x = np.arange(-50, 101)
c = max(p(x) / q(x))

total_samples = 100000
numbers = []
plot2 = []
for i in range(0, total_samples):
    z = np.random.normal(35, 8)
    u = np.random.uniform(0, c*q(z))
    if u <= p(z):
	   numbers.append(z)


l = np.array(numbers)
print("Media obtenida: ", round(l.mean(), 4))
print("Varianza obtenida: ", round(l.var(), 4))



mp.hist(numbers, 50, normed = True)
mp.plot(x, p(x))

mp.savefig("4-hist.png")
