import pygame as p
import time
import pyr_pg.map_ as m

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
    if len(opt) == 4:
        m.red_area(win,x,y,int(opt[3]),ts,opt[2],opt[0],opt[1],0)
        m.red_area(win,x,y,int(opt[3]),ts,opt[2],opt[0],opt[1],1)
    
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
    elif dir_ == "LUP":
        pos_y = (y + 1)* ts
        pos_x = (x + 1) * ts
        win.blit(player_sprite[1],(pos_x - step, pos_y - step))
    elif dir_ == "RUP":
        pos_y = (y + 1)* ts
        pos_x = (x - 1) * ts
        win.blit(player_sprite[0],(pos_x + step, pos_y - step))
    elif dir_ == "LWN":
        pos_y = (y - 1)* ts
        pos_x = (x + 1) * ts
        win.blit(player_sprite[2],(pos_x - step, pos_y + step))
    elif dir_ == "RWN":
        pos_y = (y - 1)* ts
        pos_x = (x - 1) * ts
        win.blit(player_sprite[3],(pos_x + step, pos_y + step))
        
    if len(opt) == 4:
        m.red_area(win,x,y,int(opt[3]),ts,opt[2],opt[0],opt[1],2)
        
def load_sprites(player):
    player_sprites = []
    faces = ["UP", "LEFT", "DOWN", "RIGHT"]
    for face in faces:
        player_sprites.append(p.image.load("./players/" + str(player) + "/" + str(face) + ".png"))
    return player_sprites