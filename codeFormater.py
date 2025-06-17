#!/bin/python3
"""
    Simple codeformater for the pyr_pg project
    (c) 2025 Spyro24
"""

import sys

class codeFormater:
    def __init__(self, infile: str, oufile: str):
        self.infile = open(infile, "r")
        self.outfile = open(oufile, "w")
        self.indent = 0
        self.curStep = 0
        self.states = {"longComment": False, "ModuleDocString": False}
        for line in self.infile.readlines():
            if line == "\n":
                continue 
            line = self.RSFBAE(line.strip("\n"))
            outline = ""
            for _ in range(self.indent):
                outline += "    "
            
            try:
                if self.curStep == 0:
                    if line[0:2] == "#!":
                        outline += "#! /usr/bin/python3"
                    self.curStep += 1
                elif self.curStep == 1:
                    if line[0:3] == f"{chr(34)}{chr(34)}{chr(34)}" and self.states['ModuleDocString'] == False:
                        self.indent += 1
                        self.states["ModuleDocString"] = True
                        outline += f"{chr(34)}{chr(34)}{chr(34)}"
                    elif self.RSFBAE(line)[0:3] == f"{chr(34)}{chr(34)}{chr(34)}" and (self.states['ModuleDocString'] == True):
                        self.curStep += 1
                        self.indent -= 1
                        outline = ""
                        self.states["ModuleDocString"] = False
                        outline += f"{chr(34)}{chr(34)}{chr(34)}" + "\n"
                    elif self.states['ModuleDocString']:
                        outline += self.RSFBAE(line)
                    else:
                        self.curStep += 1
                elif self.curStep == 2:
                    test = self.checkImport(self.RSFBAE(line))
                    if test == bool:
                        self.curStep +=1
                    else:
                        outline = self.checkImport(test)
            except:
                pass
            
            if line[0] == "#" and not line[0:2] == "#!":
                continue 
            outline += "\n"
            self.outfile.write(outline)
    
    def RSFBAE(self, string: str): #removeSpacesFromBeginAndEnd
        begin = 0
        end = len(string)
        try:
            while True:
                if string[begin] == " ":
                    begin += 1
                    continue
                break
            while True:
                if string[end - 1] == " ":
                    end -= 1
                    continue
                break
            return string[begin:end]
        except:
            return string
    
    def checkImport(self, line: str):
        if line.startswith("from") or line.startswith("import"):
            newLine = ""
            oldLine = line.split(" ")
            curPointer = 0
            for element in oldLine:
                if element == "" or element == ",":
                    continue
                elif element == "from":
                    newLine += "from "
                    curPointer += 1
                elif element == "import":
                    newLine += "import "
                    curPointer += 1
                elif element == "as":
                    newLine += "as "
                    curPointer += 1
                else:
                    if curPointer >= 2:
                        newLine += element + ", "
                    else:
                        newLine += element + " "
            if curPointer >= 2:
                newLine = newLine[0:-2]
            else:
                newLine = newLine[0:-1]
            return newLine
    
if __name__ == "__main__":
    args = sys.argv
    codeFormater(args[1], args[2])