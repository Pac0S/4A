#Imports from the matplotlib library
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import math
from opti1 import new_position_grad
#--------------------------------------

#Definition of what to plot
fig = plt.figure() #opens a figure environment
ax = fig.gca(projection='3d') #to perform a 3D plot
X = np.arange(-15, 15, 0.5) #x range
Y = np.arange(-15, 15, 0.5) #y range
X, Y = np.meshgrid(X, Y) #creates a rectangular grid on which to plot the function values (Z)
Z= X**2-Y**2 #defines the function values
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, antialiased=False, cmap=cm.viridis) #plot definition and options


a = 0.01
n=50
val1 = [-5,5]
val2 = [0,0]
val3 = [8,0]
coords = [val1,val2,val3]

def trace_grad(n,x0,y0,a):
	z0 = x0**2-y0**2
	
	x = [x0]
	y = [y0]
	z = [z0]
	
	xnow = x0
	ynow = y0
	znow = z0
	
	#while(math.sqrt(grad_xnow**2+grad_ynow**2) <0.000001):
	for k in range(n):
		p = new_position_grad(xnow,ynow,a)
		xnow = p[0]
		ynow = p[1]
		znow = znow = xnow**2 - ynow**2
		x.append(xnow)
		y.append(ynow)
		z.append(znow)
		k=k+1
	return x,y,z
	

col_ind = 0
colors = ['tab:orange', 'm','r','g','b', 'c', 'y',  'k', 'w' , 'slateblue', 'lime', 'maroon', 'gold', 'grey', 'indigo', 'ivory' ]
for val in coords:
		tr = trace_grad(n,val[0],val[1],a)
		x = tr[0]
		y = tr[1]
		z = tr[2]
		ax.plot(x,y,z,color = colors[col_ind])
		col_ind= col_ind+1

#Runs the plot command
plt.show()
