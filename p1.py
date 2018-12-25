import math

n = 0

for i in range(1000):
    if math.remainder(i, 3) == 0 or math.remainder(i, 5) == 0:
        n = n + i


print(n)
