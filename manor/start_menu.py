import pyr_pg
import pygame as p

class startMenu():
    def __init__(self, container: pyr_pg.container.container):
        '''Setup the game ENV'''
        self.container = container
        self.cache = container.cache
        self.debug = container.debugMode
        self.window = container.window
        self.setup()
    
    def setup(self):
        self.backGround = p.transform.scale(self.cache["mainMenu/bg"], (self.lowestSize, self.lowestSize))
        self.titlePNG = p.transform.scale(self.cache["mainMenu/title"], (self.menuSize * 4, self.menuSize * 2))

    def main_loop(self) -> None:
        '''Creating and handling of the main menu'''
        #scale all mainmenu images
        title = p.transform.scale(self.cache["mainMenu/title"], (self.menuSize * 4, self.menuSize * 2))
        #buttons
        startNewButton = self.createButton((5, 6.5), (4, 1), "New Game")
        loadGameButton = self.createButton((5, 8), (4, 1), "Load Game")
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
                    startNewButton.draw_debug()
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
    
    def render(self):
        self.game_win.blit(self.backGround, (0,0))
        self.game_win.blit(title, (self.menuSize * 3, self.menuSize))
    
    def debug_render(self):
        pass
    
    def on_window_update(self):
        self.lowestSize = self.window.lowestSize
        
    def menu_settings(self):
        render = True
        settings_menu = True
        redraw = True
        back_button = p.transform.scale(p.image.load("./images/main_menu/settings/back.png"), (self.menuSize, self.menuSize))
        background = p.transform.scale(p.image.load("./images/main_menu/back.png"), (self.lowestSize, self.lowestSize))
        seting_background = p.transform.scale(p.image.load("./images/main_menu/settings/settings_back.png"), (self.menuSize * 8, self.menuSize * 8))
        #setup rectangle buttons
        back = 0
        while settings_menu:
            for event in p.event.get():
                if event.type == p.QUIT:
                    settings_menu = False
                    self.close_game()            
            m_click = p.mouse.get_pressed()
            m_pos = p.mouse.get_pos()                    
            if redraw:
                self.game_win.blit(background,(self.b_pos_x, self.b_pos_y))
                back = self.game_win.blit(back_button, (self.b_pos_x, self.b_pos_y))
                self.game_win.blit(seting_background, (self.b_pos_x + self.menuSize, self.b_pos_y + self.menuSize))
                if self.debug:
                    pass
                render = True
                redraw = False            
            if render:
                p.display.flip()
                render = False                
            if m_click[0]:
                if back.collidepoint(m_pos):
                    settings_menu = False
    
    #----Helper Functions
    def createButton(self, pos: tuple[int, int], size: tuple[int, int], text: str, alignment=4, icon=None, icon_scale=0.7):
        return pyr_pg.ui.button(self.window, pos, self.menuSize, size, self.cache["buttons/defaultBackground"], fontSystem=self.font, text=text, zeroPos=(self.b_pos_x, self.b_pos_y), alignment=alignment, icon=icon, iconScale=icon_scale)

def scaleImageLowest(container: pyr_pg.container.container, image):
    return p.transform.scale(image, (container.window.lowestSize, container.window.lowestSize))