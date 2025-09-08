import pygame as p

class displayManager:
    def __init__(self, initSize: tuple[int, int], ratio: tuple[int, int])->None:
        self.ratio = ratio
        self.window = p.display.set_mode(initSize, flags=p.RESIZABLE)
        self.zeroPos = (0, 0)
        self.windowResize()
    
    def windowResize(self):
        windowSize = self.window.get_size()
        windowMidpoint = self.window.get_rect().center
        windowH, windowW = windowSize
        if windowH > windowW:
            windowH, windowW = windowW, windowH
        
    def blit(self, source, dest=(0, 0), area=None, special_flags=0):
        pass
        
    def get_size():
        pass