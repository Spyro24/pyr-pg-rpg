"""
    Dialog System for PYR_PG (V4)
    (c) 2025 Spyro24
"""
import pygame as p
import time
import pygame as p

class DialogScript():
    def __init__(self, runtimeStore):
        self.rs       = runtimeStore
        self.logsys   = self.rs[9]
        self.font     = self.rs[15]
        self.window   = self.rs[13]
        self.config   = {"gridsize":(16,16), "blit_pos":(0,0), "tile_size":0}
        self.cache    = {"configData":{}, "textbox":{"image":p.surface.Surface((1,1)),"pos":(0,0), "text_pos":(1,1), "lines":3}, "config_file":{}}
        self.__setup_env()
        self.commands = {"exec":self.cExec,
                         "break":self.cBreak,
                         "execstack":self.NULL,
                         "jmp":self.cJMP,
                         "log":self.cLog,
                         "killgame":self.cExcept,
                         "store":self.cStore,
                         "textbox":self.cTextbox,
                         "dialog":self.cDialog,
                         }
    
    def execDialogScript(self, diascript: str) -> None:
        script_file = open(diascript,"r")
        script      = script_file.readlines()
        script_file.close()
        scriptEnd   = len(script)
        pc = 0 #Programm Counter
        while True:
            if pc >= scriptEnd: #Checks if the Dialog has finished
                break
            curInstruction   = script[pc].strip()
            instructionTable = curInstruction.split("|")
            instruction      = instructionTable[0]
            try: #try to execute a command
                if len(instruction) == 0:
                    pc += 1
                    continue 
                elif instruction[0] == "#": #check if the curentline is a commend
                    pc += 1
                    continue
                else:
                    returnVal = self.commands[instruction](instructionTable)
                    if returnVal[0] == 1: #continue the loop without increment the PC
                        pc = returnVal[1]
                        continue
                    elif returnVal[0] == 2: #end the curent Dialogscript Execution
                        break
            except KeyError: #Handle the Dialog if its not a command
                pass 
            
            pc += 1 #increment the programm counter
    
    def cTextbox(self, argList: list) -> tuple:
        text_box_config = argList[1]
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
        box_config = self.configLookUp(path, param)
        print(box_config)
        self.__create_textbox([box_config["position"],(16,5),(1,1),3], "./res/textboxes/gray_rounded.png")
        return (0, 0)
    
    def cDialog(self, argList: list) -> list:
        bx, by   = self.config['blit_pos']
        ts       = self.config['tile_size']
        blit_pos = self.cache['textbox']['pos']
        self.window.blit(self.cache['textbox']['image'], (bx + ts * blit_pos[0], by + ts * blit_pos[1]))
        self.__draw_text(argList[3], "box")
        p.display.update()
        return(0, 0)
        
    def cStore(self, argList: list) -> tuple:
        value   = argList[3]
        path    = argList[1]
        valType = argList[2]
        if valType == "string":
            value = str(value)
        elif valType == "float":
            value = float(value)
        elif valType == "int":
            value = int(value)
        return (0, 0)
    
    def cJMP(self, argList):
        return (1, int(argList[1]))
    
    def cBreak(self, argList: list) -> tuple:
        return (2, 0)
    
    def cLog(self, argList: list) -> tuple:
        self.logsys(int(argList[1]), "[DialogHandler]" + str(argList[2]))
        return (0, 0)
    
    def cExec(self, argList: list) -> tuple:
        self.execDialogScript(argList[1])
        return (0, 0)
    
    def cExcept(self, argList: list) -> None:
        """Never ever use this function! (its only for unit testing)"""
        raise BaseException
    
    def NULL(self, argList: list) -> None:
        pass
    
    def configLookUp(self, file, KEY) -> tuple or int:
        returnVal = {}
        try:
            returnVal = self.cache["configData"][file][KEY]
        except KeyError:
            conf = open(file, "r")
            config_file = conf.readlines()
            conf.close()
            cur_key = ""
            cur_file = file
            self.cache["configData"][cur_file] = {}
            for line in config_file:
                currentLine = line.strip()
                if currentLine == "":
                    pass
                elif currentLine[0] == "[":
                    cur_key = currentLine.strip("[]")
                    self.cache["configData"][cur_file][cur_key] = {}
                elif currentLine != "":
                    data = currentLine.split("=")
                    values = data[1].split(",")
                    valuesInt = []
                    for val in values:
                        valuesInt.append(int(val))
                    if len(valuesInt) > 1:
                        self.cache["configData"][cur_file][cur_key][data[0]] = tuple(valuesInt)
                    else:
                        self.cache["configData"][cur_file][cur_key][data[0]] = valuesInt[0]
            print(self.cache["config_file"])
            returnVal = self.cache["configData"][file][KEY]
        return returnVal
    
    def __draw_text(self, text: str, type_, more_opn=None):
        if type_ == "box":
            lines  = str(text).rsplit("\\n")
            x, y   = self.cache['textbox']['pos']
            ox, oy = self.cache['textbox']['text_pos'] # X and Y offset
            font   = self.font
            size   = self.config['tile_size']
            bx, by = self.config['blit_pos']
            for n in range(len(lines)):
                font.draw(lines[n], size / 10 * 9, (bx + ((x + ox) * size), by + ((y + oy + n) * size)))
                if n >= self.cache["textbox"]["lines"]:
                    break
    
    def __create_textbox(self, config, png):
        tileSize = self.config['tile_size']
        self.cache['textbox']['pos'] = config[0]
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
        textbox.blit(textbox_tile_list[8],((config[1][0] - 1) * tileSize,(config[1][1] - 1) * tileSize))
        textbox.blit(textbox_tile_list[6],((config[1][0] - 1) * tileSize,0))
        textbox.blit(textbox_tile_list[2],(0,(config[1][1] - 1) * tileSize))
        if config[1][0] > 2:
            if config[1][1] > 2:
                for x in range(config[1][0] - 2):
                    textbox.blit(textbox_tile_list[3],((x + 1) * tileSize,0))
                for y in range(config[1][1] - 2):
                    textbox.blit(textbox_tile_list[1],(0,(y + 1) * tileSize))
                for x in range(config[1][0] - 2):
                    textbox.blit(textbox_tile_list[5],((x + 1) * tileSize,(config[1][1] - 1) * tileSize))
                for y in range(config[1][1] - 2):
                    textbox.blit(textbox_tile_list[7],((config[1][0] - 1) * tileSize,(y + 1) * tileSize))
                for x in range(config[1][0] - 2):
                    for y in range(config[1][1] - 2):
                        textbox.blit(textbox_tile_list[4],((x + 1) * tileSize,(y + 1) * tileSize))
                
        self.cache['textbox']['image'] = textbox
    
    def __setup_env(self):
        window_wh     = self.window.get_size()
        shortest_side = window_wh[1]
        if window_wh[0] < window_wh[1]:
            shortest_side = window_wh[0]
        blit_point = (0, 0)
        midpoint                 = (window_wh[0]/2, window_wh[1]/2)
        blit_point               = (midpoint[0] - shortest_side/2, midpoint[1] - shortest_side/2)
        self.config["blit_pos"]  = blit_point
        self.config["tile_size"] = int(shortest_side / self.config["gridsize"][0])