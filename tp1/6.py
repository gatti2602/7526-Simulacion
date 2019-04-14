#!/usr/bin/env python
""" 
	Ejercicio 6 TP1
	Gatti Nicolas
"""


import random as r
import numpy as np
import matplotlib.pyplot as mp
import math as m

def box_mul():
	""" 
	Devuelve dos numero Normal Estandar independientes por metodo box muller 
	"""
	u0=r.uniform(0,1)
	u1=r.uniform(0,1)
	z0 = m.sqrt((-2) * m.log(u0)) * m.cos(2 * m.pi * u1)
	z1 = m.sqrt((-2) * m.log(u0)) * m.sin(2 * m.pi * u1)
	return (z0, z1)

def main():
	a = 10000
	l = np.random.rand(a, 2) #array de muestras uniforme entre 0 y 1
	l = (l * 2) - 1 		# Uniforme entre -1 y 1

	#convierto las dos uniformes en radio y angulo
	l[:,0] = (l[:,0] + 1) / 2 #Entre 0 y 1
	l[:,1] = (l[:,1] + 1) * m.pi #Entre 0 y 2pi

	fig = mp.figure()
	ax = fig.add_subplot(111, projection='polar')
	ax.scatter(l[:,1],l[:,0])
	mp.title("Scatter Plot en coordenadas polares")
	mp.savefig("6-scatter.png")
main()