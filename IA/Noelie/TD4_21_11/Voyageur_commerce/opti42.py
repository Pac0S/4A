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

def generate_map(nb,size):
	coords = np.random.randint(size+1,size=(2,nb))
	return coords






#############
#	Main	#
#############

if __name__=='__main__':
	map1 = generate_map(5,10)
	print(map1)


	plt.scatter(map1[0],map1[1])
	axes = plt.gca()
	axes.set_xlim([-1,11])
	axes.set_ylim([-1,11])
	plt.show()
