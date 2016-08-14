#! /usr/bin/python
#
# calculate solutions to y**2 = x**3 + 7 mod prime_modulo 
# in the finite field (x,y) = (0,0) - (prime_modulo, prime_modulo)


# MAIN #
prime_modulo=67

for x in range( 0, prime_modulo**2 ):
	x_cube = x**3 + 7 
	for y in range( 0, prime_modulo**2 ):
		y2 = y**2
		##print x, y, x_cube, y2, x_cube - y2, (x_cube-y2) % prime_modulo
		if( (x_cube-y2) % prime_modulo == 0 ):
			print x%prime_modulo, ",", y%prime_modulo

		

