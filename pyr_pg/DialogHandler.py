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
        self.cache    = {"configData":{}}
        self.commands = {"exec":self.cExec,
                         "break":self.cBreak,
                         "execstack":self.NULL,
                         "jmp":self.cJMP,
                         }
        
    def execDialogScript(self, diascript) -> None:
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
                returnVal = self.commands[instruction](instructionTable)
                if returnVal[0] == 1:
                    pc = returnVal[1] #set the programm counter to X
                    continue
                elif returnVal[0] == 2:
                    break
            except KeyError: #Handle the Dialog if its not a command
                pass 
            
            pc += 1 #increment the programm counter
    def cJMP(self, argList):
        return (1, int(argList[1]))
    
    def cBreak(self, argList) -> tuple:
        return (2, 0)
    
    def cExec(self, argList) -> tuple:
        self.execDialogScript(argList[1])
        return (0, 0)
    
    def NULL(self, argList) -> None:
        pass
    
    def configLookUp(self, file, KEY) -> tuple or int:
        return_ = {}
        try:
            return_ = self.cache["configData"][file][KEY]
        except KeyError:
            conf = open(file, "r")
            config_file = conf.readlines()
            conf.close()
            cur_key = ""
            cur_file = file
            self.runtime_config["configData"][cur_file] = {}
            for line in config_file:
                cur_line = line.strip()
                if cur_line == "":
                    pass
                elif cur_line[0] == "[":
                    cur_key = cur_line.strip("[]")
                    self.runtime_config["configData"][cur_file][cur_key] = {}
                elif cur_line != "":
                    data = cur_line.split("=")
                    values = data[1].split(",")
                    values_int = []
                    for val in values:
                        values_int.append(int(val))
                    if len(values_int) > 1:
                        self.runtime_config["configData"][cur_file][cur_key][data[0]] = tuple(values_int)
                    else:
                        self.runtime_config["configData"][cur_file][cur_key][data[0]] = values_int[0]
            print(self.runtime_config["config_file"])
            return_ = self.runtime_config["configData"][file][KEY]
        return return_
    
if __name__ == "__main__":
    import font
    
    _test_win    = p.display.set_mode((800,16*32))
    _test_font   = font.font(_test_win, "./res/fonts/standard")
    _test_config = {"font":_test_font, "pg_window":_test_win}
    _test_dialog = DialogScript(_test_config)
    _test_dialog.execDialogScript("./res/tests/dialog/test2.dls")
    p.display.flip()