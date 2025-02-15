"""
    save game class for pyr_pg
    (c) 2025 Spyro24
"""

class saveFile():
    def __init__(self):
        self.version = "0.0.1"
        #---added with version 0.0.1---
        self.playerName: str
        self.playerFacing: str
        self.playerLives: int
        self.playerPosition: tuple #(mapX, mapY, tileX, tileY, microPosX, microPosY)
        self.curency: int
        
    def injectRPGconfig(self, rpgConfigDict: dict) -> None:
        pass
    
    def loadFromFile(self, filePath: str) -> None:
        saveFile = open(filePath, "br")
        saveData = saveFile.read()
        saveFile.close()
        #---Version Creation---
        modulVersion = self.version.split(".")
        saveDataVersion = int(modulVersion[0]) * 1000000 + int(modulVersion[1]) * 1000 + int(modulVersion[2])
    
    def saveToFile(self, filePath: str) -> None:
        saveData = b"\xF5" #initial Byte for recognition of a pyr_pg save
        version = self.version.split(".")
        for number in version:
            saveData += int(number).to_bytes()
        if len(saveData) != 4:
            raise ValueError("Save version write Failed!")
        
        #---Write the save data in the save file---
        saveFile = open(filePath, "bw")
        saveFile.write(saveData)
        saveFile.close()
         
if __name__ == "__main__": #In Module unit test
    test = saveFile()
    test.saveToFile("./testData/testSave")
    