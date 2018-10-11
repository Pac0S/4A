#Imports from the matplotlib library
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
#--------------------------------------
import math
import numpy as np





def g(x,a):
	g = math.exp(-a*x)
	return g

## f est la somme des erreurs au carre ##
def f(x,y,a):
	f = 0
	for i in range(len(x)):
		f = f + (y[i] - g(x[i], a))**2
	f = f/2
	return f

# Gradient de f en fonction de a #
def gradient(x,y,a):
	grad = 0
	for i in range(len(x)):
		grad = grad + (y[i] - g(x[i], a))* (-x[i] * math.exp(-a*x[i]))
	grad = -grad
	return grad
	
#Derivee 2nde de f par rapport a une variable a
def derivee2(x,a):
	der = 0
	for i in range(len(x)):
		der = der + (x[i]**2 * math.exp(-a*x[i]))
		#der = der + (-x[i]* math.exp(-a1*x[i]))*(-x[i]* math.exp(-a2*x[i]))
	return der
	
	
	

if __name__=="__main__":


	###Test fonction g###
	#g1 = g(1,1)
	#print("g = " + str(g1))
	
	
	###Creation du jeu de donnees bruite###
	
	data = np.zeros((2,int(3/0.001)+1))
	#print(data.shape)
	

	##Creation des donnees
	a = 2.
	b = 0.01
	
	data = np.zeros((2,301))
	data[0] = np.arange(0,3.01,0.01)
	gs = np.zeros((301)) #Liste des valeurs theoriques
	for i in range(len(data[0])):
		data[1][i] = g(data[0][i],a) + b * np.random.randn()
		gs[i] = g(data[0][i],a)
	
	f1 = f(data[0],data[1],a)
	print("f = " + str(f1))
	
	grad1 = gradient(data[0],data[1],a)
	print("gradient : " + str(grad1))
	
	der1 = derivee2(data[0],a)
	print("derivee 2nde : " + str(der1))

	#print(data)
	
	plt.plot(data[0], gs, 'r', label = 'Courbe theorique de g')
	plt.scatter(data[0],data[1], s=1, c='g', marker='o', label = 'Valeurs bruitees de g')
	plt.legend(loc = 'upper right')
	plt.xlabel('x')
	plt.ylabel('y')
	
	#plt.show()
	
	
