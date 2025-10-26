"""
    soundsystem for pyr-pg
    Copyright (C) 2025 Spyro24

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
import os

p.mixer.init()

class sound:
    def __init__(self, audioPath: str):
        self.volumes = {"main":100, "fx":100}
        self.channels = {"fx1":p.mixer.Channel(0)}
        self.audio = {}
        self.audioPath = audioPath.strip("/")
        self.load_audio()
        
    def load_audio(self):
        config = open(self.audioPath + "/load.cfg", "r")
        lines = config.read()
        lines = lines.split("\n")
        config.close()
        for line in lines:
            if line != "":
                splited = line.split(";")
                self.audio[splited[1]] = {}
                self.audio[splited[1]]["sound"] = p.mixer.Sound(self.audioPath + "/" + splited[0])
                self.audio[splited[1]]["channel"] = splited[2]
    
    def play(self, sound: str):
        sound = self.audio[sound]
        self.channels[sound["channel"]].play(sound["sound"])
