from math import sin
from math import radians
from math import sqrt


Mp = 938.272


def Qsq(E, Ep, theta):
	return 4*E*Ep*(sin(radians(theta/2)))**2


def nu(E, Ep):
	return E - Ep


def W(E, Ep, theta):
	return Mp**2 + 2*Mp*nu(E, Ep) - Qsq(E, Ep, theta)


def xbj(E, Ep, theta):
	return Qsq(E, Ep, theta)/(2*Mp*nu(E, Ep))


def gamma(E, Ep, theta):
	return sqrt(Qsq(E, Ep, theta))/nu(E, Ep)
