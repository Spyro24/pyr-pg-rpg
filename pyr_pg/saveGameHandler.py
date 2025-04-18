"""
    save game class for pyr_pg
    (c) 2025 Spyro24
"""

class saveFile():
    def __init__(self):
        self.version = "0.0.1"
        #---added with version 0.0.1---
        self.__saveDict = {"playerName": str,
                         "layerFacing": str,
                         "playerLives": int,
                         "playerPosition": tuple, #(mapX, mapY, tileX, tileY, microPosX, microPosY)
                         "curency": int,
                         }
        
    def injectRPGconfig(self, rpgConfigDict: dict) -> None:
        pass
    
    def changeObjectValue(self, obj: str, value) -> None:
        self.__saveDict[obj] = value
        
    def injectRawConfig(self, rawConfig: dict) -> None:
        for key in rawConfig.keys():
            self.saveDict[key] = rawConfig[key]
    
    def loadFromFile(self, filePath: str) -> None:
        saveFile = open(filePath, "br")
        saveData = saveFile.read()
        saveFile.close()
        #---Version Creation---
        modulVersion = self.version.split(".")
        saveDataVersion = int(modulVersion[0]) * 1000000 + int(modulVersion[1]) * 1000 + int(modulVersion[2])
        #---check if its a valid save file---
        if 
    
    def saveToFile(self, filePath: str) -> None:
        saveData = b"\xF5" #initial Byte for recognition of a pyr_pg save
        version = self.version.split(".")
        for number in version:
            saveData += int(number).to_bytes()
        if len(saveData) != 4:
            raise ValueError("Save version write Failed!")
        #---Export version 0.0.1 config---
        saveData += self.__encodeStrToSavedata(self.__saveDict['playerName'])
        #---Write the save data in the save file---
        saveFile = open(filePath, "bw")
        saveFile.write(saveData)
        saveFile.close()
        
    def __encodeStrToSavedata(self, string: str) -> bytes:
        return len(string).to_bytes(1) + string.encode("UTF-8")
         
if __name__ == "__main__": #In Module unit test
    test = saveFile()
    testData = {"playerName": "Synthesys",
                "playerFacing": "LEFT",
                }
    test.injectRawConfig(testData)
    test.saveToFile("./testData/testSave")
    