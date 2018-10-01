import math

def gradient(x,y):
	grad_x = 4*(x-y)**3+4*x-1
	grad_y = -4*(x-y)**3+2*y+2
	grad = [grad_x, grad_y]
	print("Gradient : " + str(grad[0]) + ", " + str(grad[1]))
	return grad
	
def direction(x,y):
	grad = gradient(x,y)
	direc = [-grad[0], -grad[1]]
	print("Direction : " + str(direc[0]) + ", " + str(direc[1]) )
	return direc
	
def new_position(x,y,alpha):
	print("Position : " + str(x) + ", " + str(y))
	d = direction(x,y)
	new_x = x + alpha * d[0]
	new_y = y + alpha * d[1]
	new_pos = [new_x, new_y]
	print("Nouvelle position : " + str(new_x) + ", " + str(new_y))
	print()
	return new_pos

x0 = 10 #Coordonnée x de départ
y0 = 10 #Coordonnée y de départ
px = x0
py = y0
p = [px,py] #Point actuel
a = 0.09 #pas de convergence

k=0 #itérateur

"""
#Condition du nombre d'itérations
while (k<200):
	p = new_position(px,py,a)
	px = p[0]
	py = p[1]
	k= k+1
	print(k)
print("Position finale : "+ str(px) +", " + str(py))
"""


#Condition de la norme du gradient
grad = gradient(px,py)
while (math.sqrt(grad[0]**2+grad[1]**2)>0.000001):
	p = new_position(px,py,a)
	grad = gradient(px,py)
	px = p[0]
	py = p[1]
	k= k+1
	print(k)
print("Position finale : "+ str(px) +", " + str(py))


"""
#Condition de la norme du pas
while (k<200):
	p = new_position(px,py,a)
	px = p[0]
	py = p[1]
	k= k+1
print("Position finale : "+ str(px) +", " + str(py))
"""
