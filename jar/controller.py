import pygame as p

class controller():
    def __init__(self):
        p.joystick.init()
        self.__type = 1 #0 = keyboard, 1 = PS4 controller, 2 = XBOX 360 Controller
        self.__controller = p.joystick.Joystick(0)
        self.__lenButtons = self.__controller.get_numbuttons()
        
    def getAxis(self, axis: int):
        print(self.__controller.get_axis(axis))
        
    def getAllAxisPS4(self) -> tuple:
        return (self.__controller.get_axis(0), self.__controller.get_axis(1), self.__controller.get_axis(2), (self.__controller.get_axis(3), self.__controller.get_axis(4)), self.__controller.get_axis(5))
    
    def getAllButtonsPS4(self) -> tuple:
        buttons = []
        for n in range(self.__lenButtons):
            buttons.append(self.__controller.get_button(n))
        return buttons
    
    def getDpadPS4(self) -> tuple:
        return self.__controller.get_hat(0)
    
    def getEvents(self) -> tuple:
        if self.__type == 0:
            pass
        if self.__type == 1:
            return (self.getDpadPS4(), self.getAllAxisPS4(), self.getAllButtonsPS4())
        
if __name__ == "__main__":
    import time
    test = controller()
    p.display.init()
    while True:
        time.sleep(0.01)
        p.event.get()
        print(test.getAllButtonsPS4())