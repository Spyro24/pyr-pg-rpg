"""
    Simple UI module for pyr_pg to create the UIs
    (c) 2025 Spyro24
"""
import pygame as p

class button:
    """Creates a simple UI button"""
    def __init__(self, window, pos: tuple, uiTileSize: int ,sizeInUiTiles: tuple, pathToButtonImage: str, fontSystem=None, text=None, alignment=4, zeroPos=(0, 0), fontSize=0.5, symbolSize=1, symbol: p.Surface=None):
        if type(pathToButtonImage) == str: 
            self.buttonTexture = p.image.load(pathToButtonImage)
        else:
            self.buttonTexture = pathToButtonImage
        self.buttonAlignment = alignment
        self.buttonText = text
        self.buttonSize = (uiTileSize * sizeInUiTiles[0],  uiTileSize * sizeInUiTiles[1])
        self.buttonRawSize = sizeInUiTiles
        self.zeroPos = zeroPos
        self.blitPos = (uiTileSize * pos[0], uiTileSize * pos[1])
        self.fontSize = uiTileSize * fontSize
        self.fontSystem = fontSystem
        self.window = window
        self.textureTiles = []
        self.recRect = p.Rect()
        self.__set_texture()
        self.__calculateButtonPos()
    
    def __set_texture(self):
        """Internal function to set the texture of the button"""
        tileSize = self.buttonTexture.get_size()[0] / 4
        buttonTiles = []
        for y in range(4):
            for x in range(4):
                buttonTiles.append(p.Surface((tileSize,tileSize), flags=p.SRCALPHA))
                buttonTiles[-1].blit(self.buttonTexture, (-(x * tileSize), -(y * tileSize)))
        finishButtonTexture = p.Surface((int(tileSize * self.buttonRawSize[0]), self.buttonRawSize[1] * tileSize), flags=p.SRCALPHA)
        if self.buttonRawSize[0] == 1:
            if self.buttonRawSize[1] == 1:
                finishButtonTexture.blit(buttonTiles[0],(0,0))
        elif self.buttonRawSize[0] >= 2:
            finishButtonTexture.blit(buttonTiles[1],(0,0))
            finishButtonTexture.blit(buttonTiles[3],((self.buttonRawSize[0] - 1) * tileSize,0))
            for n in range(self.buttonRawSize[0] - 2):
                finishButtonTexture.blit(buttonTiles[2],((n + 1) * tileSize,0))
        self.buttonTexture = p.transform.scale(finishButtonTexture, self.buttonSize)
        if self.fontSystem != None and self.buttonText != None:
            self.fontSystem.draw(self.buttonText, self.fontSize, (self.buttonTexture.get_width() / 2, self.buttonTexture.get_height() / 2), placement=4, blitSurface=self.buttonTexture)
    
    def __calculateButtonPos(self):
        """Internal function to calculate the values for the button"""
        if self.buttonAlignment == 0:
            pass
        elif self.buttonAlignment == 4:
            self.blitPos = (self.blitPos[0] - self.buttonTexture.get_width() / 2, self.blitPos[1] - self.buttonTexture.get_height() / 2)
        self.recRect = self.window.blit(self.buttonTexture, (self.zeroPos[0] + self.blitPos[0], self.zeroPos[1] + self.blitPos[1]))
    
    def check_click(self, mousePos: tuple):
        """Check if the button gets chovered with the mouse"""
        return self.recRect.collidepoint(mousePos)
    
    def show_button(self):
        """Shows the button on screen"""
        self.window.blit(self.buttonTexture, (self.zeroPos[0] + self.blitPos[0], self.zeroPos[1] + self.blitPos[1]))
        
    def draw_debug(self):
        """Only for debug purpose"""
        p.draw.rect(self.window, (255,255,0), self.recRect, width=3)
