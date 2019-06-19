"""
Ejercicio 4
"""
import numpy as np
import simpy

class Instruction(object): 
	
	_i_types = ['simple','complex']
	
	def __init__(self, env, type):
		self.env = env
		self.type = type
		self.mem = 'yes' if np.random.uniform() <= .65 else 'no'
		self.cache = '-'
		self.i_type = np.random.choice(self._i_types, p=[0.6,0.4])
		if self.type == 2:
			self.cache = 'hit' if np.random.uniform() < .6 else 'miss'
 
	def _Simular_Mem_Access(self):
		if self.type == 1:
			#Sin cache
			return np.random.exponential(scale=1./2000)
		else:
			time = np.random.exponential(scale=1./500)
			if self.cache == 'miss':
				time = time + np.random.exponential(scale=1./1500)
			return time

	def run(self, core):
		"""
		Devuelve el tiempo que lleva ejecutar la instruccion
		"""
		mean = 60. if self.i_type == 'simple' else 10.
		
		#time en microsegundos
		time = np.random.exponential(scale = 1./mean)
		if self.mem == 'yes':
			time = time + self._Simular_Mem_Access()
		
		with core.request() as req:
			yield req
			yield self.env.timeout(time)
		print (self.type, self.i_type, self.mem, self.cache, time)
		
def SimularInstrucciones(env, amount, type):
    core = simpy.Resource(env, capacity = 1)
    for i in range(amount):
        instr = Instruction(env,type)
		#instr = Instruction(env,2) #Cambiar para sim con cache
        env.process(instr.run(core))
        t = np.random.exponential(scale = 1./250)
        yield env.timeout(t)

amount = 100000
env = simpy.Environment()
env.process(SimularInstrucciones(env, amount, 1))
env.run()

env = simpy.Environment()
env.process(SimularInstrucciones(env, amount, 2))
env.run()	