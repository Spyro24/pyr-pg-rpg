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
        p.mixer.init()
        self.aud_pat = audio_path
        self.win = win
        self.mainVulume = 100 
        self.c_ambiente = p.mixer.Channel(0)
        self.c_voiceline = p.mixer.Channel(1)
        self.sfx_1 = p.mixer.Channel(2)
        self.sfx_2 = p.mixer.Channel(3)
        self.sfx_3 = p.mixer.Channel(4)
        self.sfx_4 = p.mixer.Channel(5)
        
        
    def set_volume(self, channel):
        pass
    
    def play(self, channel, sound):
        if (channel == "ambiente") or channel == 0:
            self.ambiente_cur = p.mixer.Sound(str(self.aud_pat) + "ambiente/" + str(sound) + ".mp3")
            self.c_ambiente.play(self.ambiente_cur, loops=-1)
            
        elif (channel == "voiceline") or channel == 1:
            pass
        
        elif (channel == "sfx_1") or channel == 2:
            self.sfx_1_cur = p.mixer.Sound(str(self.aud_pat) + "sfx/" + str(sound) + ".mp3")
            self.sfx_1.play(self.sfx_1_cur)
    
    def stop(self, channel):
        if (channel == "all") or channel == -1: #stop all channels at onece
            self.c_ambiente.stop()
            self.c_voiceline.stop()
            
        elif (channel == "ambiente") or channel == 0:
            self.c_ambiente.stop()
    
        elif (channel == "voiceline") or channel == 1:
            self.c_voiceline.stop()
            
    def pause(self, channel):
        if channel == -2: #only pause the chanels that aren't required for the dialog
            self.c_ambiente.pause()
            
        elif (channel == "all") or channel == -1: #stop all channels at onece
            self.c_ambiente.pause()
            self.c_voiceline.pause()
            
        elif (channel == "ambiente") or channel == 0:
            self.c_ambiente.pause()
    
        elif (channel == "voiceline") or channel == 1:
            self.c_voiceline.pause()
    
    def unpause(self, channel):
        if channel == -2: #only unpause the chanels that aren't required for the dialog
            self.c_ambiente.unpause()
            
        elif (channel == "all") or channel == -1: #stop all channels at onece
            self.c_ambiente.unpause()
            self.c_voiceline.unpause()
            
        elif (channel == "ambiente") or channel == 0:
            self.c_ambiente.unpause()
    
        elif (channel == "voiceline") or channel == 1:
            self.c_voiceline.unpause()
            
    def play_voiceline(self, character, voiceline):
        self.voiceline_cur = p.mixer.Sound(str(self.aud_pat) + "voiceline/" + str(character) + "/" + str(voiceline) + ".mp3")
        self.c_voiceline.play(self.voiceline_cur)
        
        
    def run(self):
        #Idk for what this function is
        pass