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
        self.cache    = {"configData":{}}
        self.commands = {"exec":self.cExec,
                         "break":self.cBreak,
                         "execstack":self.NULL,
                         "jmp":self.cJMP,
                         "log":self.cLog,
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