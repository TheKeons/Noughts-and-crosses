from matplotlib.pyplot import draw
import pygame
import sys

pygame.init()

HEIGHT = 629
WIDTH = 629

#pygame.time.Clock.get_fps

screen = pygame.display.set_mode((HEIGHT, WIDTH))
grid = pygame.image.load('Noughts and crosses\snake\grid.png')
grid_list = [[0 for _ in range(20)] for _ in range(20)]
grid_list[2][10] = 't'
grid_list[3][10] = 'b'
grid_list[4][10] = 'b'
grid_list[5][10] = 'h'

class Board:
    def __init__(self, grid_board) -> None:
        self.grid_board = grid_board

    def draw_board(self):
        screen.blit(grid, (0, 0))


class Snake:
    def __init__(self) -> None:
        self.head = pygame.image.load('Noughts and crosses\snake\head.png')
        self.body = pygame.image.load('Noughts and crosses\snake\Body.png')
        self.tail = pygame.image.load('Noughts and crosses\snake\Tail.png')

    def draw_snake(self):
        for i in range(len(game.grid_board)):
            for j in range(len(game.grid_board[0])):
                match game.grid_board[i][j]:
                    case 't':
                        self.draw_tail(i, j)

                    case 'b':
                        self.draw_body(i, j)

                    case 'h':
                        self.draw_head(i, j)

    def draw_tail(self, x, y):
        screen.blit(self.tail, (31.45 * x, 31.45 * y))

    def draw_body(self, x, y):
        screen.blit(self.body, (31.45 * x, 31.45 * y))

    def draw_head(self, x, y):
        screen.blit(self.head, (31.45 * x, 31.45 * y))

    def move_snake(self, direction):
        match direction:
            case 'left':
                rotate_img_left(self.head)
                game.draw_board()
                self.draw_snake()
                pygame.display.update()
                print('t')


def rotate_img_right(img):
    return pygame.transform.rotate(img, -90)


def rotate_img_left(img):
    return pygame.transform.rotate(img, 90)

game = Board(grid_list)
snek = Snake()
direction = None
game.draw_board()
snek.draw_snake()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_UP:
                    direction = 'up'
                case pygame.K_DOWN:
                    direction = 'down'
                case pygame.K_LEFT:
                    direction = 'left'
                case pygame.K_RIGHT:
                    direction = 'right'
                case pygame.K_w:
                    direction = 'up'
                case pygame.K_s:
                    direction = 'down'
                case pygame.K_a:
                    direction = 'left'
                case pygame.K_d:
                    direction = 'right'

    snek.move_snake(direction)
    pygame.display.update()
    direction = None
