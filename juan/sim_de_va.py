import random
import numpy as np
import matplotlib.pyplot as mp

def inv_exp(a, l):
    b = (-1/l) * np.log(1-a)
    return b
    
def inv_11(a):
    b = 1/((-4/5) * a + 1)
    return b

a = [] 
for i in range(1,int(1e7)): 
    a.append(inv_11(random.uniform(0,1)))

mp.hist(a,1000)
mp.show()