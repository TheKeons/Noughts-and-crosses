import pygame
import sys
import random
import time


pygame.font.init()

font = pygame.font.SysFont('Times New Roman', 30)
width = 600
height = 600
black = (14, 58, 83)
lines = (14, 58, 83)
square_size = 200
white = (255, 255, 255)
background = (162,228,184)
button = [230, 360, 140, 40]


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Noughts and crosses')
screen.fill(background)

grid = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']]


class Game:
    def __init__(self, first, last, won, board):
        self.first = first
        self.last = last
        self.board = board
        self.won = won

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

    def play(self, x, y):
        col = x // square_size
        row = y // square_size

        if self.won:
            return False

        if self.is_illegal(row, col):
            return True

        self.board[row][col] = self.first
        self.draw_figures()
        pygame.display.update()
        self.first, self.last = self.last, self.first

        if self.winner():
            time.sleep(1)
            screen.fill(background)
            text_surface = font.render(f'{"Noughts" if self.winner() == "0" else "Crosses"} has won the game', False, lines)
            text_rect = text_surface.get_rect(center=(width/2, height/2))
            screen.blit(text_surface, text_rect)
            self.won = True
            return False

        if self.is_full():
            time.sleep(1)
            screen.fill(background)
            text_surface = font.render('Board is full. Game is lost :(', False, lines)
            
            text_rect = text_surface.get_rect(center=(width/2, height/2))
            screen.blit(text_surface, text_rect)
            self.won = True
            return False

        return True


    def draw_figures(self):
        for row in range(3):
            for col in range(3):

                if self.board[row][col] == '0':
                    pygame.draw.circle(screen, white, (int(col * square_size + square_size // 2),
                                            int(row * square_size + square_size // 2)), 60, 15)

                elif self.board[row][col] == 'X':
                    pygame.draw.line(screen, black, (col * square_size + 55, row * square_size + square_size - 55),
                                            (col * square_size + square_size - 55,row * square_size + 55), 15)
                    pygame.draw.line(screen, black, (col * square_size + 55, row * square_size + 55),
                                            (col * square_size + square_size - 55, row * square_size + square_size - 55), 15)


def draw_lines():
    pygame.draw.line(screen, lines, (200, 0), (200, 600), 5)
    pygame.draw.line(screen, lines, (400, 0), (400, 600), 5)
    pygame.draw.line(screen, lines, (0, 200), (600, 200), 5)
    pygame.draw.line(screen, lines, (0, 400), (600, 400), 5)


def play_again(x, y):
    pygame.draw.rect(screen, lines, button)
    text_surface = font.render('Play Again', False, background)
    text_rect = text_surface.get_rect(center=(width/2, 380))
    screen.blit(text_surface, text_rect)
    if button[0] <= x <= button[0] + 140 and button[1] <= y <= button[1] + 40:    
        return True


def main():
    screen.fill(background)
    start = random.choice(['X', '0'])

    if start == 'X':
        last = '0'
    elif '0':
        last = 'X'

    game = Game(start, last, False, [
                            [' ', ' ', ' '],
                            [' ', ' ', ' '],
                            [' ', ' ', ' ']])
    draw_lines()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]

                if not game.play(x, y):
                    if play_again(x, y):     
                        main()
                    
        pygame.display.update()


if __name__ == '__main__':
    main()
