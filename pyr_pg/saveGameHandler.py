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
        