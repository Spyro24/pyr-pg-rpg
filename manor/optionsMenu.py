import pygame as p
import pyr_pg

class optionsMenu:
    def __init__(self, container: pyr_pg.container.container):
        self.modul_name = "options_menu"
        self.container = container
        self.cache = container.cache
        self.debug = container.debugMode
        self.window = container.window
        self.font = container.font
        self.lastFunction = None
        self.windowHasResized = False
        self.setup()
        self.index = 0
        self.maxIndex = 0
        
    def setup(self):
        self.lowestSize = self.window.lowestSize
        self.menuSize = self.lowestSize / 10
    
    def main_loop(self) -> tuple[None | str, None | int, None]:
        '''Creating and handling of the main menu'''
        for event in p.event.get():
            if event.type == p.QUIT:
                return ("QUIT", None, None)
            elif event.type == p.WINDOWRESIZED:
                return (None, 1, None)
            elif event.type == p.KEYDOWN:
                if event.key == p.K_w:
                    if self.index > 0:
                        self.index -= 1
        return (None, None, None)
    
    def render(self):
        pass
    
    def debug_render(self):
        pass
    
    def on_window_update(self):
        self.windowHasResized = False