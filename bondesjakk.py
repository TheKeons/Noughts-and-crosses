import random
import os
import time


def startplayer():
    startPlayer = random.randint(1, 3)
    if startPlayer == 1:
        start = 'X'
        last = '0'
        print('Player X starts the game')
    
    else:
        start = '0'
        last = 'X'
        print('Player 0 starts the game')

    return start, last


def drawboard(board):
    for i in range(len(board)):
        if i != 0:
            print('--------')
        for j in range(len(board[0])):
            if j != 0:
                print('|', end='')
            if j == 2:
                print(board[i][j])
            else:
                print(board[i][j] + ' ', end='')


def clear():
    os.system('cls' if os.name == 'nt' else clear())


def turns(start, last, board, lastplayed):
    if lastplayed != None:
        start = lastplayed
        last = last

    clear()
    drawboard(board)
    pos0 = int(input('Where do you want to place vertical?'))
    pos1 = int(input('Where do you want to place Horisontal?'))

    if board[pos0-1][pos1-1] == ' ':
        board[pos0-1][pos1-1] = start

    else:
        print('There is already something there. Try again')
        time.sleep(2)
        return start

    clear()
    drawboard(board)

    pos0 = int(input('Where do you want to place vertical?'))
    pos1 = int(input('Where do you want to place Horisontal?'))

    if board[pos0-1][pos1-1] == ' ':
        board[pos0-1][pos1-1] = last
        
    else:
        print('There is already something there. Try again')
        time.sleep(2)
        return last

    clear()
    drawboard(board)

    return None


def main():
    won = False
    board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
    clear()
    start, last = startplayer()
    time.sleep(2)

    lastplayed = None

    while won == False:  
        if ' ' not in [val for sublist in board for val in sublist]:
            break

        lastplayed = turns(start, last, board, lastplayed)

    
        if ' ' not in [val for sublist in board for val in sublist]:
            break
                    
        turns(start, last, board, lastplayed)

if __name__ == '__main__':
    main()
