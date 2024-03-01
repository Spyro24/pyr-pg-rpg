def launch_wrapper(launch_file):
    #setting up the vars
    game_name = "NOT SET"
    version = 0.0
    tilesize = 1
    winsize = 1
    icon = None
    scale = 1
    init_map = (0, 0)
    init_pos = (0, 0)
    
    
    #Load the init file from the main folder
    init_file = open(launch_file,"r")
    wrap = init_file.readlines()
    
    #scan the file for valid options
    for option in wrap:
        element = option.split("=")
        
        #iterate the elemnt for a vald option(Ignore invalid data)
        if element[0] == "name":
            game_name = element[1].strip()
        elif element[0] == "version":
            version = float(element[1])
        elif element[0] == "tilesize":
            tilesize = int(element[1])
        elif element[0] == "winsize":
            winsize = int(element[1])
        elif element[0] == "icon":
            if element[1] != "None":
                icon = element[1].strip()
        elif element[0] == "scale":
            scale = round(float(element[1]))
        elif element[0] == "init_pos":
            pos_tmp = element[1].split(",")
            init_pos = (int(pos_tmp[0]), int(pos_tmp[1]))
        elif element[0] == "init_map":
            pos_tmp = element[1].split(",")
            init_map = (int(pos_tmp[0]), int(pos_tmp[1]))
            
            
            
    #return all vars
    return [game_name, version, tilesize, winsize, icon, scale, init_map, init_pos]