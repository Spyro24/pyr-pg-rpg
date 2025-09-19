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
        self.lastFunction = None
        self.setup()
        
    def setup(self):
        self.lowestSize = self.window.lowestSize
        self.menuSize = self.lowestSize / 10
        self.fontSize = self.menuSize * 0.8
        self.backGround = p.transform.scale(self.cache["mainMenu/bg"], (self.lowestSize, self.lowestSize))
        self.textBackground = pyr_pg.ui.create_textbox((10,9), self.menuSize, self.cache["textbox/background/menu"])
        self.backButton = pyr_pg.ui.button(self.window, (5, 9.25), self.menuSize, (3, 1), self.cache["buttons/defaultBackground"], fontSystem=self.font, text="Back")

    def main_loop(self) -> tuple[None | str, None | int, None]:
        '''Creating and handling of the main menu'''
        nextFuction = None
        for event in p.event.get():
            if event.type == p.QUIT:
                return ("QUIT", None, None)
            elif event.type == p.WINDOWRESIZED:
                return (None, 1, None)
            elif event.type == p.MOUSEBUTTONDOWN:
                mouseButton = p.mouse.get_pressed()
                mousePosition = p.mouse.get_pos()
                if mouseButton[0]:
                    if self.backButton.check_click(mousePosition):
                        nextFuction = self.lastFunction
        return (nextFuction, None, None)
    
    def render(self):
        self.window.blit(self.backGround, (0, 0))
        self.window.blit(self.textBackground, (0, 0))
        self.backButton.show_button()
    
    def debug_render(self):
        self.backButton.draw_debug()