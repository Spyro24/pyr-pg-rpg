import pygame as p
import pyr_pg

class infoMenu:
    def __init__(self, container: pyr_pg.container.container):
        self.modul_name = "info_menu"
        self.container = container
        self.cache = container.cache
        self.debug = container.debugMode
        self.window = container.window
        self.font = container.font
        self.setup()
        
    def setup(self):
        self.lowestSize = self.window.lowestSize
        self.menuSize = self.lowestSize / 10
        self.backGround = p.transform.scale(self.cache["mainMenu/bg"], (self.lowestSize, self.lowestSize))
        self.textBackground = pyr_pg.ui.create_textbox((10,9), self.menuSize, self.cache["textbox/background/menu"])

    def main_loop(self) -> tuple[None | str, None | int, None]:
        '''Creating and handling of the main menu'''
        for event in p.event.get():
            if event.type == p.WINDOWRESIZED:
                return (None, 1, None)
        return (None, None, None)
    
    def render(self):
        self.window.blit(self.backGround, (0, 0))
        self.window.blit(self.textBackground, (0, 0))
    
    def debug_render(self):
        pass