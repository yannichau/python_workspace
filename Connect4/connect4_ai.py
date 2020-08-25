import numpy as np
import pygame
import sys
import math

# Global Variables
ROW_COUNT = 6
COL_COUNT = 7
WIN_CON = 4
PLAYER = 1
AI = 2

# Colors
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255, 255, 0)

# Screen Rendering Dimensions
SQUARE_SIZE = 100
RADIUS = int(SQUARE_SIZE/2 - 5)
width = COL_COUNT * SQUARE_SIZE
height = (ROW_COUNT+1) * SQUARE_SIZE # additional empty row above
size = (width, height) #tuple

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

# Draw Board (Graphics)
def draw_board(board):
    # Draw background
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            # board: pygame.draw.rect(Surface, color, Rect, width or outline=0), rectangle(poition on x axis, position on y axis, width, height)
            pygame.draw.rect(screen, BLUE, (c*SQUARE_SIZE, (r+1)*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))            
            # black empty circle(surface, color, centre_pos, radius, width)
            pygame.draw.circle(screen, BLACK, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), int((r+1)*SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS) 

    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1: # Player 1
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), height-int(r*SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
            elif board[r][c] == 2: # Player 2
                pygame.draw.circle(screen, RED, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), height-int(r*SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
            else:
                pass
    pygame.display.update()

#################################### INITIATE VARIABLES ######################################
board = create_board()
print_board(board)
game_over = False
turn = PLAYER
col = 3

#pygame variables
pygame.init()
screen = pygame.display.set_mode(size)
draw_board(board)
myfont = pygame.font.SysFont("monospace",50)

#################################### MAIN LOOP ###########################################

# While loop for entire game
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Render circle on the top
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0,width, SQUARE_SIZE)) # reset background to black everytime
            pos_x = event.pos[0]
            if turn == PLAYER:
                pygame.draw.circle(screen, YELLOW, (pos_x, int(SQUARE_SIZE/2)), RADIUS)
            elif turn ==AI:
                pygame.draw.circle(screen, RED, (pos_x, int(SQUARE_SIZE/2)), RADIUS)
            else:
                pass
            pygame.display.update()

        # Main game
        if event.type == pygame.MOUSEBUTTONDOWN:

            pygame.draw.rect(screen, BLACK, (0,0,width, SQUARE_SIZE))

            print(event.pos)
            # Ask for Player input
            pos_x = event.pos[0] # Zeroeth element is horizontal axis, first element is vertical axis
            col = int(math.floor(pos_x/SQUARE_SIZE))

            # Check for valid location
            if is_valid_location(board,col):
                row = get_next_open_row(board,col)
                drop_piece(board, row, col, turn)

            # Check for winning move
            if winning_move(board, turn):
                print("Player ", turn, " Wins!")
                if turn == PLAYER:
                    label = myfont.render(("Player wins!"), 1, YELLOW)
                elif turn == AI:
                    label = myfont.render(("AI wins!"), 1, RED)
                else:
                    pass
                screen.blit(label, (40,10)) #only updates specific part of screen
                game_over = True

            print_board(board)
            draw_board(board)
            
            # Next Player
            if turn == PLAYER:
                turn = AI
            else:
                turn = PLAYER
        
        # Wait for a while before closing the game
        if game_over:
            pygame.time.wait(5000)

