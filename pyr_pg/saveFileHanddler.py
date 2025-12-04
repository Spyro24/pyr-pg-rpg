class saveFileHandler:
    def __init__(self):
        self.version = 1
        self.playerName: str = ""
        self.mapPos = (0, 0)
        self.posOnMap = (0, 0)
    
    def readFile(self, file):
        pass
    
    def writeFile(self, file):
        file = open(file, "br")
        file.write(self.version.to_bytes(2, "little"))