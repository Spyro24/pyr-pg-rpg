import pygame as p
import zlib

class map:
    def __init__(self, *settings):
        self.state = {"load":False}
        self.params = {"window":None,"map_xy":[0,0], "map_dir":"./map/","bg_tiles":[],"gd_tiles":[],"ov_tiles":[],"map_wh":(16,16),
                       "map_byte_size":2,"layers":8,"tile_size":(1,1), "debug_col":{"map_hitbox":(0,127,127)}} # contains a list with all parameters of the game
        self.map_hitboxes = [] #<- list with all hitboxes in [y][x] format
        self.map_raw_hitboxes = [] #<- list with all raw hitboxes in [y][x] format
        #---Add +settings to the parameter list
        for key in settings[0].keys(): #overwrite and add parameters to the map
            self.params[key] = settings[0][key]
        #---legacy code---
        self.debug_col       = self.params["debug_col"]["map_hitbox"]
        self.layers          = self.params["layers"]
        self.tile_bytes      = self.params["map_byte_size"]
        self.gw              = self.params["window"] #Pygame window object
        self.pos_x           = 0 #Blit x position
        self.pos_y           = 0 #Blit x position
        self.map_x           = self.params["map_xy"][0] #Map x position
        self.map_y           = self.params["map_xy"][1] #Map x position
        self.map_path        = self.params["map_dir"] #The path to the map files
        self.mw, self.mh     = self.params["map_wh"] #Map with in tiles
        self.tile_list       = [self.params["bg_tiles"], self.params["gd_tiles"]] #A list with all tiles sorted by layer
        self.byteConfig      = (2, 2, 2, 2, 2, 1) #Ground, Groundoverlay, overlay, oververlay, shadows, hitboxes
        self.rawMap          = []
        self.gw_x, self.gw_y = self.gw.get_size()
        set_scale            = 0
        if self.gw_y > self.gw_x: set_scale = self.gw_x
        else: set_scale = self.gw_y
        self.scale = set_scale / self.mw
        self.g_layer = p.Surface(self.gw.get_size())
        self.gov_layer = p.Surface(self.gw.get_size())
        self.in_x = (self.gw_x / 2) - ((self.mw / 2) * self.scale)
        self.in_y = (self.gw_y / 2) - ((self.mw / 2) * self.scale)
        
    def load(self):
        self.rawMap = []
        mapFile     = open(str(self.params["map_dir"]) + str(self.map_x) + "_" + str(self.map_y), "br")
        compMap     = mapFile.read()
        decompMap   = zlib.decompress(compMap)
        mapFile.close()
        rawMap = []
        for byteLenght in self.byteConfig:
            rawMap.append([])
            for n in range(self.mw * self.mh):
                extractByte = b""
                for n in range(byteLenght):
                    extractByte += int.to_bytes(mapData[curBytePos])
                    curBytePos  += 1
                self.mapAray[layer].append(int.from_bytes(extractByte, "big"))
        self.rawMap = rawMap
        
        for n in range(self.layers):
            map.append([])
            for tile in range(0,self.mw * self.mh):
                #create the ground layer
                if n == 0:
                    test = int.from_bytes(map_f.read(self.tile_bytes), "big")
                    if test > 0:
                        tmp =(p.transform.scale(self.params["bg_tiles"][test - 1],(self.scale,self.scale)))
                        map[n].append(tmp.convert())
                    else:
                        map[n].append(0)
                #create the hitboxes        
                elif n == 1:
                    map[n].append(int.from_bytes(map_f.read(self.tile_bytes), "big"))
                #create the ground overlay layer
                elif n == 2:
                    test = int.from_bytes(map_f.read(self.tile_bytes), "big")
                    if test > 0:
                        tmp =(p.transform.scale(self.tile_list[1][test - 1],(self.scale,self.scale)))
                        map[n].append(tmp.convert_alpha())
                    else:
                        map[n].append(0)
        
        #---code for creating the hitboxes---
        #clear hitboxes
        self.map_hitboxes = []
        self.map_raw_hitboxes = []
        n = 0
        for h in range(self.mh):
            self.map_raw_hitboxes.append([])
            for w in range(self.mw):
                self.map_raw_hitboxes[h].append(map[1][n])
                n += 1
        self.map = map
        self.create_surface()
        self.state["load"] = True
        
    
    def move(self,x,y):
        self.map_x += x
        self.map_y += y
        self.load()
        self.create_surface()
        
    
    def create_surface(self):
        count = 0
        tmp0 = p.Surface((self.mw * self.scale, self.mh * self.scale))
        tmp1 = p.Surface((self.mw * self.scale, self.mh * self.scale), flags=p.SRCALPHA)
        for h in range(self.mh):
            self.map_hitboxes.append([])
            for w in range(self.mw):
                if self.map_raw_hitboxes[h][w] == 1:
                    self.map_hitboxes[h].append(p.Rect((self.in_x + (self.scale * w), self.in_y + (self.scale * h)), (self.scale, self.scale)))
                else:
                    self.map_hitboxes[h].append(0)
                if self.map[0][count] != 0:
                    tmp0.blit(self.map[0][count],(w * self.scale, h * self.scale))
                if self.map[2][count] != 0:
                    tmp1.blit(self.map[2][count],(w * self.scale, h * self.scale))
                count += 1
        self.g_layer = tmp0.convert()
        self.gov_layer = tmp1.convert_alpha()
    
    def get_dia(self):
        return self.map[2]
    
    def get_pos(self):
        return 0,0 #self.map_x,self.map_y
    
    def get_raw(x,y): #-> bool
        pass
    
    def get_hitbox(self, x, y): #-> 0 or pygame.Rect()
        hb = 0
        try:
            hb = self.map_hitboxes[y][x]
        except:
            hb = 0
        return hb
    
    
    def render(self): #-> None
       self.gw.blit(self.g_layer,(self.in_x, self.in_y))
       self.gw.blit(self.gov_layer,(self.in_x, self.in_y))
    
    def debug(self):
        for h in range(self.mh):
            for w in range(self.mw):
                if self.map_hitboxes[h][w] != 0:
                    p.draw.rect(self.gw, self.debug_col, self.map_hitboxes[h][w], width=3)