#(c) 2024 spyro24

import pygame as p
import shader as sh

disp_size = 512
test = p.display.set_mode((disp_size*1.5,disp_size))
xs = 16
ys = 16
transp = 0
maxtrp = 255
steps = maxtrp - transp; steps = steps / (xs * ys - 1)
testobj = p.Surface((xs,ys),flags=p.SRCALPHA)

for x in range(xs):
    print(transp)
    for y in range(ys):
        testobj.set_at((x,y),(0,0,0,transp))
        transp += steps
    
test.fill((255,255,255))
test.blit(p.transform.scale(testobj,(disp_size,disp_size)),(0,0))
p.display.flip()
        