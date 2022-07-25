import random
import sys
import time
import numpy as np
import pygame
import math
from client import send, get_player_move, get_player_number, receive
# from title import selection
# Constant Row and Column length
ROW_COUNT = 6
COL_COUNT = 7
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


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


def draw_board(board):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (
            int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()


# Create board



# selection = int(input("CONNECT 4\n1)Player vs Player\n2)Player vs AI\n3)Online\n4)Exit\n"))
# selection = 0
# Player vs Player



SQUARESIZE = 100
# define width and height of board
width = COL_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE / 2 - 5)
screen = pygame.display.set_mode(size)

board = create_board()
# if selection == 1:
def selection1():

    game_over = False
    turn = 0
    # initialize pygame
    pygame.init()
    # define our screen size

    # Calling function draw_board again
    draw_board(board)
    pygame.display.update()
    myfont = pygame.font.SysFont("monospace", 75)

    print("  0  1  2  3  4  5  6")
    print_board(board)
    draw_board(board)
    pygame.display.update()
    while not game_over:

        # Ask for player 1 input
        # if turn == 0:
        #     col = int(input("Player 1: Select Column(0-6):"))
        #     if is_valid(board, col):  # If Valid, Player 1 will drop a piece on the board
        #         row = next_row(board, col)
        #         play_piece(board, row, col, 1)
        #         if win(board, 1):
        #             print("Player 1 Wins")
        #             game_over = True
        #     else:
        #         if board_full():
        #             print("Tie")
        #             game_over = True
        #         else:
        #             print("Move not valid")
        #             turn += 1
        #             turn = turn % 2
        # # Ask for player 2 input
        # else:
        #     col = int(input("Player 2: Select Column(0-6):"))
        #     if is_valid(board, col):  # If valid, Player 2 will drop a piece on the board
        #         row = next_row(board, col)
        #         play_piece(board, row, col, 2)
        #         if win(board, 2):
        #             print("Player 2 Wins")
        #             game_over = True
        #     else:
        #         if board_full():
        #             print("Tie")
        #             game_over = True
        #         else:
        #             print("Move not valid")
        #             turn += 1
        #             turn = turn % 2
        #
        # print("  0  1  2  3  4  5  6")
        # print_board(board)
        #
        # turn += 1
        # turn = turn % 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                col = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, RED, (col, int(SQUARESIZE / 2)), RADIUS)
                else:
                    pygame.draw.circle(screen, YELLOW, (col, int(SQUARESIZE / 2)), RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                # print(event.pos)
                # Ask for Player 1 Input
                if turn == 0:
                    col = event.pos[0]
                    col = int(math.floor(col / SQUARESIZE))

                    if is_valid(board, col):
                        row = next_row(board, col)
                        play_piece(board, row, col, 1)

                        if win(board, 1):
                            label = myfont.render("Player 1 wins!", 1, RED)
                            screen.blit(label, (40, 10))
                            game_over = True

                    else:
                        if board_full():
                            # print("Tie")
                            label = myfont.render("Tie!", 1, BLUE)
                            screen.blit(label, (40, 10))
                            game_over = True


                # Ask for Player 2 Input
                else:
                    col = event.pos[0]
                    col = int(math.floor(col / SQUARESIZE))

                    if is_valid(board, col):
                        row = next_row(board, col)
                        play_piece(board, row, col, 2)

                        if win(board, 2):
                            label = myfont.render("Player 2 wins!!", 1, YELLOW)
                            screen.blit(label, (40, 10))
                            game_over = True

                print_board(board)
                draw_board(board)

                turn += 1
                turn = turn % 2

                if game_over:
                    pygame.time.wait(3000)

# Player vs AI
# if selection == 2:
# ----------------------------------------------START AI CODE-----------------------------------------------------------
def selection2():
    game_over = False
    turn = 0
    # initialize pygame
    pygame.init()
    # define our screen size

    # Calling function draw_board again
    draw_board(board)
    pygame.display.update()
    myfont = pygame.font.SysFont("monospace", 75)
    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
                else:
                    pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                # print(event.pos)
                # Ask for Player 1 Input
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))

                    if is_valid(board, col):
                        row = next_row(board, col)
                        play_piece(board, row, col, 1)

                        if win(board, 1):
                            label = myfont.render("Player 1 wins", 1, RED)
                            screen.blit(label, (40, 10))
                            game_over = True

                    else:
                        if board_full():
                                # print("Tie")
                                label = myfont.render("Tie!", 1, BLUE)
                                screen.blit(label, (40, 10))
                                game_over = True



               # Ask for player 2 (AI)
                else:
                    col = random.randint(0,6)

                    if is_valid(board, col):
                        row = next_row(board, col)
                        play_piece(board, row, col, 2)
                        if win(board, 2):
                            label = myfont.render("Player 2 wins", 1, YELLOW)
                            screen.blit(label, (40,10))
                            game_over = True


                print_board(board)
                draw_board(board)

                turn += 1
                turn = turn % 2

                if game_over:
                    pygame.time.wait(3000)
                
