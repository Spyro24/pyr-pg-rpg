class saveFileHandler:
    def __init__(self):
        self.version = 1
        self.playerName: str = ""
    
    def readFile(self, file):
        pass
    
    def writeFile(self, file):
        file = open(file, "br")
        file.write(self.version.to_bytes(2, "little"))