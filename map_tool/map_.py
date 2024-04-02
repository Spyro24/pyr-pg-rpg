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
    if opn == ():
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