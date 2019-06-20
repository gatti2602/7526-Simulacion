
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
<<<<<<< HEAD
    global N
    sumatoria = 0
    for z in range(i,N):
        sumatoria += aumenta(i, z)
    return (1 - sumatoria) / (i - 1)
=======
	global N
	sumatoria = 0
	for z in range(i,N):
		print(i,N,z)
		sumatoria += aumenta(i, z)

	return (1 - sumatoria) / (i)
>>>>>>> 12aa480dac386f965e83e3d4f32288abe3d733b4

N = 50
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
