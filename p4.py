import math
import scipy
import numpy

list1 = [1]
list2 = [1, 1]


class Pallin:
    def __init__(self, num):
        self.num = num

    def ispal(self):
        pal = int(str(self.num)[::-1])
        if pal == self.num:
            return True
        else:
            return False


for i in range(100, 999):
    for k in range(100, 999):
        if Pallin(i * k).ispal():
            list1.append(i * k)
            list2.append([i, k])

print(max(list1))
print(list2[list1.index(max(list1))])
