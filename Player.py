while not game_over:
    #Ask for player 1 input
    if turn == 0:
        col = int(input("Player 1, Choose a column(0-6):"))
        #Player 1 will drop a piece on the board
        if is_valid_location(board,col):
            row = get_next_open_row(board,col)
            drop_piece(board,row,col,1)
         
    #Ask for player 2 input
    else:
        col = int(input("Player 2, Choose a column(0-6):"))
        #Player 2 will drop a piece on the board
        if is_valid_location(board,col):
            row = get_next_open_row(board,col)
            drop_piece(board,row,col,2)
 
    print_board(board)
             
    turnOrder += 1
    turnOrder = turnOrder % 2
