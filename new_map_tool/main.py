"""
    Map tool to edit pyr-pg maps.
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
import map_
import tile_selector
import min_map
import input_geter as inget

screen_res = map_.get_screen_res()
print(screen_res)
x_s_w = 48 #X size of the window
y_s_w = 32 #Y size of the window
gs = 16 #gridsize in px not the real size of the tiles)
factor = 1 #Scale factor (to use the tool on every display)
snap = gs * factor #Abs grid size

gw = p.display.set_mode((x_s_w * snap, y_s_w * snap))
mini_map = min_map.min_map(gw, ((x_s_w / 3) * 2 + 1) * snap, snap, ((x_s_w / 3) - 2) * snap)
map = map_.map_(gw, 16,16, 8, snap, (x_s_w / 3),0)
map.add_min_map(mini_map, 9)
tile_sel = tile_selector.tile_selector(gw,)
run = True
render = True
print(gw.get_size())
tile_sel.selector(snap * 4,(x_s_w / 3) * snap, (y_s_w  / 2) * snap,  map.export_tiles())
map_inp = inget.input_(gw,snap * (x_s_w / 3),0,snap,16,map)

while run:
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
            
    mouse_pos = p.mouse.get_pos()
    mouse_pres = p.mouse.get_pressed()
    
    if mouse_pres == (1,0,0):
        tile_sel.click(mouse_pos)
        map_inp.input(mouse_pos)
        render = True
        
            
    if render:
        #Put the render code here
        map.render()
        p.display.flip()
        render = False
            
p.quit()