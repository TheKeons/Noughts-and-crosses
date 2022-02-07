import time
import os
import random


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
        if x_axis < 1 or x_axis > 3 or y_axis < 1 or y_axis > 3:
            return True

        if self.board[x_axis - 1][y_axis - 1] != ' ':
            return True

        return False

    def winner(self):
        for i in range(len(self.board)):

            if self.board[i] == ['X', 'X', 'X']:
                print('X has won the game')
                return True

            elif self.board[i] == ['0', '0', '0']:
                print('0 has won the game')
                return True
        
            elif [item[i] for item in self.board] == ['0', '0', '0']:
                print('0 has won the game')
                return True

            elif [item[i] for item in self.board] == ['X', 'X', 'X']:
                print('X has won the game')
                return True

            elif self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
                print(f'{self.board[0][0]} won the game')
                return True

            elif self.board[2][0] == self.board[1][1] == self.board[0][2] != ' ':
                print(f'{self.board[2][0]} won the game')
                return True

        return False

    def is_full(self):
        if ' ' not in [val for sublist in self.board for val in sublist]:
            return True

    def prompt(self):
        print(f'Player {self.first}')
        y = int(input('Where do you want to place horisontal? '))
        x = int(input('Where do you want to place vertical? '))
        
        if self.is_illegal(x, y):
            print('That move is illegal. Try again')
            time.sleep(2)
            x, y = self.prompt()
        
        return x, y

    def play_game(self):
        clear()

        if self.winner():
            return False

        if self.is_full():
            print('Board is full. game lost')
            time.sleep(2)
            return False

        self.show_board()
        x, y = self.prompt()
        self.board[x - 1][y - 1] = self.first
        time.sleep(2)
        self.first, self.last = self.last, self.first

        return True


def clear():
    os.system('cls' if os.name == 'nt' else clear())


def main():
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
        ]

    start = random.choice(['X', '0'])

    if start == 'X':
        last = '0'
    elif '0':
        last = 'X'

    game = Game(start, last, board)
    clear()
    print(f'{game.first} starts the game')
    input('Press enter to start')

    while game.play_game():
        pass


if __name__ == '__main__':
    main()
