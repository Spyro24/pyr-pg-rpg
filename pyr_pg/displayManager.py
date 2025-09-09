import pygame as p

class displayManager:
    def __init__(self, initSize: tuple[int, int], ratio: tuple[int, int])->None:
        self.ratio = ratio[0] / ratio[1]
        self.window = p.display.set_mode(initSize, flags=p.RESIZABLE)
        self.zeroPos = (0, 0)
        self.windowSize = (0,0)
        self.windowResize()
        self.lowestSize = 0
    
    def windowResize(self):
        windowSize = self.window.get_size()
        windowMidpoint = self.window.get_rect().center
        windowH, windowW = windowSize
        lowest_size = windowH
        if windowH > windowW:
            lowest_size = windowW
        self.lowestSize = lowest_size
        self.windowSize = (lowest_size, lowest_size * self.ratio)
        self.zeroPos = (windowMidpoint[0] - self.windowSize[0] / 2, windowMidpoint[1] - self.windowSize[1] / 2)
        
    def blit(self, source, dest=(0, 0), area=None, special_flags=0):
        self.window.blit(source, (dest[0] + self.zeroPos[0], dest[1] + self.zeroPos[1]), area, special_flags) 
        
    def get_size(self):
        return self.windowSize