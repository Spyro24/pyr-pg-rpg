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
from os import name as posix_nt
from subprocess import run as sub_run
from subprocess import PIPE

def get_screen_res():
    disp = p.display.set_mode((0,0))
    return disp.get_size()

class map_():
    def __init__(self, gw, w, h, layers, *ts):
        print(ts)
        self.sys_name = posix_nt
        self.gw = gw #game window(or pygame surface object)
        self.gw_x, self.gw_y = self.gw.get_size()
        set_scale = 0
        if self.gw_y > self.gw_x: set_scale = self.gw_x
        else: set_scale = self.gw_y
        self.grid_size = set_scale / 10
        if len(ts) >= 1:
            self.grid_size = ts[0]
        print(self.grid_size)
        self.tile_size = int(self.grid_size)
        print(self.tile_size)
        self.target = (self.tile_size, self.tile_size) #Target Position for the map bliting
        if len(ts) == 3:
            self.target = (self.grid_size * ts[1], self.grid_size * ts[2])
        
        self.minmap = None #Add mini map suppot (Requested by Kem)
        self.map_w = w #Width of the map in tiles
        self.map_h = h #Hight of the map in tiles
        self.tiles_folder = "../tiles/"
        self.tiles_list = "../tile.list"
        self.tiles = []
        self.load_tiles()
        self.x = 0 #Curent Position for X
        self.y = 0 #Curent Position for Y
        self.bs = 2 #how many bytes a tile uses in the map file
        self.layers = layers #The amount of layers of a map
        self.load() #load the curent map
        self.render_method = "full" #Set the render method to [full, tile, None] to change the behavior of the map rendering
        self.render_layers = [0]
        self.edit_layer = 0
        self.e_tile = 1 #Set the curent tile toset on the map
        self.s_l0 = p.Surface((0,0))
        
        
        
        
    def load(self):
        map_tmp = [] #This is the actual map.
        try:
            map_file = open("../map/" + str(self.x) + "_" + str(self.y), "br") #Open the curent map file for position X_Y
            for layer in range(0,self.layers):
                    map_tmp.append([]) #Create a new layer
                    for tile in range(0, self.map_w * self.map_h):
                        map_tmp[layer].append(int.from_bytes(map_file.read(self.bs), "big"))
            self.map = map_tmp
            print(self.map)
        except BaseException as err:
            print(err)
            self.new()
            
    def load_tiles(self):
        tile_list = open(self.tiles_list, "r")
        if self.sys_name == "posix":
            ground = sub_run(["ls","-v",self.tiles_folder + "ground"],stdout=PIPE)
            ground_list =ground.stdout.decode("UTF-8").splitlines()
            self.tiles.append([])
            for tiles in ground_list:
                self.tiles[0].append(p.image.load(self.tiles_folder + "ground" + "/" + tiles))
            
            overlay = sub_run(["ls","-v",self.tiles_folder + "overlay"],stdout=PIPE)
            overlay_list = overlay.stdout.decode("UTF-8").splitlines()
            self.tiles.append([])
            for tiles in overlay_list:
                self.tiles[1].append(p.image.load(self.tiles_folder + "overlay" + "/" + tiles))
            
        else:
            raise BaseException("Can't load parsing routines for map tiles.\n Are you using Windows?")
        
    
    def new(self):
        map_cur = []
        for layer in range(0,self.layers):
            map_cur.append([])
            for obj in range(0, self.map_w * self.map_h):
                if layer == 0:
                    map_cur[layer].append(1)
                else:
                    map_cur[layer].append(0)
        self.map = map_cur
    
    def change_tile(self,pos):
        self.map[self.edit_layer].pop(pos)
        self.map[self.edit_layer].insert(pos, self.e_tile)
    
    def render(self):
        if self.render_method == "full":
            if self.minmap != None:
                self.minmap.create(self.mm_rad, "../map",(self.x, self.y))
                self.minmap.render()
            for number in self.render_layers:
                if number == 0:
                    get_map = 0
                count = 0 #set the counter to zero
                for w in range(0,self.map_w):
                    for h in range(0,self.map_h):
                        self.gw.blit(p.transform.scale(self.tiles[number][self.map[get_map][count] - 1],(self.tile_size, self.tile_size)),(self.target[0] + (self.tile_size * (h)), self.target[1] + (self.tile_size * (w))))
                        count += 1 #increase the counter to 1 to get the corect map value
    
    def export_tiles(self):
        return self.tiles
    
    def add_min_map(self, mm, rad):
        self.minmap = mm
        self.mm_rad = rad
        
    
    def save(self):
        pass