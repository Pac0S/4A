#Imports from the matplotlib library
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
#--------------------------------------
import math
import numpy as np




	#########################
	#	Calcul de g(x,a)	#
	#########################

def g(x,a):
	g = math.exp(-a*x)
	return g
	
	
	
	#########################################
	#		Calcul de la derivee de g par a	#
	#########################################

def derg(x,a):
	dgda = -x*math.exp(-a*x)
	return dgda
	
		

	#########################################
	#	f est la somme des ecarts au carre	#
	#########################################

def f(x,y,a):
	f = 0
	for i in range(len(x)):
		f = f + (y[i] - g(x[i], a))**2
	f = f*0.5
	return f
	



	#####################################
	#	Gradient de f en fonction de a	#
	#####################################

def gradient(x,y,a):
	grad = 0
	for i in range(len(x)):
		grad = grad + (y[i] - g(x[i], a)) * (-x[i] * math.exp(-a*x[i]))
	grad = -grad
	return grad
	

	#########################################################
	#		Derivee 2nde de f par rapport a une variable a	#
	#########################################################

def derf2(x,a):
	der = 0
	for i in range(len(x)):
		der = der + (derg(x[i],a)**2) #Derivee de g au carre (en fo de a)
	return der
	
	
	#########################################
	#		Methode de Levenberg-Marquardt	#
	#########################################	

def lev_mar(l_init, a_init, x, y, n, grad_lim):
	l = l_init
	a = a_init
	k = 1
	grad = 1
	lambda_list = []
	a_list = []
	f_list =[]
	grad_list = []
	k_list = []
	
	while (k <= n):# and abs(grad) > grad_lim):
		
		#Ajout de k a une liste
		print("k = " + str(k))
		k_list.append(k)
		
		#Ajout de lambda a une liste
		print ("lambda : " + str(l))
		lambda_list.append(l)
		
		#Ajout dea a une liste
		print( "a : " + str(a))
		a_list.append(a)
		
		#ajout du gradient a une liste
		grad = gradient(x,y,a) #Gradient de f en x
		print ("Gradient : " + str(grad))
		grad_list.append(abs(grad))
		
		der2 = derf2(x,a) #derivee seconde de la fonction f
		hLM = der2*(1+l)  #Matrice hessienne ponderee = derivee seconde ponderee dans ce cas
		d = - grad/hLM #Direction de descente
		
		#calcul et ajout de f a une liste
		f_act = f(x,y,a)
		f_next = f(x,y,a+d)
		f_list.append(f_act)
		print("f_act : " + str(f_act) + "\nf_next : " + str(f_next))
			
			
		#Verification de la condition
		if f_next < f_act :
			a = a+d
			l = l/10
			#middle = False
		else :
			l = l*10
			#middle = True
			
		
		k += 1
		
		
		#print("f_next < f_act : ", not middle)
		
		print("\n\n")
		
	param = [k_list, a_list, lambda_list, grad_list, f_list]
	return param
	
	

if __name__=="__main__":


	#################################################
	#		Test fonction g et derivee seconde		#
	#################################################
	
	###x = 1, a = 1###
	
	g1 = g(1,1)
	dg1 = derg(1,1)
	print("a=1, x=1, g = " + str(g1))
	print("a=1, x=1, dg/da = " + str(dg1))
	
	#########################
	#		Parametres		#
	#########################
	
	a = 2
	b = 0.1
	n=20
	
	
	#####################################################
	#		Creation du jeu de donnes non bruitees		#
	#####################################################
	
	init = (2,301)
	nonoised = np.zeros(init)
	
	xi=0
	for i in range(len(nonoised[0])):
		nonoised[0][i] = xi
		xi+=0.01
	
	i=0
	for xi in nonoised[0]:
		nonoised[1][i] = g(xi,a)
		i+=1
	#print(nonoised)
	
	
	#################################################
	#		Creation du jeu de donnes bruitees		#
	#################################################

	
	noised = np.zeros(init)
	
	xi=0
	for i in range(len(noised[0])):
		noised[0][i] = xi
		xi+=0.01
	
	i=0
	for xi in noised[0]:
		noised[1][i] = g(xi,a)+ b * np.random.randn()
		i+=1
	#print(noised)
	
	#############################################
	#		Test de f sur les donnees bruitees	#
	#############################################
	
	f1 = f(noised[0], noised[1], a)
	print("f donnees bruitees : " + str(f1))
	#f = 0 sur les donnees non bruitees (somme des ecarts au carre = 0)
	
	
	#####################################################
	#		Test de gradient sur les donnees bruitees	#
	#####################################################
	
	grad1 = gradient(noised[0], noised[1], a)
	print("gradient donnees bruitees : " + str(grad1))
	#grad = 0 sur les donnees non bruitees
	
	
	#####################################################
	#		Test de derivee seconde pour la fonction g	#
	#####################################################
	
	df2 = derf2(noised[0], a)
	print("derivee seconde de f par rapport a a : " + str(df2))
	
	print("")
	print("")
	
	#####################################################
	#		Test de la methode de Levenberg-Marquardt	#
	#####################################################	
	
	
	lm1 = lev_mar(0.001, 1.5, noised[0], noised[1], n, 0.0001)
	#	  lev_mar(lambda, a , 		x  ,		y , n ,  grad_lim      )
	
	k_list = lm1[0]
	a_list = lm1[1]
	lambda_list = lm1[2]
	grad_list = lm1[3]
	f_list = lm1[4]
	
	a_opt = a_list[n-1]
	
	
	plt.plot(k_list, a_list, 'r')
	plt.xlabel('k')
	plt.ylabel('a')
	plt.title('Evolution du parametre a')
	plt.show()
	
	plt.plot(k_list, lambda_list, 'g')
	plt.xlabel('k')
	plt.ylabel('lambda')
	plt.title('Evolution du parametre lambda')
	plt.show()
	
	plt.plot(k_list, grad_list, 'b')
	plt.xlabel('k')
	plt.ylabel('Norme du gradient')
	plt.title('Evolution de la norme du gradient')
	plt.show()
	
	plt.plot(k_list, f_list, 'm')
	plt.xlabel('k')
	plt.ylabel('f(a)')
	plt.title('Evolution du parametre f(a)')
	plt.show()
	
	
	#Jeu de donnees pour le a optimal
	g_aopt = []
	i=0
	for xi in nonoised[0]:
		g_aopt.append(g(xi,a_opt))
		i+=1
	#print(noised)
	
	#plt.plot(nonoised[0], nonoised[1], 'r', label = 'Courbe theorique de g avec a=2')
	plt.plot(nonoised[0], g_aopt, 'r', label = 'Courbe optimisee de g')
	plt.scatter(noised[0],noised[1], s=1, c='g', marker='o', label = 'Valeurs bruitees de g')
	plt.legend(loc = 'upper right')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.show()

	
#Modification inutile
	
	
