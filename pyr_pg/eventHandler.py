import pygame as p

class eventHandler:
    def __init__(self):
        self.control = {"UP":"w", "DOWN":"s", "LEFT":"a", "RIGHT":"d"}
        self.keys = {"a":p.K_a, "b":p.K_b, "c":p.K_c}
        self.key_states = {}
        for key in self.keys.keys():
            self.key_states[key] = False
    
    def get_keys_down(self):
        pass
    
    def get_keys_control(self):
        pass
    
    def update_events(self):
        for event in p.event.get():
            pass