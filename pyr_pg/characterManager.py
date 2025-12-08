"""
    Character system for pyr_pg
    (c) 2025 Spyro24
"""

import pygame as p
import os
import pyr_pg
import pathlib

class characterManager:
    def __init__(self, image_path: str, config_path: str):
        self.configPath = config_path
        self.imagePath = image_path
        self.allConfigs = []
        self.allImages = []
        for file in os.listdir(self.configPath):
            if file.endswith(".conf"):
                self.allConfigs.append(file)
        print(self.allImages, self.allConfigs)
        for conf in self.allConfigs:
            curConfig = pyr_pg.configParse.parse_config(pathlib.Path(self.configPath, conf))
            print(curConfig)

class character:
    def __init__(self):
        self.is_playable = False
        self.name = ""
        self.discription = ""