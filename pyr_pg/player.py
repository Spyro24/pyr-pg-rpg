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
        
    def __init__(self, game_win, mf_w, mf_h, ts, p_f, start_pos, map):
        self.gw = game_win
        self.mf_w = mf_w #move field width (in Tiles)
        self.mf_h = mf_h #move field hight (in Tiles)
        self.ts = ts #tile size
        self.facing = 0
        sprites = ["UP", "DOWN", "LEFT", "RIGHT"] #This contains all sprites
        self.x = 0
        self.y = 0
        self.tx = start_pos[0] #x position on tile map
        self.ty = start_pos[1] #y position on tile map
        self.reset_state()
        self.ww, self.wh = self.gw.get_size()
        self.points_x = self.ww / (self.mf_w * self.ts)
        self.points_y = self.wh / (self.mf_h * self.ts)
        self.player_scale = self.ww / self.mf_w
        self.map = map
        tmp = []
        for sprite in sprites:
            tmp.append(p.transform.scale(p.image.load("./players/" + str(p_f) + "/" + str(sprite) + ".png"),(self.player_scale, self.player_scale)))
        self.sprites = tmp
            
    def update(self):
        pass
    
    def move(self, x, y):
        #hitboxscript
        #movescript
        self.x += x
        self.y += x
        
        if self.x >= self.ts:
            self.tx += 1
            self.x = 0
        elif self.x < 0:
            self.tx += -1
            self.x = self.ts - 1
        if self.tx < 0 and self.x < 8:
            self.tx = self.mf_w - 1
            self.map.move(-1,0)
            
        self.state.pop(0)
        self.state.insert(0, True)
    
    def render(self):
        self.gw.blit(self.sprites[self.facing],(((self.tx *self.ts) + self.x) * self.points_y, self.y * self.points_y))
        
    def get_state(self, state):
        return self.state[state]   