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

    
    def is_illegal(self, xaxis, yaxis):
        if xaxis < 1 or xaxis > 3 or yaxis < 1 or yaxis > 3:
            return True

        if self.board[xaxis - 1][yaxis - 1] != ' ':
            return True

        return False


    def winner(self):
        for i in range(len(self.board)):
            match i:

                case ['X', 'X', 'X']:
                    print('X has won the game')
                    return True

                case ['0', '0', '0']:
                    print('0 has won the game')
                    return True
            
            if [item[i] for item in self.board] == ['0', '0', '0']:
                print('0 has won the game')
                return True

            elif [item[i] for item in self.board] == ['X', 'X', 'X']:
                print('X has won the game')
                return True

            if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
                print(f'{self.board[0][0]} won the game')
                return True

        return False


    def is_full(self):
        if ' ' not in [val for sublist in self.board for val in sublist]:
            return True


    def promt(self):
        print(f'Player {self.first}')
        y = int(input('Where do you want to place Horisontal? '))
        x = int(input('Where do you want to place vertical? '))
        
        if self.is_illegal(x, y):
            print('That move is illegal. Try again')
            time.sleep(2)
            x, y = self.promt()
        
        return x, y


    def play_game(self):
        clear()

        if self.winner():
            return False

        if self.is_full():
            print('Board is full. game lost')
            time.sleep(2)
            return False

        x, y = self.promt()
        self.board[x - 1][y - 1] = self.first
        self.show_board()
        time.sleep(2)
        self.first, self.last = self.last, self.first

        return True


def clear():
    os.system('cls' if os.name == 'nt' else clear())

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
    ]

start = random.choice(['X', '0'])
match start:
    case 'X':
        last = '0'
    case '0':
        last = 'X'

game = Game(start, last, board)
clear()
print(f'{game.first} starts the game')
input('Press enter to start')

while game.play_game():
    print('smt')

