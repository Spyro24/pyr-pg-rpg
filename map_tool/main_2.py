import pygame as p

WindowTileSize = 24
WindowTilling = (48,34)
Window = p.display.set_mode((WindowTilling[0] * WindowTileSize, WindowTilling[1] * WindowTileSize))

run = True
while run:
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
p.quit()
exit()