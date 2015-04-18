import numpy as np
from numpy.random import rand


def generatePane(num=6):
    return [int(rand() * num) for i in range(0, 30)]


class ACO():
    def __init__(self, m, ter, s_sum, dist, start):
        self.x = 0
        self.m = m
        self.ter = ter
        self.s_sum = s_sum
        self.dist = dist
        self.start = start
        self.count = 0
        self.orgPane = generatePane()
        self.goalPane = generatePane()
        self.bestPane = None
        self.bestPath = []
        self.bestScore = 0
        self.finalPane = self.orgPane.copy()
        self.ph = [[1 for i in range(30)] for j in range(30)]
        self.p = [[0 for i in range(30)] for j in range(30)]
        self.dph = [[[0 for i in range(30)] for j in range(30)]
                    for k in range(m)]
        pass
    pass

    def run(self):
        while not self.terminate():
            state = self.start
            self.calcProb()
            for k in range(self.m):
                self.move(state, 30, k)
                pass
            self.update()

    def allowedStep(self, state):
        if state == 0:
            return [state, 1, 6, 7]
        elif state == 5:
            return [state, 4, 10, 11]
        elif state == 24:
            return [state, 18, 19, 25]
        elif state == 29:
            return [state, 28, 22, 23]
        elif 0 < state < 5:
            return [state, state + 6, state - 1, state + 1]
        elif 24 < state < 29:
            return [state, state - 6, state - 1, state + 1]
        elif state == 6 or state == 12 or state == 18:
            return [state, state - 6, state + 6, state + 1]
        elif state == 11 or state == 17 or state == 23:
            return [state, state - 6, state + 6, state - 1]
        else:
            tmp = [7, 6, 5, 1, 0, -1, -5, -6, -7]
            return [state + k for k in tmp]
        pass

    def terminate(self):
        if self.count == 200:
            return True
        self.count += 1
        return False

    def calcProb(self):
        for i in range(6 * 5):
            J = self.allowedStep(i)
            total = sum((self.ph[i][j] for j in J))
            for j in J:
                self.p[i][j] = self.ph[i][j] / total

    def update(self):
        q = 0.1
        for i in range(30):
            for j in range(30):
                self.ph[i][j] = (1 - q) * self.ph[i][j] +\
                    sum(self.dph[k][i][j] for k in range(self.m))

    def move(self, start, times, k):
        state = start
        path = [state]
        for t in range(times):
            J = self.allowedStep(state)
            r = rand()
            tmp = 0
            for j in J:
                nextState = j
                if tmp < r:
                    tmp += self.p[state][j]
                else:
                    break
            path.append(nextState)
            state = nextState
        for i in range(len(path) - 1):
            self.swap(path[i], path[i+1])
        score = self.score()
        cost = (score) / 100
        for i in range(len(path) - 1):
            self.dph[k][path[i]][path[i+1]] = cost
        if score > self.bestScore:
            self.bestPane = self.finalPane.copy()
            self.bestScore = score
            self.bestPath.append(path)
        elif score == self.bestScore:
            self.x += 1
        self.finalPane = self.orgPane.copy()

    def score(self):
        score = 0
        for i in range(30):
            if self.goalPane[i] == self.finalPane[i]:
                score += 1
        return score

    def swap(self, x, y):
        self.finalPane[x], self.finalPane[y] = self.finalPane[y],\
            self.finalPane[x]


def main():
    m = 100
    s_num = 10
    terminate = None
    dist = None
    start = 15
    total = 0
    for i in range(0, 1):
        ant = ACO(m, terminate, s_num, dist, start)
        # pane = generatePane()
        # for i in range(5):
        #     for j in range(6):
        #         print(pane[i * 6 + j], end=' ')
        #     print("")
        ant.run()
        total += ant.bestScore
    for i in ant.bestPath:
        for j in i:
            print(str(j).zfill(2), end=" ")
        print("")
    print(total)
    pass


if __name__ == '__main__':
    main()
