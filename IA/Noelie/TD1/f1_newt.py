#Imports from the matplotlib library
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import math
import opti1 as op
#--------------------------------------

#Definition of what to plot
fig = plt.figure() #opens a figure environment
ax = fig.gca(projection='3d') #to perform a 3D plot
X = np.arange(-1, 1, 0.05) #x range
Y = np.arange(-1, 1, 0.05) #y range
X, Y = np.meshgrid(X, Y) #creates a rectangular grid on which to plot the function values (Z)
Z= (X-Y)**4 + 2*X**2 + Y**2 - X + 2*Y #defines the function values
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, antialiased=False, cmap=cm.viridis) #plot definition and options


n=2
x0=1
y0=1
def trace_newt(n,x0,y0):
	z0 = (x0-y0)**4 + 2*x0**2 + y0**2 - x0 + 2*y0
	px = x0
	py = y0
	pz = z0
	x = [x0]
	y = [y0]
	z = [z0]
	for k in range(n):
		p = op.new_position_newt(px,py)
		px = p[0]
		py = p[1]
		pz = (px-py)**4 + 2*px**2 + py**2 - px + 2*py
		x.append(px)
		y.append(py)
		z.append(pz)
	return x,y,z
		
valx0 = [-0.5,0.5,1]
valy0 = [-0.5,0.5,1]
col_ind = 0
colors = ['b', 'g', 'r', 'c', 'm', 'y',  'k', 'w', 'tab:orange', 'slateblue', 'lime', 'maroon', 'gold', 'grey', 'indigo', 'ivory' ]
for i in valx0:
	for j in valy0:
		tr = trace_newt(n,i,j)
		x = tr[0]
		y = tr[1]
		z = tr[2]
		ax.plot(x,y,z,color = colors[col_ind])
		col_ind= col_ind+1
	
#Runs the plot command
plt.show()



