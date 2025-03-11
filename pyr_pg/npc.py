class Npc():
   def __init__(self, game_win, config, test=False):
        self.config_version = "0.0.1"
        self.storage        = {"player_name":"", "position":[0,0,0,0,0,0]}
        if not test:
            import pyr_pg
            self.gw                          = game_win
            self.main_config                 = config
            self.tiles_x, self.tiles_y       = config["tiles_xy"]
            self.debug_colors                = config["debug_colors"]
            self.grid_pos_x, self.grid_pos_y = config["player_start_pos_xy"]
            self.state = [False]
            self.map = config["map"]
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
            self.player_hitbox       = p.Rect((self.grid_zero_x + self.grid_pos_x * self.tile_size, self.grid_zero_y + self.grid_pos_y* self.tile_size),(self.tile_size, self.tile_size))
            self.player_hitbox_color = self.debug_colors["player_hitbox"]
            self.npc_hitboxes        = []
            #-----------------------------------------------------------------
            #---setup hitpoints---
            self.diff     = config["micro_tiling"] / 2
            self.max_diff = config["micro_tiling"]
            #-----------------------------------------------------------------
            #---setup player positions---
            self.minor_pos_x = self.diff
            self.minor_pos_y = self.diff
            #---setup player other vars---
            self.facing              = "UP"
            self.state_table         = {"UP":(0,-1,-1,-1,1,-1,1,0,-1,0), "DOWN":(0,1,1,1,-1,1,-1,0,1,0),"LEFT":(-1,0,-1,1,-1,-1,0,-1,0,1),"RIGHT":(1,0,1,-1,1,1,0,1,0,-1)}
            self.NPCFlags            = {"DEATH":False, "ATACK":False, "INVULNERABLE": False, "AKTIVE": True}
            self.sprite_laoder       = pyr_pg.cutting_edge.CuttingEdge(str(config["player_sprite"]) + ".conf", str(config["character_path"]))
            self.NPCSpriteTable = self.sprite_laoder.return_sprite_table()
            self.player_sprite       = p.transform.scale(self.player_sprite_table[self.facing],(self.tile_size, self.tile_size)) # rewrite this line in the future for the new sprites
            #-----------------------------------------------------------------
        
    def update(self):
        self.hit_map = self.map.get_hitbox()
        self.dia_map = self.map.get_dia()
        
    def set_flag(self, flag, value, table="FLAG_TABLE"):
        pass
    
    def move(self, x, y):
        #save all values that are modified
        test_hitbox     = self.player_hitbox.move(self.micro_tile * x, self.micro_tile * y)
        tmp_minor_pos_x = self.minor_pos_x + x
        tmp_minor_pos_y = self.minor_pos_y + y        
        hitbox_trigger  = False
        grid_pos_x      = self.grid_pos_x
        grid_pos_y      = self.grid_pos_y
        
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
        
        test_hitbox = p.Rect((self.grid_zero_x + ((grid_pos_x * self.tile_size) + ((tmp_minor_pos_x - self.diff) * self.micro_tile)), self.grid_zero_y + ((grid_pos_y * self.tile_size) + ((tmp_minor_pos_y - self.diff) * self.micro_tile))),(self.tile_size, self.tile_size))
            
        state = self.state_table[self.facing]
        get_hitbox = self.map.get_hitbox(self.grid_pos_x + state[0] , self.grid_pos_y + state[1])
        if get_hitbox != 0:
            if test_hitbox.colliderect(get_hitbox):
                hitbox_trigger = True
        get_hitbox_left  = self.map.get_hitbox(self.grid_pos_x + state[2], self.grid_pos_y + state[3])
        get_hitbox_right = self.map.get_hitbox(self.grid_pos_x + state[4], self.grid_pos_y + state[5])
        if (get_hitbox_left != 0) and test_hitbox.colliderect(get_hitbox_left):
            tmp_minor_pos_x += state[6]
            tmp_minor_pos_y += state[7]
        if (get_hitbox_right != 0) and test_hitbox.colliderect(get_hitbox_right):
            tmp_minor_pos_x += state[8]
            tmp_minor_pos_y += state[9]
                        
        #set all vars if the hitboxe arent trigered
        if not hitbox_trigger:
            self.minor_pos_x   = tmp_minor_pos_x
            self.minor_pos_y   = tmp_minor_pos_y
            self.grid_pos_x    = grid_pos_x
            self.grid_pos_y    = grid_pos_y
            self.player_hitbox = test_hitbox
            
        #set the state to move
        self.state.pop(0)
        self.state.insert(0, True)
    
    def render(self):
        self.gw.blit(self.player_sprite, self.player_hitbox)
        
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
        self.player_sprite = p.transform.scale(self.player_sprite_table[self.facing],(self.tile_size, self.tile_size))
        
    def store(self, param):
        params = param
        if params[0] == "NPCName":
            self.storage['NPCName'] = params[1]
    
    def _debug(self): #the function for the debug class(its a external module thats loads with the main script)
        p.draw.rect(self.gw, self.player_hitbox_color, self.player_hitbox, width=3)