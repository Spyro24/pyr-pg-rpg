import pygame as p
import map_pg

class multi_editor():
    def __init__(self, log=print):
        self.logsys = log
        self.logsys("[MAP_TOOL](INIT) init map tool")
        self.window        = p.display.set_mode((720,480), flags=p.RESIZABLE)
        self.ui_size       = 30
        self.font_size     = self.ui_size - 2
        self.font          = map_pg.font.font(self.window, "./res/fonts/standard")
        self.colors        = [(0, 133, 255)]
        self.global_config = {}
        self.images        = {}
        self.buttons       = []
        self.menus         = []
        self.visible_rects = []
        self.editor_mode   = 0
        self.editor_md_tag = "Mapeditor"
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
            
            mpos   = p.mouse.get_pos()
            mclick = p.mouse.get_pressed()
            """
            for key in range(0, len(key_ar)):
                if key_ar[key]:
                    print(key)
            """
            
            if mclick[0] == True:
                self.menus[0].open(mpos)
                self.menus[1].open(mpos)
                update = True
                
            if update:
                self.window.fill("BLACK")
                self.menu_bar()
                if self.editor_mode == 0:
                    p.draw.rect(self.window, (100,100,100), self.tile_choser_rect, 3)
                    p.draw.rect(self.window, (100,100,100), self.maped_rect, 3)
                elif self.editor_mode == 1:
                    self.font.draw("Coming Soon", self.font_size, (self.ui_size * 10, self.ui_size * 5))
                self.left_side_menu()
                p.draw.rect(self.window, (100,100,100), self.tool_options_rect, 3)
                p.display.flip()
                update = False
            
    def load_maped(self):
        logo = p.image.load("./res/symbols/logo.png")
        logo_scaled = p.transform.scale(logo, (self.font_size, self.font_size))
        self.images["logo_scaled"] = logo_scaled
        self.buttons.append(self.window.blit(logo_scaled,(0,0)))
        self.visible_rects.append(p.Rect((self.ui_size, self.ui_size * 4),(self.ui_size * 6, self.ui_size)))
        self.buttons.append(self.visible_rects[0])
        self.menus.append(map_pg.DropDown.drop_down(self.window, self.font_size, (0, self.font_size), 5, self.font, [(0, 128, 128),(128, 0, 128)], self.buttons[0], {"Settings":self.settings, "About":None, "Exit":self.end}, mode="advance"))
        self.menus.append(map_pg.DropDown.drop_down(self.window, self.font_size, (self.ui_size, self.ui_size * 5), 6, self.font, [(0, 128, 128),(128, 0, 128)], self.buttons[1], {"Mapeditor":self.set_mode_mapeditor, "Paintmode":self.set_mode_paint}, mode="advance"))
    
    def settings(self):
        pass
    
    def menu_bar(self):
        self.window.blit(self.images["logo_scaled"],(0,0))
        
    def left_side_menu(self):
        p.draw.rect(self.window, self.colors[0], self.visible_rects[0])
        self.font.draw(self.editor_md_tag, self.font_size, self.visible_rects[0].topleft)
    
    def end(self):
        p.quit()
        exit(0)
        
    def reload_ui(self):
        self.logsys("[MAP_TOOL][UI](reload) Reload UI")
        win_w, win_h = self.window.get_size()
        self.tile_choser_rect  = p.Rect((win_w - (self.ui_size * 8), self.ui_size * 3),(self.ui_size * 8, win_h - self.ui_size * 3))
        self.tool_options_rect = p.Rect((0, self.ui_size * 3),(self.ui_size * 8, win_h - self.ui_size * 3))
        self.maped_rect        = p.Rect((self.ui_size * 8,self.ui_size * 3),(win_w - (self.ui_size * 16),(win_h - self.ui_size * 3) / 2))
        
    def set_mode_mapeditor(self):
        self.editor_md_tag = "Mapeditor"
        self.editor_mode   = 0
    
    def set_mode_paint(self):
        self.editor_md_tag = "Paintmode"
        self.editor_mode   = 1

if __name__ == "__main__":
    while True:
        multi_editor()