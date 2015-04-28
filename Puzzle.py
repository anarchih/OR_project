from queue import PriorityQueue
from copy import deepcopy
GOAL_4X4 = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
GOAL_3X3 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


class Puzzle():
    def __init__(self, width, height, board):
        self.width = width
        self.height = height
        self.board = board
        self.str_ = str()
        self.pointer = self.findPointer()

    def solved(self):
        return self.board == GOAL_3X3

    def possible_moves(self):
        j, i = self.pointer
        if i > 0:
            b = deepcopy(self.board)
            b[i - 1][j], b[i][j] = self.board[i][j], self.board[i - 1][j]
            yield Puzzle(self.width, self.height, b)
        if i < self.width - 1:
            b = deepcopy(self.board)
            b[i + 1][j], b[i][j] = self.board[i][j], self.board[i + 1][j]
            yield Puzzle(self.width, self.height, b)
        if j > 0:
            b = deepcopy(self.board)
            b[i][j - 1], b[i][j] = self.board[i][j], self.board[i][j - 1]
            yield Puzzle(self.width, self.height, b)
        if j < self.height - 1:
            b = deepcopy(self.board)
            b[i][j + 1], b[i][j] = self.board[i][j], self.board[i][j + 1]
            yield Puzzle(self.width, self.height, b)

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
        return hash(str(self.board))


class Node():
    def __init__(self, puzzle, g, n):
        self.puzzle = puzzle
        self.solved = False
        self.h = self.H()
        self.g = g
        self.f = self.h + self.g
        self.back = n

    def H(self):
        p = self.puzzle
        t = 0
        for i in range(p.width):
            for j in range(p.height):
                a = int(p.board[i][j] / p.width)
                b = p.board[i][j] % p.width
                t = abs(a - j) + abs(b - i)
        return t * 10

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
    def __init__(self, start):
        self.start = start

    def solve(self):
        q = PriorityQueue()
        q.put(Node(self.start, 0, None))
        s = set()
        s.add(self.start)
        if self.start.solved():
            print(self.start.board)
            return 1
        while not q.empty():
            node = q.get()
            for p in node.puzzle.possible_moves():
                if p not in s:
                    n = Node(p, node.g + 1, node)
                    s.add(n.puzzle)
                    q.put(n)
                    if n.puzzle.solved():
                        return n


def main():
    b = [[9, 6, 2, 13],
         [8, 15, 7, 11],
         [12, 3, 4, 1],
         [10, 5, 0, 14]]
    b = [[5, 1, 6],
         [0, 3, 8],
         [4, 2, 7]]
    p = Puzzle(3, 3, b)
    s = Solver(p)
    count = 0
    q = s.solve()
    while q:
        print(q.puzzle.board)
        q = q.back
        count += 1
    print(count - 1)

if __name__ == '__main__':
    main()
