import pygame
from rectangle import Rectangle,Snake
from Constans_SNAKE_ import *




clock = pygame.time.Clock()



pygame.init()
# definiowanie okna gry
win = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('My game')

snake = Snake(win, COLOR_B,[WIDTH_CENTER,HEIGHT_CENTER],CELL_SIZE, CELL_SIZE)
apple = Rectangle(win, COLOR_R,(RAND_A, RAND_B) ,CELL_SIZE, CELL_SIZE)

run = True
# pętla główna
while run:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    snake.move()

    for x in range(0,WIDTH,CELL_SIZE):
        for y in range(0,HEIGHT,CELL_SIZE):
            pygame.draw.rect(win, COLOR_B, pygame.Rect(x, y, CELL_SIZE, CELL_SIZE), width=1)


    while RAND_A == HEIGHT_CENTER and RAND_B == WIDTH_CENTER:
        print(RAND_A)
        print(RAND_B)
        print("sanake_")
        RAND_A = random.randrange(0, WIDTH, CELL_SIZE)
        RAND_B = random.randrange(0, WIDTH, CELL_SIZE)

    clock.tick(10)
    snake.draw()
    apple.draw()
    pygame.display.update()
    pygame.time.delay(50)
    win.fill(BLACK)