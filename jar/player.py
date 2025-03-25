import jar

class player():
    def __init__(self):
        self.__onGround = False #State True if the Player is touching the ground
        self.__respawnPos = (0,0)
        self.__hitboxOffset = (-1,0)
        self.__hitboxSize = (2,2)
        self.__hitbox = jar.hitbox.hitbox(().())