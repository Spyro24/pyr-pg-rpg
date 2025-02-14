#!/bin/python3
"""
    Character Selector for pyr_pg
    (c) 2025 Spyro24
"""
import os
import pygame as p

class characterSelector:
    def __init__(self, window: p.Surface, characterPath: str, debug=False):
        self.window = window
        self.characterPath = characterPath
        self.__envReady()
        self.debug = debug
        
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
        
    def render(self) -> None:
        if self.debug:
            self.__debug()
            
if __name__ == "__main__": #Unit test
    window = p.display.set_mode((400, 300))
    test = characterSelector(window, "./", debug=True)
    test.render()
    p.display.flip()