# The Following is not part of the code, as I could not get it ready in time ----------------------------------------------------------------

#def score_position(board, piece):
 #   score = 0

    # Center Column
 #   center_array = [int(i) for i in list(board[:, COLUMN_COUNT // 2])]
 #   center_count = center_array.count(piece)
 #   score += center_count * 3

    # Horizontal
 #   for r in range(ROW_COUNT):
 #       row_array = [int(i) for i in list(board[r, :])]
 #       for c in range(COLUMN_COUNT - 3):
#            window = row_array[c:c + WINDOW_LENGTH];
 #           score += evaluate_window(window, piece);

    # Vertical
  #  for c in range(COLUMN_COUNT):
 #       col_array = [int(i) for i in list(board[:, c])]
   #     for r in range(ROW_COUNT - 3):
  #          window = col_array[r:r + WINDOW_LENGTH];
 #           score += evaluate_window(window, piece);

    # Positive slope diagonal
  #  for r in range(ROW_COUNT - 3):
    #    for c in range(COLUMN_COUNT - 3):
   #         window = [board[r + i][c + i] for i in range(WINDOW_LENGTH)]
  #          score += evaluate_window(window, piece)

    # Negative slope diagonal
 #   for r in range(ROW_COUNT - 3):
    #    for c in range(COLUMN_COUNT - 3):
   #         window = [board[r + 3 - i][c + i] for i in range(WINDOW_LENGTH)]
  #          score += evaluate_window(window, piece)

 #   return score


#def evaluate_window(window, piece):
   # score = 0
  #  opp_piece = PLAYER_PIECE
 #   if piece == PLAYER_PIECE:
#        opp_piece = AI_PIECE

    # If a window has a winning position, score it highly
  #  if window.count(piece) == 4:
 #       score += 100
   # elif window.count(piece) == 3 and window.count(EMPTY) == 1:
  #      score += 5
 #   elif window.count(piece) == 2 and window.count(EMPTY) == 2:
   #     score += 2

    # Avoid situations where opponent is close to winning
   # if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
  #      score -= 4

 #   return score


#def get_valid_locations(board):
 #   valid_locations = []
#    for col in range(COLUMN_COUNT):
  #      if is_valid_location(board, col):
 #           valid_locations.append(col)
#    return valid_locations


#def is_terminal_node(board):
 #   return winning_move(board, PLAYER_PIECE) \
  #         or winning_move(board, AI_PIECE) \
 #          or len(get_valid_locations(board)) == 0


#def minimax(board, depth, alpha, beta, maximizingPlayer):
 #   valid_locations = get_valid_locations(board)
#    is_terminal = is_terminal_node(board)  # For determining if current state is terminal

    # On end of search depth or winning board


  #  if depth == 0 or is_terminal():
   #     if is_terminal:
     #       if winning_move(board, PLAYER_PIECE):
    #            return (None, 1e10)
     #       elif winning_move(board, PLAYER_PIECE):
    #            return (None, -1e10)
    #        else:  # game over, and there are no valid moves
   #             return (None, 0)
  #      else:  # Depth is zero
 #           return (None, score_position(board, AI_PIECE))

    # max step
  #  if maximizingPlayer:
 #       value = -math.inf
#        column = random.choice(valid_locations)

    # Branching each possible move
     #   for col in valid_locations:
    #        row = get_next_open_row(board, col)
            # Copy board here
   #         b_copy = board.copy()
  #          drop_piece(b_copy, row, col, AI_PIECE)

        # extend score to new board with piece
 #           new_score = minimax(b_copy, depth - 1, alpha, beta, False)[1]

        # chose move with highest score
      #      if new_score > value:
     #           value = new_score
    #            column = col

   #         alpha = max(alpha, value)
  #          if alpha >= beta:
 #               break;
#        return column, value

# Minimum step
   # else:
     #   value = math.inf;
    #    column = random.choice(valid_locations);
   #     for col in valid_locations:
    #        row = get_next_open_row(board, col)
   #         b_copy = board.copy()
      #      drop_piece(b_copy, row, col, PLAYER_PIECE)
     #       new_score = minimax(b_copy, depth - 1, alpha, beta, True)[1]
    #        if new_score < value:
   #             value = new_score
     #           column = col
    #            beta = min(beta, value)
   #             if alpha >= beta:
  #                  break
 #       return column, value


#board = create_board()
#print_board(board)
#game_over = False
#turn = 0

# initalize pygame
#pygame.init()

