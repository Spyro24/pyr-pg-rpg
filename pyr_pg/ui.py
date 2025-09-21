"""
    Simple UI module for pyr_pg to create the UIs
    (c) 2025 Spyro24
"""
import pygame as p

class button:
    """Creates a simple UI button"""
    def __init__(self, window, pos: tuple, uiTileSize: int, sizeInUiTiles: tuple, pathToButtonImage: [str | p.Surface], fontSystem=None, text=None, alignment=4, zeroPos=(0, 0), fontSize=0.5, iconScale=1, icon: [p.Surface | str]=None):
        if type(pathToButtonImage) == p.surface.Surface:
            self.buttonTexture = pathToButtonImage
        else:
            self.buttonTexture = p.image.load(str(pathToButtonImage))
        self.buttonAlignment = alignment
        self.buttonText = text
        self.icon_size = uiTileSize
        self.icon = icon
        self.icon_scale = iconScale
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
        if self.icon != None:
            if type(self.icon) == str:
                icon = p.image.load(self.icon).convert_alpha()
            elif type(self.icon) == p.surface.Surface:
                icon = self.icon
            lowest_button_size = self.buttonTexture.get_height()
            if self.buttonTexture.get_width() < lowest_button_size:
                lowest_button_size = self.buttonTexture.get_width()
            icon = p.transform.scale(icon, (lowest_button_size * self.icon_scale, lowest_button_size * self.icon_scale))
            icon_size = icon.get_size()
            button_size = self.buttonTexture.get_size()
            self.buttonTexture.blit(icon, (button_size[0] / 2 - icon_size[0] / 2, button_size[1] / 2 - icon_size[1] / 2))
        if self.fontSystem != None and self.buttonText != None:
            self.fontSystem.draw(self.buttonText, self.fontSize, (self.buttonTexture.get_width() / 2, self.buttonTexture.get_height() / 2), placement=4, blitSurface=self.buttonTexture)
    
    def __calculateButtonPos(self):
        """Internal function to calculate the values for the button"""
        if self.buttonAlignment == 0:
            self.blitPos = (self.blitPos[0], self.blitPos[1])
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
        self.window.draw_rect(self.recRect, (255,255,0), width=3)

def create_textbox(sizeInTiles: tuple[int, int], tileSize: int, image: p.surface.Surface) -> p.surface.Surface:
        box_tilesheet = image
        textBoxSize = sizeInTiles
        textbox_tile_list = []
        box_tilesize = box_tilesheet.get_size()[0] / 3
        for x_tile in range(3):
            for y_tile in range(3):
                cur_tile = p.surface.Surface((box_tilesize,box_tilesize), flags=p.SRCALPHA)
                cur_tile.blit(box_tilesheet,(-(x_tile * box_tilesize), -(y_tile * box_tilesize)))
                textbox_tile_list.append(cur_tile)
                #textbox_tile_list.append(p.transform.scale(cur_tile, (tileSize, tileSize)))
                
        textbox = p.surface.Surface((textBoxSize[0] * box_tilesize, textBoxSize[1] * box_tilesize), flags=p.SRCALPHA)
        textbox.blit(textbox_tile_list[0], (0, 0))
        textbox.blit(textbox_tile_list[8], ((textBoxSize[0] - 1) * box_tilesize,(textBoxSize[1] - 1) * box_tilesize))
        textbox.blit(textbox_tile_list[6], ((textBoxSize[0] - 1) * box_tilesize,0))
        textbox.blit(textbox_tile_list[2], (0, (textBoxSize[1] - 1) * box_tilesize))
        if textBoxSize[0] > 2:
            if textBoxSize[1] > 2:
                for x in range(textBoxSize[0] - 2):
                    textbox.blit(textbox_tile_list[3], ((x + 1) * box_tilesize,0))
                for y in range(textBoxSize[1] - 2):
                    textbox.blit(textbox_tile_list[1], (0,(y + 1) * box_tilesize))
                for x in range(textBoxSize[0] - 2):
                    textbox.blit(textbox_tile_list[5], ((x + 1) * box_tilesize,(textBoxSize[1] - 1) * box_tilesize))
                for y in range(textBoxSize[1] - 2):
                    textbox.blit(textbox_tile_list[7], ((textBoxSize[0] - 1) * box_tilesize,(y + 1) * box_tilesize))
                for x in range(textBoxSize[0] - 2):
                    for y in range(textBoxSize[1] - 2):
                        textbox.blit(textbox_tile_list[4], ((x + 1) * box_tilesize,(y + 1) * box_tilesize))
        return p.transform.scale(textbox, (tileSize * textBoxSize[0], tileSize * textBoxSize[1]))

class plotter:
    def __init__(self, steps: int, min_max: tuple[int, int], color: tuple[tuple[int, int, int, int], tuple[int, int, int, int]]=((255, 0, 0, 0), (0, 255, 0, 0))):
        self.cur_step = 0
        self.cycle = False
        self.colors = color
        self.ixels = []
        self.steps = steps
        for step in range(self.steps):
            self.pixels.append(0)
        