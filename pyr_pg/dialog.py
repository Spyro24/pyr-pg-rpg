import pygame as p
import pyr_pg.map_ as map_to 

def dialog_wrapper(win,map_,script,var):
    gmap = var[2]
    w, h = var[3]
    ppos = None
    iter_ = 0
    cpos = 0
    run_ = True
    script = open("./dialog/" + str(map_[0]) + "_" + str(map_[1]) + "/" + str(script) + ".dialog")
    code = script.readlines()
    empty3829 = len(code)
    while cpos < int(empty3829) and run_:
        cur = code[cpos]
        print(cur)
        csp = cur.split(";")
        if csp[0] == "#end":
            run_ = False
        elif csp[0] == "#setpos":
            x = int(csp[1])
            y = int(csp[2])
            ppos = (x,y)
        
        cpos += 1
    
    map_to.map_blit(win,w,h,gmap,16)
    return [ppos, True]