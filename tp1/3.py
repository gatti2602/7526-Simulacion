#!/usr/bin/env python
""" 
	Ejercicio 3 TP1
	Gatti Nicolas
"""


import random as r
import numpy as np
import matplotlib.pyplot as mp
import math as m

def box_mul():
	""" Devuelve dos numero Normal Estandar independientes por metodo box muller """
	u0=r.uniform(0,1)
	u1=r.uniform(0,1)
	z0 = m.sqrt((-2) * m.log(u0)) * m.cos(2 * m.pi * u1)
	z1 = m.sqrt((-2) * m.log(u0)) * m.sin(2 * m.pi * u1)
	return (z0, z1)

def main():
	a = 100000
	l = []
	for i in range(0, a):
		z0, z1 = box_mul()
		l.append(z0)

	mp.hist(l,100, density = True)
	mp.title("Dist. Normal por Box-Muller")	
	mp.savefig("3-hist.png")

	l = np.array(l)
	print("Media obtenida: ", round(l.mean(), 4))
	print("Varianza obtenida: ", round(l.var(), 4))

main()