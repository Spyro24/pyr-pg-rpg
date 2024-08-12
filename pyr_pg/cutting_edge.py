import pygame as p

class CuttingEdge():
    def __init__(self, table, path, debug=None, debug_output=None):
        self.debug = debug
        self.debug_output = debug_output
        self.sprite_sheet_path = path
        self.sprite_sheet = None #Contains the spritesheet after the load table section
        self.sprite_table = {}
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
                execute = True
                if self.debug == "shell":
                    print("Spritesheet '" + self.sprite_sheet_path + str(tmp[1]) + "' is loaded.")
            if execute:
                while count < max_count:
                    cur_obj = sprite_table_raw[count]
                    obj_config = cur_obj.split("=")
                    obj_properties = obj_config[1].split(",")
                    obj_wh = obj_properties[0].split(":")
                    obj_size = obj_properties[1].split("x")
                    obj_texture = p.Surface((0,0), flags=p.SRCALPHA)
                    self.sprite_table[obj_config[0]] = obj_texture.convert_alpha()
                    if debug:
                        if debug_type == "shell":
                            print(cur_obj, obj_config, obj_properties, obj_wh, obj_size)
                    count += 1
                    
            if debug:
                if debug_type == "shell":
                    print(self.sprite_table)
        except:
            raise BaseException("Sprite table looks broken or not exist. Try to restart the script :(")
        
    def load(self):
        pass
    
    def _unit_test(self):
        pass
    
if __name__ == "__main__":
    window = p.display.set_mode((1000,1000))
    test_sprite = CuttingEdge("blue_cube.conf", "../characters/", debug="shell")