import jar

class player():
    def __init__(self, camera: jar.camera.Camera, hitboxManager: jar.hitbox.hitboxManager, debug=False):
        self.debug = debug
        self.__camera = camera
        self.__hitboxManager = hitboxManager
        self.__onGround = False #State True if the Player is touching the ground
        self.__falling = True
        self.__jump = False
        self.__canJump = True
        self.__moveSpeed = 20
        self.__fallSpeed = 20
        self.__jumpHight = 10
        self.__respawnPos = (0,0)
        self.__hitboxOffset = (-1,2)
        self.__hitboxSize = (2,2)
        self.__posX = 0
        self.__posY = 0
        self.__hitbox = jar.hitbox.hitbox((self.__hitboxOffset[0], self.__hitboxOffset[1]),(self.__hitboxSize[0], self.__hitboxSize[1]))
        self.calcFrameStuff(60)
        
    def calcFrameStuff(self, FPS: int) -> None:
        self.__frameMoveSpeed = self.__moveSpeed / FPS
        self.__frameFallSpeed = self.__fallSpeed / FPS
        
    def respawn(self) -> None:
        self.__posX = self.__respawnPos[0]
        self.__posY = self.__respawnPos[1]
        self.__hitbox = jar.hitbox.hitbox((self.__hitboxOffset[0] + self.__respawnPos[0], self.__hitboxOffset[1] + self.__respawnPos[1]),(self.__hitboxSize[0], self.__hitboxSize[1]))
    
    def movePlayer(self, directionAmount: tuple) -> None:
        self.__posX += directionAmount[0]
        self.__posY += directionAmount[1]
        self.__hitbox.moveInPlace(directionAmount)
    
    def tick(self, controllerStuff: tuple) -> None:
        buttons = controllerStuff[2]
        if controllerStuff[0][0] != 0:
            self.movePlayer((self.__frameMoveSpeed * controllerStuff[0][0], 0))
        #falling and jumping
        if (buttons[0] and self.__canJump):
            self.movePlayer((0, self.__frameFallSpeed * 1.3))
            self.__falling = True
        else:
            if self.__falling:
                self.__canJump = False
                self.movePlayer((0, -self.__frameMoveSpeed))
                if self.__hitboxManager.checkHit((self.__posX, self.__posY)):
                    self.movePlayer((0, self.__hitboxManager.lastHitbox.renderRectOnCamera()[2] - self.__posY))
                    self.__falling = False
                    self.__canJump = True
        if self.__posY < -50:
            self.respawn()
                    
    def onRender(self):
        if self.debug:
            self.__camera.renderRect(self.__hitbox, (255,255,0))
        
        