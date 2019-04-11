import sympy
import math


class PrimeFac:
    def __init__(self, num):
        self.num = num

    def factors(self):
        n = self.num
        z = 2
        thing = [1]
        loop = True
        while loop:
            if math.remainder(n, z) == 0:
                n = int(n / z)
                thing.append(z)
                z = 2
            else:
                if z**2 > n or sympy.isprime(n):
                    loop = False
                    thing.append(n)
                else:
                    z = sympy.nextprime(z)
        return thing
