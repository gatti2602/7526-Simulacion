
import numpy as np
import simpy as sp
import math

def matrixMul(a, n):
    if(n == 1):
        return a
    else:
        tempArr = a;
        for i in range(1, n-1):
            tempArr = np.matmul(a, tempArr)
        return tempArr

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
		print(i,N,z)
		sumatoria += aumenta(i, z)

	return (1 - sumatoria) / (i)

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

newarray = matrixMul(array, 1000)
sum = 0
for i in range(40, 50):
    sum += newarray[i][0]

print(array)
print(newarray)
print(sum)
