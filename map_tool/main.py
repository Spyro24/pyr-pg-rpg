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
import time
from time import sleep
import map_pg
from map_pg import tile_handler

class Main():
    def __init__(self):
        #---mapeditor configuration---
        self.debug = True
        self.tiling_wh = (48,34)
        self.caption = "PYR_PG Map Editor V0.1"
        self.tiles_per_page = 12 * 6
        #-----------------------------
        self.init_window()
        self.load_tiles()
        #---internal vars (DO NOT CHANGE)---
        self.map_size_tiles = (16,16)
        self.settings = {"window":self.editor_display, "bg_tiles":self.ground_tiles.retun_tiles(), "gd_tiles":self.overlay_tiles.retun_tiles(), "ov_tiles":[]}
        self.quit = False
        self.editor_tile_sheet_pos = 0
        self.cur_selected_tile = 0
        self.edit_mode = 0
        self.tile_editor_action_bar = map_pg.clickgrid.ClickGrid((12,2),(0, 26*self.tiling_size, 48*self.tiling_size, 8*self.tiling_size))
        self.tile_choser_tile_selector = map_pg.clickgrid.ClickGrid((12,6),(0, 2*self.tiling_size, 48*self.tiling_size, 24*self.tiling_size))
        self.map_manipulator_grid = map_pg.clickgrid.ClickGrid(self.map_size_tiles,(16 * self.tiling_size, 2 *self.tiling_size, 16 * self.tiling_size, 16 * self.tiling_size))
        self.bg_col = (0,0,0)
        #-----------------------------------
        #---loading images---
        self.tile_selctor_menu_bar = p.image.load("./symbols/menu_bar_tile_selector.png")
        self.editor_images_dict = {"no_tile":p.transform.scale(p.image.load("./symbols/no_tile.png"),(4*self.tiling_size, 4*self.tiling_size))}
        #--------------------
        self.create_map_obj(self.settings)
        self.editor_loop()
        
    def load_tiles(self):
        self.ground_tiles = tile_handler.tile_handler("../tiles/ground", {"size":"12x6"})
        self.overlay_tiles = tile_handler.tile_handler("../tiles/overlay", {"size":"12x6"})
        self.ground_tiles.add_gw(self.editor_display)
        self.overlay_tiles.add_gw(self.editor_display)
        
    def create_map_obj(self, param_dict):
        self.map_object = map_pg.map_.map(param_dict)
        self.map_object.load()
        
    def init_window(self):
        self.create_config()
        p.display.set_caption(self.caption)
    
    def create_config(self):
        get_size_win = p.display.set_mode()
        win_size = get_size_win.get_size()
        win_w, win_h = win_size
        self.tiling_size = 0
        if win_w > win_h:
            self.tiling_size = int(win_h / self.tiling_wh[0])
        else:
            self.tiling_size = int(win_w / self.tiling_wh[1])
        self.editor_display = p.display.set_mode((self.tiling_size * self.tiling_wh[0], self.tiling_size * self.tiling_wh[1]))
        
    def render_map(self):
        if self.edit_mode == 0:
            self.map_object.render(0, (16 * self.tiling_size, 2 *self.tiling_size), (16 * self.tiling_size, 16 * self.tiling_size))
            
    def show_single_tile(self, pos, size, tile):
        if self.edit_mode == 0:
            self.editor_display.blit(p.transform.scale(self.settings["bg_tiles"][tile], size), pos)
            
    def show_tile_sheet(self):
        if self.edit_mode == 0:
            self.ground_tiles.draw_map(self.editor_tile_sheet_pos, (0,2*self.tiling_size), 24*self.tiling_size)
        
    def tile_selector(self):
        run = True
        update = True
        redraw = True
        clicked = False
        while run:
            if redraw:
                self.editor_display.fill(self.bg_col)
                self.show_tile_sheet()
                self.editor_display.blit(map_pg.image_helper.scale_on_h(self.tile_selctor_menu_bar, 8 * self.tiling_size), (0, 26*self.tiling_size))
                if self.cur_selected_tile > 0:
                        self.show_single_tile((self.tiling_size * 8, self.tiling_size * 30), (self.tiling_size * 4, self.tiling_size * 4), self.cur_selected_tile - 1)
                redraw = False
                update = True
                
            for event in p.event.get():
                if event.type == p.QUIT:
                    run = False
                    self.quit = True
            
            mpos = p.mouse.get_pos()
            mclick = p.mouse.get_pressed()
            
            if (not clicked) and (mclick[0] == True):
                clicked = True
                action_bar_pos = self.tile_editor_action_bar.get_click(mpos)
                selected_tile_pos = self.tile_choser_tile_selector.get_click(mpos)
                selected_tile_num = self.tile_choser_tile_selector.return_number(mpos)
                print(selected_tile_num)
                print(action_bar_pos)
                if action_bar_pos == (1, 1):
                    run = False
                elif action_bar_pos == (6, 1):
                    self.editor_tile_sheet_pos = 0
                    self.cur_selected_tile = 0
                    redraw = True
                elif action_bar_pos == (4, 1):
                    self.editor_tile_sheet_pos += 1
                    try:
                        self.show_tile_sheet()
                        redraw = True
                    except:
                        self.editor_tile_sheet_pos -= 1
                elif action_bar_pos == (3, 1):
                    if self.editor_tile_sheet_pos > 0:
                        self.editor_tile_sheet_pos -= 1
                        redraw = True
            elif mclick[0] == False:
                clicked = False
                    
                        
                
            if (selected_tile_num + 1) > 0:
                self.cur_selected_tile = (self.editor_tile_sheet_pos * self.tiles_per_page) + (selected_tile_num + 1)
                if self.cur_selected_tile > 0:
                    self.show_single_tile((self.tiling_size * 8, self.tiling_size * 30), (self.tiling_size * 4, self.tiling_size * 4), self.cur_selected_tile - 1)
                    update = True
                    
            
            if update:
                p.display.flip()
            
    def change_tile(self, pos):
        if self.edit_mode == 0:
            self.map_object.change_tile(pos, 0, self.cur_selected_tile)
        
    def editor_loop(self):
        update = True
        redraw = True
        selector_activate = self.editor_display.blit(self.editor_images_dict["no_tile"],(self.tiling_size * 16, self.tiling_size * 18))
        while not self.quit:
            if redraw:
                self.editor_display.fill(self.bg_col)
                self.render_map()
                if self.cur_selected_tile == 0:
                    self.editor_display.blit(self.editor_images_dict["no_tile"],(self.tiling_size * 16, self.tiling_size * 18))
                else:
                    self.show_single_tile((self.tiling_size * 16, self.tiling_size * 18),(self.tiling_size * 4, self.tiling_size * 4), self.cur_selected_tile - 1)
                redraw = False
                update = True
            
            for event in p.event.get():
                if event.type == p.QUIT:
                    run = False
                    self.quit = True
            
            mpos = p.mouse.get_pos()
            mclick = p.mouse.get_pressed()
            if mclick[0] == True:
                if selector_activate.collidepoint(mpos):
                    self.tile_selector()
                    redraw = True
                    
                elif self.map_manipulator_grid.activate_rect.collidepoint(mpos):
                    change_tile_coords = self.map_manipulator_grid.get_click(mpos)
                    print(change_tile_coords)
                    self.change_tile(change_tile_coords)
                    redraw = True
            
            if update:
                p.display.flip()
            
    def quit_editor(self):
        self.map_object.save_map()
        p.quit()

if __name__ == "__main__":
    #try:
        Editor = Main()
    #except BaseException as err:
    #    print(err)
    #finally:
        Editor.quit_editor()
        