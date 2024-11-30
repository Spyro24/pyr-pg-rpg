import pygame as p

class CuttingEdge():
    def __init__(self, table, path, debug=None, debug_output=None):
        self.debug = debug
        self.debug_output = debug_output
        self.sprite_sheet_path = path
        self.sprite_sheet = None #Contains the spritesheet after the load table section
        self.sprite_table = {} #contains all sprites
        self.property_table = {} #contains the properties of the sprites
        self.tile_size = (0,0)
        self.sheet_h = 0
        self.sheet_w = 0
        self.table = self.load_table(path, table)
        
    def load_table(self, path, table):
        debug = False
        debug_type = None
        if self.debug == "shell":
            debug = True
            debug_type = "shell"
        try:
            sprite_table_file = open(path + table, "r")
            sprite_table_raw = sprite_table_file.readlines()
            sprite_table_file.close()
            sprite_table_raw = [line.strip() for line in sprite_table_raw]
            print(sprite_table_raw)
            max_count = len(sprite_table_raw)
            count = 0
            tmp = sprite_table_raw[count].split("x")
            self.sheet_w = int(tmp[0])
            self.sheet_h = int(tmp[1])
            count += 1
            tmp = sprite_table_raw[count].split(">")
            count += 1
            execute = False
            if tmp[0] == "SPRITESHEET":
                self.sprite_sheet = p.image.load(self.sprite_sheet_path + str(tmp[1]))
                px_w, px_h = self.sprite_sheet.get_size()
                tile_size = int(px_h /self.sheet_h)
                self.tile_size = (tile_size, tile_size)
                execute = True
                if self.debug == "shell":
                    print("Spritesheet '" + self.sprite_sheet_path + str(tmp[1]) + "' is loaded.")
                    print("Table Hight: " + str(px_h) + "px, Table tiles_size: " + str(self.tile_size))
            if execute:
                while count < max_count:
                    #---creating the config for the curent obj---
                    cur_obj = sprite_table_raw[count] #get the obj
                    obj_config = cur_obj.split("=") #split the param name from the rest of the code
                    obj_properties = obj_config[1].split(",") #split the psotition and the size of the object in half
                    obj_wh = obj_properties[0].split(":") #generate the position
                    obj_size = obj_properties[1].split("x") #generate the size
                    #---create the sprite and set it in the table---
                    obj_texture = p.Surface((self.tile_size[0] * int(obj_size[0]), self.tile_size[1] * int(obj_size[1])), flags=p.SRCALPHA)
                    obj_texture.blit(self.sprite_sheet, (0,0), p.Rect((self.tile_size[0] * int(obj_wh[0]), self.tile_size[1] * int(obj_wh[1])),(self.tile_size[0] * int(obj_size[0]), self.tile_size[1] * int(obj_size[1]))))
                    self.sprite_table[obj_config[0]] = obj_texture.convert_alpha()
                    #---save the properties---
                    self.property_table[obj_config[0]] = (int(obj_size[0]), int(obj_size[1]), int(obj_wh[0]), int(obj_wh[1]))
                    if debug:
                        if debug_type == "shell":
                            print(cur_obj, obj_config, obj_properties, obj_wh, obj_size, obj_texture)
                    count += 1
                    
            if debug:
                if debug_type == "shell":
                    print(self.sprite_table, "\n", self.property_table)
        except:
            raise BaseException("Sprite table looks broken or not exist. Try to restart the script :(\nOr get contact to the developer of the game\n(Were only accept isues from pyr-pg-rpg)")
    
    def resize_to_tile_size(self, tile_size):
        pass
    
    def return_sprite_table(self):
        return self.sprite_table
    
    def return_resize_tile(self, tile, tile_size):
        selected_tile = tile
        selected_tile_infos = self.property_table[tile]

if __name__ == "__main__":
    window = p.display.set_mode((1000,1000))
    test_sprite = CuttingEdge("blue_cube.conf", "./res/characters/", debug="shell").return_sprite_table()
    sprites = list(test_sprite.keys())
    print(sprites)
    for n in range(len(sprites)):
        window.blit(test_sprite[sprites[n]], (0, n * 20))
    p.display.flip()