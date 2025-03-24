"""
    This is the jar demo (unit and gameplay test)
    (c) 2025 Spyro24
"""
import pygame as p
import jar
import time

class jarRun():
    def __init__(self, pygameWindow: p.display.set_mode, debug=False):
        self.debug = debug
        self.window = pygameWindow
        self.camera = jar.camera.Camera(self.window)
        self.testHitboxen = [jar.hitbox.hitbox((0,3),(1,0)), jar.hitbox.hitbox((1,1),(3,0)), jar.hitbox.hitbox((3,0),(4,3))]
        self.bound = jar.hitbox.hitbox((0,0),(10,10))
        self.camera.zoom = 40
        self.camera.setPos((5,5))
        self.joystick = jar.controller.controller()
        
    def mainLoop(self) -> None:
        update = True
        self.camera.debug()
        self.run = True
        zoomTime = time.time()
        timing = []
        timing.append(time.time())
        while self.run:
            frameTime = time.time()
            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
            
            pressedButtons = self.joystick.getEvents()
            if pressedButtons[0] != (0, 0):
                if timing[0] + 0.01 < frameTime:
                    timing[0] = frameTime
                    self.camera.move(pressedButtons[0])
                    update = True
                    
            if update:
                self.window.fill((0,0,0))
                for hitbox in self.testHitboxen:
                    self.camera.renderRect(hitbox,(255,0,255))
                self.camera.renderRect(self.bound,(0,255,0))
                p.display.flip()
                update = False
        
if __name__ == "__main__":
    testWindow = p.display.set_mode((1280, 720))
    testObject = jarRun(testWindow, debug=True)
    testObject.mainLoop()