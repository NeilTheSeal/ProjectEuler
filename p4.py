import math
import scipy
import numpy


class Pallin:
    def __init__(self, num):
        self.num = num

    def ispal(self, num):
        pal = int(str(num)[::-1])
        if pal == num:
            return True
        else:
            return False

    return
