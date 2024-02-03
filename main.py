import pygame as p
import pyr_pg.map_ as rpg_map
import pyr_pg.player as rpg_player
import pyr_pg.kb as rpg_kb
from pyr_pg.dialog import dialog_wrapper
import time

version_ = 0.1

sleeeep = True #Set it to False  if the programm runs to slow

game = p.display.set_mode((16*16,16*16))

size = 16
maxx, maxy = 16,16
max_lim = 0
last_dir= "UP"
sp_ = "UP"
inventory = []
player_stats = []


mapx,mapy = 0, 0
map_ = rpg_map.map_load(0,0,16,16,2)
print(map_)
print(map_[1])
rpg_map.map_blit(game,16,16,map_,size)


x_move, y_move = 0, 0

pls = 0 

update = 1

x_pos, y_pos = 8,8
last_xy = x_pos, y_pos

run = 1

while run:
    if sleeeep:
        time.sleep(0.1)

    
    events_ = p.event.get()
    p.event.clear()
    # Update script
    if update:
        rpg_map.red_area(game,x_pos,y_pos,1,size,map_,maxx,maxy)
        game.blit(p.image.load("./players/" + str(pls) + "/" + str(sp_) + ".png"),(x_pos * size, y_pos * size))
        p.display.flip()
        update = 0
    
    # menu script
    
    # move script
    dir_, pressed = rpg_kb.wasd_arrow_2d()
    if pressed:
        last_xy = x_pos, y_pos
        if dir_ == "LUP":
            y_pos -= 1
            x_pos -= 1
            sp_ = "UP"
        elif dir_ == "RUP":
            y_pos -= 1
            x_pos += 1
            sp_ = "RIGHT"
        elif dir_ == "RWN":
            y_pos += 1
            x_pos += 1
            sp_ = "DOWN"
        elif dir_ == "LWN":
            y_pos += 1
            x_pos -= 1
            sp_ ="LEFT"
        elif dir_ == "UP":
            y_pos -= 1
            sp_ ="UP"
        elif dir_ == "DOWN":
            y_pos += 1
            sp_ ="DOWN"
        elif dir_ == "LEFT":
            x_pos -= 1
            sp_ ="LEFT"
        elif dir_ == "RIGHT":
            x_pos += 1
            sp_ ="RIGHT"
        
        if dir_ != None:
            last_dir = dir_
        update = 1
    
    # hitbox script
    if rpg_map.map_hit(x_pos,y_pos, map_, maxx, maxy):
        x_pos, y_pos = last_xy
        pressed = False
    
    #test for actions on map
    dial = rpg_map.map_dia(x_pos,y_pos, map_, maxx, maxy)
    if dial[0] != False:
        pressed == False
        dialog = dialog_wrapper(game, (mapx, mapy), int(dial[1]), [player_stats, inventory, map_, [maxx, maxy]])
        print(dialog)
        if dialog[0] != None:
            pos_this = dialog[0]
            x_pos = pos_this[0]
            y_pos = pos_this[1]
        
    # Around Script and show Player move
    if pressed == True:
        rpg_player.move(game,x_pos,y_pos,dir_,size,0.01,["",0],map_,16,16,sp_)
        if x_pos >= maxx:
            x_pos = 0
            mapx += 1
            max_lim = 1
        if x_pos < 0:
            x_pos = maxx - 1
            mapx -= 1
            max_lim = 1
        if y_pos >= maxy:
            y_pos = 0
            mapy += 1
            max_lim = 1
        if y_pos < 0:
            y_pos = maxy -1
            mapy -= 1
            max_lim = 1
        if max_lim:
            game.fill("black")
            map_ = rpg_map.map_load(mapx,mapy,16,16,2)
            rpg_map.map_blit(game,16,16,map_,size)
            rpg_player.move(game,x_pos,y_pos,dir_,size,0.001,["",0],map_,16,16,sp_)
            max_lim = 0
    
    
    # save script
    
    # load script
    
    # exit script
    for event in events_:
        if event.type == 256:
            run = 0
    
    p.quit()