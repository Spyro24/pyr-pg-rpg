"""
    Input System for pyr_pg
    (c) 2025 Spyro24
"""
import pygame as p
import pyr_pg

class inputSystem:
    def __init__(self, runtimeStore):
        self. rs = runtimeStore
        self.window = self.rs[10][13]
        self.buttons = [p.K_w, p.K_d, p.K_s, p.K_a, p.K_ESCAPE]
        self.fireOnKeyPressed = True
        self.fireKeyDown = False
        self.fireKeyUp = False
        
    def setEventFire(self, keyType):
        '''Set the fire type for the events [PRESSED, UP, DOWN]'''
        pass
        
    def getEvents(self):
        events = []
        for event in p.event.get():
            if event.type == p.QUIT:
                events.append(pyr_pg.QUIT)
        if self.fireOnKeyPressed:
            key_ar = p.key.get_pressed()
            if key_ar[self.buttons[1]]:
                events.append(pyr_pg.K_UP)
        return events
    
class touchInput:
    def __init__(self, window):
        pass
    
class controllerInput:
    def __init__(self, window):
        pass