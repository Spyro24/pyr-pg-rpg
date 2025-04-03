#!/bin/python3
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
        self.__windowRect = pygameWindow.get_rect()
        self.__lerpX = 0
        self.__lerpY = 0
        self.__lerpState = False
        self.__lerpSpeed = 0
    
    def __calcVertexPosOnScreen(self, vertexX: int, vertexY: int) -> int:
        return ((vertexX - self.__posX) * self.zoom + self.__zero[0], -((vertexY - self.__posY) * self.zoom) + self.__zero[1])
    
    def renderRect(self, hitboxObj: jar.hitbox.hitbox, color: tuple) -> None:
        lines = hitboxObj.renderRectOnCamera()
        #lines = (lines[0], lines[1], lines[3], lines[2])
        #we don't need to render the lines outside the window
        midPoint = hitboxObj.getMidpoint()
        if self.__windowRect.collidepoint(self.__calcVertexPosOnScreen(midPoint[0], midPoint[1])) or True:
            topLeft = self.__calcVertexPosOnScreen(lines[0], lines[2])
            buttomLeft = self.__calcVertexPosOnScreen(lines[0], lines[3])
            topRight = self.__calcVertexPosOnScreen(lines[1], lines[2])
            buttomRight = self.__calcVertexPosOnScreen(lines[1], lines[3])
            p.draw.line(self.__window, color, topLeft, buttomRight)
            p.draw.line(self.__window, color, topLeft, topRight)
            p.draw.line(self.__window, color, buttomLeft, buttomRight)
            p.draw.line(self.__window, color, topLeft, buttomLeft)
            p.draw.line(self.__window, color, topRight, buttomRight)
            
    def collidePoint(self, point: tuple, size: int) -> bool:
        return self.__posX - size < point[0] < self.__posX + size and self.__posY - size < point[1] < self.__posY + size
    
    def setPos(self, position: tuple) -> None:
        self.__posX = position[0]
        self.__posY = position[1]
        
    def getPos(self) -> tuple:
        return (self.__posX, self.__posY)
        
    def goto(self, position: tuple, speed: int) -> bool:
        dx, dy = position[0] - self.__posX, position[1] - self.__posY
        dist = (dx**2 + dy**2)**0.5
        self.__lerpState = True
        if position[0] != self.__posX:
            self.__lerpX = (dx / dist) * speed
        if position[1] != self.__posY:
            self.__lerpY = (dy / dist) * speed
    
    def deactivateLerp(self) -> None:
        self.__lerpState = False
        
    def move(self, direction: tuple) -> None:
        self.__posX += direction[0] / self.zoom
        self.__posY += direction[1] / self.zoom
    
    def tick(self) -> None:
        if self.__lerpState == True:
            self.move((self.__lerpX, self.__lerpY))
            
    def debug(self):
        print(self.__zero)
        
class cameraBox:
    def __init__(self, begin: tuple, end: tuple):
        self.__hitBoxes = []
        