import pygame as p
try:
    import kb as kb
except:
    import pyr_pg.kb as kb

def title_screen(win, lst_scr):
    if lst_scr[0] == True:
        background = win.blit(p.image.load("./back.png"))