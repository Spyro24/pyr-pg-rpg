"""
    Character system for pyr_pg
    (c) 2025 Spyro24
"""

import os
import pathlib
import pygame as p
import pyr_pg

class CharacterManager:
    def __init__(self, image_path: str, config_path: str):
        self.configPath = config_path
        self.imagePath = image_path
        self.allConfigs = [] #contains every character configuration
        self.characters: list[Character] = []
        for file in os.listdir(self.configPath):
            if file.endswith(".conf"):
                self.allConfigs.append(file)
        for conf in self.allConfigs:
            curConfig = pyr_pg.configParse.parse_config(pathlib.Path(self.configPath, conf))
            self.characters.append(Character())
            curCharacter = self.characters[-1]
            curCharacter.configTable = curConfig
            curCharacter.name = curConfig["main"]["name"]
            curCharacter.description = curConfig["main"]["desc"]
            print(curCharacter)
    
    def cut_spritesheets(self):
        """Internal function"""
        pass

class Character:
    def __init__(self):
        self.is_playable = False
        self.name = ""
        self.description = ""
        self.configTable: dict = None
    
    def __repr__(self):
        return f"pyr_pg.Character <name: {self.name}, description: {self.description}>"

class Player:
    def __init__(self):
        self.name: str = None
        self.character: Character = None
    
    def check_ready(self) -> bool:
        pass
