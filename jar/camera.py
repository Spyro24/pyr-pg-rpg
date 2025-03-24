import pygame as p
import jar

class Camera():
    def __init__(self, pygameWindow: p.display.set_mode):
        self.zoom = 10 #default zoom (how many px are 1 unit)
        self.window = pygameWindow
        self.posX = 0
        self.posY = 0
        self.zero = pygameWindow.get_rect().center
    
    def renderRect(self, hitboxObj: jar.hitbox.hitbox, color: tuple) -> None:
        lines = hitboxObj.renderRectOnCamera()
        topLeft = ()
        topRight = ()
        buttomRight = ()
        buttomLeft = ()
    
    def __debug(self):
        print(self.zero)