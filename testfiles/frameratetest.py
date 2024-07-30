import pygame as p
from random import randint
import time

disp = p.display.set_mode((0,0),flags=p.FULLSCREEN)
green = (0, 255, 0)
red = (255,0,0)
blue = (0,0,255)
col= [red,green,blue]
w, h = disp.get_size()
r,g,b = 255,255,255
c=3.4952533333333335 / 1.25
t = time.time()
frames = 0
for x in range(w):
    for y in range(h):
        
        '''
        if r > 255:
            r = 0
            g += c
        if g > 255:
            g = 0
            b += c
        '''
        try:
            test = randint(0,1)
            if test:
                disp.set_at((x,y),(r,g,b))
        except:
            pass
        #r += c
        
    frames += 1
    if time.time() > (t + 1):
        print(frames)
        frames = 0
        t = time.time()
    p.display.update()
p.display.flip() 

