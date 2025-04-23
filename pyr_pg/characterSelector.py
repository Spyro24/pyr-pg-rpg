#!/bin/python3
"""
    Character Selector for pyr_pg
    (c) 2025 Spyro24
"""
import os
import pygame as p
import time

class characterSelector:
    def __init__(self, characterPath: str, runtimeStore: dict, debug=False):
        self.window = runtimeStore[10][13] #the runtimestore system is not available in the module. runtimeStore[13] = rs.Window
        self.characterPath = characterPath
        self.runtimeStore = runtimeStore
        self.__envReady()
        self.debug = debug
        self.DebugRects = []
        
    def __envReady(self) -> None:
        winW, winH = self.window.get_size()
        self.windowMidpoint = self.window.get_rect().center
        self.lowestSize = winH
        if winH > winW: self.lowestSize = winW
        self.tileSize = self.lowestSize / 10
        self.virtWindow = p.Rect(self.windowMidpoint[0] - self.lowestSize / 2, self.windowMidpoint[1] - self.lowestSize / 2, self.lowestSize, self.lowestSize)
        self.zeroPos = self.virtWindow.topleft
        
    def __debug(self) -> None:
        p.draw.rect(self.window, (0, 255, 0), self.virtWindow, width=3)
        p.draw.rect(self.window, (128, 128, 0), self.DebugRects[0], width=3)
    
    def openSelector(self, assets: dict) -> tuple:#[characterPathForLoader: str, forward: bool, exit: bool]:
        self.backgroud = p.transform.scale(assets["bg"], (self.lowestSize, self.lowestSize))
        self.fdButtonTexture = p.transform.scale(assets["forward"], (self.tileSize, self.tileSize))
        fdButton = self.window.blit(self.fdButtonTexture,(self.virtWindow.right - self.tileSize, self.virtWindow.bottom - self.tileSize))
        self.DebugRects.append(fdButton)
        run = True
        renderTime = 1 / self.runtimeStore[2] #rs.DefaultFps
        lastFrame = 0
        while run:
            frameTime = time.time() #the time the frame has begin to render
            for event in p.event.get():
                if event.type == p.QUIT:
                    return (None, False, True)
                if event.type == p.MOUSEBUTTONDOWN:
                    mouseKeys = p.mouse.get_pressed()
                    mousePos = p.mouse.get_pos()
                    if mouseKeys[0]:
                        if fdButton.collidepoint(mousePos):
                            run = False
                            
            if frameTime - renderTime > lastFrame:
                lastFrame = frameTime
                self.render()
        return (None, True, False)
        
    def render(self) -> None:
        self.window.fill((0, 0, 0))
        self.window.blit(self.backgroud, self.virtWindow.topleft)
        self.window.blit(self.fdButtonTexture,(self.virtWindow.right - self.tileSize, self.virtWindow.bottom - self.tileSize))
        if self.debug:
            self.__debug()
        p.display.flip()