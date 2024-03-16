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
player_m_s = 0.15 #Player movement speed in seconds to move to the next field
player_m_t = 0 #this var is the actual time whilethe player is moving
player_m_state = False #this is True if the player move
player_character = 0 #The player sprite as a number
player_name = "" #The name of the player
player_sprite = rpg_player.load_sprites(player_character) #allplayer sprites as a frame bud obj
player_f_exit = False #This ia a function var to get if the player outside the window

#map vars
map_p_x = 0 #Map X position
map_p_y = 0 #Map Y position
map_load = False #if this is true the map are reloaded
map_map = [] #contains the the map in raw format (with the loaded tiles)
map_s_w = 16 #Wight of the map in Tiles
map_s_h = 16 #Hight of the map in Tiles
map_len = 2  #the length in bytes of a tile (numeric)
map_blit = False #Show the curent map

#dialog script vars
dialog_test = False #if this True the script tests the curent pos for a dialog script
dialog_run = False #runs the dialog script
dialog_num = None #the dialog script number

#key vars
key_wasd = True #Activate the WASD keys

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
        rpg_player.move_step(game_win, player_p_x, player_p_y, player_dir, player_sprite,(tile_size * tile_zoom) , (tile_size * tile_zoom))
        game_update = True
        while game:
            for event in p.event.get(): #we can call event.get() once in a run
                if event.type == p.QUIT:
                    game = False
                    run = False                    
            
            key_ar = list(p.key.get_pressed()) #get all pressed keys           
            if key_wasd: #get if WASD keys active
                player_move = rpg_kb.key_wasd(key_ar)
                
                if player_move != None:
                    player_dir = player_move #Set the players face direction to the movement direction
                    rpg_player.move_step(game_win, player_p_x, player_p_y, player_dir, player_sprite,(tile_size * tile_zoom) , (tile_size * tile_zoom))
                    hit_test = rpg_player.change_x_y(player_p_x, player_p_y, player_move, 1) #Change the player X and Y position to the new position for the hitbox test
                    if rpg_map.hit(hit_test[1], hit_test[0], map_s_w, map_s_h, map_map) == False:
                        player_p_x = hit_test[0]
                        player_p_y = hit_test[1]
                        player_m_state = True
                        
                    game_update = True
            
            if player_m_state:
                key_wasd = False
                if time_get() > (player_m_t + (player_m_s / (tile_size * tile_zoom))):
                    player_p_c += 1
                    if player_p_c > (tile_size * tile_zoom):
                        player_p_c = 0
                        player_m_state = False
                        key_wasd = True
                        player_f_exit = True
                        dialog_test = True
                    else:
                        rpg_player.move_step(game_win, player_p_x, player_p_y, player_dir, player_sprite, player_p_c, (tile_size * tile_zoom), map_s_w, map_s_h, map_map, 2)
                        game_update = True
                        player_m_t = time_get()
            
            if player_f_exit:
                map_load = True
                player_m_state = True
                if player_p_x > map_s_w - 1:
                    player_p_x = 0
                    map_p_x += 1 
                elif player_p_x < 0:
                    player_p_x = map_s_w - 1
                    map_p_x -= 1
                elif player_p_y > map_s_h - 1:
                    player_p_y = 0
                    map_p_y += 1
                elif player_p_y < 0:
                    player_p_y = map_s_h - 1
                    map_p_y -= 1
                else:
                    map_load = False
                    player_m_state = False
                    
                player_f_exit = False
                
            if dialog_test:
               dialog_run, dialog_num = rpg_map.diascr(player_p_x, player_p_y, map_s_w, map_s_h, map_map)
               dialog_test = False
               
            if dialog_run:
                reba = dialog_wrapper(game_win,[map_p_x, map_p_y], dialog_num)
                for n in range(0,len(reba)):
                    test_str = reba[n]
                    if test_str == "player_p_set":
                        rpg_player.hide(game_win, player_p_x, player_p_y, (tile_size * tile_zoom), map_s_w, map_s_h, map_map, 2)
                        player_p_x = reba[n + 1]
                        player_p_y = reba[n + 2]
                        rpg_player.move_step(game_win, player_p_x, player_p_y, player_dir, player_sprite, (tile_size * tile_zoom), (tile_size * tile_zoom), map_s_w, map_s_h, map_map, 2)
                
                game_update = True
                dialog_run = False
                
            if map_load: #load the map
                map_map = rpg_map.load(map_p_x, map_p_y, map_s_w, map_s_h, map_len)
                map_blit = True
                map_load = False

                
            if map_blit: #show curent map
                game_win.fill("black")
                rpg_map.blit(game_win,map_s_w, map_s_h, map_map,tl_size)
                update = True
                map_blit = False
            
            #update the display
            if game_update:
                p.display.flip()
                game_update = False
            
            #update the programm counter
            counter += 1
    
    
    if reset_save: #start reset loop to reset the save
        while reset_save:
            if game_update:
                p.display.flip()
                update = False
                
            

#on exit
p.quit()