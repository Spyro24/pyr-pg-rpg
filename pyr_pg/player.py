"""
    Player class for pyr_pg
    Copyright (C) 2023-2024 Spyro24

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
import time

class player():
    def reset_state(self):
        self.state = [False]
        
    def __init__(self, game_win, mf_w, mf_h, ts, p_f, start_pos, map, dia):
        self.gw = game_win
        self.dia = dia #Dialog object(to wrap the dia files
        self.mf_w = mf_w #move field width (in Tiles)
        self.mf_h = mf_h #move field hight (in Tiles)
        self.ts = ts #tile size
        self.facing = 0
        sprites = ["UP", "DOWN", "LEFT", "RIGHT"] #This contains all sprites
        self.x = 0
        self.y = 0
        self.tx = start_pos[0] #x position on map
        self.ty = start_pos[1] #y position on map
        self.reset_state()
        self.ww, self.wh = self.gw.get_size()
        #code for get the corect scale for the textures
        self.set_scale = 0
        if self.ww > self.wh: set_scale = self.wh
        else: self.set_scale = self.ww
        self.set_scale = self.set_scale / self.mf_w
        print(self.set_scale)
        #calculate the size for a move
        self.gw_x, self.gw_y = self.gw.get_size()
        set_scale = 0
        if self.gw_y > self.gw_x: set_scale = self.gw_x
        else: set_scale = self.gw_y
        self.scale = set_scale / self.mf_w
        self.in_x2 = int((self.gw_x / 2) - ((self.mf_w / 2) * self.scale))
        self.in_y2 = int((self.gw_y / 2) - ((self.mf_w / 2) * self.scale))
        print(self.in_x2, self.in_y2)
        self.points_x = self.scale * self.mf_w / (self.mf_w * self.ts)
        self.points_y = self.scale * self.mf_w / (self.mf_h * self.ts)
        
        self.player_scale = self.scale #Scale of the player sprite
        self.map = map
        tmp = []
        for sprite in sprites:
            tmp.append(p.transform.scale(p.image.load("./players/" + str(p_f) + "/" + str(sprite) + ".png"),(self.player_scale, self.player_scale)))
        self.sprites = tmp
        self.hit_map = map.get_hitbox()
        self.dia_map = self.map.get_dia()
        
        self.in_x = (self.ww / 2) - ((self.mf_w / 2) * self.set_scale)
        self.in_y = (self.wh / 2) - ((self.mf_h / 2) * self.set_scale)
        print(self.in_x, self.in_y)
            
    def update(self):
        self.hit_map = self.map.get_hitbox()
        self.dia_map = self.map.get_dia()
    
    def move(self, x, y):
        cur_tx = self.tx
        cur_ty = self.ty
        if y > 0: # Move DOWN
            test = self.ty + 1
            if test > self.mf_h - 1: test = self.mf_h - 1
            if not(self.hit_map[(test * self.mf_h) + self.tx] == 1):
                self.y += y
                
            if self.y >= self.ts:
                self.y = 0
                self.ty += 1
                
        elif y < 0: #Move UP
            test = self.ty
            if test < 0: test = 0
            if not(self.hit_map[(test * self.mf_h) + self.tx] == 1):
                self.y += y
                
            if self.y < 0:
                self.y = self.ts - 1
                self.ty -= 1
                
        if x > 0: #Move Right
            test = self.tx + 1
            if test > self.mf_h- 1: test = self.mf_h - 1
            if not(self.hit_map[(self.ty * self.mf_h) + test] == 1):
                self.x += x
                
            if self.x >= self.ts:
                self.x = 0
                self.tx += 1
                
        elif x< 0: #Move LEFT
            test = self.tx
            if test < 0: test = 0
            if not(self.hit_map[(self.ty * self.mf_h) + test] == 1):
                self.x += x
                
            if self.x < 0:
                self.x = self.ts - 1
                self.tx -= 1
        #move to the next map
        if (self.ty < 0) and (self.y < int(self.ts / 2)):
            self.map.move(0,-1)
            self.update()
            self.ty = self.mf_h - 1
            
        elif (self.ty > self.mf_h - 2) and (self.y > int(self.ts / 2) + 1):
            self.map.move(0,1)
            self.update()
            self.ty = -1
            
        if (self.tx < 0) and (self.x < int(self.ts / 2)):
            self.map.move(-1,0)
            self.update()
            self.tx = self.mf_w - 1
            
        elif (self.tx > self.mf_w - 2) and (self.x > int(self.ts / 2) + 1):
            self.map.move(1,0)
            self.update()
            self.tx = -1
        
        if (cur_tx != self.tx) or (cur_ty != self.ty):
            test = self.dia_map[(self.ty * self.mf_h) + self.tx]
            if not(test == 0):
                self.dia.wrap(test, self.map.get_pos())
            
        #set the state to move
        self.state.pop(0)
        self.state.insert(0, True)
    
    def render(self):
        print((self.in_x2 + (((self.tx *self.ts) + self.x) * self.points_x), self.in_y2 + (((self.ty *self.ts) + self.y) * self.points_x)))
        self.gw.blit(self.sprites[self.facing],(self.in_x2 + (((self.tx *self.ts) + self.x) * self.points_x), self.in_y2 + (((self.ty *self.ts) + self.y) * self.points_x)))
        
    def get_state(self, state):
        return self.state[state]
    
    def _debug(self): #the function for the debug class(its a external module thats loads with the main script)
        return self.facing, self.x, self.y, self.tx, self.ty