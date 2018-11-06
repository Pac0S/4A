#Imports from the matplotlib library
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
#--------------------------------------
import math
import numpy as np
import random

	
def f(x):
	val = x**4 - x**3 - 20*x**2 + x + 1
	return val
	
def farray(x):
	array = np.zeros(len(x))
	for i in range(len(x)):
		array[i] = f(x[i])
	return array
	
def run(k1, k2, t, x0):
	xarr = []
	x = x0
	#xarr.append(x0)
	for step in t:
		T = 1./step
		D = k1*math.exp(-1/(1000*T)) * np.random.randn()
		newx = x+D
		if(f(newx) < f(x)):
			x = newx			
		else:
			proba = k2*math.exp(-1/(1000*T))
			roll = random.random()
			if roll<=proba:
				x = newx
		xarr.append(x)
	print('x final : ' + str(xarr[len(xarr)-1]))
	print('f(x) = ' + str(f(xarr[len(xarr)-1])))
	return xarr
			
if __name__=='__main__':



	#print(f(3))

	x1 = np.arange(-5,6,0.1)
	fx1 = farray(x1)
	
	time = np.arange(1,2000,1)
	result1 = run(0.15,5,time,-0.2)
	
	plt.plot(x1, fx1, label = 'Courbe theorique de f')
	plt.plot(result1, farray(result1),'r', label = 'Courbe de recherche du minimum')
	plt.xlabel('x value')
	plt.ylabel('f(x) value')
	plt.legend(loc='upper left')
	
	plt.show()
	
	'''
	plt.plot(time, farray(result1), 'm')
	plt.xlabel('time t')
	plt.ylabel('f(x_t)')

	plt.show()
	
	plt.plot(time, result1, 'g')
	plt.xlabel('time t')
	plt.ylabel('x_t')

	plt.show()
	'''
	
