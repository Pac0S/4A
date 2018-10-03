#Imports from the matplotlib library
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import math
#--------------------------------------

#Definition of what to plot
fig = plt.figure() #opens a figure environment
ax = fig.gca(projection='3d') #to perform a 3D plot
X = np.arange(-1, 1, 0.05) #x range
Y = np.arange(-1, 1, 0.05) #y range
X, Y = np.meshgrid(X, Y) #creates a rectangular grid on which to plot the function values (Z)
Z= (X-Y)**4 + 2*X**2 + Y**2 - X + 2*Y #defines the function values
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, antialiased=False, cmap=cm.viridis) #plot definition and options





def trace(n,x0,y0,a):
	z0 = (x0-y0)**4 + 2*x0**2 + y0**2 - x0 + 2*y0
	
	x = []
	y = []
	z = []
	
	x.append(x0)
	y.append(y0)
	z.append(z0)
	
	xnow = x0
	ynow = y0
	znow = z0
	
	grad_xnow = 4*(xnow-ynow)**3+4*xnow-1
	grad_ynow = -4*(xnow-ynow)**3+2*ynow+2
		
	k=0
	
	#while(math.sqrt(grad_xnow**2+grad_ynow**2) <0.000001):
	for k in range(n):
		#Calcul du gradient
		grad_xnow = 4*(xnow-ynow)**3+4*xnow-1
		grad_ynow = -4*(xnow-ynow)**3+2*ynow+2
		#Calcul de la direction
		direc_xnow = -grad_xnow
		direc_ynow = -grad_ynow
		#Calcul des nouvelles coordonnees
		xnow = xnow + a * direc_xnow
		ynow = ynow + a * direc_ynow
		znow = (xnow-ynow)**4 + 2*xnow**2 + ynow**2 - xnow + 2*ynow
		#Ajout des nouvelles coordonnees aux listes
		x.append(xnow)
		y.append(ynow)
		z.append(znow)
		k=k+1
	return x,y,z
	
a = 0.01
n=100

valx0 = [-0.5,0.5,1]
valy0 = [-0.5,0.5,1]
col_ind = 0
colors = ['b', 'g', 'r', 'c', 'm', 'y',  'k', 'w', 'tab:orange', 'slateblue', 'lime', 'maroon', 'gold', 'grey', 'indigo', 'ivory' ]
for i in valx0:
	for j in valy0:
		tr = trace(n,i,j,a)
		x = tr[0]
		y = tr[1]
		z = tr[2]
		ax.plot(x,y,z,label = "(x0,y0)="+"("+str(i)+","+str(j)+")",color = colors[col_ind])
		col_ind= col_ind+1
	
#Runs the plot command
plt.show()

