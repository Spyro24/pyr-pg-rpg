import pygame as p
import shader as sh

gw = p.display.set_mode((512,512))
shader = sh.shader(gw,16,16)
white = (255,255,255)
clock = p.time.Clock()

shader.create([(0,0)], "torch", 0, 0, 0, 3, 0, 64, (0,0,0))

while True:
    gw.fill(white)
    shader.render()
    p.display.flip()
    clock.tick(5)
