import pyr_pg.npc

class NpcHandler():
    def __init__(self, mapFileHandler):
        self.mapFileHandler = mapFileHandler
        self.NPCs :list     = []
    
    def createNPCs(self, mapRegion) -> None:
        for NPC in self.NPCs:
            NPC.kill()