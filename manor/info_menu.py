import pygame as p
import pyr_pg

class infoMenu:
    def __init__(self, container: pyr_pg.container.container):
        self.modul_name = "info_menu"
        self.container = container
        self.cache = container.cache
        self.debug = container.debugMode
        self.window = container.window
        self.font: pyr_pg.font.font = container.font
        self.windowHasResized = False
        self.lastFunction = None
        self.textList = self.__read_info()
        self.textList.append(""); self.textList.append(f"PYR_PG VERSION {pyr_pg.version}")
        self.mouseHandler = container.mousHandler
        self.uses_pygame_ce = getattr(p, "IS_CE", False)
        self.setup()
        self.mousePos = (-1, -1)
        self.soundSystem = container.soundSystem
        
    def setup(self):
        self.lowestSize = self.window.lowestSize
        self.menuSize = self.lowestSize / 10
        self.fontSize = self.menuSize * 0.6
        self.backGround = p.transform.scale(self.cache["mainMenu/bg"], (self.lowestSize, self.lowestSize))
        self.textBackground = pyr_pg.ui.create_textbox((10,9), self.menuSize, self.cache["textbox/background/menu"])
        self.backButton = pyr_pg.ui.button(self.window, (5, 9.25), self.menuSize, (3, 1), self.cache["buttons/defaultBackground"], fontSystem=self.font, text="Back")
        if self.uses_pygame_ce:
            self.pygame_ce_pb_logo = self.__scale_image_by_h(self.cache["info/is_pb_pygame-ce"], self.menuSize * 1.5)
        self.__renderTextToTextbox()

    def main_loop(self) -> tuple[None | str, None | int, None]:
        '''Creating and handling of the main menu'''
        nextFuction = None
        self.mousePos = p.mouse.get_pos()
        for event in p.event.get():
            if event.type == p.QUIT:
                return ("QUIT", None, None)
            elif event.type == p.WINDOWRESIZED:
                return (None, 1, None)
            elif event.type == p.MOUSEBUTTONDOWN:
                mouseButton = p.mouse.get_pressed()
                mousePosition = self.mousePos
                if mouseButton[0]:
                    if self.backButton.check_click(mousePosition):
                        self.soundSystem.play("mouseClick")
                        nextFuction = self.lastFunction
        return (nextFuction, None, None)
    
    def render(self):
        self.window.blit(self.backGround, (0, 0))
        self.window.blit(self.textBackground, (0, 0))
        self.backButton.show_button()
        self.mouseHandler.set_cursor("normal")
        if self.backButton.check_hover(self.mousePos):
            self.mouseHandler.set_cursor("clickable")
        if self.uses_pygame_ce:
            mid_x, mid_y = self.pygame_ce_pb_logo.get_rect().center
            self.window.blit(self.pygame_ce_pb_logo, (self.menuSize * 5 - mid_x, self.menuSize * 6.5 - mid_y))
    
    def debug_render(self):
        self.backButton.draw_debug()
        
    def on_window_update(self):
        self.setup()
        self.windowHasResized = False
    
    #---Internal helper functions---
    def __scale_image_by_h(self, image: p.Surface, high: int):
        w, h = image.get_size()
        width = w / h * high
        return p.transform.scale(image, (width, high))
    
    def __read_info(self):
        infoFile = open("./info.txt", "r")
        info = []
        for line in infoFile.readlines():
            info.append(line.strip())
        infoFile.close()
        return info
        
    def __renderTextToTextbox(self):
        self.font.draw("Info", self.fontSize, (self.menuSize * 5.05, self.menuSize * 1.55), placement=4, color=(0, 0, 0), blitSurface=self.textBackground)
        self.font.draw("Info", self.fontSize, (self.menuSize * 5, self.menuSize * 1.5), placement=4, color=(200, 200, 200), blitSurface=self.textBackground)
        for n in range(len(self.textList)):
            self.font.draw(self.textList[n], self.fontSize * 0.5, (self.menuSize * 5.03, self.menuSize * (2.53 + (n * 0.4))), placement=4, color=(0, 0, 0), blitSurface=self.textBackground)
            self.font.draw(self.textList[n], self.fontSize * 0.5, (self.menuSize * 5, self.menuSize * (2.5 + (n * 0.4))), placement=4, color=(200, 200, 200), blitSurface=self.textBackground)
        pass