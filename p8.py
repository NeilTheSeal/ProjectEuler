import numpy as np
theNumber = ""

fileRead = np.loadtxt("bigNumber.txt", dtype=str)

for i in fileRead:
    theNumber += i

adj13 = []
prods = []

for i in range(0, len(theNumber) - 12):
    if str(theNumber[i:i+13]).find("0") == -1:
        adj13.append(theNumber[i:i+13])

for i in range(0, len(adj13)):
    prods.append(1)
    for j in range(0, 13):
        prods[i] *= int(str(adj13[i])[j])

print(max(prods))
