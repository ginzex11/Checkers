import pygame

# board specs
BOARD_WIDTH, BOARD_HEIGHT = 800, 800
NUM_OF_ROWS, NUM_OF_COLS = 8, 8
SQUARE_SIZE = BOARD_WIDTH // NUM_OF_COLS
BLANK = 0

# coloring
RED = (200, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 200)
GREY = (128, 128, 128)

# images
CROWN = pygame.transform.scale(
    pygame.image.load('assets/crown.png'), (25, 15))
