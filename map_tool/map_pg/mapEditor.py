import pygame as p
import map_pg

class mapEditor:
    def __init__(self, window, mapFileHandler, alignRect=p.Rect((0,0,0,0))):
        self.mapHandler = mapFileHandler
        self.window     = window
        self.tileSize   = 64
        self.mapWidth   = 16
        self.mapHigth   = 16
        self.tiles      = {"ground":None}
        self.aligRect   = alignRect
        self.clear()
        self.editLayer  = 1
        self.renderMode = 0
    
    def loadMapEditor(self, *x):
        if x[0] == 0:
            return "Load Mapeditor"
        else:
            self.clear()
    
    def reload(self, alignRect):
        self.aligRect = alignRect
        
    def clear(self):
        self.empty   = p.surface.Surface((self.tileSize, self.tileSize), flags=p.SRCALPHA)
        self.empty.fill((255,255,255,255))
        self.ground  = p.surface.Surface((self.tileSize * self.mapWidth, self.tileSize * self.mapHigth))
        self.overlay = p.surface.Surface((self.tileSize * self.mapWidth, self.tileSize * self.mapHigth), flags=p.SRCALPHA)
        
    def createMap(self):
        xPos = 0
        yPos = 0
        for groundTile in self.mapHandler.mapAray[0]:
            if groundTile != 0:
                self.ground.blit(self.tiles["ground"][groundTile - 1], (self.tileSize * xPos, self.tileSize * yPos)) 
            xPos += 1
            if xPos >= self.mapWidth:
                xPos = 0
                yPos += 1
        xPos = 0
        yPos = 0
        for groundOverlayTile in self.mapHandler.mapAray[1]:
            if groundOverlayTile != 0:
                self.overlay.blit(self.tiles["overlay"][groundOverlayTile - 1], (self.tileSize * xPos, self.tileSize * yPos)) 
            xPos += 1
            if xPos >= self.mapWidth:
                xPos = 0
                yPos += 1
        
    def drawStack(self, posX, posY):
        pass
    
    def drawHitbox(self, posX, posY):
        pass
        
    def addTiles(self, tileSet, tileSetName):
        self.tiles[tileSetName] = tileSet
        
    def calcPos(self, *x):
         if x[0] == 0:
            return "Load Mapeditor"
         else:
            rectDimension = self.aligRect.size, self.aligRect.center, self.aligRect.top
            self.blitSize = rectDimension[0][1]
            self.blitX    = rectDimension[1][0] - round(self.blitSize / 2)
            self.blitY    = rectDimension[2]
            self.createInputGrid()
            
    def createInputGrid(self):
        self.inputGrid = map_pg.clickgrid.ClickGrid((self.mapWidth, self.mapHigth),(self.blitX,self.blitY,self.blitSize,self.blitSize))
        
    def blitTile(self, xY, tileNumber):
        if self.editLayer == 0:
            self.ground.blit(self.tiles["ground"][tileNumber], (self.tileSize * xY[0], self.tileSize * xY[1]))
        elif self.editLayer == 1:
            self.overlay.blit(self.empty, (self.tileSize * xY[0], self.tileSize * xY[1]), special_flags=p.BLEND_RGBA_SUB)
            self.overlay.blit(self.tiles["overlay"][tileNumber], (self.tileSize * xY[0], self.tileSize * xY[1]))
        
    def changeTile(self, destination, tileNumber):
        pass
        
            
    def render(self):
        if self.renderMode == 0:
            if self.editLayer >= 0:
                self.window.blit(p.transform.scale(self.ground, (self.blitSize, self.blitSize)), (self.blitX, self.blitY))
            if self.editLayer >= 1:
                self.window.blit(p.transform.scale(self.overlay, (self.blitSize, self.blitSize)), (self.blitX, self.blitY))