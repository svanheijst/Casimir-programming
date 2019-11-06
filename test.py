print('hello world')
print('-----------')

import numpy as np

# circumference circle
def circ(r):
	"""This function will calculate the circumference of a circle of radius r.

	Parameters: radius, r
	Returns: circumference"""
	return 2*np.pi*r

R=float(input('Give the radius of the circle [cm]: '))
C=circ(R)
print('A circle with a radius of %0.2f cm has a circumference of %0.2f cm' %(R,C))
