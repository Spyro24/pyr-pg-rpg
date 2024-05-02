"""
    Audioplayer for pyr-pg
    Copyright (C) 2024 Spyro24

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import pygame as p
from time import time as tg

class sound():
    def __init__(self,win, audio_path):
        self.aud_pat = audio_path
        self.win = win
        self.c_ambiente = p.mixer.Channel(0)
        
    def set_volume(self, channel):
        pass
    
    def play(self, channel, sound):
        if (channel == "ambiente") or channel == 0:
            self.ambiente_cur = p.mixer.Sound(str(self.aud_pat) + "ambiente/" + str(sound) + ".mp3")
            self.c_ambiente.play(self.ambiente_cur, loops=-1)
            
    def run(self):
        pass