import pygame as p
import pyr_pg

class game:
    def __init__(self, container: pyr_pg.container.container):
        self.modul_name = "main_game"
        self.container = container
        self.cache = container.cache
        self.debug = container.debugMode
        self.window = container.window
        self.font = container.font
        self.mapSystem = container.mapSystem
        self.lastFunction = None
        self.windowHasResized = False
        self.perlinNoise = pyr_pg.math_.PerlinNoise2D(seed=255)
        self.setup()
        
    def setup(self):
        self.lowestSize = self.window.lowestSize
    
    def main_loop(self) -> tuple[None | str, None | int, None]:
        '''Creating and handling of the main menu'''
        for event in p.event.get():
            if event.type == p.QUIT:
                return ("QUIT", None, None)
            elif event.type == p.WINDOWRESIZED:
                return (None, 1, None)
        return (None, None, None)
    
    def render(self):
        for y in range(16):
            for x in range(16):
                noise = self.perlinNoise.noise(x*0.1, y*0.1)
                if noise < 0.4:
                    self.mapSystem.blit_tile("ground", 5, (x,y))
                elif noise < 0.6:
                    self.mapSystem.blit_tile("ground", 4, (x,y))
                else:
                    self.mapSystem.blit_tile("ground", 1, (x,y))
        self.window.blit(p.transform.scale(self.mapSystem.ground, (self.lowestSize, self.lowestSize)))
    
    def debug_render(self):
        pass
    
    def on_window_update(self):
        self.windowHasResized = False
        self.setup()