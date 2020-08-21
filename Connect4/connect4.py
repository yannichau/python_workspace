import numpy as np

ROW_COUNT = 6
COL_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT,COL_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col): # between 0-6, column not full
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col): # loop through rows
    for r in range(ROW_COUNT): # (non exclusive)
        if board[r][col] == 0:
            return r

def print_board(board): # flip the matrix over (what we expect to see for a connect4 game)
    print(np.flip(board, axis = 0))

def winning_move(board, piece):
    # check all horizontal locations
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT): # Horizontal win can only start on column 3
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    
    # check all horizontal locations
    for r in range(ROW_COUNT):
        for c in range(COL_COUNT): # Horizontal win can only start on column 3
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

# Initiate Variables
board = create_board()
print_board(board)
game_over = False
turn = 0
col = 3

while not game_over:
    # Ask for Player 1 Input
    if turn == 0:
        col = int(input("Player 1 make your selection(0-6)")) # want to make sure that it is an int rather than a string.

        if is_valid_location(board,col):
            row = get_next_open_row(board,col)
            drop_piece(board, row, col, 1)

            if winning_move(board, 1):
                print("Player 1 Wins!")
                game_over = True

    # Ask for player 2 input
    else:
        col = int(input("Player 2 make your selection(0-6)"))

        if is_valid_location(board,col):
            row = get_next_open_row(board,col)
            drop_piece(board, row, col, 2)

            if winning_move(board, 2):
                print("Player 2 Wins!")
                game_over = True
    
    print_board(board)
    turn +=1
    turn = turn % 2 #Takes the remainder when divided by 2

