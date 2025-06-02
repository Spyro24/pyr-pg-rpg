import pygame as p

class button:
    def __init__(self, windows, pos: tuple, uiSize: int ,sizeInUiTiles: tuple, pathToButtonImage: str, fontSystem=None, text=None, alignment=4, zeroPos=(0, 0)):
        self.buttonTexture = p.image.load(pathToButtonImage)
        self.
        self.zeroPos = zeroPos
        
    def __setTexture(self):
        pass
    
    def checkClick(self, mousePos: tuple):
        pass
    
    def showButton(self):
        pass