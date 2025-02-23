import pygame as p

class mapEditor:
    def __init__(self, window, mapFileHandler):
        self.mapHandler = mapFileHandler
        self.window     = window
        self.tileSize   = 64
        self.mapWidth   = 16
        self.mapHigth   = 16
        self.tiles      = {}
        
    def drawStack(self, posX, posY):
        pass
    
    def drawHitbox(self, posX, posY):
        pass
        
    def addTiles(self, tileSet, tileSetName):
        self.tiles[tileSetName] = tileSet