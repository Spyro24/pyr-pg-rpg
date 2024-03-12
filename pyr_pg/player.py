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

def blit(game_win, px, py, rot, player_spr, ts):
    spr = player_spr
    sprite = "UP"
    if rot == "UP":
        sprite = "UP"
    elif rot == "DOWN":
        sprite = "DOWN"
    elif rot == "LEFT":
        sprite = "LEFT"
    elif rot == "RIGHT":
        sprite = "RIGHT"
    elif rot == "LUP":
        sprite = "LEFT"
    elif rot == "RUP":
        sprite = "UP"
    elif rot == "RWN":
        sprite = "RIGHT"
    elif rot == "LWN":
        sprite = "DOWN"
    
    game_win.blit(player,(px,py))
    

def change_x_y(cur_x, cur_y, face, num):
    rx = cur_x #set the return for x to curent x
    ry = cur_y #set the return for y to curent y
    fields = int(num) #The fields how long the player can move
    
    if face == "UP":
        ry -= fields
    elif face == "DOWN":
        ry += fields
    elif face == "LEFT":
        rx -= fields
    elif face == "RIGHT":
        rx += fields
    elif face == "LUP":
        ry -= 1
        rx -= 1
    elif face == "RUP":
        ry -= 1
        rx += 1
    elif face == "RWN":
        ry += 1
        rx += 1
    elif face == "LWN":
        rx -= 1
        ry += 1
    
    return rx, ry

def move_step(win, x, y, dir_, player_sprite, step, ts, *opt):
    #opt contents: map_w, map_h, map_map, area_with
    if len(opt) > 0:
        if len(opt) == 4:
            m.red_area(win,x,y,int(opt[3]),ts,opt[2],opt[0],opt[1])
    
    if dir_ == "DOWN":
        pos_y = (y - 1) * ts
        pos_x = x * ts
        win.blit(player_sprite[2],(pos_x, pos_y + step))
    elif dir_ == "UP":
        pos_y = (y + 1) * ts
        pos_x = x * ts
        win.blit(player_sprite[0],(pos_x, pos_y - step))
    elif dir_ == "LEFT":
        pos_y = y * ts
        pos_x = (x + 1) * ts
        win.blit(player_sprite[1],(pos_x - step, pos_y))
    elif dir_ == "RIGHT":
        pos_y = y * ts
        pos_x = (x - 1) * ts
        win.blit(player_sprite[3],(pos_x + step, pos_y))
        
def load_sprites(player):
    player_sprites = []
    faces = ["UP", "LEFT", "DOWN", "RIGHT"]
    for face in faces:
        player_sprites.append(p.image.load("./players/" + str(player) + "/" + str(face) + ".png"))
    return player_sprites