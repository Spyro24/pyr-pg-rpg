#!/bin/python3
"""
    Character Selector for pyr_pg
    (c) 2025 Spyro24
"""
import os
import pygame as p

class characterSelector:
    def __init__(self, window: p.Surface, characterPath: str):
        self.window = window
        self.characterPath = characterPath
        self.__
        
    def __envReady(self):
        winW, winH = self.window.get_size()
        self.windowMidpoint = self.window.get_rect().center()
        self.lowestSize = WinH
        if winH > winW: self.lowestSize = winW