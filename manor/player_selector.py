import pygame as p
import pyr_pg
import os

class playerSelector:
    def __init__(self, container: pyr_pg.container.container):
        '''Init the module for the loader'''
        self.modul_name = "player_selector"
        self.container = container
        self.cache = container.cache
        self.debug = container.debugMode
        self.window = container.window
        self.font = container.font
        self.windowHasResized = False
        self.lastFunction = None
        self.maxAvailableCharacters = 0
        self.availablePlayers = []
        self.prepare_players()
        self.setup()
    
    def setup(self):
        self.lowestSize = self.window.lowestSize
        self.menuSize = self.lowestSize / 10
        self.fontSize = self.menuSize * 0.6
        self.backGround = p.transform.scale(self.cache["mainMenu/bg"], (self.lowestSize, self.lowestSize))
        self.charactersPlacerRects = [p.rect.Rect((0, self.menuSize / 2 * 3), (self.menuSize, self.menuSize)),
                                      p.rect.Rect((self.menuSize, self.menuSize), (self.menuSize * 2, self.menuSize * 2)),
                                      p.rect.Rect((self.menuSize * 3, 0), (self.menuSize * 4, self.menuSize * 4)),
                                      p.rect.Rect((self.menuSize * 7, self.menuSize), (self.menuSize * 2, self.menuSize * 2)),
                                      p.rect.Rect((self.menuSize * 9, self.menuSize / 2 * 3), (self.menuSize, self.menuSize))]
        self.textBackground = pyr_pg.ui.create_textbox((8, 5), self.menuSize, self.cache["textbox/background/menu"])
        self.textBGBlitPos = (self.menuSize, self.menuSize * 5)
        
    def main_loop(self) -> tuple[None | str, None | int, None]:
        '''Creating and handling of the main menu'''
        for event in p.event.get():
            if event.type == p.WINDOWRESIZED:
                return (None, 1, None)
        return (None, None, None)
        '''
         cleanUp = False
        self.selectedCharacter = 0
        FPS = 0
        RFPS = 0
        plotTime = 0
        self.__load_sprites()
        self.fdButtonTexture = p.transform.scale(assets["forward"], (self.menuSize, self.menuSize))
        self.backButtonTexture = p.transform.scale(assets["back"], (self.menuSize, self.menuSize))
        self.textBoxBG = self.__create_textbox(self.menuSize, "./res/textboxes/gray_rounded_playerSelectort.png")
        fdButton = self.window.blit(self.fdButtonTexture,(self.virtWindow.right - self.menuSize, self.virtWindow.bottom - self.menuSize))
        backButton = self.window.blit(self.backButtonTexture,(self.virtWindow.left, self.virtWindow.bottom - self.menuSize))
        self.DebugRects.append(fdButton)
        self.microTiling = self.menuSize / 10
        self.fontSize = self.microTiling * 6
        run = True
        renderTime = 1 / self.runtimeStore[2] #rs.DefaultFps
        lastFrame = 0
        while run:
            frameTime = time.time() #the time the frame has begin to render
            for event in p.event.get():
                if event.type == p.QUIT:
                    return (None, False, True)
                if event.type == p.MOUSEBUTTONDOWN:
                    mouseKeys = p.mouse.get_pressed()
                    mousePos = p.mouse.get_pos()
                    if mouseKeys[0]:
                        if fdButton.collidepoint(mousePos):
                            run = False
                        elif backButton.collidepoint(mousePos):
                            run = False
                            self.cleanUp()
                            return ("", False, False)
                if event.type == p.KEYDOWN:
                    if event.key == p.K_LEFT or event.key == p.K_a:
                        self.selectedCharacter = (self.selectedCharacter - 1) % self.maxAvailablePlayableChars
                    elif event.key == p.K_RIGHT or event.key == p.K_d:
                        self.selectedCharacter = (self.selectedCharacter + 1) % self.maxAvailablePlayableChars
                        
            if frameTime - renderTime > lastFrame:
                lastFrame = frameTime
                self.render()
                RFPS += 1
            FPS += 1
            if self.debug:
                if plotTime + 1 < frameTime:
                    plotTime = frameTime
                    print("FPS:", FPS, "RFPS:", RFPS)
                    FPS = 0; RFPS = 0
        return (self.playableCharacters[self.selectedCharacter]['charDescFile'], True, False)
        '''
    
    def render(self) -> None:
        self.window.blit(self.backGround, (0,0))
        self.window.blit(self.textBackground, self.textBGBlitPos)
    
    def debug_render(self) -> None:
        for rects in self.charactersPlacerRects:
            rect = (rects[0] + self.window.zeroPos[0], rects[1] + self.window.zeroPos[1], rects[2], rects[3])
            self.window.draw_rect(rect, (255, 0, 0), width=3)
    
    def on_window_update(self):
        self.setup()
        self.windowHasResized = False
    
    #----Helper Functions
    def createButton(self, pos: tuple[int, int], size: tuple[int, int], text: str, alignment=4, icon=None, icon_scale=0.7):
        return pyr_pg.ui.button(self.window, pos, self.menuSize, size, self.cache["buttons/defaultBackground"], fontSystem=self.font, text=text, alignment=alignment, icon=icon, iconScale=icon_scale)
    
    def prepare_players(self):
        players = []
        for file in os.listdir("./res/characters/"):
            if file.endswith(".desc"):
                players.append(file)
        for player in players:
            self.availablePlayers.append({"Name": None, "Desc": None, "cutingEdge": None, "charDescFile": player[0:-5]})
            descContent = descFile.read().splitlines()
            descFile.close()
            self.availablePlayers[-1]["Name"] = descContent[0]
            self.availablePlayers[-1]["Desc"] = descContent[1]
        print(players)

def scaleImageLowest(container: pyr_pg.container.container, image):
    return p.transform.scale(image, (container.window.lowestSize, container.window.lowestSize))