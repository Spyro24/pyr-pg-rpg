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
        self.global_config = {}
        self.images        = {}
        self.buttons       = []
        self.menus         = []
        self.editor_mode   = 0
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
                update = True
                
            if update:
                self.window.fill("BLACK")
                self.menu_bar()
                if self.editor_mode == 0:
                    p.draw.rect(self.window, (100,100,100), self.tile_choser_rect, 3)
                p.draw.rect(self.window, (100,100,100), self.tool_options_rect, 3)
                p.display.flip()
                update = False
            
    def load_maped(self):
        logo = p.image.load("./res/symbols/logo.png")
        logo_scaled = p.transform.scale(logo, (self.font_size, self.font_size))
        self.images["logo_scaled"] = logo_scaled
        self.buttons.append(self.window.blit(logo_scaled,(0,0)))
        self.menus.append(map_pg.DropDown.drop_down(self.window, self.font_size, (0, self.font_size), 5, self.font, [(0, 128, 128),(128, 0, 128)], self.buttons[0], {"Settings":self.settings, "About":None, "Exit":self.end}, mode="advance"))
    
    def settings(self):
        pass
    
    def menu_bar(self):
        self.window.blit(self.images["logo_scaled"],(0,0))
    
    def end(self):
        p.quit()
        exit(0)
        
    def reload_ui(self):
        self.logsys("[MAP_TOOL][UI](reload) Reload UI")
        win_w, win_h = self.window.get_size()
        self.tile_choser_rect  = p.Rect((win_w - (self.ui_size * 8), self.ui_size * 3),(self.ui_size * 8, win_h - self.ui_size * 3))
        self.tool_options_rect = p.Rect((0, self.ui_size * 3),(self.ui_size * 8, win_h - self.ui_size * 3))

if __name__ == "__main__":
    while True:
        multi_editor()