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
    def __init__(self, runtimeStore: dict, test=False):
        self.config_version = "0.0.1"
        self.storage        = {"player_name":"",
                               "position":[0,0,0,0,0,0],#xPos, yPos, tileXPos, tileYPos, mapXPos, mapYPos
                               }
        if not test:
            import pyr_pg
            self.runtimeStore = runtimeStore
            self.gameWindow                  = self.runtimeStore[10][13]
            self.tiles_x, self.tiles_y       = self.runtimeStore[17]
            self.debug_colors                = self.runtimeStore[8]
            self.gridPosX, self.gridPosY = self.runtimeStore[19]
            self.state = [False]
            self.map = self.runtimeStore[21]
            self.microTiling = self.runtimeStore[3]
            self.characterPath = self.runtimeStore[16]
            self.playerSpriteName = self.runtimeStore[22]
            #---get shortest window size and create the tile sys for player---
            gw_w, gw_h = self.gameWindow.get_size()
            self.shortest_window_size = gw_w
            if gw_w > gw_h: self.shortest_window_size = gw_h
            self.tileSize = self.shortest_window_size / self.tiles_y
            self.grid_zero_x, self.grid_zero_y = (gw_w / 2) - ((self.tiles_x / 2) * self.tileSize), (gw_h / 2) - ((self.tiles_y / 2) * self.tileSize)
            self.micro_tile = self.tileSize / self.microTiling
            #-----------------------------------------------------------------
            #---setup hitboxes---
            self.player_hitbox       = p.Rect((self.grid_zero_x + self.gridPosX * self.tileSize, self.grid_zero_y + self.gridPosY* self.tileSize),(self.tileSize, self.tileSize))
            self.player_hitbox_color = self.debug_colors["player_hitbox"]
            self.npc_hitboxes        = []
            #-----------------------------------------------------------------
            #---setup hitpoints---
            self.diff     = self.microTiling / 2
            self.max_diff = self.microTiling
            #-----------------------------------------------------------------
            #---setup player positions---
            self.minorPosX = self.diff
            self.minorPosY = self.diff
            #---setup player other vars---
            self.facing              = "UP"
            self.state_table         = {"UP":(0,-1,-1,-1,1,-1,1,0,-1,0), "DOWN":(0,1,1,1,-1,1,-1,0,1,0),"LEFT":(-1,0,-1,1,-1,-1,0,-1,0,1),"RIGHT":(1,0,1,-1,1,1,0,1,0,-1)}
            self.player_flags        = {"DEATH":False, "ATACK":False, "INVULNERABLE": False, "AKTIVE": True}
            self.sprite_laoder       = pyr_pg.cutting_edge.CuttingEdge(str(self.playerSpriteName) + ".conf", str(self.characterPath))
            self.player_sprite_table = self.sprite_laoder.return_sprite_table()
            self.player_sprite       = p.transform.scale(self.player_sprite_table[self.facing],(self.tileSize, self.tileSize)) # rewrite this line in the future for the new sprites
            self.map.load()
            #-----------------------------------------------------------------
        
    def update(self):
        self.hit_map = self.map.get_hitbox()
        self.dia_map = self.map.get_dia()
        
    def set_flag(self, flag, value, table="FLAG_TABLE"):
        pass
    
    def move(self, x, y):
        #save all values that are modified
        test_hitbox     = self.player_hitbox.move(self.micro_tile * x, self.micro_tile * y)
        tmp_minor_pos_x = self.minorPosX + x
        tmp_minor_pos_y = self.minorPosY + y        
        hitbox_trigger  = False
        grid_pos_x      = self.gridPosX
        grid_pos_y      = self.gridPosY
        
        #get colisions with other rects
        #set new positions
        if tmp_minor_pos_x > self.max_diff:
            while tmp_minor_pos_x > self.max_diff:
                tmp_minor_pos_x -= self.max_diff
                grid_pos_x      += 1
                
        elif tmp_minor_pos_x < 0:
            while tmp_minor_pos_x < 0:
                tmp_minor_pos_x += self.max_diff
                grid_pos_x      -= 1
                
        if tmp_minor_pos_y > self.max_diff:
            while tmp_minor_pos_y > self.max_diff:
                tmp_minor_pos_y -= self.max_diff
                grid_pos_y      += 1
                
        elif tmp_minor_pos_y < 0:
            while tmp_minor_pos_y < 0:
                tmp_minor_pos_y += self.max_diff
                grid_pos_y      -= 1
        
        
        #go around the screen
        if grid_pos_x < 0:
            grid_pos_x = self.tiles_x - 1
            self.map.move(-1,0)
        elif grid_pos_x >= self.tiles_x:
            grid_pos_x = 0
            self.map.move(1,0)
            
        if grid_pos_y < 0:
            grid_pos_y = self.tiles_y - 1
            self.map.move(0,-1)
        elif grid_pos_y >= self.tiles_y:
            grid_pos_y = 0
            self.map.move(0,1)
        
        test_hitbox = p.Rect((self.grid_zero_x + ((grid_pos_x * self.tileSize) + ((tmp_minor_pos_x - self.diff) * self.micro_tile)), self.grid_zero_y + ((grid_pos_y * self.tileSize) + ((tmp_minor_pos_y - self.diff) * self.micro_tile))),(self.tileSize, self.tileSize))
            
        state = self.state_table[self.facing]
        get_hitbox = self.map.get_hitbox(self.gridPosX + state[0] , self.gridPosY + state[1])
        if get_hitbox != 0:
            if test_hitbox.colliderect(get_hitbox):
                hitbox_trigger = True
        get_hitbox_left  = self.map.get_hitbox(self.gridPosX + state[2], self.gridPosY + state[3])
        get_hitbox_right = self.map.get_hitbox(self.gridPosX + state[4], self.gridPosY + state[5])
        if (get_hitbox_left != 0) and test_hitbox.colliderect(get_hitbox_left):
            tmp_minor_pos_x += state[6]
            tmp_minor_pos_y += state[7]
        if (get_hitbox_right != 0) and test_hitbox.colliderect(get_hitbox_right):
            tmp_minor_pos_x += state[8]
            tmp_minor_pos_y += state[9]
                        
        #set all vars if the hitboxe arent trigered
        if not hitbox_trigger:
            self.minorPosX   = tmp_minor_pos_x
            self.minorPosY   = tmp_minor_pos_y
            self.gridPosX    = grid_pos_x
            self.gridPosY    = grid_pos_y
            self.player_hitbox = test_hitbox
            
        #set the state to move
        self.state.pop(0)
        self.state.insert(0, True)
    
    def render(self):
        self.gameWindow.blit(self.player_sprite, self.player_hitbox)
        
    def get_state(self, stat):
        return self.state[stat]
    
    def reset_resetable_states(self):
        self.state.pop(0)
        self.state.insert(0, False)
    
    def reset_state(self, stat):
        self.state.pop(stat)
        self.state.insert(stat, False)
    
    def resume_game(self, save_dict):
        self.facing = save_dict["player_facing"]
        
    def set_facing(self, facing_dir):
        self.facing        = facing_dir
        self.player_sprite = p.transform.scale(self.player_sprite_table[self.facing],(self.tileSize, self.tileSize))
        
    def import_file(self, file):
        pass
    
    def export_file(self, file):
        export = open(file, "bw")
        version = self.config_version.split(".")
        for num in version:
            export.write(int.to_bytes(int(num), 1, "little"))
        export.write(bytes(self.storage['player_name'], "UTF8")) #Player name
        export.write(int.to_bytes(255, 1, "little")) #spacer
        for pos in self.storage['position']:
            export.write(bytes(str(pos), "UTF8"))
            export.write(int.to_bytes(255, 1, "little")) #spacer
        export.close()
        
    def store(self, param):
        params = param
        if params[0] == "PlayerName":
            self.storage['player_name'] = params[1]
    
    def _debug(self): #the function for the debug class(its a external module thats loads with the main script)
        p.draw.rect(self.gameWindow, self.player_hitbox_color, self.player_hitbox, width=3)
        
if __name__ == "__main__":
    test_player = player(None, None, test=True)
    test_player.store(["PlayerName", "Test_Player"])
    test_player.export_file("./test_player")