import pygame
pygame.init()
screen=pygame.display.set_mode((640,480))
background = pygame.Surface(screen.get_size())
background.fill((255,255,255))     # fill the background white 
background = background.convert()  # prepare for faster blitting
ballsurface = pygame.Surface((50,50))     # create a rectangular surface for the ball
#pygame.draw.circle(Surface, color, pos, radius, width=0) 
# draw blue filled circle on ball surface
pygame.draw.circle(ballsurface, (0,0,255), (25,25),25) 
ballsurface = ballsurface.convert() 
ballx = 320
bally = 240
 
#------- try out some pygame draw functions --------
# see the original documentation at http://www.pygame.org/docs/ref/draw.html
 
# pygame.draw.rect(Surface, color, Rect, width=0): return Rect
# rect: (x-position of topleft corner, y-position of topleft corner, width, height)
pygame.draw.rect(background, (0,255,0), (50,50,100,25))
# pygame.draw.circle(Surface, color, pos, radius, width=0): return Rect
pygame.draw.circle(background, (0,200,0), (200,50), 35)
# pygame.draw.polygon(Surface, color, pointlist, width=0): return Rect
pygame.draw.polygon(background, (0,180,0), ((250,100),(300,0),(350,50)))
# pygame.draw.arc(Surface, color, Rect, start_angle, stop_angle, width=1): return Rect
# radiant instead of grad
pygame.draw.arc(background, (0,150,0),(400,10,150,100), 0, 3.14) 
 
#------- blit the surfaces on the screen to make them visible
screen.blit(background, (0,0))     # blit the background on the screen (overwriting all)
screen.blit(ballsurface, (ballx, bally))  # blit the topleft corner of ball surface at pos (ballx, bally)
clock = pygame.time.Clock()
mainloop = True
FPS = 30 # desired framerate in frames per second. try out other values !
playtime = 0.0
 
while mainloop:
    milliseconds = clock.tick(FPS) # do not go faster than this frame rate
    playtime += milliseconds / 1000.0
    # ----- event handler -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False # pygame window closed by user
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False # user pressed ESC
    pygame.display.set_caption("Frame rate: {:0.2f} frames per second." 
                               " Playtime: {:.2} seconds".format(
                               clock.get_fps(),playtime))
    pygame.display.flip()      # flip the screen like in a flipbook
print("this 'game' was played for %.2f seconds" % playtime)