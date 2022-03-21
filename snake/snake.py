import pygame
import sys

pygame.init()

HEIGHT = 629
WIDTH = 629

screen = pygame.display.set_mode((HEIGHT, WIDTH))
grid = pygame.image.load('Noughts and crosses\snake\grid.png')
grid_list = [[0 for _ in range(20)] for _ in range(20)]

class Board:
    def __init__(self, grid_board) -> None:
        self.grid_board = grid_board

    def draw_board(self):
        screen.blit(grid, (0, 0))

class Snake:
    def __init__(self) -> None:
        self.head_up = pygame.image.load('Noughts and crosses\snake\headUp.png')
        self.head_right = pygame.image.load('Noughts and crosses\snake\headRight.png')
        self.head_down = pygame.image.load('Noughts and crosses\snake\headDown.png')
        self.head_left = pygame.image.load('Noughts and crosses\snake\headLeft.png')
        self.body = pygame.image.load('Noughts and crosses\snake\Body.png')
        self.tail = pygame.image.load('Noughts and crosses\snake\Tail.png')

    def start_pos(self):
        screen.blit(self.head_right, (157.5, 315))
        screen.blit(self.body, (126, 315))
        screen.blit(self.body, (94.5, 315))
        screen.blit(self.tail, (63, 315))

game = Board(grid_list)
snek = Snake()

while True:
    game.draw_board()
    snek.start_pos()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()