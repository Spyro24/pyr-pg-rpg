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
import map_ as mp

def map_load(x,y,w,h,leng):
    show = [] #ground layer
    hit  = [] #hitbox layer
    overlay = [] #Overdraw over the ground layer
    act  = [] #action laxer (for the dialog script)
    acthit = [] #IDK
    overdraw = [] #drawed over the character layer
    load_ = 1
    fil = open("../map/" + str(x) + "_" + str(y), "br")
    
    if load_:
        for a in range(0,w):
            for b in range(0,h):
                show.append(int.from_bytes(fil.read(leng), "big"))
                
        for a in range(0,w):
            for b in range(0,h):
                hit.append(int.from_bytes(fil.read(leng), "big"))
        
        #load script for overlay
        for a in range(0,w):
            for b in range(0,h):
                overlay.append(int.from_bytes(fil.read(leng), "big"))
        
        #load action map
        for a in range(0,w):
            for b in range(0,h):
                act.append(int.from_bytes(fil.read(leng), "big"))
                
        for a in range(0,w):
            for b in range(0,h):
                acthit.append(int.from_bytes(fil.read(leng), "big"))
                
        for a in range(0,w):
            for b in range(0,h):
                overdraw.append(int.from_bytes(fil.read(leng), "big"))
            
    return show,hit,overlay,act,acthit,overdraw

def draw_map(win, pos, scale, map_, h_w, *opn):
    xp = int(pos[0])
    yp = int(pos[1])
    size = (int(scale), int(scale))
    iter_ = 0
    if (opn == ()):
        opn = ("","")
    if opn[0] == "X":
        for h in range(0, int(h_w[0])):
            for w in range(0, int(h_w[0])):
                if map_[iter_] != 0:
                    img_ = p.transform.scale(p.image.load("./symbols/X.png"),size)
                    win.blit(img_,(xp + w * size[0], yp + h * size[1]))
                iter_ += 1
    elif opn[0] == "ov":
        for h in range(0, int(h_w[0])):
            for w in range(0, int(h_w[0])):
                if map_[iter_] != 0:
                    img_ = p.transform.scale(p.image.load("../tiles/overlay/" + str(map_[iter_]) + ".png"),size)
                    win.blit(img_,(xp + w * size[0], yp + h * size[1]))
                iter_ += 1
    else:
        for h in range(0, int(h_w[0])):
            for w in range(0, int(h_w[0])):
                if map_[iter_] != 0:
                    img_ = p.transform.scale(p.image.load("../tiles/" + str(map_[iter_]) + ".png"),size)
                    win.blit(img_,(xp + w * size[0], yp + h * size[1]))
                iter_ += 1
                
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
        print("Mapabove not exist")
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
        print("Mapabove not exist")
    map_border.append(empty2)
    
    try:
        empty3 = []
        iter_ = 0 
        cur_x = mpx + 1
        cur_y = mpy
        map_cur = mp.map_load(cur_x, cur_y, mw, mh, bs)
        for n in range(0, len(map_cur)):
            empty2.append([])
            for i in range(iter_, mh):
                print(i)
                empty3[n].append(map_cur[n][((i + 1) * mw) - 1])
    except BaseException as err:
        print(err)
        print("Map Left not exist")
    map_border.append(empty2)
    return map_border
            
def map_border_blit(win,mw,mh,pos,size,border, *opn):
    black = p.transform.scale(p.image.load("./symbols/task/gray_out.png"),(size, size))
    try:
        for e in range(0, len(border[0][0])):
            set_x = int(pos[0]) + (int(size) * e)
            set_y = int(pos[1]) - size + 1
            img_ = p.transform.scale(p.image.load("../tiles/" + str(border[0][0][e]) + ".png"),(size, size))
            win.blit(img_,(int(set_x),int(set_y)))
            win.blit(black,(int(set_x),int(set_y)))
    except:
        pass
    
    try:
        for e in range(0, len(border[1][0])):
            set_x = int(pos[0]) + (int(size) * e)
            set_y = int(pos[1]) + int(size) * mh
            img_ = p.transform.scale(p.image.load("../tiles/" + str(border[1][0][e]) + ".png"),(size, size))
            win.blit(img_,(int(set_x),int(set_y)))
            win.blit(black,(int(set_x),int(set_y)))
    except:
        pass
    
    try:
        for e in range(0, len(border[2][0])):
            set_x = int(pos[0]) - int(size)
            set_y = int(pos[1]) (int(size) * e)
            img_ = p.transform.scale(p.image.load("../tiles/" + str(border[1][0][e]) + ".png"),(size, size))
            win.blit(img_,(int(set_x),int(set_y)))
            win.blit(black,(int(set_x),int(set_y)))
    except:
        pass
