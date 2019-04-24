#!/usr/bin/env python
""" 
	Ejercicio 9 TP1
	Gatti Nicolas
"""


import random as r
import numpy as np
import matplotlib.pyplot as mp
import scipy.stats
import math as m

class GCL():

	def __init__(self, current = 0):
		self.current = current

	def random(self, seed):
		self.current = round(((1013904223 * seed) + 1664525) % (2 ^ 32))
		return self.current / (2^32)

	def next(self):
		number = self.random(self.current)
		return number

def gap_test(samples, a, b, t):
	n = len(samples)/10 
	j, s, count = -1, 0, t*[0]

	while s != n and j != len(samples):
		j, r = j+1, 0
		while j != len(samples) and not (a < samples[j] < b ):
			j, r = j+1, min(r+1, t)
		#print(j, r)
		count[r] += 1
		s += 1
		if j == len(samples): 
			raise "Fin de Lista: Encontrados %d de %d" % (s, n)

	expected = t*[0]
	p = b - a
	expected[t-1] = ((1-p)**t) * n

	for i in range(0, t-1):
		expected[i] = (p*(1-p)**i) * n
	#print("Sample", samples)
	print ("------------------")
	print("Samples %d" % len(samples))
	print("Count:", count)
	print("Expected:", [round(e,2) for e in expected])
	s, p = scipy.stats.chisquare(count, expected)

	return s, p	

def main():
	for i in range(3, 8):
		for t in range(5, 20):
			seed = 93570
			generator = GCL(seed)
			total_samples = 10**i
			numbers = []
			for i in range(0, total_samples):
				numbers.append(generator.next())
			s, p = gap_test(numbers, 0.2, 0.5, t)
			print("p-value: %d" % p)
			print("t was %d" % t)
		
main()		
		
		