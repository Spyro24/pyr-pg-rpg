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
p.init(); gw = p.display.set_mode((int(init_val[2]) * int(init_val[3]), int(init_val[2]) * int(init_val[3]))); p.display.set_caption(init_val[0])
gww = int(init_val[2]) * int(init_val[3]); gwh = int(init_val[2]) * int(init_val[3]); tl_size = (init_val[2] * init_val[5])


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
            if update: #Update the Display
                gw.blit(background,(0,0))
                pwn.draw_rect(gw, 0, (gwh / 8 * 4), gww, (gwh / 8 * 3), (0,127,255))
                pwn.draw_rect(gw, 0, (gwh / 8 * (4 + int(choser))), gww, (gwh / 8 * 1), (255,42,0))
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
        while game:
            
            #we can call event.get() once in a run
            for event in p.event.get():
                if event.type == p.QUIT:
                    game = False
                    run = False
                    
            #get all pressed keys
            key_ar = list(p.key.get_pressed())
            
            #WASD key Script
            if wasd_act:
                direction = None
                if key_ar[3+23] and key_ar[3+1]:
                    direction = "LUP"                    
                elif key_ar[3+23] and key_ar[3+4]:
                    direction = "RUP"                    
                elif key_ar[3+1] and key_ar[3+19] :
                    direction = "LWN"                    
                elif key_ar[3+4]  and key_ar[3+19]:
                    direction = "RWN"                
                elif key_ar[3+23]:
                    direction = "UP"                    
                elif key_ar[3+1]:
                    direction = "LEFT"                    
                elif key_ar[3+19]:
                    direction = "DOWN"
                elif key_ar[3+4]:
                    direction = "RIGHT"
                    
            if load_map: #load the map
                if hit_on_map:
                    nex_map = rpg_map.map_load((x_m, y_m), (16,16), 2)
                else:
                    cur_map = rpg_map.map_load((x_m, y_m), (16,16), 2)
                load_map = False
                
            if blit_map: #show curent map
                game.fill("black")
                rpg_map.map_blit(game,mapx,mapy,cur_map,tl_size)
                update = True
                blit_map = False
                
            if p_moved: #get the move state of the player
                pass
            
            #update the display
            if update:
                p.display.flip()
                update = False
            
            #update the programm counter
            counter += 1
    
    
    if reset_save: #start reset loop to reset the save
        while reset_save:
            if update:
                p.display.flip()
                update = False
                
            

#on exit
p.quit()