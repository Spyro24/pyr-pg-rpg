"""
    Map class to handle the binary maps.
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
"""
import pygame as p

class map:
    def __init__(self,win,x,y,mx,my,mp,tp,ts,mh,mw,tb):
        self.load_state = False
        self.layers = 8
        self.tile_bytes = tb
        self.gw = win #Pygame window object
        self.pos_x = x #Blit x position
        self.pos_y = y #Blit x position
        self.map_x = mx #Map x position
        self.map_y = my #Map x position
        self.map_path = mp #The path to the map files
        self.mw = mw #Map with in tiles
        self.mh = mh #Map hight in tiles
        self.tile_path = tp
        self.gw_x, self.gw_y = self.gw.get_size()
        self.scale = self.gw_x / self.mw
        self.g_layer = p.Surface(self.gw.get_size())
        self.y = 0
        self.x = 0
        
    def load(self):
        self.load_state = True
        map_f = open(str(self.map_path) + str(self.map_x) + "_" + str(self.map_y), "br")
        map = []
        for n in range(0,self.layers):
            map.append([])
            for tile in range(0,self.mw * self.mh):
                if n == 0:
                    test = int.from_bytes(map_f.read(self.tile_bytes), "big")
                    if test > 0:
                        tmp =(p.transform.scale(p.image.load(str(self.tile_path) + str(test) + ".png"),(self.scale,self.scale)))
                        map[n].append(tmp.convert())
                    else:
                        map[n].append(0)
                        
                elif n == 1:
                    map[n].append(int.from_bytes(map_f.read(self.tile_bytes), "big"))
        print(map[1])         
        self.map = map
        self.create_surface()
        
    
    def move(self,x,y):
        self.map_x += x
        self.map_y += y
        self.load()
        self.create_surface()
        
    
    def create_surface(self):
        count = 0
        tmp0 = p.Surface(self.gw.get_size())
        for h in range(0,self.mh):
            for w in range(0,self.mw):
                if self.map[0][count] != 0:
                    tmp0.blit(self.map[0][count],(w * self.scale, h * self.scale))
                count += 1
        self.g_layer = tmp0
    
    def get_hitbox(self):
        return self.map[1]
    
    def render(self):
       self.gw.blit(self.g_layer,(self.x,self.y))