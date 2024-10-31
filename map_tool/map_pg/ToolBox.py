import pygame as p

class ToolBox():
    def __init__(self):
        self._loaded = {"Grid":False, "Map":False}
        self._Tool = "DRAW"
        self._Tool_on = "CLICK"
    
    def ChangeTool(self,Tool):
        self._Tool = Tool
    
    def ChangeToolSize(self,Size):
        pass
    
    def AddToolGrid(self, ClickGrid): #Add the ClickGrid object
        pass
        #self.
    
    def AddMapObject(self, MapObjekt): #Add the map Object
        pass
    
    def _StateMachine(*args):
        pass
    
    def _Tool_Circle(self, X_Position, Y_Position, Rad):
        pass
    
    def _Tool_Rect(FirstPosition,SecondPosition):
        _FPX = 0 #First Mouse X Position
        _FPY = 0 #First Mouse Y Position
        _SPX = 0 #Second Mouse X Position