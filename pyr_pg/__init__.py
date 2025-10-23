#!/bin/python3
'''
    PYR_PG is a python RPG libary for making custom RPGs.
    PYR_PG supports modding(pyr-pg-rpg) custom scripts and more.
    Lincense: GPLv3
    (c) 2023-2025 Spyro24
'''

import pyr_pg.config, pyr_pg.audioMixer, pyr_pg.map_, pyr_pg.player
import pyr_pg.tile_handler, pyr_pg.cutting_edge, pyr_pg.infobox, pyr_pg.font
import pyr_pg.DialogHandler
import pyr_pg.options_menu
import pyr_pg.log_system
import pyr_pg.npc
import pyr_pg.npc_handler
import pyr_pg.speechSynth
import pyr_pg.characterSelector
import pyr_pg.inputSystem
import pyr_pg.ui
import pyr_pg.container
import pyr_pg.displayManager
import pyr_pg.sound
import pyr_pg.math_

version = "0.4.6"

#static constants for the input system
QUIT = 1
K_UP = 2
K_DOWN = 3
K_LEFT = 4
K_RIGHT = 5
K_ESC = 6

#Splashscreen for pyr_pg
def splash(win, splash_duration: float) -> None:
    """create the pyr_pg splash(You dont need any image for that.)"""
    import base64
    import zlib
    import pygame as p
    import time
    splash_png_base64 = "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"
    splash_png = p.image.frombytes(zlib.decompress(base64.b64decode(splash_png_base64)), (256,256), "RGBA")
    w, h = win.get_size()
    lowest_size = 0
    if w > h:
        lowest_size = h
    else:
        lowest_size = w
    b_pos_x = (w / 2) - (lowest_size / 2)
    b_pos_y = (h / 2) - (lowest_size / 2)
    transp = 51
    a = p.Surface((1, 1), flags=p.SRCALPHA)
    a.convert()
    splash_png = p.transform.scale(splash_png, (lowest_size, lowest_size))
    splash_png.convert()
    for n in range(5, -1, -1):
        a.set_at((0,0),(0,0,0,transp * n))
        win.blit(splash_png, (b_pos_x, b_pos_y))
        win.blit(p.transform.scale(a, (lowest_size, lowest_size)), (b_pos_x, b_pos_y))
        p.display.flip()
        time.sleep(0.05)
    time.sleep(splash_duration)
    for n in range(0,6):
        a.set_at((0,0),(0,0,0,transp * n))
        win.blit(splash_png, (b_pos_x, b_pos_y))
        win.blit(p.transform.scale(a, (lowest_size, lowest_size)), (b_pos_x,b_pos_y))
        p.display.flip()
        time.sleep(0.05)
    time.sleep(0.1)
