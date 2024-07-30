import pygame as p

class tile_selector():
    def __init__(self, gw):
        self.win = gw
        self.ww, self.wh = gw.get_size()
        self.tile = 0
        self.ui_p = "./ui/" #The path of the UI Elements
        ui_list = ["exit"] #The needed UI elemts for the selecto
        self.ui = []
        #for element in ui_list:
         #   self.ui.append(p.image.load(self.ui_p + element + ".png"))
        
    def selector(self,size, xp, yp, tile_map):
        self.click_area = p.Rect(xp - 1, yp - 1, size, size)
        self.icon_ps = xp, yp, size, size
        self.tiles = tile_map
    
    def click(self, mpos):
        if self.click_area.collidepoint(mpos):
            self.__selector_open()
        
    def __selector_open(self):
        pass
    
    def render(self, form):
        if form == "minimized": #if Minimized the Selector tile will show on the selector position
            pass
        elif form == "extended": #if extended the selector UI will shown in the intire window
            pass
        else:
            if form:
                print("wrong parameter", form)
            else:
                print("Form is empty")
                