'''
    Tile loader for loading the new pyr_pg tile maps
    Copyright (C) 2024 Spyro24

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
import pygame as p

class tile_handler():
    def __init__(self, folder, config, *font, mode="new"):
        '''
            To use the font you have to make a Text obj from the pyr_pg libary
            The modes are "new" for tile tables and "legacy" if you have
        '''
        tmp = config["size"].split("x")
        tmx = int(tmp[0])
        tmy = int(tmp[1])
        draw_font = False
        self.tile_maps = []
        self.tiles = []
        if len(font) > 0:
            draw_font = True
        try:
            n = 0
            if mode == "new":
                while True:
                    if draw_font:
                        pass # ("Loading Tilemap str(n))
                        p.display.flip()
                    self.tile_maps.append(p.image.load(folder + "/" + str(n) + ".png"))
                    n += 1
        except:
            pass
        
        max_tile_maps = len(self.tile_maps)
        
        for tmap in range(max_tile_maps):
            cur_tmap = self.tile_maps[tmap]
            tw, th = cur_tmap.get_size()
            sx, sy = tw / tmx, th / tmy
            for h in range(tmy):
                for w in range(tmx):
                    tmp = p.Surface((sy, sy), flags=p.SRCALPHA)
                    tmp.blit(cur_tmap,(0,0),(sx * w, sy * h, sx, sy))
                    self.tiles.append(tmp)
    
    def add_gw(self, gw):
        self.gw = gw
        
    def retun_tiles(self):
        return self.tiles
    
    def draw_map(self, map_number, position, h_size):
        map_num = map_number
        x_size, y_size = self.tile_maps[map_num].get_size()
        rezise = x_size / y_size
        self.gw.blit(p.transform.scale(self.tile_maps[map_num],(rezise * h_size, h_size)), position)
        
                

#Unit test of the modul
if __name__ == "__main__":
    of = 0
    b = 0
    win = p.display.set_mode((700,700))
    tiles = tile_handler("../../tiles/ground", {"size":"12x6"})
    tiles = tiles.retun_tiles()
    ov = tile_handler("../../tiles/overlay", {"size":"12x6"})
    ov = ov.retun_tiles()
    print(len(tiles))
    for t in range(len(tiles)):
        win.blit(tiles[t],(b * 64, of * 64))
        win.blit(ov[t],(b * 64, of * 64))
        b += 1
        if (t + 1) % 12 == 0:
            of += 1
            b = 0
        print(t)
    p.display.update()
    