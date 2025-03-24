"""
    This is the jar demo (unit and gameplay test)
    (c) 2025 Spyro24
"""
import pygame as p
import jar

class jarRun():
    def __init__(self, pygameWindow: p.display.set_mode, debug=False):
        self.debug = debug
        self.window = pygameWindow
        self.camera = jar.camera.Camera(self.window)
        self.testHitbox = jar.hitbox.hitbox((-1,1),(1,-1))
        
    def mainLoop(self) -> None:
        update = True
        self.camera.debug()
        self.run = True
        while self.run:
            if update:
                self.camera.renderRect(self.testHitbox,(255,0,255))
                p.display.flip()
                update = False
        
if __name__ == "__main__":
    testWindow = p.display.set_mode((1280, 720))
    testObject = jarRun(testWindow, debug=True)
    testObject.mainLoop()