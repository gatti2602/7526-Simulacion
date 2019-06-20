
import numpy as np
import simpy as sp
import math



def aumenta(i, j):
	global N
	M = N-1
	global p
	permutations = math.factorial(M) / math.factorial(M - (j-i))
	combinations = permutations / math.factorial(j-i)
	return (combinations) * (p**(j-i)) * ((1-p)**(M-(j-i)))

def disminuye(i, j):
	global N
	sumatoria = 0
	for z in range(i,N):
		sumatoria += aumenta(i, z)

	return (1 - sumatoria) / (i)

N = 51
p = 0.7
array = np.zeros((N,N))

for i in range(N):
	for j in range(N):
		if (j >= i):
			array[i][j] = aumenta(i, j)
		else:
			array[i][j] = disminuye(i, j)
			#array[i][j] = array[i][j]

print(array)
#Punto b			
clientes=[]
values = [i for i in range(N)]

#Inicio vacio
pi = np.zeros(N)
pi[0] = 1

for i in range(10):
	pi = array.dot(pi)
	print(pi)
	value = np.random.choice(values, p=pi)
	clientes.append([i, value])
	


