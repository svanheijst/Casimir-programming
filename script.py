print('This is a script with the name script.py')

import test

Radius=float(input('Give the radius of the circle [cm]: '))
C = test.circ(Radius)
S = test.surface(Radius)

print('A circle of radius %0.2f cm has a circumference of %0.2f cm and a surface of %0.2f cm^2' %(Radius,C,S))
