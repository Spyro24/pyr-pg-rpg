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
        self.characters: list[character] = []
        for file in os.listdir(self.configPath):
            if file.endswith(".conf"):
                self.allConfigs.append(file)
        print(self.allConfigs)
        for conf in self.allConfigs:
            curConfig = pyr_pg.configParse.parse_config(pathlib.Path(self.configPath, conf))
            self.characters.append(character())
            curCharacter = self.characters[-1]
            curCharacter.configTable = curConfig
            curCharacter.name = curConfig["main"]["name"]
            curCharacter.description = curConfig["main"]["desc"]
            print(curCharacter)
    
    def cut_spritesheets(self):
        pass

class character:
    def __init__(self):
        self.is_playable = False
        self.name = ""
        self.description = ""
        self.configTable: dict = None
    
    def __repr__(self):
        return f"pyr_pg.character<name: {self.name}, description: {self.description}>"

class player:
    def __init__(self):
        self.name: str = None
        self.character: character = None
    
    def check_ready(self) -> bool:
        pass