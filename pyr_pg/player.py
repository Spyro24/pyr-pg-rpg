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
    def __init__(self, game_win, config):
        self.gw = game_win
        self.main_config = config
        self.tiles_x, self.tiles_y = config["tiles_xy"]
        self.pos_x, self.pos_y = 0, 0
        self.debug_colors = config["debug_colors"]
        self.grid_pos_x, self.grid_pos_y = config["player_start_pos_xy"]
        self.state = [False]
        #---get shortest window size and create the tile sys for player---
        self.shortest_window_size = 0
        gw_w, gw_h = self.gw.get_size()
        if gw_w > gw_h: self.shortest_window_size = gw_h
        else: self.shortest_window_size = gw_w
        self.tile_size = self.shortest_window_size / self.tiles_y
        self.grid_zero_x, self.grid_zero_y = (gw_w / 2) - ((self.tiles_x / 2) * self.tile_size), (gw_h / 2) - ((self.tiles_y / 2) * self.tile_size)
        self.micro_tile = self.tile_size / config["micro_tiling"]
        #-----------------------------------------------------------------
        #---setup hitboxes---
        self.player_hitbox = p.Rect(( self.grid_zero_x + self.grid_pos_x * self.tile_size, self.pos_y),(self.tile_size, self.tile_size))
        self.player_hitbox_color = self.debug_colors["player_hitbox"]
        #-----------------------------------------------------------------
        
    def update(self):
        self.hit_map = self.map.get_hitbox()
        self.dia_map = self.map.get_dia()
    
    def move(self, x, y):
        #move the hitbox
        self.player_hitbox.move_ip(self.micro_tile * x, self.micro_tile * y)
        #set the state to move
        self.state.pop(0)
        self.state.insert(0, True)
    
    def render(self):
        pass
        
    def get_state(self, stat):
        return self.state[stat]
    
    def reset_resetable_states(self):
        self.state.pop(0)
        self.state.insert(0, False)
    
    def reset_state(self, stat):
        self.state.pop(stat)
        self.state.insert(stat, False)
    
    def _debug(self): #the function for the debug class(its a external module thats loads with the main script)
        p.draw.rect(self.gw, self.player_hitbox_color, self.player_hitbox, width=3)