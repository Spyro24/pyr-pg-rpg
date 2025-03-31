import jar

class player():
    def __init__(self, camera: jar.camera.Camera, hitboxManager: jar.hitbox.hitboxManager, debug=False):
        self.debug = debug
        self.__camera = camera
        self.__hitboxManager = hitboxManager
        self.__moveSpeed = 12
        self.__jumpHight = 4
        self.__fallSpeed = self.__jumpHight / 0.35
        self.__climbingSpeed = 6
        self.__curentJumpHight = 0
        self.__respawnPos = (0,0)
        self.__hitboxOffset = (-1,3)
        self.__hitboxSize = (2,3)
        self.__posX = 0
        self.__posY = 0
        self.__hitbox = jar.hitbox.hitbox((self.__hitboxOffset[0], self.__hitboxOffset[1]),(self.__hitboxSize[0], self.__hitboxSize[1]))
        self.__makeStateMachineReady()
        self.calcFrameStuff(60)
     
    def __makeStateMachineReady(self) -> None:
        self.__jump = False #the player is jumping
        self.__canJump = True #the player can jump but not now
        self.__falling = True #the player is falling
        self.__onGround = False #State True if the Player is touching the ground
        self.__jumpReady = True #the player can now jump
        self.__lookingDir = 0 #looking direction of the player
        self.__climbing = False
        self.__canMove = True
        self.__onGround = False
        
    def calcFrameStuff(self, FPS: int) -> None:
        self.__frameMoveSpeed = self.__moveSpeed * 2 / FPS
        self.__frameFallSpeed = self.__fallSpeed * 2 / FPS
        self.__maxJumpHight   = self.__jumpHight * 2
        self.__frameClimbingSpeed = self.__climbingSpeed * 2 / FPS
        
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
        #climbing
        if self.__climbing:
            self.__curentJumpHight = 0
            self.__canJump = True
            if controllerStuff[0][1] != 0:
                self.movePlayer((0, self.__frameClimbingSpeed * controllerStuff[0][1]))
        else:
            self.__canMove = True
        #moving left and right
        if controllerStuff[0][0] != 0:
            self.__lookingDir = controllerStuff[0][0]
            if self.__canMove:
                self.movePlayer((self.__frameMoveSpeed * controllerStuff[0][0], 0))
                self.__falling = True
                if controllerStuff[0][0] < -0.2 and self.__hitboxManager.checkHitpointList(self.__hitbox.getHitPoints(2)):
                    self.movePlayer((self.__hitboxManager.lastHitbox.renderRectOnCamera()[1] - self.__posX -self.__hitboxOffset[0] , 0))
                elif controllerStuff[0][0] > 0.2 and self.__hitboxManager.checkHitpointList(self.__hitbox.getHitPoints(0)):
                    self.movePlayer((self.__hitboxManager.lastHitbox.renderRectOnCamera()[0] - self.__posX + self.__hitboxOffset[0] , 0))
        #activate climbing
        if buttons[6] and self.__hitboxManager.checkHit((self.__posX , self.__posY), (self.__lookingDir * 1.5, 1.5)):
            if self.__lookingDir == 1:
                self.movePlayer((self.__hitboxManager.lastHitbox.renderRectOnCamera()[0] - self.__posX + self.__hitboxOffset[0], 0))
            if self.__lookingDir == -1:
                self.movePlayer((self.__hitboxManager.lastHitbox.renderRectOnCamera()[1] - self.__posX -self.__hitboxOffset[0] , 0))
            self.__climbing = True
            self.__canMove = False
            self.__falling = False
        else:
            self.__climbing = False
            self.__falling = True
        #falling and jumping
        if buttons[0] and self.__canJump and self.__jumpReady:
            self.movePlayer((0, self.__frameFallSpeed))
            self.__curentJumpHight += self.__frameFallSpeed
            self.__falling = True
            if self.__curentJumpHight >= self.__maxJumpHight:
                self.__canJump = False
                self.__jumpReady = False
        else:
            if self.__falling:
                self.__canJump = False
                self.movePlayer((0, - (self.__frameMoveSpeed + (self.__frameMoveSpeed / 4) * (controllerStuff[0][1] < 0 and not self.__onGround))))
                if self.__hitboxManager.checkHitpointList(self.__hitbox.getHitPoints(1)): #check if the player is on ground
                    self.movePlayer((0, self.__hitboxManager.lastHitbox.renderRectOnCamera()[2] - self.__posY))
                    self.__falling = False
                    self.__onGround = True
                    self.__curentJumpHight = 0
                    self.__canJump = True
                else:
                    self.__onGround = False
        if not buttons[0]:
            self.__jumpReady = True
        if self.__posY < -50 or self.__hitboxManager.checkDeath((self.__posX, self.__posY)):
            self.respawn()
        if not self.__camera.collidePoint((self.__posX, self.__posY), 10):
            self.__camera.setPos((self.__posX, self.__posY))
                    
    def onRender(self):
        if self.debug:
            self.__camera.renderRect(self.__hitbox, (255,255,0))
        
        