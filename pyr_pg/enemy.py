import pygame as p

class enemy():
    def __init__(self):
        self.config_table = {"tile_size":(0,0)}
        self.state_table = {"DEATH":False}