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
    def __init__(self, *settings):
        self.state = {"load":False}
        self.params = {"window":None,"map_xy":[0,0], "map_dir":"./map/","bg_tiles":[],"gd_tiles":[],"ov_tiles":[],"map_wh":(16,16),
                       "map_byte_size":2,"layers":8,"tile_size":(1,1)} # contains a list with all parameters of the game
        self.map_hitboxes = [] #<- list with all hitboxes in [y][x] format
        self.map_raw_hitboxes = [] #<- list with all raw hitboxes in [y][x] format
        #---legacy code---
        self.layers = self.params["layers"]
        self.tile_bytes = self.params["map_byte_size"]
        self.gw = self.params["window"] #Pygame window object
        self.pos_x = 0 #Blit x position
        self.pos_y = 0 #Blit x position
        self.map_x = self.params["map_xy"][0] #Map x position
        self.map_y = self.params["map_xy"][1] #Map x position
        self.map_path = self.params["map_dir"] #The path to the map files
        self.mw = mw #Map with in tiles
        self.mh = mh #Map hight in tiles
        self.tile_list = tile_list #A list with all tiles sorted by layer
        self.gw_x, self.gw_y = self.gw.get_size()
        set_scale = 0
        if self.gw_y > self.gw_x: set_scale = self.gw_x
        else: set_scale = self.gw_y
        self.scale = set_scale / self.mw
        self.g_layer = p.Surface(self.gw.get_size())
        self.in_x = (self.gw_x / 2) - ((self.mw / 2) * self.scale)
        self.in_y = (self.gw_y / 2) - ((self.mw / 2) * self.scale)
        print("A",self.in_x, self.in_y)
        
        for key in settings.keys(): #overwrite and add parameters to the map
            self.params[key] = settings[key]
        
    def load(self):
        self.state["load"] = True
        map_f = open(str(self.params["map_dir"]) + str(self.params["map_xy"][0]) + "_" + str(self.params["map_xy"][1]), "br")
        map = []
        for n in range(0,self.layers):
            map.append([])
            for tile in range(0,self.mw * self.mh):
                if n == 0:
                    test = int.from_bytes(map_f.read(self.tile_bytes), "big")
                    if test > 0:
                        tmp =(p.transform.scale(self.params["bg_tiles"][test],(self.scale,self.scale)))
                        map[n].append(tmp.convert())
                    else:
                        map[n].append(0)
                        
                elif n == 1:
                    map[n].append(int.from_bytes(map_f.read(self.tile_bytes), "big"))
                elif n == 2:
                    map[n].append(int.from_bytes(map_f.read(self.tile_bytes), "big"))
                    
        self.map = map
        self.create_surface()
        
    
    def move(self,x,y):
        self.map_x += x
        self.map_y += y
        self.load()
        self.create_surface()
        
    
    def create_surface(self):
        count = 0
        tmp0 = p.Surface((self.mw * self.scale, self.mh * self.scale))
        for h in range(0,self.mh):
            for w in range(0,self.mw):
                if self.map[0][count] != 0:
                    tmp0.blit(self.map[0][count],(w * self.scale, h * self.scale))
                count += 1
        self.g_layer = tmp0
    
    def get_hitbox(self):
        return self.map[1]
    
    def get_dia(self):
        return self.map[2]
    
    def get_pos(self):
        return 0,0 #self.map_x,self.map_y
    
    def get_raw(x,y): #-> bool
        pass
    
    
    def render(self): #-> None
       self.gw.blit(self.g_layer,(self.in_x + self.x, self.in_y + self.y))
    
    def debug(self):
        for h in range(0):
            for w in range(0):
                pass