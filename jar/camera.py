import pygame as p
import jar

class Camera():
    def __init__(self, pygameWindow: p.display.set_mode):
        self.zoom = 10 #default zoom (how many px are 1 unit)
        self.__window = pygameWindow
        self.__posX = 0
        self.__posY = 0
        self.__zero = pygameWindow.get_rect().center
        self.__windowSize = pygameWindow.get_size()
    
    def renderRect(self, hitboxObj: jar.hitbox.hitbox, color: tuple) -> None:
        lines = hitboxObj.renderRectOnCamera()
        topLeft = ((lines[0] - self.__posX) * self.zoom + self.__zero[0], (lines[2] - self.__posY) * self.zoom + self.__zero[1])
        topRight = ((lines[1] - self.__posX) * self.zoom + self.__zero[0], (lines[2] - self.__posY) * self.zoom + self.__zero[1])
        buttomRight = ()
        buttomLeft = ()
        #we don't need to render the lines outside the window 
        if (0,0) < topLeft < self.__windowSize or (0,0) < topRight < self.__windowSize:
            print(p.draw.line(self.__window, color, topLeft, topRight))
    
    def debug(self):
        print(self.__zero)