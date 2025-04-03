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
        self.__vertices = ((self.left, self.top), (self.right, self.top), (self.left, self.buttom), (self.right, self.buttom))
        self.__midPoint = (int((self.right - self.left) / 2 + self.left), int((self.top - self.buttom) / 2 + self.buttom))
        self.__posTuple = (self.left,self.right,self.top,self.buttom)
        self.__hasMoved = False
    
    def moveInPlace(self, move: tuple) -> None:
        self.__hasMoved = True
        self.left += move[0]
        self.right += move[0]
        self.top += move[1]
        self.buttom += move[1]
    
    def collidePoint(self, point: tuple) -> bool:
        return self.left < point[0] < self.right and self.buttom < point[1] < self.top
    
    def getVertices(self) -> tuple:
        if not self.__hasMoved:
            return self.__vertices
        return ((self.left, self.top), (self.right, self.top), (self.left, self.buttom), (self.right, self.buttom))
    
    def getHitPoints(self, side: int, offset=0, stepSize=1) -> list:
        pointList = []
        if side == 0: #left
            x = self.right + offset
            y = self.buttom
            while y < self.top:
                pointList.append((x,y))
                y += stepSize
            if pointList[-1][1] < self.top:
                pointList.append((x,self.top))
        elif side == 2:
            x = self.left - offset
            y = self.buttom
            while y < self.top:
                pointList.append((x,y))
                y += stepSize
            if pointList[-1][1] < self.top:
                pointList.append((x,self.top))
        elif side == 1: #buttom
            x = self.left
            y = self.buttom - offset
            while x < self.right:
                pointList.append((x,y))
                x += stepSize
            if pointList[-1][0] < self.right:
                pointList.append((self.right, y))
        return pointList
    
    def getMidpoint(self) -> bool:
        if not self.__hasMoved:
            return self.__midPoint
        return (int((self.right - self.left) / 2 + self.left), int((self.top - self.buttom) / 2 + self.buttom))
    
    def renderRectOnCamera(self) -> tuple:
        if not self.__hasMoved:
            return self.__posTuple
        return (self.left,self.right,self.top,self.buttom)
    
class hitboxManager():
    def __init__(self):
        self.__ENVINIT = False
        self.__defaultHitboxes = []
        self.__triggerHitboxes = []
        self.__directionalHitboxes = [[],[],[],[]]
        self.__deathBoxes = []
        self.lastHitbox: hitbox
    
    def addENV(self, camera) -> None:
        self.__camera = camera
        self.__ENVINIT = True
        
    def addHitbox(self, begin: tuple, size: tuple)-> None:
        self.__defaultHitboxes.append(hitbox(begin, size))
        self.lastHitbox = self.__defaultHitboxes[-1]
        
    def addDeathbox(self, begin: tuple, size: tuple)-> None:
        self.__deathBoxes.append(hitbox(begin, size))
        self.lastHitbox = self.__defaultHitboxes[-1]
        
    def addDirectionalHitbox(self, begin: tuple, size: tuple, direction: int)-> None:
        self.__directionalHitboxes[direction].append(hitbox(begin, size))
        self.lastHitbox = self.__defaultHitboxes[-1]
        
    def checkHit(self, point: tuple, hitMaker=(0,0)) -> bool:
        point = (point[0] + hitMaker[0], point[1] + hitMaker[1])
        for hitbox in self.__defaultHitboxes:
            if hitbox.collidePoint(point):
                self.lastHitbox = hitbox
                return True
        return False
    
    def checkMultiHit(self, point: tuple, hitMakers=((0,0),(0,0))) -> bool:
        for hitmaker in hitMakers:
            point = (point[0] + hitmaker[0], point[1] + hitmaker[1])
            for hitbox in self.__defaultHitboxes:
                if hitbox.collidePoint(point):
                    self.lastHitbox = hitbox
                    return True
        return False
    
    def checkHitpointList(self, hitPointList: list[tuple]) -> bool:
        hit = False
        for hitPoint in hitPointList:
            for hitbox in self.__defaultHitboxes:
                if hitbox.collidePoint(hitPoint):
                    self.lastHitbox = hitbox
                    hit = True
                    break
            if hit:
                break
        return hit
    
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