import random as r
import numpy as np
import matplotlib.pyplot as mp
import scipy.stats as sp
import math as m

def box_mul():
	""" Devuelve dos numero Normal Estandar independientes por metodo box muller """
	u0=r.uniform(0,1)
	u1=r.uniform(0,1)
	z0 = m.sqrt((-2) * m.log(u0)) * m.cos(2 * m.pi * u1)
	z1 = m.sqrt((-2) * m.log(u0)) * m.sin(2 * m.pi * u1)
	return (z0, z1)

a = 1000
l = []
norm = []
for i in range(0, a):
    z0, z1 = box_mul()
    l.append(z0)
    norm.append(np.random.normal(loc = 0))



ks = sp.kstest(l, 'norm')
print(ks[0], ks[1])
mp.hist(l, alpha=0.5, label='Real')
mp.hist(norm, alpha=0.5, label='Empirica')
mp.legend(loc='upper right')
mp.savefig("10-hist.png")
