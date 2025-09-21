import sys
import pygame as p
import time

version = "0.0.0"

if __name__ == "__main__":
    print("You cannot use manor directly")
    sys.exit(0)

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
import manor.player_selector
import manor.info_menu 

container = pyr_pg.container.container()

def start(log=print)->None:
    log(f"[manor] Log method is {log.__module__}")
    container.window = pyr_pg.displayManager.displayManager((1080,720),(1,1))
    container.cache = manor.cache.cacheStuff()
    container.logSystem = log
    container.font = pyr_pg.font.font(container.window, "./res/fonts/standard")
    window = container.window
    flags = sys.argv
    if flags.__contains__("-d"):
        container.debugMode = True
        log(f"[manor] Programm is running in debug/developer mode")
    if not container.debugMode or flags.__contains__("--splash"):
        pyr_pg.splash(window, container.splashDuration)
    game_loop(on_init(container))

def on_init(container_var):
    modules = (manor.start_menu.startMenu,
               manor.player_selector.playerSelector,
               manor.info_menu.infoMenu,
               )
    moduleAllocation = {}
    for modul in modules:
        cur_init = modul(container_var)
        moduleAllocation[cur_init.modul_name] = cur_init
    return moduleAllocation
        
def game_loop(game_content)->None:
    container.logSystem("[manor] starting main_loop")
    run = True
    cur_function = game_content["main_menu"]
    window = container.window
    container.logSystem(f"[manor] lowest size is {window.lowestSize}px")
    is_debug_mode = container.debugMode
    frameCounter = 0
    lastSecond = time.time()
    FPS = 1/60
    lastRendereFrame = 0
    while run:
        frameTime = time.time()
        cur_states = cur_function.main_loop()
        if cur_states[0] != None:
            lastFunction = cur_function.modul_name
            cur_function = game_content[cur_states[0]]
            cur_function.lastFunction = lastFunction
            if cur_function.windowHasResized:
                cur_function.on_window_update()
        if cur_states[1] == 1:
            window.windowResize()
            for obj in game_content.values():
                obj.windowHasResized = True
            cur_function.on_window_update()
        if lastRendereFrame + FPS < frameTime:
            lastRendereFrame = frameTime
            window.window.fill((0, 0, 0))
            cur_function.render()
            if is_debug_mode:
                cur_function.debug_render()
            window.flip()
        frameCounter += 1
        if frameTime - 1 > lastSecond:
            print(frameCounter)
            lastSecond = frameTime
            frameCounter = 0
