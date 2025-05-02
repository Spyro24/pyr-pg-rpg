"""
    IO Handler for PYR_PG to reduce lag
    (c) 2025 Spyro24
"""
import pygame as p
from threading import Thread

class ioSchedule:
    def __init__(self, runtimeStore, debug=False):
        pass
    
    def scheduleTask(self, pathToOBJ: str, taskType: int) -> None:
        pass
    
    def execSchedules(self) -> None:
        pass
    
    def getData(self, pathToOBJ: str) -> object:
        pass