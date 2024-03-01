import pygame as p
import pyr_pg.map_ as map_to 

def dialog_wrapper(win,map_,script,var, *debug):
    #init all vars
    gmap = var[2]
    w, h = var[3]
    ppos = None
    iter_ = 0
    cpos = 0
    run_ = True
    script = open("./dialog/" + str(map_[0]) + "_" + str(map_[1]) + "/" + str(script) + ".dialog")
    code = script.readlines()
    empty3829 = len(code)
    
    #run the dialog script file
    while cpos < int(empty3829) and run_:
        #get curent code
        cur = code[cpos]
        print(cur)
        
        #split the string at ;
        csp = cur.split(";")
        
        #check forthe end of execution
        if csp[0] == "#end":
            run_ = False
            
        #set the player position
        elif csp[0] == "#setpos":
            x = int(csp[1])
            y = int(csp[2])
            ppos = (x,y)
            
        #jump to the chosen line
        elif csp[0] == "#jmp":
            cpos = int(csp[1]) - 2
        
        cpos += 1
    
    map_to.map_blit(win,w,h,gmap,16)
    return [ppos, True]