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
        #---user vars---
        #---------------
        #---internal vars---
        self.death_end = b""
        self.state = {"load":False}
        self.params = {"window":None,"map_xy":[0,0], "map_dir":"../map/","bg_tiles":[],"gd_tiles":[],"ov_tiles":[],"map_wh":(16,16),
                       "map_byte_size":2,"layers":8,"tile_size":(1,1), "debug_col":{"map_hitbox":(0,127,127)}} # contains a list with all parameters of the game
        self.map_hitboxes = [] #<- list with all hitboxes in [y][x] format
        self.map_raw_hitboxes = [] #<- list with all raw hitboxes in [y][x] format
        #-------------------
        #---Add settings to the parameter list
        for key in settings[0].keys(): #overwrite and add parameters to the map
            self.params[key] = settings[0][key]
        #---legacy code---
        self.debug_col = self.params["debug_col"]["map_hitbox"]
        self.layers = self.params["layers"]
        self.tile_bytes = self.params["map_byte_size"]
        self.gw = self.params["window"] #Pygame window object
        self.pos_x = 0 #Blit x position
        self.pos_y = 0 #Blit x position
        self.map_x = self.params["map_xy"][0] #Map x position
        self.map_y = self.params["map_xy"][1] #Map x position
        self.map_path = self.params["map_dir"] #The path to the map files
        self.mw, self.mh = self.params["map_wh"] #Map with in tiles
        self.tile_list = [self.params["bg_tiles"], self.params["gd_tiles"]] #A list with all tiles sorted by layer
        self.gw_x, self.gw_y = self.gw.get_size()
        set_scale = 0
        if self.gw_y > self.gw_x: set_scale = self.gw_x
        else: set_scale = self.gw_y
        self.scale = set_scale / self.mw
        self.g_layer = p.Surface(self.gw.get_size())
        self.gov_layer = p.Surface(self.gw.get_size())
        self.in_x = (self.gw_x / 2) - ((self.mw / 2) * self.scale)
        self.in_y = (self.gw_y / 2) - ((self.mw / 2) * self.scale)
        
    def load(self):
        self.death_end = b""
        self.state["load"] = True
        map_f = open(str(self.params["map_dir"]) + str(self.map_x) + "_" + str(self.map_y), "br")
        map = []
        raw_map = []
        for n in range(0,self.layers):
            map.append([])
            for tile in range(0,self.mw * self.mh):
                #create the ground layer
                if n == 0:
                    test = int.from_bytes(map_f.read(self.tile_bytes), "big")
                    #tmp = p.transform.scale(self.params["bg_tiles"][test - 1],(self.scale,self.scale)) #hold this for 
                    map[n].append(test)
                    
                #create the hitboxes        
                elif n == 1:
                    map[n].append(int.from_bytes(map_f.read(self.tile_bytes), "big"))
                #create the ground overlay layer
                elif n == 2:
                    test = int.from_bytes(map_f.read(self.tile_bytes), "big")
                    #tmp =(p.transform.scale(self.tile_list[1][test - 1],(self.scale,self.scale)))
                    map[n].append(test)
                else:
                    self.death_end += int.to_bytes(0, self.tile_bytes, "big")
        
        #---code for creating the hitboxes---
        #clear hitboxes
        self.map_hitboxes = []
        self.raw_hitboxes = []
        n = 0
        #create the hitboxes
        for h in range(self.mh):
            self.raw_hitboxes.append([])
            for w in range(self.mw):
                self.raw_hitboxes[h].append(map[1][n])
                n += 1
        
        #---create changeable ground layer---
        self.raw_ground_layer = []
        n = 0
        for h in range(self.mh):
            self.raw_ground_layer.append([])
            for w in range(self.mw):
                self.raw_ground_layer[h].append(map[0][n])
                n += 1
                
        #---create changeable ground overlay layer---
        self.raw_ground_ov_layer = []
        n = 0
        for h in range(self.mh):
            self.raw_ground_ov_layer.append([])
            for w in range(self.mw):
                self.raw_ground_ov_layer[h].append(map[2][n])
                n += 1
        
        #---prepare the map
        map.pop(0)
        map.insert(0, self.raw_ground_layer) #insert the ground layer
        map.pop(1)
        map.insert(1, self.raw_hitboxes)
        map.pop(2)
        map.insert(2, self.raw_ground_ov_layer)
        
        print("lenght of map is: " + str(len(map)))
        self.map = map
        self.create_surface()
        
    
    def move(self,x,y):
        self.map_x += x
        self.map_y += y
        self.load()
        self.create_surface()
        
    def save_map(self):
        map_bytes = b""
        #unpack ground layer and put it in map_bytes (section 0)
        for h in range(len(self.map[0])):
            for w in range(len(self.map[0][h])):
                map_bytes += int.to_bytes(self.map[0][h][w], self.tile_bytes, "big")
        
        #unpack hitbox and put it in map_bytes (section 1)
        for h in range(len(self.map[1])):
            for w in range(len(self.map[1][h])):
                map_bytes += int.to_bytes(self.map[1][h][w], self.tile_bytes, "big")
                
        #unpack ground overlay layer and put it in map_bytes (section 1)
        for h in range(len(self.map[2])):
            for w in range(len(self.map[2][h])):
                map_bytes += int.to_bytes(self.map[2][h][w], self.tile_bytes, "big")
        
        #add the death end (compatibility issue)
        map_bytes += self.death_end
        print(map_bytes)
        print(len(map_bytes))
        try:
            map_f = open(str(self.params["map_dir"]) + str(self.map_x) + "_" + str(self.map_y), "bw")
            map_f.write(map_bytes)
        except:
            print("Map Data are not writen to file :(")
        finally:
            map_f.close()
    
    def change_tile(self, pos, layer, number):
        change_x, change_y = pos
        if layer == 0:
            self.map[0][change_y].pop(change_x)
            self.map[0][change_y].insert(change_x, number)
        
        self.create_surface()
    
    def update_surface(self, pos, layer, number):
        pass
    
    def show_hitboxes(self):
        pass
    
    def create_surface(self):
        count = 0
        tmp0 = p.Surface((self.mw * self.scale, self.mh * self.scale)) #groundlayer
        tmp1 = p.Surface((self.mw * self.scale, self.mh * self.scale), flags=p.SRCALPHA)
        for h in range(self.mh):
            self.map_hitboxes.append([])
            for w in range(self.mw):
                if self.raw_hitboxes[h][w] == 1:
                    self.map_hitboxes[h].append(p.Rect((self.in_x + (self.scale * w), self.in_y + (self.scale * h)), (self.scale, self.scale)))
                else:
                    self.map_hitboxes[h].append(0)
                if self.map[0][h][w] != 0:
                    tmp0.blit(p.transform.scale(self.params["bg_tiles"][self.map[0][h][w] - 1],(self.scale,self.scale)) ,(w * self.scale, h * self.scale))
                if self.map[2][h][w] != 0:
                    tmp1.blit(p.transform.scale(self.tile_list[1][self.map[2][h][w] - 1],(self.scale,self.scale)) ,(w * self.scale, h * self.scale))
                count += 1
        self.g_layer = tmp0.convert()
        self.gov_layer = tmp1.convert_alpha()
    
    def get_dia(self):
        return self.map[2]
    
    def get_pos(self):
        return 0,0 #self.map_x,self.map_y
    
    def get_raw(x,y): #-> bool
        pass
    
    def get_hitbox(self, x, y): #-> 0 or pygame.Rect()
        hb = 0
        try:
            hb = self.map_hitboxes[y][x]
        except:
            hb = 0
        return hb
    
    
    def render(self, layer, pos, size): #-> None
        if layer == 0:
            self.gw.blit(p.transform.scale(self.g_layer,size),pos)
        elif layer == 1:
            self.gw.blit(p.transform.scale(self.gov_layer,size),pos)
    
    def debug(self):
        for h in range(self.mh):
            for w in range(self.mw):
                if self.map_hitboxes[h][w] != 0:
                    p.draw.rect(self.gw, self.debug_col, self.map_hitboxes[h][w], width=3)