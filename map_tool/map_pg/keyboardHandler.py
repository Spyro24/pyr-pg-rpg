"""
    a Simple pygame.key to string converter
    (c) 2025 Spyro24
"""

import pygame as p

class keyboard:
    def __init__(self):
        self.keyToStr = {p.K_0: "0", p.K_1: "1", p.K_2: "2", p.K_LESS: "<"}
        self.modAltGr = {p.K_LESS: "|"}
    
    def returnString(self) -> str:
        pass
    
    def returnSingleChar(self, key: int, mod) -> str or None:
        try:
            if mod & p.KMOD_RALT or mod & p.KMOD_MODE:
                return self.modAltGr[key]
            elif mod & p.KMOD_SHIFT:
                if key == p.K_LESS:
                    return ">"
                else:
                    return self.keyToStr[key].upper() 
            else:
                return self.keyToStr[key]
        except KeyError:
            pass
        return None

if __name__ == "__main__":
    testWindows = p.display.set_mode((1,1))
    testKeyboard = keyboard()
    while True:
        for event in p.event.get():
            keys = p.key.get_pressed()
            if event.type == p.QUIT:
                p.quit()
            elif event.type == p.KEYDOWN:
                for key in range(len(keys)):
                    if keys[key]:
                        check = testKeyboard.returnSingleChar(key, event.mod)
                        if check != None:
                            print(check)
