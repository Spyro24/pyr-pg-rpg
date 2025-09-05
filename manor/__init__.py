version = "0.0.0"
print("[manor] ---Init---")
print(f"[manor] version {version}")
try:
    import pyr_pg
    print("[manor] pyr_pg found")
    print(f"[manor] pyr_pg version {pyr_pg.version}")
except BaseException:
    print("[manor] This module needs pyr_pg to work")
    exit(1)

container = manor.container.container()

def start(log=print)->None:
    log(f"[manor] Log method is {log.__module__}")
    