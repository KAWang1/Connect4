import numpy as np


def create_board():
    board = np.zeros((6, 7))
    return board


# initialize board
board = create_board()
# We will initialize the game_over as False.
game_over = False
turn = 0

while not game_over:
    # Ask for player 1 input
    if turn == 0:
        selection = int(input("Player 1, Make your Selection(0-6):"))

    # Ask for player 2 input
    else:
        selection = int(input("Player 2, Make your Selection(0-6):"))

    turn += 1
    turn = turn % 2


def win():
    if board[0][0] == 0:
        print(board[0][0])
        print("this works")


"""
1 player 1 piece
2 player 2 piece

[0-5][0-6]

horiz
board[X][Y]
count = 0

for (int Y = 6; Y>=0; Y--)
if count == 4
    if board[curX][curY] = 1
        player 1 win
        break
    else
        player2 win
        break
        
if board[curX][Y] = 1board[curX][Y-1]
    count ++


vert
board[][]

diag
board[][]


"""