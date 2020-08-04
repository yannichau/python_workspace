import pygame
from pygame.sprite import Group

def main():

    #load game and start instance of screen
    pygame.init()
    screen_width = 240
    screen_height = 180
    screen = pygame.display.set_mode((screen_width,screen_height))

    # load and set logo, windows titles
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("movement")

    #load background image and smiley face, set background of smiley to transparent
    background = pygame.image.load("background.png")
    image = pygame.image.load("01_image.png") #smiley_face icon
    #image.set_alpha(None) #ensures that colors can be removed
    image.set_alpha(128) #make the image half transparent using the per surface alpha
    image.set_colorkey((255,0,255)) #makes this color (pink) completely transparent, doesn't work if there is an alpha

    #Place smiley and background on screen, remember that oroder matters
    # screen.fill((218,150,148)) # fill background with a pinkish red
    screen.blit(background, (0,0))

    # Smiley position relative to upper left corner of screen
    xpos = 50
    ypos = 50
    step_x = 10 #how much it moves each time
    step_y= 10

    screen.blit(image,(xpos,ypos)) 
    
    #update screen
    pygame.display.flip()
    clock = pygame.time.Clock() # a clock for controlling the fps later

    # define a variable to control the main loop
    running = True

        # main loop
    while running:
         # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # check for keypress and check if it was Esc
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # check if the smiley is still on screen, if not change direction
        if xpos>screen_width-64 or xpos<0: #64 to prevent smiley from getting completely out of screen before changing direction and returning.
            step_x = -step_x
        if ypos>screen_height-64 or ypos<0:
            step_y = -step_y
        # update the position of the smiley
        xpos += step_x # move it to the right
        ypos += step_y # move it down

        # now blit the smiley on screen
        screen.blit(background,(0,0))
        screen.blit(image, (xpos, ypos))
        
        # and update the screen (don't forget that!)
        #pygame.display.flip()
        pygame.sprite.RenderUpdates.draw()

        # this will slow it down to 10 fps, so you can watch it, 
        # otherwise it would run too fast
        clock.tick(5)

if __name__ == "__main__":
    main()