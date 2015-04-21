from numpy.random import rand
from Queue import PriorityQueue


def generatePane(num=3):
    a = [i for i in range(0, num * num)]
    for i in range(num * num):
        r = int(rand() * 30)
        a[i], a[r] = a[r], a[i]
    return a


class Astar():
    def __init__(self, pane, start):
        self.pane = pane
        self.width = len(pane[0])
        self.height = len(pane[1])
        self.findResult = False
        self.openNode = PriorityQueue()
        self.total = self.width, self.height

    def run(self):
        while not self.findResult:
            self.g() * self.h()

    def h(self):
        pass

    def g(self):
        pass


def main():
    pane = generatePane()
    start = len(pane[0]) * len(pane) - 1
    a = Astar(pane, start)
    a.run()

if __name__ == '__main__':
    main()
