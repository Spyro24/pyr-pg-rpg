"""
    Aseprite File loader for pyr_pg (to use the raw data directly(only for develepment))
    (c) 2025 Spyro24
"""
"""
    BYTE: An 8-bit unsigned integer value
    WORD: A 16-bit unsigned integer value
    SHORT: A 16-bit signed integer value
    DWORD: A 32-bit unsigned integer value
    LONG: A 32-bit signed integer value
    FIXED: A 32-bit fixed point (16.16) value
    FLOAT: A 32-bit single-precision value
    DOUBLE: A 64-bit double-precision value
    QWORD: A 64-bit unsigned integer value
    LONG64: A 64-bit signed integer value
    BYTE[n]: "n" bytes.
"""

import zlib

class fileLikeOBJ:
    def __init__(self, byteStream: bytes, byteOrder="little"):
        self.byteStram = byteStream
        self.byteOrder = byteOrder
        self._words = {"BYTE":(1, False),
                       "WORD":(2, False),
                       "SHORT":(2, True),
                       }
        self.bytesOffset = 0
        self.curBytePos = 0
    
    def skipBytes(self, count: int):
        
        
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