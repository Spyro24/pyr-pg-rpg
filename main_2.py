#! /usr/bin/python3

"""
    main script to run a pyr_pg based rpg
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
import pyr_pg.map_ as rpg_map
import pyr_pg.player as rpg_player
import pyr_pg.kb as rpg_kb
from pyr_pg.dialog import dialog_wrapper
from pyr_pg.launch_wrapper import launch_wrapper
import pyr_pg.pywin as pwn
from time import sleep
from time import time as time_get

#settings
init_val = launch_wrapper("./game.rpg"); x_m = 0; y_m = 0
speed_glob = 0.5
mpx, mpy = init_val[6]

#internal vars(DO NOT CHANGE)
update = False; counter = 0; load_map = False; next_map = None; blit_map = False; title_screen = False; next_map = None; hit_on_map = False;
game = True; choser = 0; block_time = 0.0; ar_key_time = 0; p_moved = False; reset_save = False; wasd_act = True

#init commands
p.init(); p.display.set_caption(init_val[0])
tl_size = (init_val[2] * init_val[5])

#game window
game_win = p.display.set_mode((int(init_val[2]) * int(init_val[3]), int(init_val[2]) * int(init_val[3]))) #Game window
game_w_w = int(init_val[2]) * int(init_val[3]) #Game window W
game_w_h = int(init_val[2]) * int(init_val[3]) #Game window H
game_update = False # update the window of the game

#player vars
player_p_x = 0 #Players X position
player_p_y = 0 #Players Y position
player_move = None #Players movement direction
player_dir = "UP" #Players face direction
player_p_c = 0 #Player position counter for move.(0 for curent field and tile_size + 1 for next field)
player_m_s = 1 #Player movement speed in seconds to move to the next field
player_m_t = 0 #this var is the actual time whilethe player is moving
player_m_state = False #this is True if the player move

#map vars
map_p_x = 0 #Map X position
map_p_y = 0 #Map Y position
map_load = False #if this is true the map are reloaded
map_map = [] #contains the the map in raw format (with the loaded tiles)
map_s_w = 16 #Wight of the map in Tiles
map_s_h = 16 #Hight of the map in Tiles
map_len = 2  #the length in bytes of a tile (numeric)

#key vars

#tiles var
tile_size = 16 #The tiles size in pixel
tile_zoom = 1 #the zoom of the tiles (DON NOT CHANGE) (this var is reserved for the internals)

#main function
run = True
title_screen = True

#uncomment this lines for beta test
title_screen = False #execute the titlescreen loop
game = True #execute the game loop


while run:
    if title_screen: #check for the title screen
        update = True #Refresh the screen
        pos = 0 #The position of the pointer
        background = p.image.load("./images/back.png") #load the title background
        while title_screen: #titlescreen loop
            events_ = p.event.get()
            p.event.clear()
            for event in events_:
                if event.type == p.QUIT:
                    run = False
                    title_screen = False
            
            key_ar = list(p.key.get_pressed()) #Aray with all keys
            if game_update: #Update the Display
                game_win.blit(background,(0,0))
                pwn.draw_rect(game_win, 0, (game_w_h / 8 * 4), game_w_w, (game_w_h / 8 * 3), (0,127,255))
                pwn.draw_rect(game_win, 0, (game_w_h / 8 * (4 + int(choser))), game_w_w, (game_w_h / 8 * 1), (255,42,0))
                p.display.flip()
                update = False
            
            if (key_ar[3+19] or key_ar[3+23]) == False:
                block_time = 0
                
            if (time_get() - block_time) > 0.25:
                if key_ar[3+19] == key_ar[3+23]:
                    pass
                
                elif key_ar[3+19]:
                    if choser < 2:
                        choser += 1
                        update = True
                        block_time = time_get()
                        
                        
                elif key_ar[3+23]:
                    if choser > 0:
                        choser -= 1
                        update = True
                        block_time = time_get()
            
            if key_ar[44]:
                if choser == 0:
                    pass
                    
                
    if game: #start Game loop
        map_map = rpg_map.load(map_p_x, map_p_y, map_s_w, map_s_h, map_len)
        rpg_map.blit(game_win, map_s_w, map_s_h, map_map, tile_size * tile_zoom)
        game_update = True
        while game:
            for event in p.event.get(): #we can call event.get() once in a run
                if event.type == p.QUIT:
                    game = False
                    run = False                    
            
            key_ar = list(p.key.get_pressed()) #get all pressed keys           
            if wasd_act: #get if WASD keys active
                player_move = None
                if key_ar[3+23] and key_ar[3+1]:
                    player_move = "LUP"                    
                elif key_ar[3+23] and key_ar[3+4]:
                    player_move = "RUP"                    
                elif key_ar[3+1] and key_ar[3+19] :
                    player_move = "LWN"                    
                elif key_ar[3+4]  and key_ar[3+19]:
                    player_move = "RWN"                
                elif key_ar[3+23]:
                    player_move = "UP"                    
                elif key_ar[3+1]:
                    player_move = "LEFT"                    
                elif key_ar[3+19]:
                    player_move = "DOWN"
                elif key_ar[3+4]:
                    player_move = "RIGHT"
                
                if player_move != None:
                    player_dir = player_move #Set the players face direction to the movement direction
                    
            if map_load: #load the map
                if hit_on_map:
                    nex_map = rpg_map.map_load((x_m, y_m), (16,16), 2)
                else:
                    cur_map = rpg_map.map_load((x_m, y_m), (16,16), 2)
                load_map = False
                
            if blit_map: #show curent map
                game.fill("black")
                rpg_map.map_blit(game,map_s_w, map_s_h, map_map,tl_size)
                update = True
                blit_map = False
                
            if p_moved: #get the move state of the player
                pass
            
            #update the display
            if game_update:
                p.display.flip()
                game_update = False
            
            #update the programm counter
            counter += 1
    
    
    if reset_save: #start reset loop to reset the save
        while reset_save:
            if update:
                p.display.flip()
                update = False
                
            

#on exit
p.quit()