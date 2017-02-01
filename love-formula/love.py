# Firstly, install packages (matplotlib numpy)
# pip install matplotlib numpy

import matplotlib.pyplot as plt 
import numpy as np

fig = plt.figure(edgecolor=(0,0,0),linewidth=10)
fig.suptitle('Formula love', fontsize=14, fontweight='bold')

""" Drawing I """
y = np.linspace(0, 10, 10)
# x are zeros
x = np.zeros(len(y))
ax = fig.add_subplot(2,8,1)  # add I graph
ax.plot(x, y, 'g')

""" Drawing L """
x = np.linspace(0.1, 5, 100)
# compute y = 1/10X^2
y = 1/(10 * x**2)

ax = fig.add_subplot(2,8,3) # add L graph
ax.get_yaxis().set_visible(False) # disable y axis
ax.plot(x, y, 'b')
##################

""" Drawing O """
theta = np.linspace(0, 2*np.pi, 100)
# the radius of the circle
r = 3
# compute x = 3cos(theta)
# compute y = 3sin(theta)
x = r*np.cos(theta)
y = r*np.sin(theta)

ax = fig.add_subplot(2,8,4) # add O graph
ax.get_yaxis().set_visible(False)	# disable y axis
ax.plot(x, y, 'b')
##################

""" Drawing V """
x = np.linspace(-1.5, 1.5, 100)
# compute y = |-3x|
y =np.abs(-3*x)

ax = fig.add_subplot(2,8,5) # add V graph
ax.get_yaxis().set_visible(False) # disable y axis
ax.plot(x, y, 'b')
##################

""" Drawing E """
y = np.linspace(0, 6, 100)
# compute x = -3|sin⁡(y)|
x = -3*np.abs(np.sin(y))

ax = fig.add_subplot(2,8,6) # add E graph
ax.get_yaxis().set_visible(False) # disable y axis
ax.plot(x, y, 'b')
##################

""" Drawing U """
x = np.linspace(-3, 3, 100)
# compute x
y = x**2

ax = fig.add_subplot(2,8,8) # add U graph
ax.plot(x, y, 'g')

""" Drawing a heart """
theta = np.linspace(0, 2*np.pi, 100)
# compute x = 16sin3(theta)
# compute y = 13cos⁡(theta)- 5cos(2theta) - 2cos⁡(3theta) - cos(4theta)
x = 16*np.sin(theta)**3
y = 13*np.cos(theta) - 5*np.cos(2*theta) - 2*np.cos(3*theta) - np.cos(4*theta)

ax = fig.add_subplot(2,3,5)
ax.plot(x, y, 'r')
##################

# Show all graphs
plt.show()		
