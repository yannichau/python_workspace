import numpy as np

# Global Variables
ROW_COUNT = 6
COL_COUNT = 7
WIN_CON = 4

################################## FUNCTIONS #############################################

# Function to Initiate Board
def create_board():
    board = np.zeros((ROW_COUNT,COL_COUNT))
    return board

# Function to drop a player's piece at a specific location
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Function to check if piece is between 0-6, column not full
def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

# Loop through all rows to get the next open row of a column.
def get_next_open_row(board, col):
    for r in range(ROW_COUNT): # (non exclusive)
        if board[r][col] == 0:
            return r

# Flip matrix before printing board.
def print_board(board): # flip the matrix over (what we expect to see for a connect4 game)
    print(np.flip(board, axis = 0))

# Check if a move is leading to a win.
def winning_move(board, piece):

    # check all horizontal locations
    for c in range(COL_COUNT-(WIN_CON-1)): # Horizontal win can only start from columns 0 to 3
        for r in range(ROW_COUNT): 
            h_connect = 0
            for w in range(WIN_CON): # Looping over all pieces
                if board[r][c+w] == piece:
                    h_connect += 1
            if h_connect == WIN_CON:
                return True
    
    # check all vertical locations
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT-(WIN_CON-1)):
            v_connect = 0
            for w in range(WIN_CON):
                if board[r+w][c] == piece: 
                    v_connect += 1
            if v_connect == WIN_CON:
                return True
    
    # check positively slope diagonals (going up to the right)
    for c in range(COL_COUNT-(WIN_CON-1)):
        for r in range(ROW_COUNT-(WIN_CON-1)):
            dr_connect = 0
            for w in range(WIN_CON): 
                if board[r+w][c+w] == piece: 
                    dr_connect += 1 
            if dr_connect == WIN_CON:
                return True

    # Check negatively slope diagonals (going up to the left)
    for c in range(COL_COUNT-3, COL_COUNT):
        for r in range(ROW_COUNT-3):
            dl_connect = 0
            for w in range(WIN_CON):
                if board[r+w][c-w] == piece: 
                    dl_connect += 1 
            if dl_connect == WIN_CON:
                return True

#################################### MAIN LOOP ###########################################

# Initiate Variables
board = create_board()
print_board(board)
game_over = False
turn = 1
col = 3

# While loop for entire game
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

