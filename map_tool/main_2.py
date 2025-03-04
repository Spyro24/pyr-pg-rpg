import pygame as p
import map_pg
import time
from multiprocessing import Pool

class multi_editor():
    def __init__(self, log=print):
        log("[MAP_TOOL](INIT) init map tool")
        self.debug            = False
        self.logsys           = log
        self.window           = p.display.set_mode((720,480), flags=p.RESIZABLE)
        self.ui_size          = 30
        self.font_size        = self.ui_size - 2
        self.font             = map_pg.font.font(self.window, "./res/fonts/standard")
        self.colors           = [(0, 133, 255)]
        self.global_config    = {}
        self.images           = {}
        self.buttons          = []
        self.menus            = []
        self.visible_rects    = []
        self.editor_mode      = 0
        self.editor_md_tag    = "Mapeditor"
        self.tilesConfig      = {"size":"6x12"}
        self.tile_sheetSize   = 12*6
        self.tileselector_pos = 0
        self.selected_tile    = 0
        self.editigLayers     = ["Ground", "GroundOverlay", "PlayerOverlay", "OverOverlay", "Shadows"]
        self.mouse_pressed    = False
        self.cur_layer        = 0
        self.cur_tilsesel_pos = 0
        self.main_menu_entrys = {"Settings":self.settings, "About":self.VOID, "Exit":self.end}
        logo                  = p.image.load("./res/symbols/logo.png")
        logo_scaled           = p.transform.scale(logo, (self.font_size, self.font_size))
        self.images["splash"] = logo
        self.images["logo_scaled"] = logo_scaled
        self.progressBarLoadSplash([self.load_maped, #load the mapeditor env
                                    self.cachingTiles, #loading and caching tilessets
                                    self.calculateUiRects, # calculate the position of the UI Rectangles
                                    self.setupMapeditor, #setup the mapediting system
                                    self.addTilesToMaped], #add the cached tiles to the mapedting system],
                                   self.colors[0])
        self.mapEditorSystem.createMap()
        self.mapEditorSystem.editLayer = self.cur_layer
        self.main_loop()
        
    def main_loop(self):
        run = True
        update = True
        while run:
            key_ar = p.key.get_pressed()
            for event in p.event.get():
                if event.type == p.QUIT:
                    self.end()
                if event.type == p.KEYDOWN or event.type == p.KEYUP:
                    if event.mod & p.KMOD_CTRL:
                        if key_ar[114]:
                            self.reload_ui()
                            update = True
                        elif key_ar[43]:
                            self.ui_size += 1
                            self.reload_ui()
                            update = True
                        elif key_ar[45]:
                            self.ui_size -= 1
                            self.reload_ui()
                            update = True
                    else:
                        if self.editor_mode == 0:
                            checkForUpdate = True
                            if key_ar[p.K_UP]:
                                if self.cur_layer < 4:
                                    self.cur_layer += 1
                            elif key_ar[p.K_DOWN]:
                                if self.cur_layer > 0:
                                    self.cur_layer -= 1
                            elif key_ar[p.K_w]:
                                self.mapEditorSystem.moveMap((0,-1))
                            elif key_ar[p.K_s]:
                                self.mapEditorSystem.moveMap((0,1))
                            elif key_ar[p.K_a]:
                                self.mapEditorSystem.moveMap((-1,0))
                            elif key_ar[p.K_d]:
                                self.mapEditorSystem.moveMap((1,0))
                            elif key_ar[p.K_e]:
                                self.tileselector_pos = 0
                            else:
                                checkForUpdate = False
                            if checkForUpdate:
                                update = True
            
            mpos   = p.mouse.get_pos()
            mclick = p.mouse.get_pressed()
            '''
            for key in range(0, len(key_ar)):
                if key_ar[key]:
                    print(key)
            '''
            
            if mclick[0] == True:
                self.menus[0].open(mpos)
                self.menus[1].open(mpos)
                update = True
                if self.editor_mode == 0:
                    if self.mouse_pressed == False:
                        if self.tile_choser_rect.collidepoint(mpos):
                            self.tileselector_pos = self.tileselector_clgr.return_number(mpos) + (self.tile_sheetSize * self.cur_tilsesel_pos) + 1
                            if self.selector_buttons.activate_rect.collidepoint(mpos):
                                click_pos = self.selector_buttons.return_number(mpos)
                                if click_pos == 0:
                                    if self.cur_tilsesel_pos > 0:
                                        self.cur_tilsesel_pos -= 1
                                        print(self.cur_tilsesel_pos)
                                elif click_pos == 5:
                                    self.cur_tilsesel_pos += 1
                                    print(self.cur_tilsesel_pos)
                    if self.mapEditorSystem.inputGrid.activate_rect.collidepoint(mpos):
                        placePos  = self.mapEditorSystem.inputGrid.get_click(mpos)
                        insertion = self.mapEditorSystem.inputGrid.return_number(mpos)
                        if placePos != (-1, -1):
                            self.mapEditorSystem.blitTile(placePos, self.tileselector_pos)
                            if 0 <= self.cur_layer <= 4:
                                self.mapFileHandleSystem.mapAray[self.cur_layer].pop(insertion)
                                self.mapFileHandleSystem.mapAray[self.cur_layer].insert(insertion, self.tileselector_pos)
                        update = True
                self.mouse_pressed = True
            else:
                self.mouse_pressed = False
                
            if update:
                self.mapEditorSystem.editLayer = self.cur_layer # set the Mapedtool layer to the editing layer
                self.window.fill("BLACK")
                self.menu_bar()
                if self.editor_mode == 0:
                    p.draw.rect(self.window, (100,100,100), self.tile_choser_rect, 3)
                    p.draw.rect(self.window, (100,100,100), self.maped_rect, 3)
                    p.draw.rect(self.window, (100,100,100), self.statusRect, 3)
                    rectX, rectY = self.statusRect.topleft
                    self.font.draw("CurMap=" + str(self.mapFileHandleSystem.mapX) + "_" + str(self.mapFileHandleSystem.mapY), self.font_size, (rectX + self.ui_size,rectY + self.ui_size))
                    if self.cur_layer == 0:
                        self.blitToTileSelector(self.tilesGround)
                    elif self.cur_layer == 1:
                        self.blitToTileSelector(self.tilesGroundOverlay)
                    elif self.cur_layer == 4:
                        p.draw.rect(self.window, (255,255,255), self.tile_choser_rect)
                        self.blitToTileSelector(self.tilesShadow)
                    rct_px, rct_py = tuple(self.tile_choser_rect.bottomleft)
                    for n in range(6):
                        self.window.blit(p.transform.scale(self.listSelectButtons[n], (self.ui_size, self.ui_size)), (rct_px + self.ui_size + (self.ui_size * n), rct_py - self.ui_size))
                    self.mapEditorSystem.render()
                    if self.debug:
                        self.tileselector_clgr.debug(self.window)
                        self.selector_buttons.debug(self.window)
                        self.mapEditorSystem.inputGrid.debug(self.window)
                elif self.editor_mode == 1:
                    self.font.draw("Coming Soon", self.font_size, (self.ui_size * 10, self.ui_size * 5))
                self.left_side_menu()
                p.draw.rect(self.window, (100,100,100), self.tool_options_rect, 3)
                p.display.flip()
                update = False
    
    def show_splash(self):
        win_w, win_h       = self.window.get_size()
        splash             = p.transform.scale(self.images["splash"], (int(win_h/2), int(win_h/2)))
        splash_w, splash_h = splash.get_size()
        self.window.fill((0, 0, 0))
        self.window.blit(splash, ((win_w / 2) - (splash_w / 2), 0))
        
    def settings(self):
        pass
    
    def menu_bar(self):
        self.window.blit(self.images["logo_scaled"],(0,0))
        
    def left_side_menu(self):
        p.draw.rect(self.window, self.colors[0], self.visible_rects[0])
        self.font.draw(self.editor_md_tag, self.font_size, self.visible_rects[0].topleft)
        
    def reload_ui(self):
        self.logsys("[MAP_TOOL][UI](reload) Reload UI")
        self.progressBarLoadSplash([self.calculateUiRects, self.rescale, self.replaceObjects, self.mapEditorSystem.calcPos], self.colors[0])
    
    def rescale(self, x):
        if x == 0:
            return "Rescaling"
        else:
            self.visible_rects[0].update((self.ui_size, self.ui_size * 4),(self.ui_size * 6, self.ui_size))
            self.menus[1].rescale(self.font_size, (self.ui_size, self.ui_size * 5), 6, self.buttons[1])
        
    def set_mode_mapeditor(self):
        self.editor_md_tag = "Mapeditor"
        self.editor_mode   = 0
    
    def set_mode_paint(self):
        self.editor_md_tag = "Paintmode"
        self.editor_mode   = 1
        
    def end(self):
        self.mapFileHandleSystem.saveMap()
        p.quit()
        exit(0)
        
    def progressBarLoadSplash(self, functionList, color):
        winW, winH   = self.window.get_size()
        winXC, winYC = self.window.get_rect().center
        percentSteps = 1 / len(functionList)
        emptyBar     = p.Rect((winW / 4, winH / 16 * 12),(winW / 4 * 2, winH / 16))
        exeStep      = 0
        fontSize     = winH / 16
        for function in functionList:
            exeStep += 1
            displayText = function(0)
            self.window.fill((0,0,0))
            self.show_splash()
            p.draw.rect(self.window, color, emptyBar, int(fontSize / 10))
            p.draw.rect(self.window, color, ((winW / 4, winH / 16 * 12),((winW / 4 * 2) * (exeStep * percentSteps), winH / 16)))
            self.font.draw(str(displayText), fontSize, (winW / 4, winH / 16 * 12 - fontSize))
            p.display.flip()
            function(1)
            #time.sleep(1)
        
    
    def VOID(self):
        pass
    
    #---repeating functions--------
    def blitToTileSelector(self, tileSet):
        rct_px, rct_py = tuple(self.tile_choser_rect.topleft)
        c = 0
        try:
            for y in range(12):
                for x in range(6):
                    self.window.blit(p.transform.scale(tileSet[c + (self.cur_tilsesel_pos * self.tile_sheetSize)], (self.ui_size, self.ui_size)), (rct_px + self.ui_size + (self.ui_size * x), rct_py + (self.ui_size * y)))
                    c += 1
        except IndexError as err:
            if self.cur_tilsesel_pos <= 0:
                pass
            else:
                self.cur_tilsesel_pos -= 1
                self.blitToTileSelector(tileSet)
    #---Loading Function Section---
    def addTilesToMaped(self, x):
        if x == 0:
            return "Ading Tiles"
        else:
            self.mapEditorSystem.addTiles(self.tilesGround, "ground")
            self.mapEditorSystem.addTiles(self.tilesGroundOverlay, "overlay")
            self.mapEditorSystem.addTiles(self.tilesShadow, "shadow")
        
    def cachingTiles(self, x):
        if x == 0:
            return "Caching Tiles"
        else:
            self.tilesGround        = map_pg.tile_handler.tile_handler("../tiles/ground",   self.tilesConfig).return_tiles()
            self.tilesGroundOverlay = map_pg.tile_handler.tile_handler("../tiles/groundov", self.tilesConfig).return_tiles()
            self.tilesPlayerOverlay = map_pg.tile_handler.tile_handler("../tiles/overlay",  self.tilesConfig).return_tiles()
            self.tilesShadow        = map_pg.tile_handler.tile_handler("../tiles/shadows",  self.tilesConfig).return_tiles()
            
    def load_maped(self, x):
        if x == 0:
            return "Load Mapeditor"
        else:
            self.buttons.append(self.window.blit(self.images["logo_scaled"],(0,0)))
            self.visible_rects.append(p.Rect((self.ui_size, self.ui_size * 4),(self.ui_size * 6, self.ui_size)))
            self.buttons.append(self.visible_rects[0])
            self.menus.append(map_pg.DropDown.drop_down(self.window, self.font_size, (0, self.font_size), 5, self.font, [(0, 128, 128),(128, 0, 128)], self.buttons[0], self.main_menu_entrys, mode="advance"))
            self.menus.append(map_pg.DropDown.drop_down(self.window, self.font_size, (self.ui_size, self.ui_size * 5), 6, self.font, [(0, 128, 128),(128, 0, 128)], self.buttons[1], {"Mapeditor":self.set_mode_mapeditor, "Paintmode":self.set_mode_paint}, mode="advance"))
            self.selectorButtonsTiles = map_pg.tile_handler.tile_handler("./res/buttons/selector_bar.png", {"size":"6x1"}, mode="single")
            self.listSelectButtons    = self.selectorButtonsTiles.return_tiles()
            self.mapFileHandleSystem  = map_pg.mapHandler.mapFileHandler(16,16,"../map")
            self.mapFileHandleSystem.failSafeLoadMap()
            
    def setupMapeditor(self, x):
        if x == 0:
            pass
        else:
            self.mapEditorSystem  = map_pg.mapEditor.mapEditor(self.window, self.mapFileHandleSystem, self.maped_rect)
            self.mapEditorSystem.calcPos(1)
    
    def replaceObjects(self, x):
        if x == 0:
            return "Replace objects"
        else:
            self.mapEditorSystem.reload(self.maped_rect)
            
    def calculateUiRects(self, x):
        if x == 0:
            return "Calculating UI"
        else:
            win_w, win_h = self.window.get_size()
            self.font_size         = self.ui_size - 2
            self.tile_choser_rect  = p.Rect((win_w - (self.ui_size * 8), self.ui_size * 3),(self.ui_size * 8, win_h - self.ui_size * 3))
            self.tool_options_rect = p.Rect((0, self.ui_size * 3),(self.ui_size * 8, win_h - self.ui_size * 3))
            self.maped_rect        = p.Rect((self.ui_size * 8,self.ui_size * 3),(win_w - (self.ui_size * 16),(win_h - self.ui_size * 3) / 2))
            rct_px, rct_py         = tuple(self.tile_choser_rect.topleft)
            self.tileselector_clgr = map_pg.clickgrid.ClickGrid((6, 12), (rct_px + self.ui_size, rct_py, self.ui_size * 6, self.ui_size * 12))
            rct_px, rct_py         = tuple(self.tile_choser_rect.bottomleft)
            self.selector_buttons  = map_pg.clickgrid.ClickGrid((6, 1), (rct_px + self.ui_size, rct_py - self.ui_size, self.ui_size * 6, self.ui_size))
            rct_px, rct_py         = tuple(self.maped_rect.bottomleft)
            self.statusRect        = p.Rect((rct_px, rct_py),(win_w - (self.ui_size * 16),(win_h - self.ui_size * 3) / 2))

if __name__ == "__main__":
    while True:
        #try:
            multi_editor()
        #except:
            #exit(1)