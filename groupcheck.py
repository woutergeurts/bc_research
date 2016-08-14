#!/usr/bin/python
prime_modulo=67
elcurv=[]
filename='elliptic_curve_finite.out'
with open(filename) as f:
	for line in f:
		data = line.split()
		elcurv.append((int(data[0]),int(data[2])))

def invert( (a,b) ):
	return(a, prime_modulo-b)


def dblonline( (x1,y1), (x3,y3) ):
	#
	# when doubling the rc is (3x1**2/2y1)
	#
	# x3p = x3 + mP
	# y3p = y3 + nP
	# 1 and 3P are on straight line, so
	# y1 = ax1 + b
	# y3 = ax3 + b
	# a = 3 x1**2 / 2 y1
	# b = y1 - 3 x1**3 / 2y1
	# y3p = a x3p + b =>  y3 + n P = ax3 + a m P + b
	# y3 + n P = (x3 + mP ) (3 x1**2 / 2 y1) + (y1 - 3 x1**3 / 2y1)
	# y1 ( y3 + n P)  = (x3 + mP ) (3 x1**2 / 2 ) + (y1**2 - 3 x1**3 / 2)
	for n in range(0,prime_modulo):
		for m in range(0,prime_modulo):
			if(  
				 2 * y1 * ( y3 + n * prime_modulo)  ==  
				(x3 + m * prime_modulo ) *  (3 *x1**2  ) + (y1**2 - 3 * x1**3 ) ):

				# print "solution", m, n, 
				return True
	return False

def isonline( (x1,y1), (x2,y2), (x3,y3) ):
	#
	# x3p = x3 + mP
	# y3p = y3 + nP
	# 1, 2 and 3P are on straight line, so
	# y1 = ax1 + b
	# y2 = ax2 + b
	# a = (y2-y1)/(x2-x1)
	# b = y1 - x1 (y2-y1)/(x2-x1)
	# y3p = ax3p + b =>  y3 + n P = ax3 + a m P + b
	# y3 + n P = x3 (y2-y1)/(x2-x1) + (y2-y1)/(x2-x1)mP + y1 - x1 (y2-y1)/(x2-x1)
	# (y3 - y1 + n P)(x2-x1) = (x3 + mP - x1 )(y2-y1) 
	for n in range(0,prime_modulo):
		for m in range(0,prime_modulo):
			if( ( y3 - y1 + n * prime_modulo ) * ( x2 - x1 ) ==
			( x3 + m * prime_modulo - x1 ) * ( y2 - y1 ) ):
				#print "solution", m, n, 
				return True
	return False

def calc_sum():
#
# determine if there is a p3 in the set that is equal to p1 + p2
# (p1 <> p2), otherwise p3 = 2*p1, which is a different formula
#
	for i in range(0,len(elcurv)):
		p1 = elcurv[i]
		for j in range(0,len(elcurv)):
			p2 = elcurv[j]
			solfound=False
			if not( i == j ):
				for k in range(0,len(elcurv)): 
					p3 = elcurv[k]
					found = isonline(p1,p2,p3)
					if found:
						print p1, " + ", p2, " = ", p3
						solfound = True
				if not solfound:
					print p1, " + ", p2, " = (?, ?)"

def calc_double():
	for i in range(0,len(elcurv)):
		p1 = elcurv[i]
		solfound=False
		for k in range(0,len(elcurv)):
			p3 = elcurv[k]
			found = dblonline(p1,p3)
			if found:
				print p1, " *  2 = ", p3
				solfound = True
		if not solfound:
			print p1,  "solution not found"


#calc_double()
calc_sum()
