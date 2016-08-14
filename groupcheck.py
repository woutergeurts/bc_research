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
	for n in range(-prime_modulo,prime_modulo):
		for m in range(-prime_modulo,prime_modulo):
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
	for n in range(-prime_modulo,prime_modulo):
		for m in range(-prime_modulo,prime_modulo):
			if( ( y3 - y1 + n * prime_modulo ) * ( x2 - x1 ) == ( x3 + m * prime_modulo - x1 ) * ( y2 - y1 ) ):
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
			for k in range(0,len(elcurv)): 
				if not ( i==j or i==k or j==k ):
					p3 = elcurv[k]
					found = isonline(p1,p2,p3)
					if found:
						print p1, " + ", p2, " = ", invert(p3),
						solfound = True
			if not solfound:
				print p1, " + ", p2, " = (?, ?)",
			print " calculated :", point_add( p1, p2, prime_modulo)

def calc_ring():
	print "N = ", len(elcurv)
	for i in range(0,len(elcurv)):
		pstart = elcurv[i]
		a = 0
		p = prime_modulo
		d = 2
		p_single = pstart
		p_double = point_dbl( p_single, a, p )
		p_4 = point_dbl( p_double, a, p )
		p_8 = point_dbl( p_4, a, p )
		p_16 = point_dbl( p_8, a, p )
		##print 4, 8, 16, p_4, p_8, p_16
		##print 1, p_single
		##print 2, p_double
		p_end = p_double
		while d < len(elcurv): 
			p_end = point_add( p_end, p_single, p ) 
			if p_end == pstart:
				break;
			d = d + 1
			##	print d, p_end,
		print pstart, d

def inverse_mod( a, n ):
# ref wikipedia: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
#function inverse(a, n)
#    t := 0;     newt := 1;    
#    r := n;     newr := a;    
#    while newr <> 0
#        quotient := r div newr
#        (t, newt) := (newt, t - quotient * newt) 
#        (r, newr) := (newr, r - quotient * newr)
#    if r > 1 then return "a is not invertible"
#    if t < 0 then t := t + n
#    return t
#
	t = 0
	newt = 1
	r = n
	newr = a % n # note: algorithm does not work with a < 0 
	while newr != 0: 
		q = r / newr
		(t, newt) = (newt, t - q * newt)
		(r, newr) = (newr, r - q * newr)
	if r > 1:
		print "a is not invertible", 
	if t < 0:
		t = t + n
	return t

def point_add( (x1,y1), (x2, y2), p ):
#
# point add formula
#
	s = ( (y2 - y1) * inverse_mod( ( x2 - x1 ), p ) ) 
#
#	s = richtingscoefficient
# 	x1 + s (x2 - x1)
#
#
	x3 = ( s**2 - x1 - x2 ) % p 
	y3 = ( s * (x1 - x3 ) - y1 ) % p 
	return (x3, y3) 
#
#
def point_dbl( (x1,y1), a, p ):
#
# point dbl formula for y2 = x3 + a x + ?
#
	s = ( (3 * x1**2 + a) * inverse_mod( ( 2 * y1 ), p ) ) 
#
#	s = derivative
#
#
	x3 = ( s**2 - 2 * x1 ) % p 
	y3 = ( s * (x1 - x3 ) - y1 ) % p 
	return (x3, y3) 
#
#



if __name__ == "__main__":
	#calc_ring() 
	calc_sum() 
	print inverse_mod(2, 17) # expect 9 (9 * 2) = 1 mod 17
	print inverse_mod(-2, 17) # expect 8 (8 * -2) = 1 mod 17
	print inverse_mod(15, 17) # 
	print "double test (6,3): ", point_dbl( (5,1), 2, 17 )
	print point_add( (2,22), (6,25), prime_modulo)
