from connect4_helpers import *

#################################### INITIATE VARIABLES ######################################

# Initialise Variables
game_over = False
turn = 1
col = None

# Colors
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255, 255, 0)

# Screen Rendering Dimensions
SQUARE_SIZE = 100
RADIUS = int(SQUARE_SIZE/2 - 5)
width = COL_COUNT * SQUARE_SIZE
height = (ROW_COUNT+1) * SQUARE_SIZE # with an additional empty row above
size = (width, height)

# Start of Game
Connect4.create_game()
Connect4.print_board()
Connect4.draw_board()

while not game_over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		# Render circle on the top
		if event.type == pygame.MOUSEMOTION:
			Connect4.reset_background()
			pos_x = event.pos[0] # Zeroeth element is horizontal axis, first element is vertical axis
			if turn == 1:
				Connect4.draw_circle(pos_x, YELLOW)
			elif turn ==2 :
				Connect4.draw_circle(pos_x, RED)

		# Main game
		if event.type == pygame.MOUSEBUTTONDOWN:
			
			Connect4.reset_background()
			
			# Ask for Player input
			print("Mouse Position = ", event.pos)
			pos_x = event.pos[0] 
			col = int(math.floor(pos_x/SQUARE_SIZE))

			# Check for valid location
			if Connect4.is_valid_location(col):
				Connect4.drop_piece(col, turn)

			Connect4.print_board()
			Connect4.draw_board()

			# Check for winning move
			if Connect4.winning_move(turn):
				print("Player ", turn, " Wins!")
				if turn == 1:
					Connect4.print_message("Player 1 wins!", YELLOW)
				elif turn == 2:
					Connect4.print_message("Player 2 wins!", RED)
				game_over = True

			# Next Player
			if turn == 1:
				turn = 2
			elif turn == 2:
				turn = 1
		
		# Wait for a while before closing the game
		if game_over:
			pygame.time.wait(5000)