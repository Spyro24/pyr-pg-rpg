import sys

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

container = pyr_pg.container.container()

def start(log=print)->None:
    log(f"[manor] Log method is {log.__module__}")
    container.window = pyr_pg.displayManager.displayManager((1080,720),(1,1))
    window = container.window
    flags = sys.argv
    if flags.__contains__("-d"):
        container.debugMode = True
        log(f"[manor] Programm is running in debug/developer mode")
    if not container.debugMode or flags.__contains__("--splash"):
        pyr_pg.splash(window, container.splashDuration)