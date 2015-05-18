import pygame
# import numpy as np
from Color import Color
from Puzzle import Solver, printPuzzle, Puzzle
from puzzleGenerator import puzGen
from time import sleep


class UI():
    def __init__(self, wNum, hNum, node):
        pygame.init()
        self.size = self.width, self.height = 300, 400
        self.wNum, self.hNum = wNum, hNum
        self.speed = [2, 2]
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.node = node
        self.skip = False
        self.x, self.y = 1, 1
        self.firstIn = True

    def run(self):
        while 1:
            self.eventHandler()
            self.update()
            self.rendering()

    def eventHandler(self):
        next_ = True
        while next_ and not self.skip:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.skip = True
                if event.type == pygame.MOUSEBUTTONUP:
                    next_ = False
                    # next_ = self.ai.step()
        pass

    def update(self):
        if self.skip:
            sleep(0.05)
        if self.firstIn:
            self.firstIn = False
        elif self.node.next_:
            self.node = self.node.next_

    def rendering(self):
        b = self.node.puzzle.board
        p = self.node.puzzle.pointer
        for i in range(0, self.hNum):
            for j in range(0, self.wNum):
                color = Color.c[b[i][j]]
                pygame.draw.circle(self.screen, color,
                                   (j * 51 + 23, i * 51 + 173), 25, )
        pygame.draw.circle(self.screen, (255, 255, 255),
                           (p[0] * 51 + 23, p[1] * 51 + 173), 25, 3)
        pygame.display.flip()
        pass


def main():
    g = [[0, 1, 2, 3, 4],
         [0, 1, 2, 3, 4],
         [0, 1, 2, 3, 4],
         [0, 1, 2, 3, 4],
         [0, 1, 2, 3, 4]]
    b = puzGen(g, 5, 5)
    # then = time.time()
    p = Puzzle(5, 5, b, (4, 4))
    s = Solver(p, g)
    printPuzzle(p)
    q = s.solve()
    width = 5
    height = 5
    ui = UI(width, height, q)
    ui.run()


if __name__ == '__main__':
    main()
