"""
    dialog class for pyr_pg to show dialogs
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
from time import sleep

class dialog():
    def __init__(self, win, dialog_path, px, py, opn_set):
        self.pvar = opn_set #contains a dictionery for all vars and options of the game (Playername, gamename and more)
        self.gw = win #game window
        self.gw_x, self.gw_y = self.gw.get_size()
        self.path = dialog_path
        self.px = px #Players map X position
        self.py = py #Players map X position
        self.text_box = p.Surface((self.gw_x / 10 * 8, self.gw_y / 10 * 3))
        self.ts = int(self.gw_x / 10)
        self._gen_box(0)
        
    def _wait_enter(self):
        wait = True
        while wait:
            sleep(0.05)
            for event in p.event.get():
                if event.type == p.KEYUP:
                    wait = False
                    
        
    def wrap(self, file_num):
        dia = open(self.path + str(self.px) + "_" + str(self.py) + "/" + str(file_num), "r")
        self.gw.blit(self.text_box,(self.ts, self.ts * 7))
        un_wrap = dia.readlines()
        un_wrap = [line.strip() for line in un_wrap]
        print(un_wrap)
        for com in un_wrap:
            com = com.split(";")
            if com[0][0] == "#":
                pass #only use is for commenting your dialog without a instruction
            elif com[0] == "wait_enter":
                self._wait_enter()
            elif com[0] == "set_box":
                self._gen_box(com[1])
                self.gw.blit(self.text_box,(self.ts, self.ts * 7))
            else:
                if com[0][0] == "{":
                    name = self.pvar[com[0][1:len(com[0])]- 1]
                
            p.display.update()
        
    def _gen_box(self, box):
        box_tiles = ["UP","DW","LE","RE","LE_UP_CO","RE_UP_CO","LE_DW_CO","RE_DW_CO","BG"] #The list with all availablen box tiles
        bxskn = str(box) #box skin number
        bxskns = [] #box skin tiles
        for bxt in box_tiles:
            bxskns.append(p.transform.scale(p.image.load(str(self.path) + "bg/" + str(bxskn) + "_" + str(bxt) + ".png"),(self.ts, self.ts)))
        
        #ik that this scriptis not optimized for its use
        for x in range(0,8):
            for y in range(0,3):
                if (x == 0) and (y == 0):
                    self.text_box.blit(bxskns[4],(self.ts * x, self.ts * y))
                elif ( 0 < x < 7) and (y == 0):
                    self.text_box.blit(bxskns[0],(self.ts * x, self.ts * y))
                elif (x == 7) and (y == 0):
                    self.text_box.blit(bxskns[5],(self.ts * x, self.ts * y))
                elif (x == 0) and (y == 1):
                    self.text_box.blit(bxskns[2],(self.ts * x, self.ts * y))
                elif ( 0 < x < 7) and (y == 1):
                    self.text_box.blit(bxskns[8],(self.ts * x, self.ts * y))
                elif (x == 7) and (y == 1):
                    self.text_box.blit(bxskns[3],(self.ts * x, self.ts * y))
                elif (x == 0) and (y == 2):
                    self.text_box.blit(bxskns[6],(self.ts * x, self.ts * y))
                elif ( 0 < x < 7) and (y == 2):
                    self.text_box.blit(bxskns[1],(self.ts * x, self.ts * y))
                elif (x == 7) and (y == 2):
                    self.text_box.blit(bxskns[7],(self.ts * x, self.ts * y))
    
test_win = p.display.set_mode((256*2, 256*2))
test_dia = dialog(test_win, "../dialog/", 0, 0, {})
test_dia.wrap(0)