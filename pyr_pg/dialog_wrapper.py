import pygame as p
import time

#@Dialog
class dialog():
    def __init__(self, globconfig):
        self.global_config  = globconfig
        self.blit_surface   = self.global_config["pg_window"]
        self.config         = {"gridsize":(16,16), "blit_pos":(0,0), "tile_size":0}
        self.runtime_config = {"textbox":{"image":p.surface.Surface((1,1)),"pos":(0,0), "text_pos":(1,1), "lines":3}, "config_file":{}}
        self.key_pressed    = False
        self.__setup_env()
    
    def parse(self, diascript):
        script_file = open(diascript,"r")
        script      = script_file.readlines()
        pointer     = 0
        max_pointer = len(script)
        run         = True
        script_file.close()
        while run:
            if pointer >= max_pointer:
                break
            cur_instruction   = script[pointer].strip()
            instruction_table = cur_instruction.split("|")
            instruction       = instruction_table[0]
            print(cur_instruction)
            print(instruction_table)
            print(instruction)
            if instruction == "break":
                break
            elif instruction == "textbox":
                text_box_config = instruction_table[1]
                text_box_config = text_box_config.split("/")
                print(text_box_config)
                param = text_box_config.pop(-1)
                path = ""
                for element in text_box_config:
                    path += element + "/"
                rm = "/" + str(param)
                path += param
                path = path.strip(rm)
                print(path)
                box_config = self.parse_config_file(path, param)
                print(box_config)
                self.__create_textbox([box_config["position"],(16,5),(1,1),3], "./res/textboxes/gray_rounded.png")
            elif instruction == "dialog":
                bx, by   = self.config['blit_pos']
                ts       = self.config['tile_size']
                blit_pos = self.runtime_config['textbox']['pos']
                self.blit_surface.blit(self.runtime_config['textbox']['image'], (bx + ts * blit_pos[0], by + ts * blit_pos[1]))
                self.__draw_text(instruction_table[3], "box")
                p.display.update()
                self.wait_key_pressed()
            pointer += 1
            
    def wait_key_pressed(self):
        wait = True
        while wait:
            time.sleep(0.01)
            for event in p.event.get():
                if event.type == p.KEYDOWN:
                    wait = False
            
    def parse_config_file(self, file, KEY):
        return_ = {}
        try:
            return_ = self.runtime_config['config_file'][file][KEY]
        except KeyError:
            conf = open(file, "r")
            config_file = conf.readlines()
            conf.close()
            cur_key = ""
            cur_file = file
            self.runtime_config['config_file'][cur_file] = {}
            for line in config_file:
                cur_line = line.strip()
                if cur_line == "":
                    pass
                elif cur_line[0] == "[":
                    cur_key = cur_line.strip("[]")
                    self.runtime_config['config_file'][cur_file][cur_key] = {}
                elif cur_line != "":
                    data = cur_line.split("=")
                    values = data[1].split(",")
                    values_int = []
                    for val in values:
                        values_int.append(int(val))
                    if len(values_int) > 1:
                        self.runtime_config['config_file'][cur_file][cur_key][data[0]] = tuple(values_int)
                    else:
                        self.runtime_config['config_file'][cur_file][cur_key][data[0]] = values_int[0]
            print(self.runtime_config["config_file"])
            return_ = self.runtime_config['config_file'][file][KEY]
        return return_
                    
                
                
        
    def __create_textbox(self, config, png):
        tile_size = self.config['tile_size']
        self.runtime_config['textbox']['pos'] = config[0]
        box_tilesheet = p.image.load(png)
        textbox_tile_list = []
        box_tilesize = box_tilesheet.get_size()[0] / 3
        for x_tile in range(3):
            for y_tile in range(3):
                cur_tile = p.surface.Surface((box_tilesize,box_tilesize), flags=p.SRCALPHA)
                cur_tile.blit(box_tilesheet,(-(x_tile * box_tilesize), -(y_tile * box_tilesize)))
                textbox_tile_list.append(p.transform.scale(cur_tile,(self.config["tile_size"], self.config["tile_size"])))
                
        textbox = p.surface.Surface((config[1][0] * self.config["tile_size"], config[1][1] * self.config["tile_size"]), flags=p.SRCALPHA)
        textbox.blit(textbox_tile_list[0],(0,0))
        textbox.blit(textbox_tile_list[8],((config[1][0] - 1) * tile_size,(config[1][1] - 1) * tile_size))
        textbox.blit(textbox_tile_list[6],((config[1][0] - 1) * tile_size,0))
        textbox.blit(textbox_tile_list[2],(0,(config[1][1] - 1) * tile_size))
        if config[1][0] > 2:
            if config[1][1] > 2:
                for x in range(config[1][0] - 2):
                    textbox.blit(textbox_tile_list[3],((x + 1) * tile_size,0))
                for y in range(config[1][1] - 2):
                    textbox.blit(textbox_tile_list[1],(0,(y + 1) * tile_size))
                for x in range(config[1][0] - 2):
                    textbox.blit(textbox_tile_list[5],((x + 1) * tile_size,(config[1][1] - 1) * tile_size))
                for y in range(config[1][1] - 2):
                    textbox.blit(textbox_tile_list[7],((config[1][0] - 1) * tile_size,(y + 1) * tile_size))
                for x in range(config[1][0] - 2):
                    for y in range(config[1][1] - 2):
                        textbox.blit(textbox_tile_list[4],((x + 1) * tile_size,(y + 1) * tile_size))
                
        self.runtime_config['textbox']['image'] = textbox
        #Unit test code. Vor commit diesen part löschen oder auskommentiren
        """
        bx, by = self.config['blit_pos']
        ts = self.config['tile_size']
        for test in range(9):
            self.blit_surface.blit(textbox_tile_list[test],(bx + ts * test, by))
        self.blit_surface.blit(textbox, (bx + ts * config[0][0], by + ts * config[0][1]))
        self.__draw_text("Hallo\nDies ist ein Text\nTest", "box")
        """
        #---------------------------------------------------------------
        
    def __draw_text(self, text, type_, more_opn=None):
        if type_ == "box":
            lines  = str(text).rsplit("\\n")
            x, y   = self.runtime_config['textbox']['pos']
            ox, oy = self.runtime_config['textbox']['text_pos'] # X and Y offset
            font   = self.global_config['font']
            size   = self.config['tile_size']
            bx, by = self.config['blit_pos']
            for n in range(len(lines)):
                font.draw(lines[n], size / 10 * 9, (bx + ((x + ox) * size), by + ((y + oy + n) * size)))
                if n >= self.runtime_config["textbox"]["lines"]:
                    break
        
    def __setup_env(self):
        window_wh     = self.blit_surface.get_size()
        shortest_side = window_wh[1]
        if window_wh[0] < window_wh[1]:
            shortest_side = window_wh[0]
        blit_point = (0, 0)
        midpoint                 = (window_wh[0]/2, window_wh[1]/2)
        blit_point               = (midpoint[0] - shortest_side/2, midpoint[1] - shortest_side/2)
        self.config["blit_pos"]  = blit_point
        self.config["tile_size"] = int(shortest_side / self.config["gridsize"][0])
        
if __name__ == "__main__":
    import font
    
    _test_win    = p.display.set_mode((800,16*32))
    _test_font   = font.font(_test_win, "./res/fonts/standard")
    _test_config = {"font":_test_font, "pg_window":_test_win}
    _test_dialog = dialog(_test_config)
    #_test_dialog._create_textbox([(0,11),(16,5),(1,1),3], "./res/textboxes/gray_rounded.png")
    _test_dialog.parse("./res/tests/dialog/test.dls")
    #print(_test_dialog.parse_config_file("./res/dialogscript/textbox", "DOWN"))
    p.display.flip()