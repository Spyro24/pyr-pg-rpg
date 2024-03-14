"""
    Map modul for binary map files for pyr_pg (python role pygame)
    Copyright (C) 2023 Spyro24

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
import copy

def load(x, y, w, h, leng):
    show = [] #ground layer
    hit  = [] #hitbox layer
    overlay = [] #Overdraw over the ground layer
    act  = [] #action laxer (for the dialog script)
    acthit = [] #IDK
    overdraw = [] #drawed over the character layer
    load_ = 1
    try:
        fil = open("./map/" + str(x) + "_" + str(y), "br")
    except:
        print("[Err: Map load failed]\n[Err: no such map " +str(x) + "_" + str(y) + " ]")
        load_ = 0
    
    if load_:
        #Load the ground layer
        for a in range(0,w):
            for b in range(0,h):
                testing = int.from_bytes(fil.read(leng), "big")
                if testing != 0:
                    show.append(p.image.load("./tiles/" + str(testing) + ".png"))
                else:
                    show.append(0)
        
        #Load the hitbox layer
        for a in range(0,w):
            for b in range(0,h):
                hit.append(int.from_bytes(fil.read(leng), "big"))
        
        #Load the ground overlay layer
        for a in range(0,w):
            for b in range(0,h):
                testing = int.from_bytes(fil.read(leng), "big")
                if testing != 0:
                    overlay.append(p.image.load("./tiles/overlay/" + str(testing) + ".png"))
                else:
                    overlay.append(0)
                    
        #Load the action layer
        for a in range(0,w):
            for b in range(0,h):
                act.append(int.from_bytes(fil.read(leng), "big"))
                
        #Load the action hit layer
        for a in range(0,w):
            for b in range(0,h):
                acthit.append(int.from_bytes(fil.read(leng), "big"))
                
        #Load the ground overlay layer
        for a in range(0,w):
            for b in range(0,h):
                testing = int.from_bytes(fil.read(leng), "big")
                if testing != 0:
                    overdraw.append(p.image.load("./tiles/p_overlay/" + str(testing) + ".png"))
                else:
                    overdraw.append(0)
            
    return [show,hit,overlay,act,acthit,overdraw]

def blit(win,w,h,map_,size):
    iter_ = 0
    print(map_[2])
    for y in range(0,w):
        for x in range(0,h):
            if map_[0][iter_] != 0:
                win.blit(map_[0][iter_],(x * size, y * size))
            
            if map_[2][iter_] != 0:
                win.blit(map_[2][iter_],(x * size, y * size))
            
            iter_ +=1
            
def red_area(win,x,y,rad,size,map_,w,h,*opt):
    #A simple redraw function to redraw a map area
    #map_blit(win,w,h,map_,size)
    if rad <= 0:
        print("[ERR: radius can't below 1]\n[ERR: radius < 1]")
        return None
    
    layer = 0
    
    xr = y - rad
    yr = x - rad
    
    if xr < 0:
        xr = 0
    if yr < 0:
        yr = 0
     
    if len(opt) > 0:
        if opt[0] == 1:
            layer = 2
        elif opt[0] == 2:
            layer = 5
            
        leng = rad * 2 + 1
        for x_f in range(0,leng):
            bx = (xr * h) + (x_f * h)
            for y_f in range(0,leng):
                by = yr + y_f
                draw = by + bx
                if draw >= h * w:
                    draw = h * w - 1
                if map_[layer][draw ] != 0:
                    win.blit(map_[layer][draw ],((yr + y_f) * size,(xr + x_f)  * size))
        return None
        
    leng = rad * 2 + 1
    for x_f in range(0,leng):
        bx = (xr * h) + (x_f * h)
        for y_f in range(0,leng):
            by = yr + y_f
            draw = by + bx
            if draw >= h * w:
                draw = h * w - 1
            if map_[0][draw ] != 0:
                win.blit(map_[0][draw ],((yr + y_f) * size,(xr + x_f)  * size))
            if map_[2][draw ] != 0:
                win.blit(map_[2][draw ],((yr + y_f) * size,(xr + x_f)  * size))
    
def hit(y,x,w,h,map_):
    hit_p_m = map_[1]
    hit = False
    hit_pos = ((w * y) + x)
    if hit_p_m[hit_pos] == 1:
        hit = True
    return hit
    
    
def map_dia(x,y,map_,w,h):
    hit = False
    try:
        hitm = map_[3]
        pos = ((y * w) + (x + 1)) - 1
        if pos >= w * h:
            pos = (w * h) - 1
        elif pos < 0:
            pos = 0
        hitf = hitm[pos]
        
        if hitf > 0:
            hit = True
        return [hit, hitf]
    
    except: pass
    
