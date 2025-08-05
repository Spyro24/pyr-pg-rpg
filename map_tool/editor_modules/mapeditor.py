"""
    The Mapeditor module for pyr_pg universal editor
    (c) 2025 Spyro24
"""
import pygame as p
import map_pg

class mapeditor:
    def __init__(self):
        """Some Variables will be overwritten by self.on_init"""
        self.window = p.Surface
        self.map = map_pg.map_.map
        self.mapEditorSystem = map_pg.mapEditor.mapEditor
        self.cur_layer = 0
        self.eventQue = p.event.get()
    
    def on_init(self, args):
        self.window = args[0]
        self.map    = args[1]
    
    def on_loop(self):
        keyList = p.key.get_pressed()
        mouseButtons = p.mouse.get_pressed()
        mousePosition = p.mouse.get_pos()
        for event in self.eventQue:
            if event.type == p.MOUSEBUTTONDOWN:
                pass
    
    def on_render(self):
        pass
    
    def on_debug(self):
        pass
    
    def on_reload(self):
        pass
    
    def on_load(self):
        self.tilesGround = map_pg.tile_handler.tile_handler("../tiles/ground", self.tilesConfig).return_tiles()
        self.tilesGroundOverlay = map_pg.tile_handler.tile_handler("../tiles/groundov", self.tilesConfig).return_tiles()
        self.tilesPlayerOverlay = map_pg.tile_handler.tile_handler("../tiles/overlay", self.tilesConfig).return_tiles()
        self.tilesShadow = map_pg.tile_handler.tile_handler("../tiles/shadows", self.tilesConfig).return_tiles()
        self.tilesPlayerOverlayOverlay = map_pg.tile_handler.tile_handler("../tiles/overoverlay", self.tilesConfig).return_tiles()
        self.mapEditorSystem.addTiles(self.tilesGround, "ground")
        self.mapEditorSystem.addTiles(self.tilesGroundOverlay, "overlay")
        self.mapEditorSystem.addTiles(self.tilesPlayerOverlay, "playerOverlay")
        self.mapEditorSystem.addTiles(self.tilesPlayerOverlayOverlay, "playerOverlayOverlay")
        self.mapEditorSystem.addTiles(self.tilesShadow, "shadow")
