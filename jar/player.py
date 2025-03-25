import jar

class player():
    def __init__(self):
        self.__onGround = False #State True if the Player is touching the ground
        self.__respawnPos = (0,0)