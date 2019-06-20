
import numpy as np
import simpy as sp
import pandas as pd
import matplotlib.pyplot as mp
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

#print(array)

#Punto b			
values = [i for i in range(N)]
#Inicio vacio
actual_clients = 0
clients = [[0,0]]
for i in range(1,100):
	actual_clients = np.random.choice(values, p=array[actual_clients])
	clients.append([i, actual_clients])

clients = pd.DataFrame(clients)
clients.columns = ['step','clients']
mp.figure()
plot = clients.plot(x='step',y='clients')
plot.set_title('Clientes por step')
mp.savefig("2-b.png")	

#Punto C
actual_clients = 0
clients = [[0,0]]
for i in range(1,100000):
	actual_clients = np.random.choice(values, p=array[actual_clients])
	clients.append([i, actual_clients])

clients = pd.DataFrame(clients)
clients.columns = ['step','clients']
mp.figure()
mp.hist(clients['clients'], bins=51)
mp.title('Histograma de estados')
mp.xlabel('Estados')
mp.savefig("2-c.png")	

#Punto D y E
newarray = matrixMul(array, 1000)
sum = 0
for i in range(40, 50):
    sum += newarray[i][0]

print(array)
print(newarray)
print(sum)

