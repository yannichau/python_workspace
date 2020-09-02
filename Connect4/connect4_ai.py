import numpy as np
import pygame
import sys
import math
import random

# Global Variables
ROW_COUNT = 6
COL_COUNT = 7
WIN_CON = 4 # also window length
PLAYER = 1
AI = 2
EMPTY = 0

# Colors
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255, 255, 0)

#

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
	return board[ROW_COUNT-1][col]  == 0

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

# Score of various positions available on the board
def score_position(board, piece):
	score = 0

	# Score, Horizontal
	for r in range(ROW_COUNT): 
		row_array = [int(i) for i in list(board[r,:])] # all column positions in a rows
		for c in range (COL_COUNT -3): # Look at all windows size of 4
			window = row_array[c:WIN_CON]
			if window.count(piece) == WIN_CON:
				score += 100
			elif window.count(piece) == WIN_CON-3 and window.count(EMPTY) == 1:
				score += 10
	return score

# Obtain the list of valid locations on the board
def get_valid_locations(board): 
	valid_locations = []
	for col in range(COL_COUNT):
		if is_valid_location(board, col):
			valid_locations.append(col)
	return valid_locations

# Return the best column
def pick_best_move(board, piece):
	best_score = 0
	valid_locations = get_valid_locations(board)
	best_col = random.choice(valid_locations)
	for col in valid_locations:
		row = get_next_open_row(board, col)
		temp_board = board.copy()
		drop_piece(temp_board, row, col, piece)
		score = score_position(temp_board, piece)
		if score > best_score:
			best_score = score
			best_col = col
	
	return best_col
		
#################################### INITIATE VARIABLES ######################################
board = create_board()
print_board(board)
game_over = False
turn = random.randint(PLAYER, AI)
col = 3
player_valid = False
AI_valid = False

#pygame variables
pygame.init()
screen = pygame.display.set_mode(size)
draw_board(board)
myfont = pygame.font.SysFont("monospace",50)

#################################### MAIN LOOP ###########################################

# While loop for entire game
while not game_over:

	# PLAYER
	if turn == PLAYER:
		player_valid = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			# Render circle on the top
			if event.type == pygame.MOUSEMOTION:
				pygame.draw.rect(screen, BLACK, (0,0,width, SQUARE_SIZE)) # reset background to black everytime
				pos_x = event.pos[0]
				pygame.draw.circle(screen, YELLOW, (pos_x, int(SQUARE_SIZE/2)), RADIUS)
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
					player_valid = True
					row = get_next_open_row(board,col)
					drop_piece(board, row, col, turn)

					# Check for winning move
					if winning_move(board, PLAYER):
						print("Player Wins!")
						label = myfont.render(("Player wins!"), 1, YELLOW)
						screen.blit(label, (40,10)) #only updates specific part of screen
						game_over = True

				print_board(board)
				draw_board(board)

	if turn == AI and not game_over:
		
		# col = random.randint(0, COL_COUNT-1)
		col = pick_best_move(board, AI)

		# Check for valid location
		if is_valid_location(board,col):
			pygame.time.wait(1500)
			AI_valid = True
			row = get_next_open_row(board,col)
			drop_piece(board, row, col, turn)

			# Check for winning move
			if winning_move(board, AI):
				print("AI Wins!")
				label = myfont.render(("AI wins!"), 1, RED)
				screen.blit(label, (40,10)) 
				game_over = True

		print_board(board)
		draw_board(board)

   
	# Next Player if it is valid
	if turn == PLAYER and player_valid == True:
		turn = AI
	elif turn == AI and AI_valid == True:
		turn = PLAYER
	else:
		pass

	# Wait for a while before closing the game
	if game_over:
		pygame.time.wait(5000)

