"""
    Map modul for binary map files for map_tool (the editor for pyr_pg maps)
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
    def __save(self): #Save a map (Only available in edit mode)
        if self.edmode:
            pass
        else:
            raise Exception("Permision denied to save the map")
    
    def __new(self): #create a initial map with a tile 1 layer
        if self.edmode:
            pass
        else:
            raise Exception("Permision denied to create a initial map")
        
    def __load(self, init): #This is a internal function for the map class.Please do not use!
        map_tmp = [] #This is the actual map.
        try:
            map_file = open(str(self.path) + str(self.x) + "_" + str(self.y), "br")
            
            for layer in range(0,6):
                    map_tmp.append([])
                    for tile in range(0, self.w * self.h):
                        map_tmp[layer].append(int.from_bytes(map_file.read(self.tsb), "big"))
            self.map = map_tmp
        except:
            raise Exception("Cant load map " + str(self.x) + "_" + str(self.y))
        
    def __init__(self,pos_x,pos_y,map_w,map_h,ts,tsb,path, map_ed, win, tile_obj):
        self.x = pos_x #The x position of the map
        self.y = pos_y #The y position of the map
        self.w = map_w #With of the map (in tiles)
        self.h = map_h #Hight of the map
        self.ts = ts #Tile size in px (Tiles are squares)
        self.tsb = tsb #Tile size in bytes (for the loading from a map file)
        self.path = path #path of the map
        self.window = win
        self.tobj = tile_obj
        self.edmode = bool(map_ed)
        self.__load(True) #load the map on init
    
    def back(self, *get_var):
        stack = []
        for element in get_var:
            if element == "map_map":
                stack.append(self.map)
        return stack
    
    def draw(self, pos_x, pos_y, scale):
        xp = int(pos_x)
        yp = int(pos_y)
        size = (int(scale), int(scale))
        iter_ = 0
        if True:
            for h in range(0, int(self.h)):
                for w in range(0, int(self.w)):
                    if self.map[0][iter_] != 0:
                        img_ = p.transform.scale(self.tobj[1][0][self.map[0][iter_] - 1],size)
                        self.window.blit(img_,(xp + w * size[0], yp + h * size[1]))
                    else:
                        pass
                    iter_ += 1
                    
    def set(self,x,y):
        #Set the map to new x and y postion
        if self.edmode:
            self.__save()
        self.x = x
        self.y = y
        self.__load()
        
def map_load(x,y,w,h,leng):
    show = [] #ground layer
    hit  = [] #hitbox layer
    overlay = [] #Overdraw over the ground layer
    act  = [] #action laxer (for the dialog script)
    acthit = [] #IDK
    overdraw = [] #drawed over the character layer

def map_border(mpx, mpy, mw, mh, bs):
    map_border = []
    try:
        empty= []
        iter_ = mw * mh - mw 
        cur_x = mpx
        cur_y = mpy - 1
        map_cur = mp.map_load(cur_x, cur_y, mw, mh, bs)
        for n in range(0, len(map_cur)):
            empty.append([])
            for i in range(iter_, mw * mh):
                empty[n].append(map_cur[n][i])
    except BaseException as err:
        print(err)
        print("Map above not exist")
    map_border.append(empty)
        
    try:
        empty2 = []
        iter_ = 0 
        cur_x = mpx
        cur_y = mpy + 1
        map_cur = mp.map_load(cur_x, cur_y, mw, mh, bs)
        for n in range(0, len(map_cur)):
            empty2.append([])
            for i in range(iter_, mw):
                empty2[n].append(map_cur[n][i])
    except BaseException as err:
        print(err)
        print("Map below not exist")
        
    map_border.append(empty2)
    
    try:
        empty3 = []
        iter_ = 0 
        cur_x = mpx - 1
        cur_y = mpy
        map_cur = mp.map_load(cur_x, cur_y, mw, mh, bs)
        print(map_cur)
        for n in range(0, len(map_cur)):
            empty3.append([])
            for i in range(0, mh):
                empty3[n].append(map_cur[n][((i + 1) * mw) - 1])
    except BaseException as err:
        print(err)
        print("Map Left not exist")
    
    map_border.append(empty3)
    
    try:
        empty4 = []
        iter_ = 0 
        cur_x = mpx + 1
        cur_y = mpy
        map_cur = mp.map_load(cur_x, cur_y, mw, mh, bs)
        print(map_cur)
        for n in range(0, len(map_cur)):
            empty4.append([])
            for i in range(0, mh):
                empty4[n].append(map_cur[n][i * mw])
    except BaseException as err:
        print(err)
        print("Map Right not exist")
    
    map_border.append(empty4)
    
    return map_border

#dev comment: make function less expensive for the programm
def map_border_blit(win,mw,mh,pos,size,border, *opn):
    black = p.transform.scale(p.image.load("./symbols/task/gray_out.png"),(size, size))
    try:
        for e in range(0, len(border[0][0])):
            if border[0][0][e] != 0:
                set_x = int(pos[0]) + (int(size) * e)
                set_y = int(pos[1]) - size
                img_ = p.transform.scale(p.image.load("../tiles/" + str(border[0][0][e]) + ".png"),(size, size))
                win.blit(img_,(int(set_x),int(set_y)))
                win.blit(black,(int(set_x),int(set_y)))
    except:
        pass
    
    try:
        for e in range(0, len(border[1][0])):
            if border[1][0][e] != 0:
                set_x = int(pos[0]) + (int(size) * e)
                set_y = int(pos[1]) + int(size) * mh
                img_ = p.transform.scale(p.image.load("../tiles/" + str(border[1][0][e]) + ".png"),(size, size))
                win.blit(img_,(int(set_x),int(set_y)))
                win.blit(black,(int(set_x),int(set_y)))
    except:
        pass
    
    try:
        for e in range(0, len(border[2][0])):
            set_x = int(pos[0]) - size
            set_y = int(pos[1]) + (int(size) * e)
            img_ = p.transform.scale(p.image.load("../tiles/" + str(border[2][0][e]) + ".png"),(size, size))
            win.blit(img_,(int(set_x),int(set_y)))
            win.blit(black,(int(set_x),int(set_y)))
    except:
        pass
    
    try:
        for e in range(0, len(border[3][0])):
            set_x = int(pos[0]) + int(size) * mw
            set_y = int(pos[1]) + (int(size) * e)
            img_ = p.transform.scale(p.image.load("../tiles/" + str(border[3][0][e]) + ".png"),(size, size))
            win.blit(img_,(int(set_x),int(set_y)))
            win.blit(black,(int(set_x),int(set_y)))
    except:
        pass