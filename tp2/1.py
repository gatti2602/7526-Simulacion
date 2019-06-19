"""
Ejercicio 1
"""
import numpy as np
import matplotlib.pyplot as mp
import random
import math

def Simular_Mem_Access(type):
	if type == 1:
		#Sin cache
		return '-', np.random.exponential(scale=2000)
	else:
		time = np.random.exponential(scale=500)
		if np.random.uniform() < .6:
			#Cache Hit
			return 'Hit', time
		else: 
			return 'Miss', time + np.random.exponential(scale=1500)

def Simular_Instruccion(type):
	"""
	Devuelve el tiempo que lleva ejecutar la instruccion
	"""
	i_types = ['simple','complex']
	while True:
		i_type = np.random.choice(i_types, p=[0.6,0.4])
		mem = 'no'
		cache = '-'
		mean = 60 if i_type == 'simple' else 10
		#time en microsegundos
		time = np.random.exponential(scale = 1/mean)
		if np.random.uniform() <= .65:
			#Tiene Datos en memoria
			mem = 'yes'
			cache, t = Simular_Mem_Access(type)
			time = time + t
		print (type, i_type, mem, cache, time)
		yield (i_type, mem, cache, time)


sim1 = Simular_Instruccion(1)
sim2 = Simular_Instruccion(2)
n = 100000
res1 = np.zeros(n)
res2 = np.zeros(n)
print('alternative i_type mem cache time')
for i in range(n):
	_, _, _, res1[i] = next(sim1)
	_, _, _, res2[i] = next(sim2)

#print(round(res1.mean(), 5))
#print(round(res2.mean(), 5))
 
	


	