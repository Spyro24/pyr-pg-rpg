"""
    (c) 2025 Spyro24
"""
import pygame as p

class mouse:
    def __init__(self, table_file: str, sprite_sheet: str):
        self.cursors = dict()
        self.cursorSize = 1
        self.__cursor_loader(table_file, sprite_sheet)
        self.curCursorName: str = ""
        self.mousePos = p.mouse.get_pos()
        self.lastPos = self.mousePos
        self.mousePressed = p.mouse.get_pressed()
        self.lastPressed = self.mousePressed
        self.updateTo = ""
        self.mouseDown = False
        self.MouseUp = False
        self.mouseWheel = 0
    
    def set_cursor(self, name: str):
        self.updateTo = name
    
    def updateCursor(self):
        name = self.updateTo
        if self.curCursorName != name and name != "":
            hotspot = (self.cursors[name]["hotspot"])
            hotspot = hotspot[0] * self.cursorSize, hotspot[1] * self.cursorSize
            image = self.cursors[name]["image"]
            imageSize = image.get_size() 
            image = p.transform.scale(image, (imageSize[0] * self.cursorSize, imageSize[1] * self.cursorSize))
            p.mouse.set_cursor(hotspot, image)
            self.curCursorName = name
        self.updateTo = ""
        self.mouseDown = False
        self.MouseUp = False
        
    def set_pos(self, pos: tuple):
        p.mouse.set_pos(pos)
        self.lastPos = pos
        self.mousePos = pos
        
    def update_mousePos(self):
        self.lastPos = self.mousePos
        self.mousePos = p.mouse.get_pos()
        self.mousePressed = p.mouse.get_pressed()
        self.lastPressed = self.mousePressed
    
    def __cursor_loader(self, table_file: str, sprite_sheet: str):
        table_file = open(table_file, "r")
        table = table_file.readlines()
        counter = 0
        table_file.close()
        size = (0,0)
        sprite_sheet = p.image.load(sprite_sheet)
        for line in table:
            line = line.strip()
            if counter == 0:
                size = line.split("x")
                size = (int(size[0]), int(size[1]))
            else:
                line = line.strip().split(",")
                name = line[0]
                tile_pos = line[1].split(":")
                tile_pos = (int(tile_pos[0]), int(tile_pos[1]))
                hotspot = line[2].split(":")
                hotspot = (int(hotspot[0]), int(hotspot[1]))
                tile = p.Surface((size[0], size[1]), flags=p.SRCALPHA)
                tile.blit(sprite_sheet, (0 - size[0] * tile_pos[0], 0 - size[1] * tile_pos[1]))
                self.cursors[name] = dict()
                self.cursors[name]["hotspot"] = hotspot
                self.cursors[name]["image"] = tile
            counter += 1


