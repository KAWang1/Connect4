import numpy as np

# Constant Row and Column length
from client import send

ROW_COUNT = 6
COL_COUNT = 7


def create_board():
    board = np.zeros((6, 7))
    return board


# Places piece on selected row/col
def play_piece(board, row, col, piece):
    board[row][col] = piece


# Checks to see if column is full
def is_valid(board, col):
    return board[5][col] == 0


# Gets next available row
def next_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


# Checks to see if the board is full
def board_full():
    if(board[5][0] == 0
            and board[5][1] == 0
            and board[5][2] == 0
            and board[5][3] == 0
            and board[5][4] == 0
            and board[5][5] == 0
            and board[5][6] == 0):
        return False
    else:
        return True


def print_board(board):
    print(np.flip(board, 0))


def win(board, piece):

    # Checks horizontal win conditions
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT):
            if (board[r][c] == piece
                    and board[r][c + 1] == piece
                    and board[r][c + 2] == piece
                    and board[r][c + 3] == piece):
                return True

    # Checks vertical win conditions
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT - 3):
            if (board[r][c] == piece
                    and board[r + 1][c] == piece
                    and board[r + 2][c] == piece
                    and board[r + 3][c] == piece):
                return True

    # Checks right diagonal win conditions
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if (board[r][c] == piece
                    and board[r + 1][c + 1] == piece
                    and board[r + 2][c + 2] == piece
                    and board[r + 3][c + 3] == piece):
                return True

    # Checks left diagonal win conditions
    for c in range(COL_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if (board[r][c] == piece
                    and board[r - 1][c + 1] == piece
                    and board[r - 2][c + 2] == piece
                    and board[r - 3][c + 3] == piece):
                return True


board = create_board()
game_over = False
turn = 0


selection = int(input("CONNECT 4\n1)Player vs Player\n2)Player vs AI\n3)Online\n4)Exit\n"))
# Player vs Player
if selection == 1:
    print("  0  1  2  3  4  5  6")
    print_board(board)
    while not game_over:
        # Ask for player 1 input
        if turn == 0:
            col = int(input("Player 1: Select Column(0-6):"))
            # Player 1 will drop a piece on the board
            if is_valid(board, col):
                row = next_row(board, col)
                play_piece(board, row, col, 1)
                if win(board, 1):
                    print("Player 1 Wins")
                    game_over = True
            else:
                if board_full():
                    print("Tie")
                    game_over = True
                else:
                    print("Move not valid")
                    turn += 1
                    turn = turn % 2
        # Ask for player 2 input
        else:
            col = int(input("Player 2: Select Column(0-6):"))
            # Player 2 will drop a piece on the board
            if is_valid(board, col):
                row = next_row(board, col)
                play_piece(board, row, col, 2)
                if win(board, 2):
                    print("Player 2 Wins")
                    game_over = True
            else:
                if board_full():
                    print("Tie")
                    game_over = True
                else:
                    print("Move not valid")
                    turn += 1
                    turn = turn % 2

        print("  0  1  2  3  4  5  6")
        print_board(board)

        turn += 1
        turn = turn % 2

# Player vs AI
if selection == 2:
    # ADD AI CODE------------------------------------------------------------------
    print("  0  1  2  3  4  5  6")
    print_board(board)
    while not game_over:
        # Ask for player 1 input
        if turn == 0:
            col = int(input("Player 1: Select Column(0-6):"))
            # Player 1 will drop a piece on the board
            if is_valid(board, col):
                row = next_row(board, col)
                play_piece(board, row, col, 1)
                if win(board, 1):
                    print("Player 1 Wins")
                    game_over = True
            else:
                if board_full():
                    print("Tie")
                    game_over = True
                else:
                    print("Move not valid")
                    turn += 1
                    turn = turn % 2
        # Ask for player 2 input
        else:
            col = int(input("Player 2: Select Column(0-6):"))
            # Player 2 will drop a piece on the board
            if is_valid(board, col):
                row = next_row(board, col)
                play_piece(board, row, col, 2)
                if win(board, 2):
                    print("Player 2 Wins")
                    game_over = True
            else:
                if board_full():
                    print("Tie")
                    game_over = True
                else:
                    print("Move not valid")
                    turn += 1
                    turn = turn % 2

        print("  0  1  2  3  4  5  6")
        print_board(board)

        turn += 1
        turn = turn % 2

# Online
if selection == 3:
    print("  0  1  2  3  4  5  6")
    print_board(board)
    while not game_over:
        # Ask for player 1 input
        if turn == 0:
            col = int(input("Player 1: Select Column(0-6):"))
            message = f"1,{col}"
            send(message)
            # Player 1 will drop a piece on the board
            if is_valid(board, col):
                row = next_row(board, col)
                play_piece(board, row, col, 1)
                if win(board, 1):
                    print("Player 1 Wins")
                    game_over = True
            else:
                if board_full():
                    print("Tie")
                    game_over = True
                else:
                    print("Move not valid")
                    turn += 1
                    turn = turn % 2
        # Ask for player 2 input
        else:
            col = int(input("Player 2: Select Column(0-6):"))
            # Player 2 will drop a piece on the board
            if is_valid(board, col):
                row = next_row(board, col)
                play_piece(board, row, col, 2)
                if win(board, 2):
                    print("Player 2 Wins")
                    game_over = True
            else:
                if board_full():
                    print("Tie")
                    game_over = True
                else:
                    print("Move not valid")
                    turn += 1
                    turn = turn % 2

        print("  0  1  2  3  4  5  6")
        print_board(board)

        turn += 1
        turn = turn % 2
else:
    game_over = True
