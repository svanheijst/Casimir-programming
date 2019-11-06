if __name__ == '__main__':
    print('hello world')
    print('-----------')

import numpy as np

# circumference circle
def circ(r):
	"""This function will calculate the circumference of a circle of radius r.

	Parameters: radius, r
	Returns: circumference"""
	return 2*np.pi*r

## used to check if the script was working
#R=float(input('Give the radius of the circle [cm]: '))
#C=circ(R)
#print('A circle with a radius of %0.2f cm has a circumference of %0.2f cm' %(R,C))

# surface circle
def surface(r):
	"""This function will calculate the surface of a circle of radius r.

	Parameters: radius, r
	Returns: surface"""
	return np.pi*r**2

## used to check if the script was working
#S=surface(R)
#print('A circle with a radius of %0.2f cm has a surface of %0.2f cm^2' %(R,S))

# define circle
def polar2cart(r,theta=np.linspace(0,2*np.pi,100)):
    x=r*np.cos(theta)
    y=r*np.sin(theta)
    return x, y