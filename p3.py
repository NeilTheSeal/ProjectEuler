import sympy
import numpy
import math

n = 24572458916752143
z = 2
thing = [1]

loop = True

while loop:
    if math.remainder(n, z) == 0:
        n = n/z
        thing.append(z)
        z = 2
    else:
        if z**2 > n or sympy.isprime(n):
            loop = False
            thing.append(n)
        else:
            z = sympy.nextprime(z)

print(n)
print(thing)
print(int(numpy.product(thing)))
