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
        # self.dir_2 = 'stop'

    def draw(self):
        pygame.draw.rect(self.win, self.color, pygame.Rect(self.pos[0], self.pos[1], self.height, self.width))

class Apple(Rectangle):
    def __init__(self,win):
        self.setpos()
        super().__init__(win, COLOR_R,self.pos)

    def setpos(self):
        self.pos = [random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)]


class Snake(Rectangle):

    no_direction = [0, 0]
    up_direction = [0, -1]
    down_direction = [0, 1]
    left_direction = [-1, 0]
    right_direction = [1, 0]


    def __init__(self,win,pos):
        self.segments = []
        super().__init__(win,COLOR_B,pos)
        self.segments.append(pos)
        print(self.segments)
        self.head = pos
        self.dir = Snake.no_direction




    def move(self):
        keys = pygame.key.get_pressed()


        if keys[pygame.K_LEFT]:
            self.dir = Snake.left_direction
        elif keys[pygame.K_UP]:
            self.dir = Snake.up_direction
        elif keys[pygame.K_RIGHT]:
            self.dir = Snake.right_direction
        elif keys[pygame.K_DOWN]:
            self.dir = Snake.down_direction

        self.head = self.head[0] + self.dir[0] * CELL_SIZE, self.head[1] + self.dir[1] * CELL_SIZE

        self.pos = self.head





