"""
    The Tool system for map_pg
    (c) 2025 Spyro24
"""

class bucketFill:
    def __init__(self, map_size: tuple):
        self.mapSize = map_size
        self.mapLayer = []
    
    def fill(self, init_pos: tuple, cur_map: list):
        returnPositions = [init_pos]
        procesPositions = {init_pos}
        self.set_ready(cur_map)
        
    def set_ready(self, cur_map: list):
        pass