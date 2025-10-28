import pygame as p
import os

class mapSystem:
    def __init__(self):
        self.tileSize = 64
        self.mapSize = (16, 16)
        self.tileSheetSize = (6, 12)
        self.tiles = {"ground": [],
                      "groundOverlay": [],
                      "playerOverlay": [],
                      "playerOveroverlay": [],
                      "shadows": [],
                      }
        self.ground = p.Surface((self.mapSize[0], self.mapSize[1]))
        self.mapXPos = 0
        self.mapXPos = 0
        
    def load_tiles(self, paths={"ground": "./res/tiles/ground"}):
        for path in paths.keys():
            tileInternalPath = path
            tileExternalPath = paths[path]
            sheetCount = len(os.listdir(tileExternalPath))
