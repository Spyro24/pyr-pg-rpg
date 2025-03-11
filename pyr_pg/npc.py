class NPC():
   def __init__(self, game_win, config):
       self.name     = config["name"]
       self.sprites  = config["sprites"]
       self.dir      = (0, 0)
       self.position = config["position"]
    
    def render(self) -> None:
        pass
    
    def debug(self) -> None:
        pass
    
    def setPosition(self, XY: tuple) -> None:
        pass
    
    def getPosition(self) -> tuple:
        pass
    
    def kill(self) -> None:
        pass
       