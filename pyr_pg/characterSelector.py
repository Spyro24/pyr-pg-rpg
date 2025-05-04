#!/bin/python3
"""
    Character Selector for pyr_pg
    (c) 2025 Spyro24
"""
import os
import pygame as p
import time
import pyr_pg

class characterSelector:
    def __init__(self, characterPath: str, runtimeStore: dict, debug=False):
        self.window = runtimeStore[10][13] #the runtimestore system is not available in the module. runtimeStore[13] = rs.Window
        self.characterPath = characterPath
        self.runtimeStore = runtimeStore
        self.fontSystem = runtimeStore[15]
        self.__envReady()
        self.debug = debug
        self.DebugRects = []
        
    def __envReady(self) -> None:
        winW, winH = self.window.get_size()
        self.windowMidpoint = self.window.get_rect().center
        self.lowestSize = winH
        if winH > winW: self.lowestSize = winW
        self.tileSize = self.lowestSize / 10
        self.virtWindow = p.Rect(self.windowMidpoint[0] - self.lowestSize / 2, self.windowMidpoint[1] - self.lowestSize / 2, self.lowestSize, self.lowestSize)
        self.zeroPos = self.virtWindow.topleft
        
    def __debug(self) -> None:
        p.draw.rect(self.window, (0, 255, 0), self.virtWindow, width=3)
        p.draw.rect(self.window, (128, 128, 0), self.DebugRects[0], width=3)
        for rect in self.charactersPlacerRects:
            p.draw.rect(self.window, (128, 0, 0), rect, width=3)
    
    def openSelector(self, assets: dict) -> tuple:#[characterConfForLoader: str, forward: bool, exit: bool]:
        self.selectedCharacter = 0
        FPS = 0
        RFPS = 0
        plotTime = 0
        self.__load_sprites()
        self.backgroud = p.transform.scale(assets["bg"], (self.lowestSize, self.lowestSize))
        self.fdButtonTexture = p.transform.scale(assets["forward"], (self.tileSize, self.tileSize))
        self.backButtonTexture = p.transform.scale(assets["back"], (self.tileSize, self.tileSize))
        self.textBoxBG = self.__create_textbox(self.tileSize, "./res/textboxes/gray_rounded_playerSelectort.png")
        fdButton = self.window.blit(self.fdButtonTexture,(self.virtWindow.right - self.tileSize, self.virtWindow.bottom - self.tileSize))
        backButton = self.window.blit(self.backButtonTexture,(self.virtWindow.left, self.virtWindow.bottom - self.tileSize))
        self.charactersPlacerRects = [p.rect.Rect((self.zeroPos[0], self.zeroPos[1] + self.tileSize / 2 * 3), (self.tileSize, self.tileSize)),
                                      p.rect.Rect((self.zeroPos[0] + self.tileSize, self.zeroPos[1] + self.tileSize),(self.tileSize * 2, self.tileSize * 2)),
                                      p.rect.Rect((self.zeroPos[0] + self.tileSize * 3, self.zeroPos[1]),(self.tileSize * 4, self.tileSize * 4)),
                                      p.rect.Rect((self.zeroPos[0] + self.tileSize * 7, self.zeroPos[1] + self.tileSize),(self.tileSize * 2, self.tileSize * 2)),
                                      p.rect.Rect((self.zeroPos[0] + self.tileSize * 9, self.zeroPos[1] + self.tileSize / 2 * 3), (self.tileSize, self.tileSize))]
        self.DebugRects.append(fdButton)
        self.microTiling = self.tileSize / 10
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
        
    def render(self) -> None:
        self.window.fill((0, 0, 0))
        self.window.blit(self.backgroud, self.virtWindow.topleft)
        self.window.blit(self.fdButtonTexture,(self.virtWindow.right - self.tileSize, self.virtWindow.bottom - self.tileSize))
        self.window.blit(self.textBoxBG,(self.virtWindow.left + self.tileSize, self.virtWindow.bottom - self.tileSize * 5))
        self.window.blit(self.backButtonTexture,(self.virtWindow.left, self.virtWindow.bottom - self.tileSize))
        for n in range(-2,3):
            self.window.blit(p.transform.scale(self.playableCharacters[(self.selectedCharacter + n) % self.maxAvailablePlayableChars]['cutingEdge']['character_sel_picture'], self.charactersPlacerRects[n + 2].size),self.charactersPlacerRects[n + 2].topleft)
        self.fontSystem.draw(self.playableCharacters[self.selectedCharacter]['Name'], self.fontSize, (self.virtWindow.left + self.tileSize *5 ,self.virtWindow.top + self.tileSize * 6 + self.microTiling), placement=1)
        descLen = len(self.playableCharacters[self.selectedCharacter]['Desc'])
        if descLen > 19:
            self.fontSystem.draw(self.playableCharacters[self.selectedCharacter]['Desc'][0:18], self.fontSize * 0.75, (self.virtWindow.left + self.tileSize *5 ,self.virtWindow.top + self.tileSize * 7 + self.microTiling), placement=1, color=(200,200,200))
            self.fontSystem.draw(self.playableCharacters[self.selectedCharacter]['Desc'][18:descLen], self.fontSize * 0.75, (self.virtWindow.left + self.tileSize *5 ,self.virtWindow.top + self.tileSize * 7 + self.fontSize + self.microTiling), placement=1, color=(200,200,200))
        else:
            self.fontSystem.draw(self.playableCharacters[self.selectedCharacter]['Desc'], self.fontSize * 0.75, (self.virtWindow.left + self.tileSize *5 ,self.virtWindow.top + self.tileSize * 7 + self.microTiling), placement=1, color=(200,200,200))
        if self.debug:
            self.__debug()
        p.display.flip()
        
    #---Internal Helper Functions---
    def __load_sprites(self) -> None:
        spritePath = "./res/characters"
        allData = os.listdir(spritePath)
        playableChars = []
        for string in allData:
            if string.endswith(".desc"):
                playableChars.append(string)
        if self.debug:
            print(playableChars)
        self.playableCharacters = []
        for desc in playableChars:
            self.playableCharacters.append({"Name":None, "Desc":None, "cutingEdge":None, "charDescFile": desc[0:-5]})
            descFile = open(os.path.join(spritePath, desc), "r")
            descContent = descFile.read().splitlines()
            descFile.close()
            self.playableCharacters[-1]["Name"] = descContent[0]
            self.playableCharacters[-1]["Desc"] = descContent[1]
            self.playableCharacters[-1]["cutingEdge"] = pyr_pg.cutting_edge.CuttingEdge(descContent[2], spritePath, debug=self.debug).return_sprite_table()
        self.maxAvailablePlayableChars = len(self.playableCharacters)
        if self.debug:
            print(self.playableCharacters)
            print(self.maxAvailablePlayableChars)
        
    def __create_textbox(self, tileSize: int, png: str) -> p.surface.Surface:
        box_tilesheet = p.image.load(png)
        textBoxSize = (8,5)
        textbox_tile_list = []
        box_tilesize = box_tilesheet.get_size()[0] / 3
        for x_tile in range(3):
            for y_tile in range(3):
                cur_tile = p.surface.Surface((box_tilesize,box_tilesize), flags=p.SRCALPHA)
                cur_tile.blit(box_tilesheet,(-(x_tile * box_tilesize), -(y_tile * box_tilesize)))
                textbox_tile_list.append(p.transform.scale(cur_tile,(tileSize, tileSize)))
                
        textbox = p.surface.Surface((textBoxSize[0] * tileSize, textBoxSize[1] * tileSize), flags=p.SRCALPHA)
        textbox.blit(textbox_tile_list[0],(0,0))
        textbox.blit(textbox_tile_list[8],((textBoxSize[0] - 1) * tileSize,(textBoxSize[1] - 1) * tileSize))
        textbox.blit(textbox_tile_list[6],((textBoxSize[0] - 1) * tileSize,0))
        textbox.blit(textbox_tile_list[2],(0,(textBoxSize[1] - 1) * tileSize))
        if textBoxSize[0] > 2:
            if textBoxSize[1] > 2:
                for x in range(textBoxSize[0] - 2):
                    textbox.blit(textbox_tile_list[3],((x + 1) * tileSize,0))
                for y in range(textBoxSize[1] - 2):
                    textbox.blit(textbox_tile_list[1],(0,(y + 1) * tileSize))
                for x in range(textBoxSize[0] - 2):
                    textbox.blit(textbox_tile_list[5],((x + 1) * tileSize,(textBoxSize[1] - 1) * tileSize))
                for y in range(textBoxSize[1] - 2):
                    textbox.blit(textbox_tile_list[7],((textBoxSize[0] - 1) * tileSize,(y + 1) * tileSize))
                for x in range(textBoxSize[0] - 2):
                    for y in range(textBoxSize[1] - 2):
                        textbox.blit(textbox_tile_list[4],((x + 1) * tileSize,(y + 1) * tileSize))
        return textbox