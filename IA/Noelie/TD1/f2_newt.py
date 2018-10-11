#Imports from the matplotlib library
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import math
from opti1 import new_position_newt
#--------------------------------------

#Definition of what to plot
fig = plt.figure() #opens a figure environment
ax = fig.gca(projection='3d') #to perform a 3D plot
X = np.arange(-30, 30, 1) #x range
Y = np.arange(-30, 30, 1) #y range
X, Y = np.meshgrid(X, Y) #creates a rectangular grid on which to plot the function values (Z)
Z= X**2-Y**2 #defines the function values
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, antialiased=False, cmap=cm.viridis) #plot definition and options



n=1
val1 = [-5,5]
val2 = [0,0]
val3 = [8,0]
val4 = [12,-13]
val5 = [-30,-30]
coords = [val1,val2,val3,val4,val5]

def trace_newt(n,x0,y0):
	z0 = x0**2-y0**2
	
	px = x0
	py = y0
	pz = z0
	
	x = [x0]
	y = [y0]
	z = [z0]
	
	for k in range(n):
		p = new_position_newt(px,py)
		px = p[0]
		py = p[1]
		pz = px**2-py**2
		x.append(px)
		y.append(py)
		z.append(pz)
	return x,y,z

col_ind = 0
colors = ['g', 'r',  'm', 'y',  'k', 'w', 'tab:orange', 'slateblue', 'lime''c', 'maroon', 'gold', 'grey', 'b','indigo', 'ivory' ]
for val in coords:
	tr = trace_newt(n,val[0],val[1])
	x = tr[0]
	y = tr[1]
	z = tr[2]
	ax.plot(x,y,z,color = colors[col_ind])
	col_ind= col_ind+1

#Runs the plot command
plt.show()
