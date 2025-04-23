import pygame as p
import time

class options_menu():
    def __init__(self, globconfig):
        self.global_config  = globconfig
        self.blit_surface   = self.global_config["pg_window"]
        self.config         = {"gridsize":(16,16), "blit_pos":(0,0), "tile_size":0}
        self.runtime_config = {"menu_bg":None, "selector":None}
        self.options        = {}
        self.__setup_env()
    
    def create(self, png):
        tile_size      = self.config['tile_size']
        grid_size      = self.config['gridsize']
        menu_tilesheet = p.image.load(png)
        menu_tile_list = []
        menu_tilesize  = menu_tilesheet.get_size()[0] / 3
        for y_tile in range(4):
            for x_tile in range(3):
                cur_tile = p.surface.Surface((menu_tilesize,menu_tilesize), flags=p.SRCALPHA)
                cur_tile.blit(menu_tilesheet,(-(x_tile * menu_tilesize), -(y_tile * menu_tilesize)))
                menu_tile_list.append(p.transform.scale(cur_tile,(self.config["tile_size"], self.config["tile_size"])))
        menu_size = int(self.config['tile_size']) * self.config['gridsize'][0], int(self.config['tile_size']) * self.config['gridsize'][1]
        print(menu_size)
        menu_bg = p.surface.Surface(menu_size, flags=p.SRCALPHA)
        menu_bg.blit(menu_tile_list[0], (0, 0))
        menu_bg.blit(menu_tile_list[2], ((grid_size[0] - 1) * tile_size, 0))
        menu_bg.blit(menu_tile_list[8], ((grid_size[0] - 1) * tile_size, (grid_size[1] - 1) * tile_size))
        menu_bg.blit(menu_tile_list[6], (0, (grid_size[1] - 1) * tile_size))
        for x in range(self.config['gridsize'][0] - 2):
            menu_bg.blit(menu_tile_list[1], (tile_size * (x + 1), 0))
        for x in range(grid_size[0] - 2):
            menu_bg.blit(menu_tile_list[7], (tile_size * (x + 1), (grid_size[1] - 1) * tile_size))
        for y in range(self.config['gridsize'][1] - 2):
            menu_bg.blit(menu_tile_list[3], (0, (tile_size * (y + 1))))
        for y in range(self.config['gridsize'][1] - 2):
            menu_bg.blit(menu_tile_list[5], ((grid_size[0] - 1) * tile_size, (tile_size * (y + 1))))
        for x in range(grid_size[0] - 2):
            for y in range(grid_size[1] - 2):
                menu_bg.blit(menu_tile_list[4], (tile_size * (x+ 1), tile_size * (y + 1)))
        selector = p.surface.Surface((tile_size * (grid_size[0] - 2),tile_size), flags=p.SRCALPHA)
        for x in range(grid_size[0] - 2):
            selector.blit(menu_tile_list[9], (tile_size * x, 0))
        self.runtime_config['menu_bg']  = menu_bg
        self.runtime_config['selector'] = selector
        
    def open(self):
        key_hold     = True
        tile_size    = self.config['tile_size']
        bx, by       = self.config['blit_pos']
        blit_obj     = self.blit_surface
        menu_bg      = self.runtime_config['menu_bg']
        selector     = self.runtime_config['selector']
        selector_bx  = bx + tile_size
        selector_by  = by + tile_size
        selector_pos = 0
        update       = True
        run          = True
        while run:
            for event in p.event.get():
                if event.type == p.QUIT:
                    run = False
            key_ar = p.key.get_pressed()
            
            if key_ar[115]:
                selector_pos += 1
                update = True
            elif key_ar[119]:
                if selector_pos > 0:
                    selector_pos -= 1
                    update = True
            elif key_ar[27]:
                if key_hold == False:
                    run = False
            else:
                key_hold = False
            
            if update:
                blit_obj.blit(menu_bg, (bx, by))
                blit_obj.blit(selector, (selector_bx, selector_by + (tile_size * (selector_pos))))
                p.display.flip()
                time.sleep(0.1)
                update = False
    
    def __setup_env(self):
        window_wh     = self.blit_surface.get_size()
        shortest_side = window_wh[1]
        if window_wh[0] < window_wh[1]:
            shortest_side = window_wh[0]
        blit_point = (0, 0)
        midpoint = (window_wh[0]/2, window_wh[1]/2)
        blit_point = (midpoint[0] - shortest_side/2, midpoint[1] - shortest_side/2)
        self.config["blit_pos"]  = blit_point
        self.config["tile_size"] = int(shortest_side / self.config["gridsize"][0])
        
if __name__ == "__main__":
    import font
    
    _test_win = p.display.set_mode((800,16*32))
    _test_font = font.font(_test_win, "./res/fonts/standard")
    _test_config = {"font":_test_font, "pg_window":_test_win}
    _test_menu = options_menu(_test_config)
    _test_menu.create("./res/menus/options_menu.png")
    _test_menu.open()
    p.quit()