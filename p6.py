sumOfSq = int(0)
sumOf = int(0)
sqOfSum = int(0)

for i in range(1, 101):
    sumOfSq += i**2
    sumOf += i

sqOfSum = sumOf**2
diff = sqOfSum - sumOfSq

print([sumOfSq, sqOfSum, diff])
