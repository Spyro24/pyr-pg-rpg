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
        
def draw_player(win,x,y,step,dir_,img_raw,ww,wh):
    #img raw is for a frame buffer obj(not a png)
    pass

def cahnge_x_y(cur_x, cur_y, face, num):
    rx = cur_x #set the return for x to curent x
    ry = cur_y #set the return for y to curent y
    fields = int(num) #The fields how long the player can move
    
    if face == "UP":
        rx -= fields
    elif face == "DOWN":
        rx += fields
    elif face == "LEFT":
        ry -= fields
    elif face == "RIGHT":
        ry += fields