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
    
    def __calcVertexPosOnScreen(self, vertexX: int, vertexY: int) -> int:
        return ((vertexX - self.__posX) * self.zoom + self.__zero[0], -((vertexY - self.__posY) * self.zoom) + self.__zero[1])
    
    def renderRect(self, hitboxObj: jar.hitbox.hitbox, color: tuple) -> None:
        lines = hitboxObj.renderRectOnCamera()
        #lines = (lines[0], lines[1], lines[3], lines[2])
        topLeft = self.__calcVertexPosOnScreen(lines[0], lines[2])
        buttomLeft = self.__calcVertexPosOnScreen(lines[0], lines[3])
        topRight = self.__calcVertexPosOnScreen(lines[1], lines[2])
        buttomRight = self.__calcVertexPosOnScreen(lines[1], lines[3])
        #we don't need to render the lines outside the window
        topLeftOnCamera = 0 < topLeft[0] < self.__windowSize[0] and 0 < topLeft[1] < self.__windowSize[1]
        topRightOnCamera = 0 < topRight[0] < self.__windowSize[0] and 0 < topRight[1] < self.__windowSize[1]
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
            
    def collidePoint(self, point: tuple, size: int) -> bool:
        return self.__posX - size < point[0] < self.__posX + size and self.__posY - size < point[1] < self.__posY + size
    
    def setPos(self, position: tuple) -> None:
        self.__posX = position[0]
        self.__posY = position[1]
        
    def goto(self, position: tuple, speed: int) -> bool:
        pass
    
    def move(self, direction: tuple) -> None:
        self.__posX += direction[0] / self.zoom
        self.__posY += direction[1] / self.zoom
        
    def debug(self):
        print(self.__zero)