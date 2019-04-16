import math

a = 1
b = 2
c = 0
c2 = 0
c2List = []
found = False

for i in range(0, 998):
    c2List.append(i**2)

while not found:
    c2 = a**2 + b**2
    if (c2 in c2List) and (a + b + math.sqrt(a**2 + b**2) == 1000):
        print("a = " + str(a))
        print("b = " + str(b))
        print("c = " + str(math.sqrt(a**2 + b**2)))
        print("abc = " + str(a*b*math.sqrt(a**2 + b**2)))
        found = True
    elif b < 998:
        b += 1
    elif b >= 998:
        a += 1
        b = a + 1
    if a >= 499:
        found = True
        print('no solution found')
