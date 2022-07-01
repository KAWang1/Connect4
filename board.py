import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((6, 7))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    # if this condition is true we will let the use drop piece here.
    # if not true that means the col is not vacant
    return board[5][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                return True

board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over:
    # Ask for player 1 input
    if turn == 0:
        col = int(input("Player 1, Make your Selection(0-6):"))
        # Player 1 will drop a piece on the board
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
            if winning_move(board, 1):
                print("Player 1 Wins")
                game_over = True

    # Ask for player 2 input
    else:
        col = int(input("Player 2, Make your Selection(0-6):"))
        # Player 2 will drop a piece on the board
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
            if winning_move(board, 2):
                print("Player 2 Wins")
                game_over = True

    print_board(board)

    turn += 1
    turn = turn % 2



# def horizwin():
#     if board[0][0] == 0:
#         print(board[0][0])
#         print("this works")


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

