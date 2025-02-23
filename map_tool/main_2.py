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
        self.tile_sheetSize   = 12*6
        self.tileselector_pos = 0
        self.selected_tile    = 0
        self.mouse_pressed    = False
        self.cur_layer        = 0
        self.cur_tilsesel_pos = 0
        self.main_menu_entrys = {"Settings":self.settings, "About":self.VOID, "Exit":self.end}
        self.load_maped()
        self.main_loop()
        
    def main_loop(self):
        self.reload_ui()
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
                            if self.tileselector_clgr.activate_rect.collidepoint(mpos):
                                self.tileselector_pos = self.tileselector_clgr.return_number(mpos) + (self.tile_sheetSize * self.cur_tilsesel_pos)
                            elif self.selector_buttons.activate_rect.collidepoint(mpos):
                                click_pos = self.selector_buttons.return_number(mpos)
                                if click_pos == 0:
                                    if self.cur_tilsesel_pos > 0:
                                        self.cur_tilsesel_pos -= 1
                                        print(self.cur_tilsesel_pos)
                                elif click_pos == 5:
                                    self.cur_tilsesel_pos += 1
                                    print(self.cur_tilsesel_pos)
                            update = True
                self.mouse_pressed = True
            else:
                self.mouse_pressed = False
                
            if update:
                self.window.fill("BLACK")
                self.menu_bar()
                if self.editor_mode == 0:
                    p.draw.rect(self.window, (100,100,100), self.tile_choser_rect, 3)
                    p.draw.rect(self.window, (100,100,100), self.maped_rect, 3)
                    rct_px, rct_py = tuple(self.tile_choser_rect.topleft)
                    if self.cur_layer == 0:
                        c = 0
                        for y in range(12):
                            for x in range(6):
                                self.window.blit(p.transform.scale(self.tilesGround[c + (self.cur_tilsesel_pos * self.tile_sheetSize)], (self.ui_size, self.ui_size)), (rct_px + self.ui_size + (self.ui_size * x), rct_py + (self.ui_size * y)))
                                c += 1
                    rct_px, rct_py = tuple(self.tile_choser_rect.bottomleft)
                    for n in range(6):
                        self.window.blit(p.transform.scale(self.listSelectButtons[n], (self.ui_size, self.ui_size)), (rct_px + self.ui_size + (self.ui_size * n), rct_py - self.ui_size))
                    if self.debug:
                        self.tileselector_clgr.debug(self.window)
                        self.selector_buttons.debug(self.window)
                elif self.editor_mode == 1:
                    self.font.draw("Coming Soon", self.font_size, (self.ui_size * 10, self.ui_size * 5))
                self.left_side_menu()
                p.draw.rect(self.window, (100,100,100), self.tool_options_rect, 3)
                p.display.flip()
                update = False
            
    def load_maped(self):
        logo = p.image.load("./res/symbols/logo.png")
        self.images["splash"] = logo
        logo_scaled = p.transform.scale(logo, (self.font_size, self.font_size))
        self.images["logo_scaled"] = logo_scaled
        self.buttons.append(self.window.blit(logo_scaled,(0,0)))
        self.visible_rects.append(p.Rect((self.ui_size, self.ui_size * 4),(self.ui_size * 6, self.ui_size)))
        self.buttons.append(self.visible_rects[0])
        self.menus.append(map_pg.DropDown.drop_down(self.window, self.font_size, (0, self.font_size), 5, self.font, [(0, 128, 128),(128, 0, 128)], self.buttons[0], self.main_menu_entrys, mode="advance"))
        self.menus.append(map_pg.DropDown.drop_down(self.window, self.font_size, (self.ui_size, self.ui_size * 5), 6, self.font, [(0, 128, 128),(128, 0, 128)], self.buttons[1], {"Mapeditor":self.set_mode_mapeditor, "Paintmode":self.set_mode_paint}, mode="advance"))
        self.selectorButtonsTiles  = map_pg.tile_handler.tile_handler("./res/buttons/selector_bar.png", {"size":"6x1"}, mode="single")
        self.listSelectButtons     = self.selectorButtonsTiles.return_tiles()
        self.cachingTiles(1)
        
    def cachingTiles(self, x):
        if x == 0:
            return "Caching Tiles"
        else:
            self.tilesGround           = map_pg.tile_handler.tile_handler("../tiles/ground", {"size":"12x6"}).return_tiles()
            self.tilesGroundOverlay    = map_pg.tile_handler.tile_handler("../tiles/groundov", {"size":"12x6"})
            self.tilesPlayerOverlay    = map_pg.tile_handler.tile_handler("../tiles/overlay", {"size":"12x6"})
    
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
        self.progressBarLoadSplash([self.calculateUiRects, self.rescale], (0,127,255))
    
    def rescale(self, x):
        if x == 0:
            pass
        else:
            self.visible_rects[0].update((self.ui_size, self.ui_size * 4),(self.ui_size * 6, self.ui_size))
            self.menus[1].rescale(self.font_size, (self.ui_size, self.ui_size * 5), 6, self.buttons[1])
    
    def calculateUiRects(self, x):
        if x == 0:
            return "Reloading UI"
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
        
        
    def set_mode_mapeditor(self):
        self.editor_md_tag = "Mapeditor"
        self.editor_mode   = 0
    
    def set_mode_paint(self):
        self.editor_md_tag = "Paintmode"
        self.editor_mode   = 1
        
    def end(self):
        p.quit()
        exit(0)
        
    def progressBarLoadSplash(self, functionList, color):
        win_w, win_h = self.window.get_size()
        winXC, winYC = self.window.get_rect().center
        percentSteps = 1 / len(functionList)
        for function in functionList:
            displayText = function(0)
            self.window.fill((0,0,0))
            self.show_splash()
            p.display.flip()
            function(1)
        
    
    def VOID(self):
        pass

if __name__ == "__main__":
    while True:
        #try:
            multi_editor()
        #except:
            #exit(1)