import pygame

def main():

    pygame.init()

    # load and set the images
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    background = pygame.image.load("background.png")
    image = pygame.image.load("01_image.png") #smiley_face icon
    #image.set_alpha(None) #ensures that colors can be removed
    image.set_alpha(256) #make the image half transparent using the per surface alpha
    image.set_colorkey((255,0,255)) #makes this color (pink) completely transparent, doesn't work if there is an alpha

    screen = pygame.display.set_mode((240,180))

    #order matters!
    # screen.fill((218,150,148)) # fill background with a pinkish red
    screen.blit(background, (0,0))
    screen.blit(image,(50,50)) #(50,50) relative to upper left corner of screen
    
    pygame.display.flip() #this updates the screen
     
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()