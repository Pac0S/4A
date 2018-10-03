import math
import numpy as np

def gradient(x,y):
	grad_x = 4*(x-y)**3+4*x-1
	grad_y = -4*(x-y)**3+2*y+2
	grad = [grad_x, grad_y]
	#print("Gradient : " + str(grad[0]) + ", " + str(grad[1]))
	return grad
	
def direction_grad(x,y):
	grad = gradient(x,y)
	direc = [-grad[0], -grad[1]]
	#print("Direction : " + str(direc[0]) + ", " + str(direc[1]) )
	return direc
	
def new_position_grad(x,y,alpha):
	#print("Position : " + str(x) + ", " + str(y))
	d = direction_grad(x,y)
	new_x = x + alpha * d[0]
	new_y = y + alpha * d[1]
	new_pos = [new_x, new_y]
	#print("Nouvelle position : " + str(new_x) + ", " + str(new_y))
	#print('')
	return new_pos
	
def direction_newt(x,y):
	grad = gradient(x,y)
	#Vecteur gradient
	vgrad = np.array([[grad[0]],[grad[1]]])
	#print(vgrad.shape)
	
	#Matrice hessienne
	hes = np.array([[12*(x-y)**2+4, -12*(x-y)**2], [-12*(x-y)**2, 12*(x-y)**2+2]])
	#print(hes.shape)
	#print(hes)
	
	#Inversion de la hessienne pour le calcul
	invhes = np.linalg.inv(hes)
	#print(invhes)
	
	#Calcul de la direction
	d = -invhes.dot(vgrad)
	#print('Vecteur direction : \n' + str(d))
	return d
	
def new_position_newt(x,y):
	#print("Position : " + str(x) + ", " + str(y))
	d = direction_newt(x,y)
	new_x = x +  d[0][0]
	new_y = y +  d[1][0]
	new_pos = [new_x, new_y]
	#print("Nouvelle position : " + str(new_x) + ", " + str(new_y))
	#print('')
	return new_pos

x0 = 1 #Coordonnee x de depart
y0 = 1 #Coordonnee y de depart
px = x0
py = y0
p = [px,py] #Point actuel
a = 0.09 #pas de convergence
lim = 0.000001 #Limite gradient


#################################
#		Descente de gradient	#
#################################


print("METHODE DE LA DESCENTE DU GRADIENT")
grad = gradient(px,py)
k=0
#for k in range(100):
while (math.sqrt(grad[0]**2+grad[1]**2)>lim):	
	p = new_position_grad(px,py,a)
	grad = gradient(px,py)
	px = p[0]
	py = p[1]
	k= k+1
print("Gradient < " + str(lim) + ", iteration no "+str(k))
print("Position finale : "+ str(px) +", " + str(py))
print('')

#################################
#		Methode de Newton		#
#################################


print('METHODE DE NEWTON')
px = x0
py = y0
k=0
grad = gradient(px,py)
#for k in range(100):
while(math.sqrt(grad[0]**2+grad[1]**2)>lim):
	p = new_position_newt(px,py)
	grad = gradient(px,py)
	px = p[0]
	py = p[1]
	k=k+1
print("Gradient < " + str(lim) + ", iteration no "+str(k))
print("Position finale : "+ str(px) +", " + str(py))
	


