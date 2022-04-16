import pygame
import sys
import random

##### GLOBAL VARIABLES #####
screen_width = 576
screen_height = 1024
screen_center = (screen_width/2, screen_height/2)
dimensions = (screen_width, screen_height)

ul_corner = (0,0) # upper left corner
gap_size = 350
floor_height = 900

bird_center_x = 100
bird_center_y = 512
bird_center = (bird_center_x, bird_center_y)

gravity = 0.25
game_active = True

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos,floor_height))
    screen.blit(floor_surface, (floor_x_pos + screen_width, floor_height)) # consecutive floor to the right

def create_pipe():
    rand_pipe_height = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (700, rand_pipe_height))
    top_pipe = pipe_surface.get_rect(midbottom = (700, rand_pipe_height - gap_size))
    return bottom_pipe, top_pipe

# Take a list of pipes and shift it to the left
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= screen_height: # If bottom of pipe is lower than bottom of the screen
            screen.blit(pipe_surface, pipe)
        else:
            flip_surface = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_surface, pipe)

def check_collision(pipes):
    if bird_rect.top <= -100 or bird_rect.bottom >= floor_height:
        death_sound.play()
        return False
    for pipe in pipes:
        if bird_rect.colliderect(pipe): # warning - takes (bit more) processing power
            death_sound.play()
            return False
    return True

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement*3, 1) # second argument is rotation, third argument is zoom
    return new_bird

def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center = (bird_center_x, bird_rect.centery)) # previous height
    return new_bird, new_bird_rect

def score_display(game_active):
    if game_active == False:
        high_score_surface = game_font.render(f" High Score: {int(high_score)}", True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center = (screen_width/2, 850))
        screen.blit(high_score_surface, high_score_rect)
    score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
    score_rect = score_surface.get_rect(center = (screen_width/2, 100))
    screen.blit(score_surface, score_rect)

def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score

pygame.init()
screen = pygame.display.set_mode(dimensions)
clock = pygame.time.Clock()

# Game Variables
bird_movement = 0 # Loop over bird frames
score = -2
high_score = 0

# Blit background surface
bg_surface = pygame.image.load("sprites/background-day.png").convert()
bg_surface = pygame.transform.scale2x(bg_surface)
game_font = pygame.font.Font('04B_19.TTF', 40)

# Blit moving floor
floor_surface = pygame.image.load("sprites/base.png").convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

# Bird
bird_downflap = pygame.transform.scale2x(pygame.image.load('sprites/bluebird-downflap.png').convert_alpha())
bird_midflap = pygame.transform.scale2x(pygame.image.load('sprites/bluebird-midflap.png').convert_alpha())
bird_upflap = pygame.transform.scale2x(pygame.image.load('sprites/bluebird-upflap.png').convert_alpha())
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = bird_center) # places a rectangle around the surface

# New event for animating bird frames
BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200) # 200 ms

# Pipes
pipe_surface = pygame.image.load('sprites/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []

# New event for spawning pipes
SPAWNPIPE = pygame.USEREVENT # Can be passed as a new event, but a system timer
pygame.time.set_timer(SPAWNPIPE, 1200) #ms
pipe_height = [400, 600, 800]

game_over_surface = pygame.transform.scale2x(pygame.image.load('sprites/message.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center = screen_center)

# Sounds
pygame.mixer.pre_init(frequency = 441000, size = 16, channels = 1, buffer = 512)
flap_sound = pygame.mixer.Sound('audio/sfx_wing.wav')
death_sound = pygame.mixer.Sound('audio/sfx_hit.wav')
score_sound = pygame.mixer.Sound('audio/sfx_point.wav')


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            flap_sound.play()
            bird_movement = -8 # When we jump we ignore gravity
            if game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = bird_center
                bird_movement = 0
                score = -2
        
        if event.type == SPAWNPIPE and game_active == True:
            pipe_list.extend(create_pipe()) # extend is append, but for tuples
            print(pipe_list)
            score += 1

        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
            bird_surface, bird_rect = bird_animation()
    
    screen.blit(bg_surface, ul_corner)

    if game_active:
        # Bird movement
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)
        game_active = check_collision(pipe_list)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        score_display(True)
    else:
        screen.blit(game_over_surface, game_over_rect)
        high_score = update_score(score, high_score)
        score_display(False)

    # 2 floors moving to the left
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -screen_width:
        floor_x_pos = 0
    
    pygame.display.update()
    clock.tick(120) # Can't run faster than 120Hz, but can run slower - depends on the efficiency of your code and your computer