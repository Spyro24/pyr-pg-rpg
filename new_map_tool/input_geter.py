import pygame as p

class input_():
    def __init__(self, gw, xp, yp, ts, w, map):
        self.gw = gw #The Game window
        self.xp = xp #X position of the box
        self.yp = yp #Y position of the box
        self.ts = ts #Tile size in px(in this case the size of a map button)
        self.ms = w  #the map size in tiles (default 16)
        self.map = map #The map object to manipulate
        self.activate = p.Rect(self.xp, self.yp, self.ts*w, self.ts*w) #the activate rectangle to activate this(the mouse position is importand)
        
    def input(self,mpos):
        if self.activate.collidepoint(mpos):
            click_pos = 0
            getit = False
            for y in range(self.ms):
                for x in range(self.ms):
                    if p.Rect(self.xp + (self.ts * x), self.yp + (self.ts * y), self.ts, self.ts).collidepoint(mpos):
                        print(click_pos)
                        self.map.change_tile(click_pos)
                        getit = True
                        break
                    click_pos += 1
                if getit: break
        