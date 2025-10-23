import pygame as p

def cacheStuff():
    cache = {}
    cache["mainMenu/bg"] = p.image.load("./res/main_menu/back.png").convert() #background Image
    cache["mainMenu/title"] = p.image.load("./res/main_menu/title.png").convert_alpha() #title Image or logo
    cache["buttons/defaultBackground"] = p.image.load("./res/buttons/ButtonBG_BlackWhite.png").convert_alpha()
    cache["icons/settings"] = p.image.load("./res/icons/settings.png").convert_alpha()
    cache["icons/info"] = p.image.load("./res/icons/info.png").convert_alpha()
    cache["textbox/background/menu"] = p.image.load("./res/textboxes/gray_rounded_playerSelectort.png").convert_alpha()
    return cache
