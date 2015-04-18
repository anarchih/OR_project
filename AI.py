from numpy.random import rand


class AI():
    def __init__(self, arr):
        self.__arr = arr
        self.finish = False
        self.path = []
        self.status = 'ready'

    def start(self):
        self.calc()
        self.status = 'moving'
        return [0, 0]
        pass

    def move(self):
        return [int(rand() * 5), int(rand() * 6)]
        pass

    def getStatus(self):
        return self.status

    def calc(self):
        pass
