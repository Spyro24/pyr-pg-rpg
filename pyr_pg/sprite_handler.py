import pygame as p

class sprite_handler():
    def __init__(self, GlobalConfig):
        self.globconfig = GlobalConfig
        self.cutedg = self.globconfig["cuttingedge"]
        
if __name__ == "__main__":
    import cutting_edge