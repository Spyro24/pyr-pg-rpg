#! /usr/bin/python3

"""
    main script to run a pyr_pg based rpg
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
import pyr_pg.map_ as rpg_map
import pyr_pg.player as rpg_player
import pyr_pg.kb as rpg_kb
from pyr_pg.dialog_ import dialog
from pyr_pg.launch_wrapper import launch_wrapper
from time import sleep
from time import time as time_get
import pyr_pg.sound as ps
import pyr_pg.debug as dbug
#import start as rpg_start_game_on_init

p.init()
run = True
#game_win = p.display.set_mode((768,512))
game_win = p.display.set_mode((256,512))
map = rpg_map.map(game_win,0,0,0,0,"./map/","./tiles/",16,16,16,2)
map.load()
dialog = dialog(game_win, "./dialog/", "./players/",  {"player":"Test", "player_sprite":"synth"})
player = rpg_player.player(game_win, 16, 16, 16, 0, (0,0), map, dialog)
music = ps.sound(game_win, "./music/")
music.play(0, "main")
MoveSpeed = 0.2
TileSize = 16
ms = MoveSpeed / TileSize
KT = time_get()
render_win = True
fc = 0
debug = True
deinf = dbug.debug(game_win, player, map, 30)


while run:
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
    
    key_ar = p.key.get_pressed()
    '''for n in range(0, len(key_ar)):
        if key_ar[n]:
            print(n)'''
    
    if (time_get() - ms) > KT:
        if key_ar[119]:
            player.move(0,-1)                    
        if key_ar[100]:
            player.move(1,0)                  
        if key_ar[115]:
            player.move(0,1)
        if key_ar[97]:
            player.move(-1,0)
        if player.get_state(0):
            KT = time_get()
            render_win = True
    
    if render_win:
        game_win.fill((0,0,0))
        player.reset_state()
        fc += 1
        map.render()
        player.render()
        if debug:
            deinf.render()
        p.display.flip()
        render_win = False


p.quit()