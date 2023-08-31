import selectors

import pygame
from Constans_SNAKE_ import *


class Rectangle():
    def __init__(self, win, color, pos):
        self.win = win
        self.color = color
        self.height = CELL_SIZE
        self.width = CELL_SIZE
        self.pos = pos
        self.dir_2 = 'stop'

    def draw(self):
        pygame.draw.rect(self.win, self.color, pygame.Rect(self.pos[0], self.pos[1], self.height, self.width))

class Apple(Rectangle):
    def __init__(self,win):
        self.setpos()
        super().__init__(win, COLOR_R,self.pos)

    def setpos(self):
        self.pos = [random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)]


class Snake(Rectangle,segments):
    def __init__(self):
        super().__init__(win,COLOR_B,)
    self.segments = segments

    def move(self):
        keys = pygame.key.get_pressed()

        dir = ['up', 'down', 'left', 'right', 'stop']

        if keys[pygame.K_LEFT]:
            self.dir_2 = dir[2]
        elif keys[pygame.K_UP]:
            self.dir_2 = dir[0]

        elif keys[pygame.K_RIGHT]:
            self.dir_2 = dir[3]

        elif keys[pygame.K_DOWN]:
            self.dir_2 = dir[1]

        if self.dir_2 == dir[2]:
            self.pos[0] -= CELL_SIZE

        elif self.dir_2 == dir[3]:
            self.pos[0] += CELL_SIZE

        elif self.dir_2 == dir[0]:
            self.pos[1] -= CELL_SIZE

        elif self.dir_2 == dir[1]:
            self.pos[1] += CELL_SIZE
        else:
            pass




