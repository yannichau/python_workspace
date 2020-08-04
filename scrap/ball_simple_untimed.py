import pygame
from pygame.sprite import Sprite
import os

class SimpleAnimation(Sprite):

    def __init__(self, frames):
        self.frames = frames
        self.current = 0
        self.image = frames[0]
        self.rect = self.image.get_rect()
        self.playing = False
        self.reverse = False
    
    def update (self, *args):
        if self.playing:
            if not self.reverse:
                self.current += 1
                if self.current == len(self.frames)-1:
                    self.reverse = True
            else :
                self.current -= 1
                if self.current == 0:
                    self.reverse = False
            self.image = self.frames[self.current]
            self.rect = self.image.get_rect(center=self.rect.center)

    def start(self):
        self.current = 0
        self.playing = True

    def stop(self):
        self.playing = False

    def pause(self):
        self.playing = False

    def resume(self):
        self.playing = True

cache = {}          
def get_sequence (frames_names, sequence, optimize = True):
    frames = []
    global cache
    for name in frames_names:
        if name not in cache:
            image = pygame.image.load(name)
            if optimize:
                if image.get_alpha()  is not None:
                    image = image.convert_alpha()
                else:
                    image = image.convert()
            cache[name] = image
    
        frames.append(cache[name])
    #new variable, don't want to return globbal
    frames2 = []
    for idx in sequence:
        frames2.append(frames[idx])
    return frames2

def get_names_list(basename, ext, length, num_digits=1, offset=0):
    names = []
    format = "%s%0" + str(num_digits) + "d.%s"
    for i in range(offset, length+1):
        names.append(format % (basename, i, ext))
    return names

def main():

    # Miscellaneous Instantiations
    pygame.init()
    logo = pygame.image.load(os.path.normpath("logo32x32.png"))
    pygame.display.set_icon(logo)
    caption_str = os.path.split(__file__)[1]+"  keys: a/q: change fps, space: pause/resume, r: start/stop "
    pygame.display.set_caption(caption_str)
    screen = pygame.display.set_mode((800,600))
    running = True

    # Generate a list of names
    image_names = get_names_list(os.path.normpath("data/ball"), "png", 20, 2, 1)
    sequence = range(20) #0,1,2,3,.....,18,19,20; or how bout self-defining a sequence?
    sequence = [0,1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,6,7,8,9,10,11,12,13,14,15,14,13,12,11,10,11,12,13,14,15,16,17,18,19]
    frames = get_sequence(image_names, sequence)

    #Prepare animation
    anim = SimpleAnimation(frames)
    anim.rect.topleft = (400-75,300-75) #use this to center the animation
    anim.start()

    # use a clock to fix the fps of the main loop
    clock = pygame.time.Clock()
    fps = 20
    pygame.key.set_repeat(500, 30) 
    #clock.tick(10)

    # main loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_a:
                    fps -= 1
                    fps = max(fps, 1)
                elif event.key == pygame.K_q:
                    fps += 1
                elif event.key == pygame.K_SPACE:
                    if anim.playing:
                        anim.pause()
                    else:
                        anim.resume()
                elif event.key == pygame.K_r:
                    if anim.playing:
                        anim.stop()
                    else:
                        anim.start()
        
        # update the caption
        pygame.display.set_caption(caption_str+" set fps: "+str(fps)+"/"+"%2d"%(clock.get_fps()))
        
        # fix the fps
        clock.tick(fps)
        
        # erase things
        screen.fill((0,0,0))
        
        # update anim and draw new anim, assign dirty rect to update only part of screen
        anim.update()
        dirty_rect = screen.blit(anim.image, anim.rect) 
        pygame.display.update(dirty_rect)

if __name__=="__main__":
    main()