import matplotlib.pyplot as mp

def punto(l):
    return ((-1*l)+9.4)/1.1

def qte(l):
	return l-0.4

initial = 8
precios = [] 
precios.append(initial)
qt = []
qt.append(qte(initial))

for i in range(1,100):
	initial = punto(initial)
	precios.append(initial)
	qt.append(qte(initial))

print precios
mp.plot(precios)
#mp.show()
mp.savefig("3-precio.png")


#mp.plot(qt, precios)
#mp.savefig("3-fases.png")