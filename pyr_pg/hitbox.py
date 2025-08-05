#!/bin/python3
"""
    Hitbox system for pyr_pg
    (c) 2025 Spyro24
"""
import pygame as p

class hitbox():
    """pyr_pg hitbox class"""
    def __init__(self, w_h: tuple, init_pos: tuple):
        self.w_h = w_h
        self.position = init_pos
    
    def get_vertices(self):
        return ((),(),(),())
    
    def debug(self, window: p.Surface, draw_offset=(0, 0)):
        pass

if __name__ == "__main__":
    pass
