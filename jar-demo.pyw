#!/bin/python3
"""
    This is the jar demo (unit and gameplay test)
    (c) 2025 Spyro24
"""
import pygame as p
import jar
import time

class jarRun():
    def __init__(self, pygameWindow: p.display.set_mode, debug=False):
        self.FPS = 60
        self.debug = debug
        self.window = pygameWindow
        self.camera = jar.camera.Camera(self.window)
        self.bound = jar.hitbox.hitbox((0,0),(10,10))
        #self.camera.zoom = 40
        #self.camera.setPos((5,5))
        self.joystick = jar.controller.controller()
        self.hitnoxManager = jar.hitbox.hitboxManager()
        self.hitnoxManager.addENV(self.camera)
        self.hitnoxManager.addHitbox((-20,-20), (40,2))
        self.hitnoxManager.addHitbox((-22, 20), (2,40))
        self.hitnoxManager.addHitbox((-10, -5), (20,2))
        self.hitnoxManager.addDeathbox((-40, 1),(15,1))
        self.player = jar.player.player(self.camera, self.hitnoxManager, debug=True)
        self.windowMidpoint = self.window.get_rect().center
        self.camera.zoom = 15
        self.player.calcFrameStuff(self.FPS)
        
    def mainLoop(self) -> None:
        update = True
        self.camera.debug()
        self.run = True
        getTimeStatus = time.time()
        frameTime = 1/self.FPS
        lastFrame = 0
        while self.run:
            curTime = time.time()
            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
            joyEvents = self.joystick.getEvents()
            #physics and render loop (I need to split this in 2 parts in the future)
            if lastFrame + frameTime < time.time():
                lastFrame = curTime
                self.player.tick(joyEvents)
                self.camera.tick()
                #render the stuff
                self.window.fill((0,0,0))
                self.window.set_at(self.windowMidpoint, (255,255,255))
                self.player.onRender()
                self.hitnoxManager.debug()
                p.display.update()
                if curTime - 1 > getTimeStatus:
                    getTimeStatus = curTime
                    finishTime = time.time()
                    print((finishTime - curTime) / frameTime * 100) #Frame usage in percent
        
if __name__ == "__main__":
    testWindow = p.display.set_mode((1280, 720))
    testObject = jarRun(testWindow, debug=True)
    testObject.mainLoop()