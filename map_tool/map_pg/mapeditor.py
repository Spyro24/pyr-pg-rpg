import pygame as p

class Mapeditor:
    def __init__(self, window, map_folder, render_pos=(0,0), tile_size=64, map_wh=(16,16)):
        self.window = window
        self.map_x      = 0
        self.map_y      = 0
        self.mode       = 0
        self.map_folder = map_folder
        self.map        = []
        self.map_w      = map_wh[0]
        self.map_h      = map_wh[1]
        
    def insertTiles(self, bg, bgov, pov, povov=[], special=[]):
        self.tiles_bg    = bg
        self.tiles_bgov  = bgov
        self.tiles_pov   = pov
        self.tiles_povov = povov
        self.special     = special
        
    def set_mode(self, mode):
        self.mode = mode
        
    def move_map(self, x, y):
        pass
    
    def load_map(self):
        self.map = []
        map_file = open(self.map_folder + "/" + str(self.map_x) + "_" + str(self.map_y), "br")
        
    def init(self):
        pass
    
    def render(self):
        pass