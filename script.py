#%matplotlib inline
import numpy as np
print('made by Maarten Bolhuis')

print('This script calls on the script test')

print('Made by Sabrya van Heijst')

import test

Radius=float(input('Give the radius of the circle [cm]: '))
C = test.circ(Radius)
S = test.surface(Radius)

print('A circle of radius %0.2f cm has a circumference of %0.2f cm and a surface of %0.2f cm^2' %(Radius,C,S))

import matplotlib.pyplot as plt
x = np.linspace(0,11,10)
y = 2*x
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(x,y)
fig.savefig('Plot')
