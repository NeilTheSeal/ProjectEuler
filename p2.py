import math

n = 0
n2 = 1
matrix = [0]
matrix2 = [0]

while n < 4e6:
    n = n + n2

    if math.remainder(n, 2) == 0:
        matrix.append(n)

    n2 = n + n2

    if math.remainder(n2, 2) == 0:
        matrix.append(n2)

print(sum(matrix))

'''just gonna go ahead and test version control here'''
