"""
    mini map class tro create a mini map for the maptool
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
from subprocess import run as sub_run
from subprocess import PIPE

class min_map():
    def __init__(self, gw, x, y, size):
        self.px = x
        self.py = y
        self.size = size
        self.gw = gw
        self.min_map = p.Surface((1,1))
        
    def create(self,rad,path,pos):
        red = (80 , 80, 80)
        green = (150, 150, 150)
        radian = 2 * rad + 1
        posx = pos[0] - rad
        posy = pos[1] - rad
        raw_min_map = sub_run(["ls","-v",path],stdout=PIPE)
        raw_min_map = raw_min_map.stdout.decode("UTF-8").splitlines()
        self.min_map = p.Surface((radian,radian))
        for x in range(0,radian):
            for y in range(0, radian):
                if str(x + posx) + "_" + str(y + posy) in raw_min_map:
                    self.min_map.set_at((x,y), green)
                else:
                    self.min_map.set_at((x,y), red)
                    
    def render(self):
        self.gw.blit(p.transform.scale(self.min_map,(self.size, self.size)),(self.px, self.py))
        
"""if __name__ == "__main__":
    print("hello")
    
    window = p.display.set_mode((512,512))
    mm = min_map(window,0,0,512)
    mm.create(7, "../map",(0,0))
    mm.render()
    p.display.flip()"""