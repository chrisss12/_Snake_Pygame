import pygame
from Constans_SNAKE_ import *



class  Rectangle():
    def __init__(self,win, color,pos, height, width):
        self.win = win
        self.color = color
        self.height = height
        self.width = width
        self.pos = pos
    def draw (self):
        pygame.draw.rect(self.win, self.color,pygame.Rect(self.pos[0],self.pos[1], self.height, self.width))



class Snake(Rectangle):
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.pos[0] -= CELL_SIZE

        if keys[pygame.K_UP]:
            self.pos[1] -= CELL_SIZE

        if keys[pygame.K_RIGHT]:
            self.pos[0] += CELL_SIZE

        if keys[pygame.K_DOWN]:
            self.pos[1] += CELL_SIZE

