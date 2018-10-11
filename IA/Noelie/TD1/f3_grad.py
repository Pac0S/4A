#Imports from the matplotlib library
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import math
from opti1 import new_position_grad
from opti1 import gradient
#--------------------------------------

#Definition of what to plot
fig = plt.figure() #opens a figure environment
ax = fig.gca(projection='3d') #to perform a 3D plot
X = np.arange(-5, 6, 0.5) #x range
Y = np.arange(-5, 6, 0.5) #y range
X, Y = np.meshgrid(X, Y) #creates a rectangular grid on which to plot the function values (Z)
Z= X**4 - X**3 - 20*X**2 + X + 1 + Y**4 - Y**3 - 20*Y**2 + Y + 1 #defines the function values
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, antialiased=False, cmap=cm.viridis) #plot definition and options

a = 0.001
n=200
'''
val1 = [3,4]
val2 = [-3,-3]
val3 = [-4,-3]
coords = [val1,val2,val3]
'''

val1 = [-0.5,-0.5]
val2 = [-0.5,0.5]
val3 = [0.5,-0.5]
val4 = [0.5,0.5]
val5 = [6,6]
val6 = [6,-5]
val7 = [-6,0]
coords = [val1,val2,val3,val4,val5,val6,val7]

def trace_grad(n,x0,y0,a):
	z0 = x0**4 - x0**3 - 20*x0**2 + x0 + 1 + y0**4 - y0**3 - 20*y0**2 + y0 + 1
	
	x = [x0]
	y = [y0]
	z = [z0]
	
	xnow = x0
	ynow = y0
	znow = z0
	
	for k in range(n):
		p = new_position_grad(xnow,ynow,a)
		xnow = p[0]
		ynow = p[1]
		znow = xnow**4 - xnow**3 - 20*xnow**2 + xnow + 1 + ynow**4 - ynow**3 - 20*ynow**2 + ynow + 1
		x.append(xnow)
		y.append(ynow)
		z.append(znow)
		k=k+1
	return x,y,z
	

col_ind = 0
colors = ['tab:orange', 'c','r','m','b', 'g', 'y',  'k', 'w' , 'slateblue', 'lime', 'maroon', 'gold', 'grey', 'indigo', 'ivory' ]
for val in coords:
		tr = trace_grad(n,val[0],val[1],a)
		x = tr[0]
		y = tr[1]
		z = tr[2]
		ax.plot(x,y,z,color = colors[col_ind])
		col_ind= col_ind+1

#Runs the plot command
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
