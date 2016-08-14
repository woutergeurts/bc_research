#! /usr/bin/python
# secp256k1 curve 
# Elliptic curve equation: y2 = x3 + 7
# 
prime_modulo = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 -1
print format(prime_modulo, "#0X")
print "0XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F"
# 
# corresponding y is
base_y = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8 
# corresponding x is
base_x = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
print "base check: ", (base_y**2 - base_x**3 - 7) % prime_modulo
#
# order is 
# FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE BAAEDCE6 AF48A03B BFD25E8C D0364141
 
