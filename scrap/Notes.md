# Python Pygame Notes

> To get help you can always do help(pygame.event.get)

For each frame in the main loop do:
- update objects (like move them, change them, what ever)
- erase objects using background
- draw objects to the screen
- update the screen using flip() or update() function (do not forget about that or you will not see anything!)
Keep that in mind, because all optimizations will be based on that. 

## General Practices
- import pygame
- initiate game with `pygame.init()` and start instance of screen
- optional: load logo and windows titles, update later with `pygame.display.set_caption()`
- load background and front image, remembering that order matters
    - define position relative to upper left corner of screen
    - define steps
    - "blit" to display on screen
        - blit also used for things like `screen.blit(font.render())`
- `pygame.display.flip()` to update screen
- initiate clock with `pygame.time.Clock()`

In main looop
- update object position/ steps
- blit, flip to update screen

## Dirty rects
`blit(...)` returns an instance of `pygame.Rect`, so we store that rect into a list and only update those areas

`flip` updates entire screen whereas `update` takes a list of rects as arguments.

But we have to update both old_rect and rew_rect, where the smiley was and where it is right now.
- Consider that the new and old_rect intersects
- the most efficient (good performance) thing to do is to union the 2 rects
- The union results in one big rect
- This is how `pygame.sprite.RenderUpdates` works

## Python Strings
`%s` is a placeholder, string formatting syntax, it alllows front or end of string to be appneded to another string, and is replaced by whatever is passed to the string after another `%` symbol

Examples:
- "Hello %s, my name is %s" % ('john', 'mike') # Hello john, my name is mike".
- "My name is %s and i'm %d" % ('john', 12) #My name is john and i'm 12

## More on Dirty Rects
- `dirty_rect = screen.blit(anim.image, anim.rect)`, where anim.image is an object of an image to be rendered, anim.rect is the part where the actual part is updated
- `pygame.display.update(dirty_rect)`
- every time, the rect is obtained by `self.image.get_rect( center=self.rect.center)`, within the `ani.update()` function, and this detects the change in the old and new rect (the parameter is optional)