# define our screen size
#SQUARESIZE = 100

# define width and height of board
#width = COLUMN_COUNT * SQUARESIZE
#height = (ROW_COUNT + 1) * SQUARESIZE

#size = (width, height)

#RADIUS = int(SQUARESIZE / 2 - 5)

#screen = pygame.display.set_mode(size)
# Calling function draw_board again
#draw_board(board)
#pygame.display.update()

#myfont = pygame.font.SysFont("monospace", 75)

#while not game_over:

   # for event in pygame.event.get():
      #  if event.type == pygame.QUIT:
     #       sys.exit()

     #   if event.type == pygame.MOUSEMOTION:
      #      pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
     #       posx = event.pos[0]
    #        if turn == 0:
   #             pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
  #          else:
 #               pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
#
#            pygame.display.update()

    #    if event.type == pygame.MOUSEBUTTONDOWN:
   #         pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            # print(event.pos)

            # Ask for Player 1 Input
    #        if turn == 0:
   #             posx = event.pos[0]
  #              col = int(math.floor(posx / SQUARESIZE))

      #          if is_valid_location(board, col):
     #               row = get_next_open_row(board, col)
    #                drop_piece(board, row, col, 1)

   #                 if winning_move(board, 1):
  #                      label = myfont.render("Player 1 wins!!", 1, RED)
 #                       screen.blit(label, (40, 10))
#                        game_over = True

         #   elif turn == 1:
         #       if Gamemode == "AIEasy":
                # Random move for Player 2
        #            col = random.randint(0,6)

       #             if is_valid_location(board, col):
      #                  row = get_next_open_row(board, col)
     #                   drop_piece(board, row, col, 2)

    #                    if winning_move(board, 2):
   #                         label = myfont.render("Player 2 wins!!", 1, YELLOW)
  #                          screen.blit(label, (40, 10))
 #                           game_over = True



        #        elif Gamemode == "AIHard":
       #             if turn == 1 and not game_over:  # asking for Player 2

                  #      col, minimax_score = minimax(board, depth=5, alpha=-math.inf, beta=math.inf, maximizingPlayer=True)
                 #       if is_valid_location(board, col):
                #            get_next_open_row(board, col)
               #             drop_piece(board, row, col, AI_PIECE)

              #              if winning_move(board, AI_PIECE):
             #                   label = myfont.render("Player 2 is wins, 1, YELLOW");
            #                    screen.blit(label, (40, 10))
           #                     game_over = True;


          #      else:
                    # Ask for Player 2 Input
         #           posx = event.pos[0];
        #            col = int(math.floor(posx / SQUARESIZE));

        #            if is_valid_location(board, col):
       #                 row = get_next_open_row(board, col);
      #                  drop_piece(board, row, col, 2);

      #                  if winning_move(board, 2):
     #                       label = myfont.render("Player 2 wins!!", 1, YELLOW);
    #                        screen.blit(label, (40, 10));
   #                         game_over = True;

   # print_board(board);
  #  draw_board(board);

    #turn += 1;
   # turn = turn % 2;

  #  if game_over:
 #       pygame.time.wait(3000)

# ----------------------------------------------END AI CODE-----------------------------------------------------------

# Online
# if selection == 3:
def selection3():
    game_over = False
    turn = 0
    # initialize pygame
    pygame.init()
    # define our screen size

    # Calling function draw_board again
    draw_board(board)
    pygame.display.update()
    myfont = pygame.font.SysFont("monospace", 75)

    # player_num = int(input("1) Player 1\n2) Player 2\n"))
