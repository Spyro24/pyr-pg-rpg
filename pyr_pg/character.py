"""
    character system for pyr_pg
    (c) 2025 Spyro24
"""
import pygame as p

class character:
    def __init__(self):
        self.isPlayable = False
        self.sprites = {}

class player:
    def __init__(self):
        self.posX = 0
        self.posY = 0
        self.microPosX = 0
        self.microPosY = 0
        self.invetory = {}
        self.character = character()
