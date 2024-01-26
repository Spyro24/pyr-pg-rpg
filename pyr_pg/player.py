import pygame as p
import time
import pyr_pg.map_ as m

def move(win,px,py,dir_,size,mt,player_inf,map_,mw,mh,sp):
    # px and py are the player pos
    # dir is the player movement direction
    # mt is for seconds per frame
    if dir_ != None:
        if dir_ == "UP":
            x, y = px , py + 1
        elif dir_ == "DOWN":
            x, y = px , py -1
        elif dir_ == "LEFT":
            x, y = px + 1, py
        elif dir_ == "RIGHT":
            x, y = px - 1, py
        elif dir_ == "LUP":
            x, y = px + 1 , py + 1
        elif dir_ == "RUP":
            x, y = px - 1 , py + 1
        elif dir_ == "RWN":
            x, y = px - 1 , py - 1
        elif dir_ == "LWN":
            x, y = px + 1, py - 1
        mx, my = x * size, y * size
        sprite = str(player_inf[1])
        spl = p.image.load("./players/" + sprite + "/" + str(sp) + ".png")
        for n in range(0,size):
            m.red_area(win,x,y,2,size,map_,mw,mh)
            win.blit(spl,(mx,my))
            if dir_ == "UP":
                my -= 1
            elif dir_ == "DOWN":
                my += 1
            elif dir_ == "LEFT":
                mx -= 1
            elif dir_ == "RIGHT":
                mx += 1
            elif dir_ == "LUP":
                my -= 1
                mx -= 1
            elif dir_ == "RUP":
                my -= 1
                mx += 1
            elif dir_ == "RWN":
                mx += 1
                my += 1
            elif dir_ == "LWN":
                mx -= 1
                my += 1
            p.display.update()
            #time.sleep(mt)
            #print("exec")
        
    