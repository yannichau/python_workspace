import numpy as np
import pygame
import sys
import math

# Global Variables
ROW_COUNT = 6
COL_COUNT = 7
WIN_CON = 4

# Colors
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255, 255, 0)

# Screen Rendering Dimensions
SQUARE_SIZE = 50
RADIUS = int(SQUARE_SIZE/2 - 5)
width = COL_COUNT * SQUARE_SIZE
height = (ROW_COUNT+1) * SQUARE_SIZE # additional empty row above
size = (width, height) #tuple

################################## FUNCTIONS #############################################

class Board:

    board = np.zeros((ROW_COUNT,COL_COUNT))
    screen = None
    myfont = None

    # Function to Initiate an empty Board
    @classmethod
    def initialise(cls):
        cls.board = np.zeros((ROW_COUNT,COL_COUNT))
        pygame.init()
        cls.screen = pygame.display.set_mode(size)
        cls.myfont = pygame.font.SysFont("monospace",50)

    # Function to drop a player's piece at the next available row in a specified column.
    @classmethod
    def drop_piece(cls, col, piece):
        for r in range(ROW_COUNT): # (non exclusive)
            if cls.board[r][col] == 0:
                cls.board[r][col] = piece
                break

    # Function to check if piece is between 0-6, column not full. Returns TRUE or FALSE.
    @classmethod
    def is_valid_location(cls, col):
        return cls.board[ROW_COUNT-1][col] == 0

    # Check if a move is leading to a win.
    @classmethod
    def is_winning_move(cls, piece):

        # check all horizontal locations
        for c in range(COL_COUNT-(WIN_CON-1)): # Horizontal win can only start from columns 0 to 3
            for r in range(ROW_COUNT): 
                h_connect = 0
                for w in range(WIN_CON): # Looping over all pieces
                    if cls.board[r][c+w] == piece:
                        h_connect += 1
                if h_connect == WIN_CON:
                    return True
        
        # check all vertical locations
        for c in range(COL_COUNT):
            for r in range(ROW_COUNT-(WIN_CON-1)):
                v_connect = 0
                for w in range(WIN_CON):
                    if cls.board[r+w][c] == piece: 
                        v_connect += 1
                if v_connect == WIN_CON:
                    return True
        
        # check positively slope diagonals (going up to the right)
        for c in range(COL_COUNT-(WIN_CON-1)):
            for r in range(ROW_COUNT-(WIN_CON-1)):
                dr_connect = 0
                for w in range(WIN_CON): 
                    if cls.board[r+w][c+w] == piece: 
                        dr_connect += 1 
                if dr_connect == WIN_CON:
                    return True

        # Check negatively slope diagonals (going up to the left)
        for c in range(COL_COUNT-3, COL_COUNT):
            for r in range(ROW_COUNT-3):
                dl_connect = 0
                for w in range(WIN_CON):
                    if cls.board[r+w][c-w] == piece: 
                        dl_connect += 1 
                if dl_connect == WIN_CON:
                    return True

    # Draw Board (Graphics)
    @classmethod
    def render(cls):
        print(np.flip(cls.board, axis = 0)) # Flip matrix before printing board

        # Draw background
        for c in range(COL_COUNT):
            for r in range(ROW_COUNT):
                # board: pygame.draw.rect(Surface, color, Rect, width or outline=0), rectangle(poition on x axis, position on y axis, width, height)
                pygame.draw.rect(cls.screen, BLUE, (c*SQUARE_SIZE, (r+1)*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))            
                # black empty circle(surface, color, centre_pos, radius, width)
                pygame.draw.circle(cls.screen, BLACK, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), int((r+1)*SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS) 

        for c in range(COL_COUNT):
            for r in range(ROW_COUNT):
                if cls.board[r][c] == 1: # Player 1
                    pygame.draw.circle(cls.screen, YELLOW, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), height-int(r*SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
                elif cls.board[r][c] == 2: # Player 2
                    pygame.draw.circle(cls.screen, RED, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), height-int(r*SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
                else:
                    pass
        pygame.display.update()

    # Draws a solid circle at a specified location (along x axis) with the specified color.
    @classmethod
    def draw_circle(cls, pos_x, color):
        pygame.draw.circle(cls.screen, color, (pos_x, int(SQUARE_SIZE/2)), RADIUS)
        pygame.display.update()

    # Resets the top portion of the screen to black.
    @classmethod
    def reset_background(cls):
        pygame.draw.rect(cls.screen, BLACK, (0,0,width, SQUARE_SIZE))

    # Blits (render/ print) a message on the top of the game.
    @classmethod
    def print_message(cls, message, color):
        print(message)
        label = cls.myfont.render(message, 1, color)
        cls.screen.blit(label, (40,10))
        pygame.display.update()
