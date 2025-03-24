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
        #lines = (lines[0], lines[1], lines[3], lines[2])
        topLeft = ((lines[0] * self.zoom) - self.__posX, (lines[2] * self.zoom) - self.__posY)
        buttomLeft = ((lines[0] * self.zoom) - self.__posX, (lines[3] * self.zoom) - self.__posY)
        topRight = ((lines[1] * self.zoom) - self.__posX, (lines[2] * self.zoom) - self.__posY)
        buttomRight = ((lines[1] * self.zoom) - self.__posX, (lines[3] * self.zoom) - self.__posY)
        #we don't need to render the lines outside the window
        topLeftOnCamera = (0,0) < topLeft < self.__windowSize
        topRightOnCamera = (0,0) < topRight < self.__windowSize
        buttomLeftOnCamera = (0,0) < buttomLeft < self.__windowSize
        buttomRightOnCamera = (0,0) < buttomRight < self.__windowSize
        if topLeftOnCamera or buttomRightOnCamera:
            p.draw.line(self.__window, color, topLeft, buttomRight)
        if topLeftOnCamera or topRightOnCamera: #the top line
            p.draw.line(self.__window, color, topLeft, topRight)
        if buttomLeftOnCamera or buttomRightOnCamera:
            p.draw.line(self.__window, color, buttomLeft, buttomRight)
        if topLeftOnCamera or buttomLeftOnCamera:
            p.draw.line(self.__window, color, topLeft, buttomLeft)
        if topRightOnCamera or buttomRightOnCamera:
            p.draw.line(self.__window, color, topRight, buttomRight)
    
    def setPos(self, position: tuple) -> None:
        self.__posX = position[0]
        self.__posY = position[1]
    
    def move(self, direction: tuple) -> None:
        self.__posX += direction[0]
        self.__posY += direction[1]
        
    def debug(self):
        print(self.__zero)