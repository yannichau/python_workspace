import numpy as np

ROW_COUNT = 6
COL_COUNT = 7
WIN_CON = 4

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
    for c in range(COL_COUNT-(WIN_CON-1)):
        for r in range(ROW_COUNT): # Horizontal win can only start on column 3
            for w in range(WIN_CON):
                print("w = ", w)
                h_connect = True
                if board[r][c+w] != piece: 
                    print("not connected")
                    h_connect = False
    
    # check all vertical locations
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT-(WIN_CON-1)): # Horizontal win can only start on column 3
            for w in range(WIN_CON):
                v_connect = True
                if board[r+w][c] != piece: 
                    v_connect = False 
    
    # check positively slope diagonals (going up to the right)
    for c in range(COL_COUNT-(WIN_CON-1)):
        for r in range(ROW_COUNT-(WIN_CON-1)):
            for w in range(WIN_CON):
                dr_connect = True
                if board[r+w][c+w] != piece: 
                    dr_connect = False 

    # Check negatively slope diagonals (going up to the left)
    for c in range(COL_COUNT-3, COL_COUNT):
        for r in range(ROW_COUNT-3):
            for w in range(WIN_CON):
                dl_connect = True
                if board[r+w][c-w] != piece: 
                    dl_connect = False 

    if h_connect == True | v_connect == True | dr_connect == True | dl_connect == True:
        return True

# Initiate Variables
board = create_board()
print_board(board)
game_over = False
h_connect = False
v_connect = False
dr_connect = False
dl_connect = False
turn = 1
col = 3

while not game_over:

    # Ask for Player input
    col = int(input(("Player ", turn, " make your selection(0-6)")))

    # Check for valid location
    if is_valid_location(board,col):
        row = get_next_open_row(board,col)
        drop_piece(board, row, col, turn)

    # Check for winning move
    if winning_move(board, turn):
        print("Player ", turn, " Wins!")
        game_over = True

    print_board(board)
    
    # Next Player
    if turn == 1:
        turn = 2
    else:
        turn = 1

