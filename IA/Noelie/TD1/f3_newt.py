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
X = np.arange(-5, 6, 0.5) #x range
Y = np.arange(-5, 6, 0.5) #y range
X, Y = np.meshgrid(X, Y) #creates a rectangular grid on which to plot the function values (Z)
Z= X**4 - X**3 - 20*X**2 + X + 1 + Y**4 - Y**3 - 20*Y**2 + Y + 1 #defines the function values
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, antialiased=False, cmap=cm.viridis) #plot definition and options

n=5

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
val8 = [-2,-0.2]
coords = [val1,val2,val3,val4,val5,val6,val7,val8]


def trace_newt(n,x0,y0):
	z0 = x0**4 - x0**3 - 20*x0**2 + x0 + 1 + y0**4 - y0**3 - 20*y0**2 + y0 + 1
	
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
		pz =  px**4 - px**3 - 20*px**2 + px + 1 + py**4 - py**3 - 20*py**2 + py + 1
		x.append(px)
		y.append(py)
		z.append(pz)
	return x,y,z

col_ind = 0
colors = ['tab:orange', 'c','r','m','b', 'g', 'y',  'k', 'w' , 'slateblue', 'lime', 'maroon', 'gold', 'grey', 'indigo', 'ivory' ]
for val in coords:
	tr = trace_newt(n,val[0],val[1])
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
