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
def deriveef2(x,a):
	der = 0
	for i in range(len(x)):
		der = der + (-x[i]* math.exp(-a*x[i]))**2 #Derivee de g au carre
	return der
	

def lev_mar(l_init, a_init, x, y):
	l = l_init
	a = a_init
	k = 1
	grad = 1
	while (k <= 20) :#and abs(grad) > 0.00001):
		print("k = " + str(k))
		print ("lambda : " + str(l) + "\na : " + str(a))
		grad = gradient(x,y,a) #Gradient de f en x
		der2 = deriveef2(x,a) #derivee seconde de la fonction f
		#middle = True
		#while (middle == True):
		hLM = der2*(1+l)  #Matrice hessienne ponderee = derivee seconde ponderee dans ce cas
		d = - grad/hLM #Direction de descente
		f_act = f(x,y,a)
		f_next = f(x,y,a+d)
		if f_next < f_act :
			a = a+d
			l = l/10
			middle = False
		else :
			l = l*10
			middle = True
		k += 1
		print ("Gradient : " + str(grad))
		print("f_act : " + str(f_act) + "\nf_next : " + str(f_next))
		print("f_next < f_act : ", not middle)
		print ("direction : " + str(d) + "\n\n")
		
		
		
	
	

if __name__=="__main__":


	###Test fonction g###
	#g1 = g(1,1)
	#print("g = " + str(g1))
	
	
	###Creation du jeu de donnees bruite###
	
	a = 1.5
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
	
	der1 = deriveef2(data[0],a)
	print("derivee 2nde : " + str(der1))
	
	print("")
	print("")
	
	lev_mar(0.001, 1.5, data[0], data[1])

	#print(data)
	
	plt.plot(data[0], gs, 'r', label = 'Courbe theorique de g')
	plt.scatter(data[0],data[1], s=1, c='g', marker='o', label = 'Valeurs bruitees de g')
	plt.legend(loc = 'upper right')
	plt.xlabel('x')
	plt.ylabel('y')
	
	plt.show()
	
	
