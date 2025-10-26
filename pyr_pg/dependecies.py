"""
    Dependencies for pyr_pg (for dependencie injetiont)
    (c) 2025 Spyro24
"""

import pygame as p

class dependcies:
    def __init__(self):
        self.storage = {"/window": p.Surface,
                        }
        
    def add(self, object_, path):
        self.storage[path] = object_
        
    def get(self, path):
        return self.storage[path]
    
    def remove(self, path):
        self.storage.pop(path)
