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


        