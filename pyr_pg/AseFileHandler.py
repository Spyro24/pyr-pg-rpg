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
        
if __name__ == "__main__":
    AseFileTest = AseFile("./testData/testAsefile.aseprite")
    print(f"Size: {AseFileTest.fileSize} bytes")
    print(f"Magic Number: {AseFileTest.magicNumber}")
    print(f"Frame count: {AseFileTest.framesCount}")
    f = open("./testData/testAsefileData", "bw")
    f.write(AseFileTest.aseData)
    f.close()