# Player 1
#     if player_num == 1:
    print("  0  1  2  3  4  5  6")
    print_board(board)
    draw_board(board)
    pygame.display.update()
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                col = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, RED, (col, int(SQUARESIZE / 2)), RADIUS)
                else:
                    pygame.draw.circle(screen, BLACK, (col, int(SQUARESIZE / 2)), RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN or turn == 1:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                if turn == 0:
                    # col = int(input("Player 1: Select Column(0-6):"))  # Ask for player 1 input
                    col = event.pos[0]
                    col = int(math.floor(col / SQUARESIZE))
                    message = f"1,{col}"
                    send(message)
                    receive()
                    if is_valid(board, col):  # If valid move, Player 1 will drop a piece on the board
                        row = next_row(board, col)
                        play_piece(board, row, col, 1)

                        if win(board, 1):
                            # print("Player 1 Wins")
                            label = myfont.render("Player 1 wins!", 1, RED)
                            screen.blit(label, (40, 10))
                            game_over = True
                    else:
                        if board_full():
                            # print("Tie")
                            label = myfont.render("Tie!", 1, BLUE)
                            screen.blit(label, (40, 10))
                            game_over = True

                # Ask for player 2 input
                else:
                    while get_player_number() != 2:
                        time.sleep(1)
                        receive()
                    col = get_player_move()

                    if is_valid(board, col):  # If valid, Player 2 will drop a piece on the board
                        row = next_row(board, col)
                        play_piece(board, row, col, 2)

                        if win(board, 2):
                            label = myfont.render("Player 2 wins!", 1, YELLOW)
                            screen.blit(label, (40, 10))
                            game_over = True
                    else:
                        if board_full():
                            label = myfont.render("Tie!", 1, BLUE)
                            screen.blit(label, (40, 10))
                            game_over = True

                print("  0  1  2  3  4  5  6")
                print_board(board)
                draw_board(board)

                turn += 1
                turn = turn % 2

                if game_over:
                    pygame.time.wait(3000)


def selection4():

    game_over = False
    turn = 0
    # initialize pygame
    pygame.init()
    # define our screen size

    # Calling function draw_board again
    draw_board(board)
    pygame.display.update()
    myfont = pygame.font.SysFont("monospace", 75)

    # player_num = int(input("1) Player 1\n2) Player 2\n"))
    # Player 1
    #     if player_num == 1:
    print("  0  1  2  3  4  5  6")
    print_board(board)
    draw_board(board)
    pygame.display.update()
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                col = event.pos[0]
                if turn == 1:
                    pygame.draw.circle(screen, YELLOW, (col, int(SQUARESIZE / 2)), RADIUS)
                else:
                    pygame.draw.circle(screen, BLACK, (col, int(SQUARESIZE / 2)), RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN or turn == 0:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                while get_player_number() != 1:
                    time.sleep(1)
                    receive()
                if turn == 0:
                    # col = int(input("Player 1: Select Column(0-6):"))  # Ask for player 1 input
                    col = get_player_move()
                    if is_valid(board, col):  # If valid move, Player 1 will drop a piece on the board
                        row = next_row(board, col)
                        play_piece(board, row, col, 1)

                        if win(board, 1):
                            # print("Player 1 Wins")
                            label = myfont.render("Player 1 wins!", 1, RED)
                            screen.blit(label, (40, 10))
                            game_over = True
                    else:
                        if board_full():
                            # print("Tie")
                            label = myfont.render("Tie!", 1, BLUE)
                            screen.blit(label, (40, 10))
                            game_over = True

                # Ask for player 2 input
                else:
                    col = event.pos[0]
                    col = int(math.floor(col / SQUARESIZE))
                    message = f"2,{col}"
                    send(message)
                    receive()

                    if is_valid(board, col):  # If valid, Player 2 will drop a piece on the board
                        row = next_row(board, col)
                        play_piece(board, row, col, 2)

                        if win(board, 2):
                            label = myfont.render("Player 2 wins!", 1, YELLOW)
                            screen.blit(label, (40, 10))
                            game_over = True
                    else:
                        if board_full():
                            label = myfont.render("Tie!", 1, BLUE)
                            screen.blit(label, (40, 10))
                            game_over = True

                print("  0  1  2  3  4  5  6")
                print_board(board)
                draw_board(board)

                turn += 1
                turn = turn % 2

                if game_over:
                    pygame.time.wait(3000)



# Exit
# else:
# def selection4():
#     game_over = True

#
# while not game_over:
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#         if event.type == pygame.MOUSEMOTION:
#             pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
#             col = event.pos[0]
#             if turn == 0:
#                 pygame.draw.circle(screen, RED, (col, int(SQUARESIZE / 2)), RADIUS)
#             else:
#                 pygame.draw.circle(screen, YELLOW, (col, int(SQUARESIZE / 2)), RADIUS)
#         pygame.display.update()
#
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
#             # print(event.pos)
#             # Ask for Player 1 Input
#             if turn == 0:
#                 col = event.pos[0]
#                 col = int(math.floor(col / SQUARESIZE))
#
#                 if is_valid(board, col):
#                     row = next_row(board, col)
#                     play_piece(board, row, col, 1)
#
#                     if win(board, 1):
#                         label = myfont.render("Player 1 wins!!", 1, RED)
#                         screen.blit(label, (40, 10))
#                         game_over = True
#
#
#             # Ask for Player 2 Input
#             else:
#                 col = event.pos[0]
#                 col = int(math.floor(col / SQUARESIZE))
#
#                 if is_valid(board, col):
#                     row = next_row(board, col)
#                     play_piece(board, row, col, 2)
#
#                     if win(board, 2):
#                         label = myfont.render("Player 2 wins!!", 1, YELLOW)
#                         screen.blit(label, (40, 10))
#                         game_over = True
#
#             print_board(board)
#             draw_board(board)
#
#             turn += 1
#             turn = turn % 2
#
#             if game_over:
#                 pygame.time.wait(3000)
