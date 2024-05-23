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
p.init()

class dialog():
    def __init__(self, win, dialog_path,sprite_path, opn_set):
        self.pvar = opn_set #contains a dictionery for all vars and options of the game (Playername, gamename and more)
        self.gw = win #game window
        self.gw_x, self.gw_y = self.gw.get_size()
        self.path = dialog_path
        self.spath = sprite_path
        self.text_box = p.Surface((self.gw_x / 10 * 8, self.gw_y / 10 * 3)) #Initial Textbox
        #get the shortest window size
        if self.gw_x > self.gw_y: scale = self.gw_y
        else: scale = self.gw_x
        
        self.ts = int(scale/ 10) #Set how big a Dialog Tile is
        self._gen_box(0)
        self.font = (p.font.SysFont(p.font.get_default_font(),int(self.gw_x / 10))) #Main Font
        self.space = (self.gw_x / 20)
        self.textco = (255,255,255)
        self.bgcol = (0,0,0)
        
    def _wait_enter(self):
        wait = True
        while wait:
            sleep(0.05)
            for event in p.event.get():
                if event.type == p.KEYDOWN:
                    wait = False
                    
        
    def wrap(self, file_num, pos):
        auto_clear = False
        name = ""
        name_pos = (0,0)
        xp, yp = pos
        dia = open(self.path + str(xp) + "_" + str(yp) + "/" + str(file_num), "r")
        self.gw.blit(self.text_box,(self.ts, self.ts * 7))
        un_wrap = dia.readlines()
        un_wrap = [line.strip() for line in un_wrap]
        print(un_wrap)
        update = True
        for com in un_wrap:
            if auto_clear: #clear the screen after every instruction
                self.gw.fill(self.bgcol)
            
            com = com.split(";")
            if com[0][0] == "#":
                pass #only use is for commenting your dialog without a instruction
            elif com[0] == "wait_enter":
                self._wait_enter()
            elif com[0] == "set_box":
                self._gen_box(com[1])
            elif com[0] == "auto_clear":
                auto_clear = True
            else:
                if com[0][0] == "{":
                    name = self.pvar[com[0][1:len(com[0]) - 1]]
                else:
                    name = com[0]
                text = []
                get_mode = False
                get = ""
                cur_line = ""
                for char in com[1]:
                    
                    if get_mode:
                        if char == "}":
                            get_mode = False
                            cur_line += str(self.pvar[get])
                            get = ""
                        else:
                            get += char
                    else:
                        cur_line += char
                text.append(cur_line)
                
                dia_image = ""
                if com[2][0] == "{":
                    dia_image += self.pvar[com[2][1:len(com[2]) - 1]] + "/"
                else:
                    dia_image += str(com[2]) + "/"
                dia_image += str(com[3]) + "_"
                        
                    
                get_pos = com[4]
                if get_pos.lower() == "left":
                    name_pos = (1,3)
                    impos = (1 * self.ts,4 * self.ts)
                    dia_image += "left.png"
                elif get_pos.lower() == "right":
                    name_pos = (6,3)
                    impos = (6 * self.ts,4 * self.ts)
                    dia_image += "right.png"
                
                image_ = p.transform.scale(p.image.load(self.spath + dia_image),(self.ts * 3, self.ts * 3))
                
                #line render code
                rend_line = 0
                self.gw.blit(self.text_box,(self.ts, self.ts * 7))
                self.gw.blit(self.font.render(name, False,self.textco),(self.ts * name_pos[0] + self.ts / 10, self.ts * name_pos[1] + self.ts / 10))
                self.gw.blit(image_, impos)
                for line in text:
                    self.gw.blit(self.font.render((line), False,self.textco),(self.ts + self.ts / 10, self.ts * 7 + self.ts / 10))
                    update = True
                    
                
                    
            if update:   
                p.display.update()
                update = False
        
    def _gen_box(self, box):
        box_tiles = ["UP","DW","LE","RE","LE_UP_CO","RE_UP_CO","LE_DW_CO","RE_DW_CO","BG"] #The list with all availablen box tiles
        bxskn = str(box) #box skin number
        bxskns = [] #box skin tiles
        for bxt in box_tiles:
            bxskns.append(p.transform.scale(p.image.load(str(self.path) + "bg/" + str(bxskn) + "_" + str(bxt) + ".png"),(self.ts, self.ts)))
        
        #ik that this script is not optimized for its use
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

if __name__ == "__main__":
    test_win = p.display.set_mode((250*2, 250*2))
    test_dia = dialog(test_win, "../dialog/", "../players/", 0, 0, {"player":"Test", "player_sprite":"synth"})
    test_dia.wrap(0)