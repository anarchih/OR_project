from numpy.random import rand
import numpy as np


class Disk():
    def __init__(self):
        self.arr = np.array([[int(rand() * 6 + 1)for i in range(0, 6)]
                             for i in range(0, 5)])
        self.status = "movable"
        pass

    def getStatus(self):
        return self.status

    def chStatus(self, status):
        self.status = status

    def eliminate(self):
        pass

    def switch(self, p, n):
        self.arr[p[0]][p[1]], self.arr[n[0]][n[1]] = self.arr[n[0]][n[1]],\
            self.arr[p[0]][p[1]]
