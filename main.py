import pygame
# import numpy as np
from AI import AI
from Color import Color
from Disk import Disk


class Game():
    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = 300, 400
        self.speed = [2, 2]
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.disk = Disk()
        self.ai = AI(self.disk.arr)
        self.skip = False
        self.x, self.y = 1, 1

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
        AIstatus = self.ai.getStatus()
        Dstatus = self.disk.getStatus()
        if Dstatus == 'movable':
            if AIstatus == 'finish':
                self.disk.chStatus('eliminate')
                pass
            elif AIstatus == 'ready':
                self.now = self.ai.start()
            elif AIstatus == 'moving':
                self.past = self.now
                self.now = self.ai.move()
                self.disk.switch(self.past, self.now)
        elif Dstatus == 'eliminate':
            self.disk.eliminate()
            pass
        elif Dstatus == 'filling':
            pass
        pass

    def rendering(self):
        for i in range(0, 5):
            for j in range(0, 6):
                color = Color.c[self.disk.arr[i][j]]
                pygame.draw.circle(self.screen, color,
                                   (j * 50 + 25, i * 50 + 175), 25, 1)
        pygame.display.flip()
        pass


def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
