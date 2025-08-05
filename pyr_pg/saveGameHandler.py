"""
    save game class for pyr_pg
    (c) 2025 Spyro24
"""

class saveFile():
    def __init__(self):
        self.fileCheck = "PYRPG"
        
    def 
class saveFileHandler():
    def __init__(self):
        self.dialogKeys = set()
        self.playerName = ""
    
    def addDialogFlag(self, flag: str):
        self.dialogKeys.add(flag)
    
    def removeDialogFlag(self, flag: str):
        try:
            self.dialogKeys.remove(flag)
            return True
        except KeyError:
            return False