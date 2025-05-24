"""
    Aseprite File loader for pyr_pg (to use the raw data directly(only for develepment))
    (c) 2025 Spyro24
"""
import zlib

class AseFile:
    def __init__(self, AseFilePath: str):
        aseFile = open(AseFilePath, "br")
        self.fileSize = int.from_bytes(aseFile.read(4), "little")
        self.magicNumber = int.from_bytes(aseFile.read(2), "little")
        self.framesCount = int.from_bytes(aseFile.read(2), "little")
        self.imageWidth = int.from_bytes(aseFile.read(2), "little")
        self.imageHeight = int.from_bytes(aseFile.read(2), "little")
        self.colorDepth =int.from_bytes(aseFile.read(2), "little")
        self.flgas = int.from_bytes(aseFile.read(4), "little")
        self.animationSpeedMS = int.from_bytes(aseFile.read(2), "little")
        aseFile.read(8) #its zero
        self.transparentColorIndex = int.from_bytes(aseFile.read(1), "little")
        aseFile.read(3) #These are ignored bytes
        self.numberOfColors = int.from_bytes(aseFile.read(2), "little")
        self.pixelWidth = int.from_bytes(aseFile.read(1), "little")
        self.pixelHeight = int.from_bytes(aseFile.read(1), "little")
        self.gridXPosition = int.from_bytes(aseFile.read(2), "little", signed=True)
        self.gridYPosition = int.from_bytes(aseFile.read(2), "little", signed=True)
        self.gridWidth = int.from_bytes(aseFile.read(2), "little")
        self.gridHeight = int.from_bytes(aseFile.read(2), "little")
        self.endOfHeader = aseFile.read(84)
        self.aseData = aseFile.read()
        self.loadFrames()
        
    def loadFrames(self):
        self.framesData = {}
        frameStreamLenght = int.from_bytes(self.aseData[0:4], "little")
        frameData = self.aseData[0:frameStreamLenght]
        magicNumber = int.from_bytes(frameData[4:6], "little")
        chunksCountOld = int.from_bytes(frameData[6:8], "little")
        frameDuration = int.from_bytes(frameData[8:10], "little")
        #forFuture = int.from_bytes(frameData[10:112], "little")
        chunksCount = int.from_bytes(frameData[12:16], "little")
        if chunksCount == 0:
            chunksCount = chunksCountOld
        print(chunksCount)
        chuncks = self.splitChuncks(frameData[16:-1], chunksCount)
        print(chuncks)
        
    
    def splitChuncks(self, chunkStream: bytes, chunksCount: int):
        chunks = []
        offset = 0
        for n in range(chunksCount):
            chunks.append(chunkStream[offset: offset + int.from_bytes(chunkStream[offset:offset + 4], "little")])
            offset = int.from_bytes(chunkStream[offset:offset + 4], "little")
        return chunks
        
        

if __name__ == "__main__":
    AseFileTest = AseFile("./testData/testAsefile.aseprite")
    print(f"Size: {AseFileTest.fileSize} bytes")
    print(f"Magic Number: {AseFileTest.magicNumber}")
    print(f"Frame count: {AseFileTest.framesCount}")