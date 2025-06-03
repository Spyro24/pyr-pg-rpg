"""
    Simple UI module for pyr_pg to create the UIs
    (c) 2025 Spyro24
"""
import pygame as p

class button:
    """Creates a simple UI button"""
    def __init__(self, window, pos: tuple, uiTileSize: int ,sizeInUiTiles: tuple, pathToButtonImage: str, fontSystem=None, text=None, alignment=4, zeroPos=(0, 0)):
        if type(pathToButtonImage) == str: 
            self.buttonTexture = p.image.load(pathToButtonImage)
        else:
            self.buttonTexture = pathToButtonImage
        self.buttonAlignment = alignment
        self.buttonText = text
        self.buttonSize = (uiTileSize * sizeInUiTiles[0],  uiTileSize * sizeInUiTiles[1])
        self.zeroPos = zeroPos
        self.window = window
        self.textureTiles = []
        self.__set_texture()
    
    def __set_texture(self):
        """Internal function to set the texture of the button"""
        tileSize = self.buttonTexture.get_size()[0] / 4
        buttonTiles = []
        for y in range(4):
            for x in range(4):
                buttonTiles.append(p.Surface((tileSize,tileSize), flags=p.SRCALPHA))
                buttonTiles[-1].blit(self.buttonTexture, (-(x * tileSize), -(y * tileSize)))
        self.buttonTiles = buttonTiles
    
    def check_click(self, mousePos: tuple):
        """Check if the button gets chovered with the mouse"""
        pass
    
    def show_button(self):
        """Shows the button on screen"""
        for n in range(16):
            self.window.blit(self.buttonTiles[n], (20 * n, 0))
