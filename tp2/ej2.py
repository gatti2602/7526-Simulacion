
import numpy as np
import simpy as sp
import math

def aumenta(i, j):
    global N
    global p
    permutations = math.factorial(N) / math.factorial(N - (j-i))
    combinations = permutations / math.factorial(j-i)
    return (combinations) * (p**(j-i)) * ((1-p)**(N-(j-i)))

def disminuye(i, j):
    global N
    sumatoria = 0
    for z in range(i,N):
        sumatoria += aumenta(i, z)
    return (1 - sumatoria) / (i - 1)

N = 3
p = 0.7
array = np.ones((N,N))

for i in range(N):
    for j in range(N):
        if (j >= i):
            array[i][j] = aumenta(i+1, j+1)
        else:
            array[i][j] = disminuye(i+1, j+1)

print(array)
