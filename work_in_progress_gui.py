import pygame
import sys
import random

pygame.font.init()

font = pygame.font.SysFont('Times New Roman', 30)
width = 600
height = 600
black = (0, 0, 0)
background = (28, 170, 156)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Noughts and crosses')
screen.fill(background)

grid = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']]


class Game:
    def __init__(self, first, last, board):
        self.first = first
        self.last = last
        self.board = board

    def show_board(self):
        for i in range(len(self.board)):
            if i != 0:
                print('--------')
            for j in range(len(self.board[0])):
                if j != 0:
                    print('|', end='')
                if j == 2:
                    print(self.board[i][j])
                else:
                    print(self.board[i][j] + ' ', end='')

    def is_illegal(self, x_axis, y_axis):
        if x_axis < 0 or x_axis > 2 or y_axis < 0 or y_axis > 2:
            return True

        if self.board[x_axis][y_axis] != ' ':
            return True

        return False

    def winner(self):
        for i in range(len(self.board)):

            if self.board[i] == ['X', 'X', 'X']:
                return 'X'

            elif self.board[i] == ['0', '0', '0']:
                return '0'

            elif [item[i] for item in self.board] == ['0', '0', '0']:
                return '0'

            elif [item[i] for item in self.board] == ['X', 'X', 'X']:
                return 'X'

            elif self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
                return self.board[0][0]

            elif self.board[2][0] == self.board[1][1] == self.board[0][2] != ' ':
                return self.board[2][0]

        return False

    def is_full(self):
        if ' ' not in [val for sublist in self.board for val in sublist]:
            return True

    def play(self, row, col):
        if self.is_illegal(row, col):
            return

        self.board[row][col] = self.first
        self.draw_figures()
        self.first, self.last = self.last, self.first

        if self.is_full():
            screen.fill(background)
            textsurface = font.render('Board is full. Game is lost :(', False, (0, 0, 0))
            screen.blit(textsurface, (140, 270))
            return False

        match self.winner():
            case 'X':
                screen.fill(background)
                textsurface = font.render('X has won the game', False, (0, 0, 0))
                screen.blit(textsurface, (170, 270))

            case '0':
                screen.fill(background)
                textsurface = font.render('O has won the game', False, (0, 0, 0))
                screen.blit(textsurface, (170, 270))

            case False:
                pass

        return True


def draw_figures(self):
    for row in range(3):
        for col in range(3):
            if grid[row][col] == '0':
                pygame.draw.circle(screen, (255, 255, 255), (int(col * 200 + 200 // 2), int(row * 200 + 200 // 2)),
                                   60, 15)

            elif grid[row][col] == 'X':
                pygame.draw.line(screen, (0, 0, 0), (col * 200 + 55, row * 200 + 200 - 55), (col * 200 + 200 - 55,
                                                                                             row * 200 + 55), 15)
                pygame.draw.line(screen, (0, 0, 0), (col * 200 + 55, row * 200 + 55), (col * 200 + 200 - 55,
                                                                                       row * 200 + 200 - 55), 15)


def draw_lines():
    pygame.draw.line(screen, black, (200, 0), (200, 600), 5)
    pygame.draw.line(screen, black, (400, 0), (400, 600), 5)
    pygame.draw.line(screen, black, (0, 200), (600, 200), 5)
    pygame.draw.line(screen, black, (0, 400), (600, 400), 5)


def main():
    start = random.choice(['X', '0'])

    if start == 'X':
        last = '0'
    elif '0':
        last = 'X'

    game = Game(start, last, grid)
    draw_lines()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]

                col = x // 200
                row = y // 200

                if not game.play(row, col):
                    break

        pygame.display.update()


if __name__ == '__main__':
    main()
