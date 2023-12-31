import pygame
from rectangle import Snake,Apple
from Constans_SNAKE_ import *

clock = pygame.time.Clock()

pygame.init()
# definiowanie okna gry
win = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('My game')

snake = Snake(win,[WIDTH_CENTER,HEIGHT_CENTER])
apple = Apple(win)

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    snake.move()

    if snake.head[0] < LEFT_EDGE or snake.head[0] > RIGHT_EDGE or snake.head [1] < TOP_EDGE or snake.head[1] > BOTTOM_EDGE:
        break

    for x in range(0,WIDTH,CELL_SIZE):
        for y in range(0,HEIGHT,CELL_SIZE):
            pygame.draw.rect(win, COLOR_B, pygame.Rect(x, y, CELL_SIZE, CELL_SIZE), width=1)


    while RAND_A == WIDTH_CENTER  and RAND_B == HEIGHT_CENTER :
        RAND_A = random.randrange(0, WIDTH, CELL_SIZE)
        RAND_B = random.randrange(0, HEIGHT, CELL_SIZE)

    if snake.pos[0] == apple.pos[0] and snake.pos[1] == apple.pos[1]:
        apple.setpos()

       
    clock.tick(7)
    snake.draw()
    apple.draw()
    pygame.display.update()
    pygame.time.delay(50)
    win.fill(BLACK)