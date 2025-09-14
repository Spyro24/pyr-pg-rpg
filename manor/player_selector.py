import pygame as p
import pyr_pg

class playerSelector:
    def __init__(self, container: pyr_pg.container.container):
        '''Init the module for the loader'''
        self.modul_name = "player_selector"
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
        self.titlePNG = p.transform.scale(self.cache["mainMenu/title"], (self.menuSize * 4, self.menuSize * 2))
        self.newGameButton = self.createButton((5, 6.5), (4, 1), "New Game")
        self.loadGameButton = self.createButton((5, 8), (4, 1), "Load Game")
        self.settingsButton = self.createButton((9, 9), (1, 1), "", alignment=0, icon=self.cache["icons/settings"])
        self.infoButton = self.createButton((0, 9), (1, 1), "", alignment=0, icon=self.cache["icons/info"])
    
    def main_loop(self) -> tuple[None | str, None | int, None]:
        '''Creating and handling of the main menu'''
        for event in p.event.get():
            if event.type == p.WINDOWRESIZED:
                return (None, 1, None)
        return (None, None, None)
        '''
        settingsButton = self.createButton((9, 9), (1, 1), "", alignment=0, icon=self.cache["icons/settings"])
        infoButton = self.createButton((0, 9), (1, 1), "", alignment=0, icon=self.cache["icons/info"])
        #setup button vars
        while run: #main menu loop
            for event in p.event.get():
                if event.type == p.QUIT:
                    return ("QUIT", None, None)
                if event.type == p.WINDOWRESIZED:
                    return (None, 1, None)
                if event.type == p.MOUSEBUTTONDOWN:
                    m_click = p.mouse.get_pressed()
                    m_pos = p.mouse.get_pos()            
                    if m_click[0]:
                        if settingsButton.check_click(m_pos):
                            #self.audioSetup.play("sfx_1", "menu_click")
                            self.menu_settings()
                            redraw = True                
                        elif startNewButton.check_click(m_pos):
                            #self.audioSetup.play("sfx_1", "menu_click")
                            run = False
                            cleanUp = True
                            start_new_game = True
                        #if infoButton.check_click(m_pos):
                          #  self.info_box.show(self.info_text)
                            
            if redraw:
                
                #this is temp code for the button text until i have coded a button class
                startNewButton.show_button()
                loadGameButton.show_button()
                settingsButton.show_button()
                infoButton.show_button()
                #------
                redraw = False
                render = True
                if self.debug:
                    loadGameButton.draw_debug()
                    settingsButton.draw_debug()
                    infoButton.draw_debug()
            if render:
                p.display.flip()
                render = False
        if cleanUp:
            del startNewButton
            del loadGameButton
        if start_new_game:
            pass
        '''
    
    def render(self) -> None:
        self.window.blit(self.backGround, (0,0))
    
    def debug_render(self) -> None:
        pass
    
    def on_window_update(self):
        self.setup()
    
    #----Helper Functions
    def createButton(self, pos: tuple[int, int], size: tuple[int, int], text: str, alignment=4, icon=None, icon_scale=0.7):
        return pyr_pg.ui.button(self.window, pos, self.menuSize, size, self.cache["buttons/defaultBackground"], fontSystem=self.font, text=text, alignment=alignment, icon=icon, iconScale=icon_scale)
    
    def __create_textbox(self, tileSize: int, png: str) -> p.surface.Surface:
        box_tilesheet = p.image.load(png)
        textBoxSize = (8, 5)
        textbox_tile_list = []
        box_tilesize = box_tilesheet.get_size()[0] / 3
        for x_tile in range(3):
            for y_tile in range(3):
                cur_tile = p.surface.Surface((box_tilesize,box_tilesize), flags=p.SRCALPHA)
                cur_tile.blit(box_tilesheet,(-(x_tile * box_tilesize), -(y_tile * box_tilesize)))
                textbox_tile_list.append(p.transform.scale(cur_tile, (tileSize, tileSize)))
                
        textbox = p.surface.Surface((textBoxSize[0] * tileSize, textBoxSize[1] * tileSize), flags=p.SRCALPHA)
        textbox.blit(textbox_tile_list[0], (0, 0))
        textbox.blit(textbox_tile_list[8], ((textBoxSize[0] - 1) * tileSize,(textBoxSize[1] - 1) * tileSize))
        textbox.blit(textbox_tile_list[6], ((textBoxSize[0] - 1) * tileSize,0))
        textbox.blit(textbox_tile_list[2], (0, (textBoxSize[1] - 1) * tileSize))
        if textBoxSize[0] > 2:
            if textBoxSize[1] > 2:
                for x in range(textBoxSize[0] - 2):
                    textbox.blit(textbox_tile_list[3], ((x + 1) * tileSize,0))
                for y in range(textBoxSize[1] - 2):
                    textbox.blit(textbox_tile_list[1], (0,(y + 1) * tileSize))
                for x in range(textBoxSize[0] - 2):
                    textbox.blit(textbox_tile_list[5], ((x + 1) * tileSize,(textBoxSize[1] - 1) * tileSize))
                for y in range(textBoxSize[1] - 2):
                    textbox.blit(textbox_tile_list[7], ((textBoxSize[0] - 1) * tileSize,(y + 1) * tileSize))
                for x in range(textBoxSize[0] - 2):
                    for y in range(textBoxSize[1] - 2):
                        textbox.blit(textbox_tile_list[4], ((x + 1) * tileSize,(y + 1) * tileSize))
        return textbox

def scaleImageLowest(container: pyr_pg.container.container, image):
    return p.transform.scale(image, (container.window.lowestSize, container.window.lowestSize))