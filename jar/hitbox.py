class hitbox():
    def __init__(self, begin: tuple, size: tuple):
        beginX = begin[0]
        endX = size[0]
        beginY = begin[1]
        endY = size[1]
        self.left = beginX
        self.right = beginX + endX
        self.top = beginY
        self.buttom = beginY - endY
    
    def moveInPlace(self, move: tuple) -> None:
        self.left += move[0]
        self.right += move[0]
        self.top += move[1]
        self.buttom += move[1]
    
    def collidePoint(self, point: tuple) -> bool:
        if self.left < point[0] < self.right and self.buttom < point[1] < self.top:
            return True
        return False
    
    def renderRectOnCamera(self) -> tuple:
        return (self.left,self.right,self.top,self.buttom)
    
class hitboxManager():
    def __init__(self):
        self.__ENVINIT = False
        self.__defaultHitboxes = []
        self.__triggerHitboxes = []
        self.__deathBoxes = []
        self.lastHitbox: hitbox
    
    def addENV(self, camera) -> None:
        self.__camera = camera
        self.__ENVINIT = True
        
    def addHitbox(self, begin: tuple, size: tuple)-> None:
        self.__defaultHitboxes.append(hitbox(begin, size))
        self.lastHitbox = self.__defaultHitboxes[-1]
        
    def checkHit(self, point: tuple) -> bool:
        for hitbox in self.__defaultHitboxes:
            if hitbox.collidePoint(point):
                self.lastHitbox = hitbox
                return True
        return False
    
    def checkDeath(self, point: tuple) -> bool:
        for hitbox in self.__deathBoxes:
            if hitbox.collidePoint(point):
                return True
        return False
        
    def debug(self):
        for hitbox in self.__defaultHitboxes:
            self.__camera.renderRect(hitbox, (255,0, 255))
        for hitbox in self.__deathBoxes:
            self.__camera.renderRect(hitbox, (255,0, 0))