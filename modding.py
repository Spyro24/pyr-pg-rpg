"""
    Default modding support file for pyr_pg-rpg
    (c) date your_name
"""
import pygame as p
import runtime_store as rs

class mod:
    def __init__(self, runtimeStore):
        #please don't change anything here.
        self.runtimeStore = runtimeStore
    
    def _on_ready(self) -> None:
        #this function is called after the initalisation of the game.
        pass
    
    def _on_key(self, keys) -> None:
        #put here your code that will execute on changed keys.
        pass
    
    def mainLoopInterupt(self):
        pass
    
    def render(self):
        pass