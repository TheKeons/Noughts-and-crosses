import pygame
import sys

pygame.init()

HEIGHT = 629
WIDTH = 629

screen = pygame.display.set_mode((HEIGHT, WIDTH))
grid = pygame.image.load(r'C:\Users\katie\OneDrive\Dokumenter\GitHub\Noughts and crosses\snake\grid.png')
grid_list = [[0 for _ in range(20)] for _ in range(20)]

class Board:
    def __init__(self, grid_board) -> None:
        self.grid_board = grid_board

    def draw_board(self):
        screen.blit(grid, (0, 0))

class Snake:
    def __init__(self) -> None:
        pass

game = Board(grid_list)

while True:
    game.draw_board()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()