import sympy
y = 0
x = 0
i = 0

while y < 2000000:
    x += y
    i += 1
    y = sympy.prime(i)

print(x)
