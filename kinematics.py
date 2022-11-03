from math import sin
from math import radians
from math import sqrt
from math import tan


Mp = 938.272


def Qsq(E, Ep, theta):
	return 4*E*Ep*(sin(radians(theta/2)))**2


def nu(E, Ep):
	return E - Ep


def Wsq(E, Ep, theta):
	return Mp**2 + 2*Mp*nu(E, Ep) - Qsq(E, Ep, theta)


def xbj(E, Ep, theta):
	return Qsq(E, Ep, theta)/(2*Mp*nu(E, Ep))


def gamma(E, Ep, theta):
	return sqrt(Qsq(E, Ep, theta))/nu(E, Ep)


def epsilon(E, Ep, theta):
	fac = 1 + nu(E, Ep)**2/Qsq(E, Ep, theta)
	return 1/(1 + fac*tan(radians(theta/2))**2)


def kappa(E, Ep, theta):
	return 1 - Qsq(E, Ep, theta)/(nu(E, Ep)**2)
