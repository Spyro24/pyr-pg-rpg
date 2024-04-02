import pygame as p

def load_tile_map():
    pass

def load_images_from_lst(img_dir, lst):
    image_lst = [[],[],[]]
    for n in range(0,3):
        if n == 0:
            pass
        elif n == 1:
            img_dir += "/overlay"
        else:
            img_dir += "/p_overlay"
        for element in lst[n]:
            if element == 0:
                continue
            image_lst[n].append(p.image.load(str(img_dir) + "/" + str(element) + ".png"))
            
    return image_lst
    
def load_tile_list():
    #init all vars
    tile_map = [[],[],[]]
    iter_ = 0
    cpos = 0 #The curent execute position for a script
    run_ = True #if this false the code stops
    script = open("../tile.list")
    code = script.readlines()
    add_tilemap = []
    count = 0
    
    for line in code:
        line = line.strip()
        add = line.split(" ")
        #(add[0])
        
        if add[0] == "":
            pass
        elif add[0][0] == "#":
            pass
        elif add[0][0] == "-":
            if count > 3:
                count = 0
            for item in add_tilemap:
                tile_map[count].append(item)
            #(tile_map)
            count += 1
            add_tilemap.clear()
        elif True:
            app = int(add[0])
            add_tilemap.append(app)
            
    tile_map.append(add_tilemap)
    tile_map.pop(0)
    
    return tile_map
    
