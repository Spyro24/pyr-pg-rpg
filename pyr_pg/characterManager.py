"""
    Character system for pyr_pg
    (c) 2025 Spyro24
"""

import pygame as p
import os

class characterManager:
    def __init__(self, image_path: str, config_path: str):
        self.configPath = config_path
        self.imagePath = image_path
        self.allConfigs = []
        self.allImages = []
        for file in os.listdir(self.imagePath):
            if file.endswith(".png"):
                self.allImages.append(file)
        for file in os.listdir(self.configPath):
            if file.endswith(".conf"):
                self.allConfigs.append(file)
        print(self.allImages, self.allConfigs)

class character:
    def __init__(self):
        self.is_playable = False
        self.name = ""
        self.discription = ""