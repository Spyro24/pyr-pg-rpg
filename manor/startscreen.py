import pygame as p
import time
import pyr_pg.math_

class startScreen:
    def __init__(self, container: pyr_pg.container.container):
        self.modul_name = "startScreen"
        self.container = container
        self.cache = container.cache
        self.debug = container.debugMode
        self.window = container.window
        self.font = container.font
        self.lastFunction = None
        self.windowHasResized = False
        self.setup()
        
    def setup(self):
        self.lowestSize = self.window.lowestSize
        self.menuSize = self.lowestSize / 10
        self.logo = self.cache["mainMenu/title"]
        self.ratio = self.logo.width / self.logo.height
        self.firstRenderTime = time.time()
        self.time = time.time()
        self.runTime = 0.35
    
    def main_loop(self) -> tuple[None | str, None | int, None]:
        '''Creating and handling of the main menu'''
        nextFunc = None 
        for event in p.event.get():
            if event.type == p.QUIT:
                return ("QUIT", None, None)
            elif event.type == p.WINDOWRESIZED:
                return (None, 1, None)
        self.time = time.time()
        if self.time - self.firstRenderTime > self.runTime:
            nextFunc = "main_menu"
        return (nextFunc, None, None)
    
    def render(self):
        sizeInterpol = pyr_pg.math_.interpolateVector((self.menuSize * 10, self.menuSize * 5),(self.menuSize * 4, self.menuSize * 2),  (self.time - self.firstRenderTime) / self.runTime)
        blitImage = p.transform.scale(self.logo, sizeInterpol)
        posInterpol = pyr_pg.math_.interpolateVector((self.menuSize * 5, self.menuSize * 2.5),(self.menuSize * 5, self.menuSize),  (self.time - self.firstRenderTime) / self.runTime)
        self.window.blit(blitImage, (posInterpol[0] - (blitImage.width / 2), posInterpol[1]))
    
    def debug_render(self):
        pass
    
    def on_window_update(self):
        self.lowestSize = self.window.lowestSize
        self.menuSize = self.lowestSize / 10
        self.windowHasResized = False