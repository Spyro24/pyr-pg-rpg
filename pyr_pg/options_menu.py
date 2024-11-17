import pygame as p
import time

class options_menu():
    def __init__(self, globconfig):
        self.global_config = globconfig
        self.blit_surface = self.global_config["pg_window"]
        self.config = {"gridsize":(16,16), "blit_pos":(0,0), "tile_size":0}
        self.runtime_config = {}
        self.options = {}
        self.__setup_env()
    
    def create(self, image):
        pass
    
    def __setup_env(self):
        window_wh = self.blit_surface.get_size()
        shortest_side = window_wh[1]
        if window_wh[0] < window_wh[1]:
            shortest_side = window_wh[0]
        blit_point = (0, 0)
        midpoint = (window_wh[0]/2, window_wh[1]/2)
        blit_point = (midpoint[0] - shortest_side/2, midpoint[1] - shortest_side/2)
        self.config["blit_pos"] = blit_point
        self.config["tile_size"] = int(shortest_side / self.config["gridsize"][0])
        
if __name__ == "__main__":
    import font
    
    _test_win = p.display.set_mode((800,16*32))
    _test_font = font.font(_test_win, "./res/fonts/standard")
    _test_config = {"font":_test_font, "pg_window":_test_win}
    _test_dialog = options_menu(_test_config)
    p.display.flip()