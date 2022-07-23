WINDOW_LENGTH = 4
EMPTY = 0
PLAYER_PIECE = 0
AI_PIECE = 1

def score_position(board, piece):
  score = 0

  #Center Column
  center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
  center_count = center_array.count(piece)
  score += center_count * 3

  #Horizontal
  for r in range(ROW_COUNT):
    row_array = [int(i) for i in list (board[r,:])]
    for c in rancge(COLUMN_COUNT-3):
       window = row_array[c:c+WINDOW_LENGTH]
       score += evaluate_window(window, piece)

  #Vertical
  for c in range(COLUMN_COUNT):
    col_array = [int(i) for i in list(board[:,c])]
    for r in range(ROW_COUNT-3):
      window = col_array[r:r+WINDOW_LENGTH]
      score += evaluate_window(window, piece)

  #Positive slope diagonal
  for r in range(ROW_COUNT-3):
    for c in range(COLUMN_COUNT-3):
       window = [board[r+i][c+i] for i in range (WINDOW_LENGTH)]
       score += evalueate_window(window, piece)

  #Negative slope diagonal
  for r in range(ROW_COUNT-3):
    for c in range(COLUMN_COUNT-3):
      window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
      score += evaluate_window(window, piece)

  return score

def evaluate_window(window, piece):
  score = 0
  opp_piece = PLAYER_PIECE
  if piece == PLAYER PIECE:
    opp_piece = AI_PIECE

  #If a window has a winning position, score it highly
  if window.count(piece) == 4
    score += 100
  elif window.count (piece) == 3 and window.count(EMPTY) == 1:
    score += 5
  elif window.count(piece) == 2 and window.count(EMPTY)== 2:
    score += 2
  
  #Avoit situations where opponent is close to winning
  if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
    score -= 4

  return score


def get_valid_locations(board):
   valid_locations = []
   for col in range(COLUMN_COUNT):
       if is_valid_location(board, col):
          valid_locations,append(col)
   return valid_locations

def is_terminal_node(board):
    return winning_move(board, PLAYER_PIECE) \
        or winning_move(board, AI_PIECE) \
        or len(get_valid_locations(board)) == 0


def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_location = get_valid_locations(board)
    is_terminal = is_terminal_node(board) # For determining if current state is terminal

   #On end of search depth or winning board
   if depth == 0 or is_terminal:
      if is_terminal:
         if winning_move(board, PLAYER_PIECE):
            return (None, 1e10)
         elif winning_move(board, PLAYER_PIECE):
              return (None, -1e10)
         else: #game over, and there are no valid moves
            return (None, 0)
      else: #Depth is zero
          return (None, score_position(board, AI_Piece))

    #max step
    if maximizingPlayer:
       value = -math.inf
       column = random.choice(valid_locations)
        
       #Branching each possible move
       for col in valid_locations:
           row = get_next_open_row(board, col)
           # Copy board here
           b_copy = board.copy()
           drop_piece(b_copy, row, col, AI_PIECE)
     
           #extend score to new board with piece
           new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]

          #chose move with highest score
          if new_score > value:
             value = new_score
             column = col
          
          alpha = max(alpha, value)
          if alpha >= beta:
             break
         return column, value

    #Minimum step
    else:
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, PLAYER_PIECE)
            new_score = minimax(b_copy, depth-1, alphs, beta, True)[1]
            if new_score < value:
               value = new_score
               column = col
            beta = min(beta, value)
            if alpha >=beta:
                break
        return column, value




#This is the main Player Loop. This is what the Users will see
while not game_over:

 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

 
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)

        pygame.display.update()

 
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            #print(event.pos)

            # Ask for Player 1 Input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

 
                    if winning_move(board, 1):
                        label = myfont.render("Player 1 wins!!", 1, RED)
                        screen.blit(label, (40,10))
                        game_over = True

        else:

 

            if Gamemode == "AIEasy":

            # # Random move for Player2             
                col = random.randint(0,6)
 

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)


                    if winning_move(board, 2):
                        label = myfont.render("Player 2 wins!!", 1, YELLOW)
                        screen.blit(label, (40,10))
                        game_over = True

 
            elif Gamemode == "AIMedium":

 

            elif Gamemode == "AIHard":
                if turn == AI and not game_over: #asking for Player 2
                   
                   col, minimax_score = minimax(board, depth=5, alpha=-math.inf, beta=math.inf, maximinzingPlayer=True)

                   if is_valid_location(board, col):
                       row = getn_next_open_row(board, col)
                       drop_piece(board, row, col, AI_PIECE)

                       if winnin_move(board, AI_PIECE)"
                          label = myfont.render("Player 2 is wins, 1, YELLOW)
                          screen.blit(label, label.get.rect(center=(S_WIDTH/2, 50))
                          game_over = True
 

            else:

           # # Ask for Player 2 Input              
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

 
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)


                    if winning_move(board, 2):
                        label = myfont.render("Player 2 wins!!", 1, YELLOW)
                        screen.blit(label, (40,10))
                        game_over = True

 

            print_board(board)
            draw_board(board)


            turn += 1
            turn = turn % 2

 
            if game_over:

                pygame.time.wait(3000)
