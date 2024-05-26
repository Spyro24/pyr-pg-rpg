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

class map_():
    def __init__(self, gw, w, h, layers):
        self.gw = gw #game window(or pygame surface object)
        self.map_w = w #Width of the map in tiles
        self.map_h = h #Hight of the map in tiles
        self.tiles_list = "../tiles.list"
        self.tiles = []
        self.load_tiles()
        self.x = 0 #Curent Position for X
        self.y = 0 #Curent Position for Y
        self.bs = 2 #how many bytes a tile uses in the map file
        self.layers = layers #The amount of layers of a map
        self.load() #load the curent map
        self.target = (0,0) #Target Position for the map bliting
        self.render_method = "full" #Set the render method to [full, tile, None] to change the behavior of the map rendering
        self.render_layers = [0]
        
    def load(self):
        map_tmp = [] #This is the actual map.
        try:
            map_file = open("../map/" + str(self.x) + "_" + str(self.y), "br") #Open the curent map file for position X_Y
            for layer in range(0,self.layers):
                    map_tmp.append([]) #Create a new layer
                    for tile in range(0, self.map_w * self.map_h):
                        map_tmp[layer].append(int.from_bytes(map_file.read(self.bs), "big"))
            self.map = map_tmp
        except BaseException as err:
            print(err)
            self.new()
            
    def load_tiles(self):
        tile_list = open(self.tiles_list, "r")
    
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
    
    def render(self):
        if self.render_method == "full":
            pass
    
    def save(self):
        pass