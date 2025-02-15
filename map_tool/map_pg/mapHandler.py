#(c) 2025 Spyro24
import pygame as p
import zlib

class mapFileHandler():
    def __init__(self, mapWidth, mapHight, mapFilePath):
        self.mapAray        = []
        self.mapBytesConfig = (2, 2, 2, 2, 2, 1) #Ground, Groundoverlay, overlay, shadows, oververlay, hitboxes
        self.mapWidth       = mapWidth
        self.mapHight       = mapHight
        self.mapFilePath    = mapFilePath
        self.mapX           = 1
        self.mapY           = 0
        
    def loadMap(self):
        self.mapAray = []
        mapFile      = open(self.mapFilePath + "/" + str(self.mapX) + "_" + str(self.mapY), "br")
        content      = mapFile.read()
        mapData      = None
        byteConfig   = ()
        try: #load a v3 mapfile
            uncompData = zlib.decompress(content)
            mapData    = uncompData
            byteConfig = self.mapBytesConfig
        except zlib.error as err: #load a v2 mapfile (supports end with this version)
            mapData    = content
            byteConfig = (2, 2, 2, 2, 2, 2, 2, 2) 
        
        checkLenght = 0
        for lenght in self.mapBytesConfig:
            checkLenght += self.mapWidth * self.mapHight * lenght
        while len(mapData) <= checkLenght:
            mapData += b"\00"
        curBytePos = 0
        layer      = 0
        for byteLenght in byteConfig:
            self.mapAray.append([])
            for n in range(self.mapHight * self.mapWidth):
                extractByte = b""
                for n in range(byteLenght):
                    extractByte += int.to_bytes(mapData[curBytePos])
                    curBytePos  += 1
                self.mapAray[layer].append(int.from_bytes(extractByte, "big"))
            layer += 1
        
    def saveMap(self):
        mapData = b""
        for byteLenght in range(len(self.mapBytesConfig)):
            for n in range(self.mapHight * self.mapWidth):
                mapData += int.to_bytes(self.mapAray[byteLenght][n], self.mapBytesConfig[byteLenght])
        mapFile = open(self.mapFilePath + "/" + str(self.mapX) + "_" + str(self.mapY), "bw")
        mapFile.write(zlib.compress(mapData,level=9))
        mapFile.close()
        
    def failSafeLoadMap(self):
        try:
            self.loadMap()
        except FileNotFoundError:
            self.mapAray = []
            for n in range(len(self.mapBytesConfig)):
                self.mapAray.append([])
                for x in range(self.mapHight * self.mapWidth):
                    self.mapAray[n].append(0)
        
if __name__ == "__main__":
    unitTest = mapFileHandler(16,16,"../../map")
    unitTest.failSafeLoadMap()
    print(len(unitTest.mapAray))
    print(unitTest.mapAray)
    unitTest.saveMap()