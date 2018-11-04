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
		T = 1/step
		D = k1*math.exp(-1/(1000*T)) * np.random.randn()
		newx = x+D
		if(f(newx) < f(x)):
			x = newx			
		#else:
			#proba = k2*math.exp(-1/(1000*T))
			#roll = random.random()
			#if roll<=proba:
			#x = newx
		xarr.append(x)
	return xarr
			
if __name__=='__main__':

	print(f(3))

	x1 = np.arange(0,5,0.5)
	fx1 = farray(x1)
	plt.plot(x1, fx1)
	plt.show()
	
	time = np.arange(1,10000,1)
	result1 = run(10,0.5,time,-2)
	plt.plot(time, farray(result1))
	plt.show()
	
	
