#Imports from the matplotlib library
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
#--------------------------------------

#Definition of what to plot
fig = plt.figure() #opens a figure environment
ax = fig.gca(projection='3d') #to perform a 3D plot
X = np.arange(-1, 1, 0.05) #x range
Y = np.arange(-1, 1, 0.05) #y range
X, Y = np.meshgrid(X, Y) #creates a rectangular grid on which to plot the function values (Z)
Z= (X-Y)**4 + 2*X**2 + Y**2 - X + 2*Y #defines the function values
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, antialiased=False) #plot definition and options

def trace(n,x0,y0,a):
	x=x0
	y=y0
	for k in range(n):
		grad_x = 4*(x-y)**3+4*x-1
		grad_y = -4*(x-y)**3+2*y+2
		direc_x = -grad_x
		direc_y = -grad_y
		x = direc_x * x
		y = direc_y * y
		plt.plot([x], [y], marker='o', markersize=3, color="red")
	return x,y
	
#Runs the plot command
plt.show()

