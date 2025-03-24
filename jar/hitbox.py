class hitbox():
    def __init__(self, begin: tuple, end: tuple):
        self.left = begin[0]
        self.right = end[0]
        self.top = begin[1]
        self.buttom = end[1]
        if self.left < self.right:
            self.left = end[0]
            self.right = begin[0]
        if self.top > self.buttom:
            self.top = end[1]
            self.buttom = begin[1]
    
    def moveInPlace(self, move: tuple) -> None:
        self.left += move[0]
        self.right += move[0]
        self.top += move[1]
        self.buttom += move[1]
    
    def renderRectOnCamera(self) -> tuple:
        return (self.left,self.right,self.top,self.buttom)