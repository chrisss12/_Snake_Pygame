import random



CELL_SIZE =40
BLACK = (0,0,0)
HEIGHT = 800
WIDTH = 800
COLOR_B = (250,250,250)
COLOR_R = (255,0,0)
COLOR_BLUE = (0, 255, 255)
RAND_A = random.randrange( 0,WIDTH,CELL_SIZE)
RAND_B = random.randrange( 0,WIDTH,CELL_SIZE)
WIDTH_CENTER = (WIDTH//CELL_SIZE)//2*CELL_SIZE
HEIGHT_CENTER = (HEIGHT//CELL_SIZE)//2*CELL_SIZE
LEFT_EDGE = 0
RIGHT_EDGE = WIDTH
TOP_EDGE = 0
BOTTOM_EDGE = HEIGHT
