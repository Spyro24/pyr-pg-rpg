import pygame as p
import pyr_pg

class modulName:
    def __init__(self, container: pyr_pg.container.container):
        self.modul_name = "modul_name"
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
    
    def main_loop(self) -> tuple[None | str, None | int, None]:
        '''Creating and handling of the main menu'''
        for event in p.event.get():
            if event.type == p.WINDOWRESIZED:
                return (None, 1, None)
        return (None, None, None)
    
    def render(self):
        pass
    
    def debug_render(self):
        pass
    
    def on_window_update(self):
        self.windowHasResized = False