import pygame
from rectangle import Snake,Apple
from Constans_SNAKE_ import *

clock = pygame.time.Clock()

pygame.init()
# definiowanie okna gry
win = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('My game')

snake = Snake(win, COLOR_B,[WIDTH_CENTER,HEIGHT_CENTER])
apple = Apple(win)

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    snake.move()

    for x in range(0,WIDTH,CELL_SIZE):
        for y in range(0,HEIGHT,CELL_SIZE):
            pygame.draw.rect(win, COLOR_B, pygame.Rect(x, y, CELL_SIZE, CELL_SIZE), width=1)


    while RAND_A == WIDTH_CENTER  and RAND_B == HEIGHT_CENTER :
        RAND_A = random.randrange(0, WIDTH, CELL_SIZE)
        RAND_B = random.randrange(0, HEIGHT, CELL_SIZE)

    snake.body = []

    if snake.pos[0] == apple.pos[0] and snake.pos[1] == apple.pos[1]:
        apple.setpos()
        snake.width += CELL_SIZE
        # new_segment = Rectangle(win, COLOR_B,snake.pos,CELL_SIZE, CELL_SIZE)
        # snake.body.append(new_segment)

    clock.tick(10)
    snake.draw()
    apple.draw()
    pygame.display.update()
    pygame.time.delay(50)
    win.fill(BLACK)