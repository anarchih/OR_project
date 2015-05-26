from queue import PriorityQueue, Queue
from copy import deepcopy
import time
from puzzleGenerator import puzGen
GOAL_4X4 = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
GOAL_3X3 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


class Puzzle():
    def __init__(self, width, height, board, pointer):
        self.width = width
        self.height = height
        self.board = board
        self.str_ = str()
        self.pointer = pointer

    def solved(self, goal):
        return self.board == goal

    def possible_moves(self):
        j, i = self.pointer
        if i > 0:
            b = deepcopy(self.board)
            b[i - 1][j], b[i][j] = self.board[i][j], self.board[i - 1][j]
            yield Puzzle(self.width, self.height, b, (j, i - 1))
        if i < self.width - 1:
            b = deepcopy(self.board)
            b[i + 1][j], b[i][j] = self.board[i][j], self.board[i + 1][j]
            yield Puzzle(self.width, self.height, b, (j, i + 1))
        if j > 0:
            b = deepcopy(self.board)
            b[i][j - 1], b[i][j] = self.board[i][j], self.board[i][j - 1]
            yield Puzzle(self.width, self.height, b, (j - 1, i))
        if j < self.height - 1:
            b = deepcopy(self.board)
            b[i][j + 1], b[i][j] = self.board[i][j], self.board[i][j + 1]
            yield Puzzle(self.width, self.height, b, (j + 1, i))

    def findPointer(self):
        p = (0, 0)
        for i in range(self.width):
            for j in range(self.height):
                if self.board[i][j] == self.width * self.height - 1:
                    p = (j, i)
        return p

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board) + (str(self.pointer)))


class Node():
    def __init__(self, puzzle, g, back, goal):
        self.puzzle = puzzle
        self.solved = False
        self.h = self.H(goal)
        self.g = g
        self.f = self.h + self.g
        self.next_ = None
        self.back = back

    def H(self, goal):
        tmp = [Queue(), Queue(), Queue(), Queue(), Queue(), Queue()]
        total = 0
        p = self.puzzle
        t = 0
        for i in range(p.height):
            for j in range(p.width):
                tmp[p.board[i][j]].put((i, j))

        for i in range(p.height):
            for j in range(p.width):
                a = tmp[goal[i][j]].get()
                total += abs(a[0] - i) + abs(a[1] - j)

        # for i in range(p.width):
        #     for j in range(p.height):
        #         a = int(p.board[i][j] / p.width)
        #         b = p.board[i][j] % p.width
        #         t = abs(a - j) + abs(b - i)
        return total * 2

    def __lt__(self, other):
        return self.f < other.f

    def __gt__(self, other):
        return self.f > other.f

    def __ge__(self, other):
        return self.f >= other.f

    def __le__(self, other):
        return self.f <= other.f

    def __eq__(self, other):
        return self.f == other.f


class Solver():
    def __init__(self, start, goal):
        self.start = start
        self.bestNode = None
        self.final = None
        self.goal = goal

    def solve(self):
        q = PriorityQueue()
        self.bestNode = Node(self.start, 0, None, self.goal)
        q.put(self.bestNode)
        s = set()
        s.add(self.start)
        count = 0
        if self.start.solved(self.goal):
            print(self.start.board)
            return 1
        while not q.empty():
            node = q.get()
            for p in node.puzzle.possible_moves():
                if p not in s:
                    n = Node(p, node.g + 1, node, self.goal)
                    s.add(n.puzzle)
                    q.put(n)
                    count += 1
                    if self.bestNode.h > node.h:
                        self.bestNode = node
                    if node.h == 0 or count > 200000:
                        self.buildPath()
                        return self.bestNode

    def buildPath(self):
        f = self.bestNode
        print("building")
        while f.back:
            f.back.next_ = f
            f = f.back
        self.bestNode = f


def printPuzzle(p):
    b = p.board
    for i in range(p.height):
        for j in range(p.width):
            print(b[i][j], end=' ')
            pass
        print("")
    print("")


def main():
    g = [[0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1],
         [2, 2, 2, 2, 2],
         [3, 3, 3, 3, 3],
         [4, 4, 4, 4, 4]]
    b = puzGen(g, 5, 5)
    then = time.time()
    p = Puzzle(5, 5, b, (4, 4))
    s = Solver(p, g)
    count = 0
    printPuzzle(p)
    q = s.solve()
    while q:
        printPuzzle(q.puzzle)
        q = q.next_
        count += 1
    now = time.time()
    print(count - 1)
    print(now - then)

if __name__ == '__main__':
    main()
