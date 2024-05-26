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

gw = p.display.set_mode((512,256+128))
map = map_.map_(gw, 16,16, 8)
run = True
render = True

while run:
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
            
    if render:
        #Put the render code here
        map.render()
        render = False
            
p.quit()