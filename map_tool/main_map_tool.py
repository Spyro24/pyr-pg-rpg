"""
    The map editor for pyr_pg(this is included in the pyr_pg package folder)
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
from text import text_field as inp
import pywin as pw
import time
import map_ as prm
import tiles
from time import sleep

mapt_w_h, mapt_w_w = 500, 500  # the size of the window
mapt_win = p.display.set_mode((mapt_w_w, mapt_w_h))
mapt_run = True #run the map tool
mapt_mode = "EDIT" #maptool mode
mapt_lock = False #lock the loop in to the mode
mapt_w_update = False
mapt_if_red = False
tile_map_int = []
tile_map = []
tile_list = tiles.load_tile_list()
tile_png_list = tiles.load_images_from_lst("../tiles", tile_list)
tile_s_page = 0
tile_sel = 0
tile_cur = 0 #curent tile
text_size = 20
edit_layer = 0
symbols_raw = ["close", "arrow_left", "arrow_right", "null"]
symbols_load = pw.load_iconset("./symbols/task",symbols_raw)
tile_display = True
map_edges = []
map_tile_bytes = 2 #the tile len in bytes (Default: 2)
map_x = 0
map_y = 0
map_w = 16
map_h = 16
map_l_x = map_x
map_l_y = map_y
map_draw = False
map_cur = None
map_load = True
map_e_mode = "GROUND"
map_new = False
map_save = False
tile_size = int(((mapt_w_h / 10) * 8) / 18)
print(tile_size)
map_goto = None
map_layers = 6
map = prm.map(0,0,16,16,16,2,"../map/", True, mapt_win, [tile_list,tile_png_list])

while mapt_run:
    if mapt_mode == "EDIT":
        mapt_lock = True
        mapt_if_red = True
        mapt_win.fill((0,0,0))
        while mapt_lock:
            
            if mapt_if_red: #draw the interface
                pw.draw_rect(mapt_win, (mapt_w_h / 10) * 8, 0, mapt_w_h / 10 * 2, mapt_w_w / 10 , (125,125,125))
                pw.draw_font(mapt_win, text_size, (mapt_w_h / 10) * 8 + (mapt_w_h / 40), mapt_w_h / 40, "Tile", (0,0,0))
                pw.blit_icon(mapt_win, (mapt_w_h / 10) * 8, (mapt_w_w/ 10) * 1, symbols_load[1], (mapt_w_h / 10))
                pw.blit_icon(mapt_win, (mapt_w_h / 10) * 9, (mapt_w_w/ 10) * 1, symbols_load[2], (mapt_w_h / 10))
                
                #Draw Edit mode Buttons
                pw.draw_rect(mapt_win, 0, mapt_w_w / 10 * 8, mapt_w_h / 10 * 2, mapt_w_w / 10 , (125,125,125))
                pw.draw_rect(mapt_win, 0, mapt_w_w / 10 * 9, mapt_w_h / 10 * 2, mapt_w_w / 10 , (100,100,100))
                pw.draw_rect(mapt_win, mapt_w_h / 10 * 2, mapt_w_w / 10 * 8, mapt_w_h / 10 * 2, mapt_w_w / 10 , (100,100,100))
                pw.draw_rect(mapt_win, mapt_w_h / 10 * 2, mapt_w_w / 10 * 9, mapt_w_h / 10 * 2, mapt_w_w / 10 , (125,125,125))
                pw.draw_font(mapt_win, tile_size, (mapt_w_h / 40), mapt_w_w / 40 * 33, "Layer 0", (0,0,0))
                pw.draw_font(mapt_win, tile_size, (mapt_w_h / 40), mapt_w_w / 40 * 37, "Layer 1", (0,0,0))
                pw.draw_font(mapt_win, tile_size, (mapt_w_h / 40 * 9), mapt_w_w / 40 * 33, "Hitbox", (0,0,0))
                pw.draw_font(mapt_win, tile_size, (mapt_w_h / 40 * 9), mapt_w_w / 40 * 37, "Action", (0,0,0))
                tile_display = True
                mapt_w_update = True
                mapt_if_red = False
                map_draw = True
            
            if map_save:
                print("saved")
                mapf = open("../map/" + str(map_l_x) + "_" + str(map_l_y), "bw")
                map_ar = map_cur
                for element in map_ar:
                    for object in element:
                        mapf.write(int.to_bytes(int(object), length=int(map_tile_bytes), byteorder="big"))
                mapf.close()
                map_l_x = map_x
                map_l_y = map_y
                map_save = False
                
            if map_load:
                try:
                    map_cur = prm.map_load(map_x,map_y, map_w, map_h, map_tile_bytes)
                except:
                    map_new = True
                map_load = False
                map_draw = True
                
            if map_new:
                map_cur = []
                for layer in range(0,int(map_layers)):
                    map_cur.append([])
                    for pos in range(0,int(map_h * map_w)):
                        if layer == 0:
                            map_cur[layer].append(1)
                        else:
                            map_cur[layer].append(0)
                        
                map_draw = True
                map_new = False                
                
            if map_draw:
                pw.draw_rect(mapt_win,0,0,(mapt_w_h / 10) * 8, (mapt_w_h / 10) *8, (0,0,0))
                map.draw((mapt_w_h / 20),(mapt_w_h / 20), ((mapt_w_h / 10) * 8) / 18)
                prm.map_border_blit(mapt_win,map_w, map_h, ((mapt_w_h / 20),(mapt_w_h / 20)),tile_size, prm.map_border(map_x, map_y,map_w,map_h,map_tile_bytes))
                mapt_w_update = True
                map_draw = False
                
            if tile_display:
                if tile_cur > 0:
                    pw.blit_icon(mapt_win, (mapt_w_h / 10) * 9, 0, tile_png_list[edit_layer][tile_cur-1], (mapt_w_h / 10))
                else:
                    pw.blit_icon(mapt_win, (mapt_w_h / 10) * 9, 0, symbols_load[3], (mapt_w_h / 10))
                mapt_w_update = True
                tile_display = False
                
            if mapt_w_update:
                p.display.update()
                mapt_w_update = False
            
            for event in p.event.get():
                if event.type == p.QUIT:
                    mapt_lock = False
                    mapt_mode = None
                    mapt_run = False
                
            if pw.p_push_button((mapt_w_h / 10) * 8, 0, mapt_w_h / 10 * 2, mapt_w_w):
                if pw.p_push_button((mapt_w_h / 10) * 8, 0, mapt_w_h / 10 * 2, mapt_w_w / 10): #open the tile selector
                    mapt_mode = "TILE_SELECT"
                    mapt_lock = False
                    
                elif pw.p_push_button((mapt_w_w / 10) * 9, (mapt_w_h / 10) * 1, mapt_w_w / 10 , mapt_w_h / 10): #Right arrow button
                    if map_e_mode == "GROUND":
                        if tile_cur < len(tile_list[0]):
                            tile_cur += 1
                        tile_display = True
                        sleep(0.1)
                        
                elif pw.p_push_button((mapt_w_w / 10) * 8, (mapt_w_h / 10) * 1, mapt_w_w / 10 , mapt_w_h / 10): #Left arrow button
                    if tile_cur > 0:
                        tile_cur -= 1
                        tile_display = True
                        sleep(0.1)
            
            if pw.p_push_button(0, mapt_w_w / 10 * 8, mapt_w_h / 10 * 6, mapt_w_w / 10 * 2): #Moide Selector
                if pw.p_push_button(0, mapt_w_w / 10 * 8, mapt_w_h / 10 * 2, mapt_w_w / 10):
                    map_e_mode = "GROUND"
                    edit_layer = 0
                    redraw = True
                    sleep(0.1)
                if pw.p_push_button(0, mapt_w_w / 10 * 9, mapt_w_h / 10 * 2, mapt_w_w / 10 ):
                    edit_mode = 2
                    redraw = True
                    sleep(0.1)
                if pw.p_push_button(mapt_w_h / 10 * 2, mapt_w_w / 10 * 8, mapt_w_h / 10 * 2, mapt_w_w / 10):
                    map_e_mode = "HITBOX"
                    redraw = True
                    sleep(0.1)
                if pw.p_push_button(mapt_w_h / 10 * 2, mapt_w_w / 10 * 9, mapt_w_h / 10 * 2, mapt_w_w / 10):
                    edit_mode = 4
                    redraw = True
                    sleep(0.1)
                        
            if pw.p_push_button(0,0,(mapt_w_h / 10) * 8,(mapt_w_h / 10) * 8): #MapInteraction
                if pw.p_push_button((mapt_w_h / 20),(mapt_w_h / 20) - tile_size,(mapt_w_h / 20) + tile_size* map_w,(mapt_w_h / 20)): #Go one map up
                    map_y -= 1
                    map_save = True
                    map_load = True
                    map_draw = True
                    sleep(0.1)
                    
                elif pw.p_push_button((mapt_w_h / 20),(mapt_w_h / 20) + (tile_size * (map_h)),(mapt_w_h / 20) + tile_size * map_h,(mapt_w_h / 20)): #Go one map down
                    map_y += 1
                    map_save = True
                    map_load = True
                    map_draw = True
                    sleep(0.1)
                    
                elif pw.p_push_button((mapt_w_w / 20) + (tile_size * (map_w)),(mapt_w_w / 20),(mapt_w_w / 20),(mapt_w_w / 20) + tile_size * map_w): #Go one map right
                    map_x += 1
                    map_save = True
                    map_load = True
                    map_draw = True
                    sleep(0.1)
                    
                elif pw.p_push_button((mapt_w_w / 20) - tile_size,(mapt_w_w / 20),(mapt_w_w / 20),(mapt_w_w / 20) + tile_size * map_w): #Go one map left
                    map_x -= 1
                    map_save = True
                    map_load = True
                    map_draw = True
                    sleep(0.1)
                        
                void, set_t = pw.button_grid((mapt_w_h / 20),(mapt_w_h / 20),tile_size,map_w,map_h)
                if set_t != None:
                    if map_e_mode == "GROUND":
                        pw.draw_tile(mapt_win, ((mapt_w_h / 20),(mapt_w_h / 20)), False, tile_size, void, tile_png_list, tile_cur)
                        map_cur[0].pop(set_t)
                        map_cur[0].insert(set_t, tile_cur)
                    
                    elif map_e_mode == "HITBOX":
                        pw.draw_x(mapt_win, ((mapt_w_h / 20),(mapt_w_h / 20)),tile_size, void)
                        tester_ = map_cur[1].pop(set_t)
                        if tester_ == 1:
                            map_cur[1].insert(set_t, 0)
                            pw.draw_tile(mapt_win, ((mapt_w_h / 20),(mapt_w_h / 20)), False, tile_size, void,tile_png_list, map_cur[0][set_t])
                            pw.draw_tile(mapt_win, ((mapt_w_h / 20),(mapt_w_h / 20)), True, tile_size, void, tile_png_list,map_cur[2][set_t])
                            time.sleep(0.1)
                        else:
                            map_cur[1].insert(set_t, 1)
                            pw.draw_tile(mapt_win, ((mapt_w_h / 20),(mapt_w_h / 20)), False, tile_size, void,tile_png_list, map_cur[0][set_t])
                            pw.draw_tile(mapt_win, ((mapt_w_h / 20),(mapt_w_h / 20)), True, tile_size, void, tile_png_list,map_cur[2][set_t])
                            pw.draw_x(mapt_win, ((mapt_w_h / 20),(mapt_w_h / 20)), tile_size, void)
                            time.sleep(0.1)
                        
                    mapt_w_update = True
                    

#----------Tile Selector script--------------------------------------------------------------
    if mapt_mode == "TILE_SELECT":
        mapt_lock = True
        mapt_if_red = True
        mapt_win.fill((0,0,0))
        sleep(0.1)
        if map_e_mode == "HITBOX":
            mapt_lock = False
            mapt_mode == "EDIT"
            
        while mapt_lock:
            
            if mapt_if_red:
                mapt_win.fill((0,0,0))
                pw.icon_grid(mapt_win, 0, 0, mapt_w_w / 10, 10, 9, tile_png_list, tile_s_page, edit_layer)
                pw.blit_icon(mapt_win, (mapt_w_h / 10) * 8, (mapt_w_w/ 10) * 9, symbols_load[0], (mapt_w_h / 10))
                pw.blit_icon(mapt_win, (mapt_w_h / 10) * 1, (mapt_w_w/ 10) * 9, symbols_load[1], (mapt_w_h / 10))
                pw.blit_icon(mapt_win, (mapt_w_h / 10) * 3, (mapt_w_w/ 10) * 9, symbols_load[2], (mapt_w_h / 10))
                if tile_cur > 0:
                    pw.blit_icon(mapt_win, (mapt_w_h / 10) * 2, (mapt_w_w/ 10) * 9, tile_png_list[edit_layer][tile_cur-1], (mapt_w_h / 10))
                else:
                    pw.blit_icon(mapt_win, (mapt_w_h / 10) * 2, (mapt_w_w/ 10) * 9, symbols_load[3], (mapt_w_h / 10))
                mapt_if_red = False
                mapt_w_update = True
                
            if mapt_w_update:
                p.display.update()
                mapt_w_update = False
                
            for event in p.event.get():
                if event.type == p.QUIT:
                    mapt_lock = False
                    mapt_mode = None
                    mapt_run = False
                    
            if pw.p_push_button((mapt_w_h / 10), (mapt_w_w/ 10) * 9, mapt_w_h / 10 * 8, mapt_w_w / 10):
                if pw.p_push_button((mapt_w_w / 10) * 8, (mapt_w_h / 10) * 9, mapt_w_w / 10 , mapt_w_h / 10): #exit the tile selector
                    mapt_mode = "EDIT"
                    mapt_lock = False
                    
                if pw.p_push_button((mapt_w_w / 10), (mapt_w_h / 10) * 9, mapt_w_w / 10 , mapt_w_h / 10): #left arrow button
                    if tile_s_page > 0:
                        tile_s_page -= 1
                        mapt_if_red = True
                        sleep(0.1)
                        
                if pw.p_push_button((mapt_w_w / 10) * 3, (mapt_w_h / 10) * 9, mapt_w_w / 10 , mapt_w_h / 10): #Right arrow button
                    if tile_s_page < 729:
                        tile_s_page += 1
                        mapt_if_red = True
                        sleep(0.1)
                        
                
                    
            if pw.p_push_button(0, 0, mapt_w_h, mapt_w_w / 10 * 9):
                void, set_tile = pw.button_grid(0,0,(mapt_w_h / 10),10,9)
                if set_tile != None:
                    tile_cur = set_tile + 1
                    if tile_cur > len(tile_png_list[edit_layer]):
                        tile_cur = len(tile_png_list[edit_layer])
                    pw.blit_icon(mapt_win, (mapt_w_h / 10) * 2, (mapt_w_w/ 10) * 9, tile_png_list[edit_layer][tile_cur-1], (mapt_w_h / 10))
                    mapt_w_update = True
                
            

p.quit()