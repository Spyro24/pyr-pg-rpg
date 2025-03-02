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
        self.shadow  = p.surface.Surface((self.tileSize * self.mapWidth, self.tileSize * self.mapHigth), flags=p.SRCALPHA)
        
    def createMap(self):
        self.createSurface(self.mapHandler.mapAray[0], self.ground,  "ground")
        self.createSurface(self.mapHandler.mapAray[1], self.overlay, "overlay")
        self.createSurface(self.mapHandler.mapAray[4], self.shadow,  "shadow")
    
    def createSurface(self, data, surface, tileSetName):
        xPos = 0
        yPos = 0
        for Tile in data:
            if Tile != 0:
                surface.blit(p.transform.scale(self.tiles[tileSetName][Tile - 1], (self.tileSize, self.tileSize)), (self.tileSize * xPos, self.tileSize * yPos)) 
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
            if tileNumber > 0:
                self.ground.blit(self.tiles["ground"][tileNumber - 1], (self.tileSize * xY[0], self.tileSize * xY[1]))
            else:
                self.ground.blit(self.empty, (self.tileSize * xY[0], self.tileSize * xY[1]), special_flags=p.BLEND_RGB_SUB)
        elif self.editLayer == 1:
            self.overlay.blit(self.empty, (self.tileSize * xY[0], self.tileSize * xY[1]), special_flags=p.BLEND_RGBA_SUB)
            if tileNumber > 0:
                self.overlay.blit(self.tiles["overlay"][tileNumber - 1], (self.tileSize * xY[0], self.tileSize * xY[1]))
        elif self.editLayer == 4:
            self.shadow.blit(self.empty, (self.tileSize * xY[0], self.tileSize * xY[1]), special_flags=p.BLEND_RGBA_SUB)
            if tileNumber > 0:
                self.shadow.blit(p.transform.scale(self.tiles["shadow"][tileNumber - 1], (self.tileSize, self.tileSize)), (self.tileSize * xY[0], self.tileSize * xY[1]))
            
    def render(self):
        if self.renderMode == 0:
            if self.editLayer >= 0:
                self.window.blit(p.transform.scale(self.ground, (self.blitSize, self.blitSize)), (self.blitX, self.blitY))
            if self.editLayer >= 1:
                self.window.blit(p.transform.scale(self.overlay, (self.blitSize, self.blitSize)), (self.blitX, self.blitY))
            if self.editLayer >= 4:
                self.window.blit(p.transform.scale(self.shadow, (self.blitSize, self.blitSize)), (self.blitX, self.blitY))
                