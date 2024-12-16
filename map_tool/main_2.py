import pygame as p
import map_pg

class multi_editor():
    def __init__(self, log=print):
        self.logsys = log
        self.logsys("[MAP_TOOL](INIT) init map tool")
        self.window = p.display.set_mode((720,480), flags=p.RESIZABLE)
        self.font_size = 20
        self.font = map_pg.font.font(self.window, "./res/fonts/standard")
        self.global_config = {}
        self.images = {}
        self.buttons = []
        self.menus = []
        self.load_maped()
        self.main_loop()
        
    def main_loop(self):
        run = True
        update = True
        while run:
            for event in p.event.get():
                if event.type == p.QUIT:
                    self.end()
            
            mpos = p.mouse.get_pos()
            mclick = p.mouse.get_pressed()
            
            if mclick[0] == True:
                self.menus[0].open(mpos)
                update = True
                
            if update:
                self.window.fill("BLACK")
                self.menu_bar()
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

if __name__ == "__main__":
    while True:
        multi_editor()