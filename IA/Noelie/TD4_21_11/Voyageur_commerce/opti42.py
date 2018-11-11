#Imports from the matplotlib library
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
#--------------------------------------
import math
import numpy as np
import random




#################
#	Methodes	#
#################

#Generer nb villes sur une carte carree de taille size
def generate_map(nb,size):
	coords = np.random.randint(size+1,size=(2,nb))
	return coords

#Calculer la distance parcourue sur le chemin des villes de coordonnees coords dans l'ordre defini par path
def distance(path, coords):
	travel = 0
	for i in range(len(path)-1):
		travel += math.sqrt((coords[0][path[i]]-coords[0][path[i+1]])**2+(coords[1][path[i]]-coords[1][path[i+1]])**2)
	return travel

#Permutation aleatoire de deux cases de l'ordre de parcours path
def permutation(path):
	newpath = np.copy(path)
	to_change1 = np.random.randint(len(newpath))
	to_change2 = to_change1
	while(to_change2==to_change1):
		to_change2 = np.random.randint(len(newpath))
	newpath[to_change1] = path[to_change2]
	newpath[to_change2] = path[to_change1]
	return newpath
	
def run(coords, path, t, k2):
	distances = []
	intervalle = 50
	k=0
	for step in t:
		T=1./step
		#Palier
		invdE=0
		for i in range(20):
			other_path = permutation(path)
			invdE += distance(other_path,coords) - distance(path,coords)
		dE = invdE/20.
		#Fin du palier
		
		#Calcul de la probabilite de garder un x moins bon
		proba  = k2*math.exp(-dE/(1000*T))
		
		#Iteration reelle
		newpath = permutation(path)
		if(distance(newpath,coords) < distance(path,coords)):
			path = newpath
		else:
			roll = random.random()
			if(roll<proba):
				path=newpath
		#On ajoute la distance au vecteur distances
		distances.append(distance(path,coords))
		
		#Affichage du chemin toutes les "intervalle" iterations
		if k%intervalle==0:
			newcoords = np.copy(coords)
			newcoords[1] = newcoords[1][path[0:len(path)+1]]
			newcoords[0] = newcoords[0][path[0:len(path)+1]]
			
			plt.plot(newcoords[0],newcoords[1])
			plt.scatter(newcoords[0],newcoords[1],color='r')
			plt.title("k= {0}, Distance = {1}".format(k, distance(path,coords)))
			axes = plt.gca()
			axes.set_xlim([-1,31])
			axes.set_ylim([-1,31])
			plt.show()
		k+=1
	return [path, distances]
	
		

#############
#	Main	#
#############

if __name__=='__main__':
	
	nb = 10
	map1 = generate_map(nb,30)
	k2=0.5
	print(map1)
	
	path1 = np.arange(0,nb,1)
	print(path1)
	
	print(distance(path1,map1))
	
	print(permutation(path1))
	
	
	time = np.arange(1,500,1)
	run1 = run(map1,path1,time,k2)
	
	final_path = run1[0]
	distances = run1[1]
	
	
	plt.plot(time, distances)
	plt.show()
