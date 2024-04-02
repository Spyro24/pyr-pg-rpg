"""
    The map editor for pyr_pg(this is included in the pyr_pg execute folder)
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
tile_e_page = 0
tile_sel = 0
text_size = 20
edit_layer = 0
symbols_raw = ["close", "arrow_left", "arrow_right"]
symbols_load =

while mapt_run:
    if mapt_mode == "EDIT":
        mapt_lock = True
        mapt_if_red = True
        mapt_win.fill((0,0,0))
        while mapt_lock:
            
            if mapt_if_red == True:
                #draw the tile choser button
                pw.draw_rect(mapt_win, (mapt_w_h / 10) * 8, 0, mapt_w_h / 10 * 2, mapt_w_w / 10 , (125,125,125))
                pw.draw_font(mapt_win, text_size, (mapt_w_h / 10) * 8 + (mapt_w_h / 40), mapt_w_h / 40, "Tile", (0,0,0))
                mapt_w_update = True
                mapt_if_red = False
            
            if mapt_w_update == True:
                p.display.update()
                mapt_w_update = False
            
            for event in p.event.get():
                if event.type == p.QUIT:
                    mapt_lock = False
                    mapt_mode = None
                    mapt_run = False
            
            if pw.p_push_button((mapt_w_h / 10) * 8, 0, mapt_w_h / 10 * 2, mapt_w_w / 10):
                print("pressed")
                print("open Tile selector")
                mapt_mode = "TILE_SELECT"
                mapt_lock = False
                
    if mapt_mode == "TILE_SELECT":
        mapt_lock = True
        mapt_if_red = True
        mapt_win.fill((0,0,0))
        while mapt_lock:
            
            if mapt_if_red:
                pw.icon_grid(mapt_win, 0, 0, mapt_w_w / 10, 10, 9, tile_png_list, tile_e_page, edit_layer)
                pw.draw_box((mapt_w_w / 10) * 8, (mapt_w_h / 10) * 9, mapt_w_w / 10 , mapt_w_h / 10 , 4,(100, 100, 100), mapt_win)
                p.draw.line(mapt_win, (50,50,50),((mapt_w_w / 10) * 8, (mapt_w_h / 10) * 9),((mapt_w_w / 10) * 9, (mapt_w_h / 10) * 10),4)
                p.draw.line(mapt_win, (50,50,50),((mapt_w_w / 10) * 9, (mapt_w_h / 10) * 9),((mapt_w_w / 10) * 8, (mapt_w_h / 10) * 10),4)
                pw.draw_rect(mapt_win, (mapt_w_h / 10), (mapt_w_w/ 10) * 9, mapt_w_h / 10 * 7, mapt_w_w / 10 , (125,125,125))
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
                if pw.p_push_button((mapt_w_w / 10) * 8, (mapt_w_h / 10) * 9, mapt_w_w / 10 , mapt_w_h / 10):
                    print("pressed")
                    print("Back to Editmode")
                    mapt_mode = "EDIT"
                    mapt_lock = False

p.quit()