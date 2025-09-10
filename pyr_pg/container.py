import pyr_pg

class container:
    def __init__(self):
        self.window: pyr_pg.displayManager.displayManager = None
        self.runtimeStore = None
        self.defaultFPS: int = 60
        self.player = None
        self.cache = None
        self.FPS = self.defaultFPS
        self.debugMode = False
        self.splashDuration = 1.2
        self.debugColors = [(0, 0, 255),(0, 255, 0),(255, 0, 0)]
        self.autoSave = False
        self.logSystem = None
