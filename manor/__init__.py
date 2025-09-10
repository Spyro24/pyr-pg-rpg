import sys
import pygame as p

version = "0.0.0"

print("[manor] ---Init---")
print(f"[manor] version {version}")
try:
    import pyr_pg
    print("[manor] pyr_pg found")
    print(f"[manor] pyr_pg version {pyr_pg.version}")
except ModuleNotFoundError:
    print("[manor] This module needs pyr_pg to work")
    exit(1)
print(f"[manor] import manor modules")
import manor.cache
import manor.start_menu

container = pyr_pg.container.container()

def on_init(container_var):
    return {"main_menu": manor.start_menu.startMenu(container_var)}

def start(log=print)->None:
    log(f"[manor] Log method is {log.__module__}")
    container.window = pyr_pg.displayManager.displayManager((1080,720),(1,1))
    container.cache = manor.cache.cacheStuff()
    container.logSystem = log
    window = container.window
    flags = sys.argv
    if flags.__contains__("-d"):
        container.debugMode = True
        log(f"[manor] Programm is running in debug/developer mode")
    if not container.debugMode or flags.__contains__("--splash"):
        pyr_pg.splash(window, container.splashDuration)
    game_loop(on_init(container))
        
def game_loop(game_content)->None:
    container.logSystem("[manor] starting main_loop")
    run = True
    cur_function = game_content["main_menu"]
    window = container.window
    container.logSystem(f"[manor] lowest size is {window.lowestSize}px")
    while run:
        cur_states = cur_function.main_loop()
        if cur_states[1] == 1:
            window.windowResize()
            for obj in game_content.values():
                obj.setup()
        window.window.fill((0, 0, 0))
        cur_function.render()
        window.flip()