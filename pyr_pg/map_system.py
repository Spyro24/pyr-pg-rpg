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
        self.ground = p.Surface((self.mapSize[0] * self.tileSize, self.mapSize[1] * self.tileSize))
        self.mapLayers = {"ground": self.ground,
                          }
        self.mapXPos = 0
        self.mapXPos = 0
        
    def load_tiles(self, paths={"ground": "./res/tiles/ground"}):
        """Load Every tile in the tile paths"""
        for path in paths.keys():
            tileInternalPath = path
            tileExternalPath = paths[path]
            sheetCount = len(os.listdir(tileExternalPath))
            for sheetNumber in range(sheetCount):
                sheet = p.image.load(f"{tileExternalPath}/{sheetNumber}.png")
                for y in range(self.tileSheetSize[1]):
                    for x in range(self.tileSheetSize[0]):
                        tile = p.Surface((self.tileSize, self.tileSize), p.SRCALPHA)
                        tile.blit(sheet, (-(x * self.tileSize), -(y * self.tileSize)))
                        self.tiles[tileInternalPath].append(tile.convert_alpha())
    
    def blit_tile(self, layer: str, tileId: int, pos: tuple[int, int]):
        """Blit a single tile to a layer of the map with the tile ID"""
        if tileId > 0:
            tileId = tileId - 1
            self.mapLayers[layer].blit(self.tiles[layer][tileId], (pos[0] * self.tileSize, pos[1] * self.tileSize))
