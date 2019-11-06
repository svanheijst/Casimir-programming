# Import all thing required
import numpy as np

# Prints only needed in first exercise
if __name__ == '__main__':
    print('hello world')
    print('-----------')


## Functions
# circumference circle
def circ(r):
    """This function will calculate the circumference of a circle of radius r.
    
    Parameters: radius, r
    
    Returns: circumference"""
    return 2*np.pi*r

# surface circle
def surface(r):
	"""This function will calculate the surface of a circle of radius r.

	Parameters: radius, r
	Returns: surface"""
	return np.pi*r**2

# convert polar cordinates to cartesian
def polar2cart(r,theta=np.linspace(0,2*np.pi,100)):
    x=r*np.cos(theta)
    y=r*np.sin(theta)
    return x, y


## Prints used to check if my script was working, before creation script.py
if __name__ == '__main__':
    R=float(input('Give the radius of the circle [cm]: '))
    C=circ(R)
    print('A circle with a radius of %0.2f cm has a circumference of %0.2f cm' %(R,C))
    
    S=surface(R)
    print('A circle with a radius of %0.2f cm has a surface of %0.2f cm^2' %(R,S))
