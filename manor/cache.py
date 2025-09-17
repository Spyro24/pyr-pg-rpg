import pygame as p

def cacheStuff():
    cache = {}
    cache["mainMenu/bg"] = p.image.load("./res/main_menu/back.png") #background Image
    cache["mainMenu/title"] = p.image.load("./images/main_menu/title.png") #title Image or logo
    cache["buttons/defaultBackground"] = p.image.load("./res/buttons/ButtonBG_BlackWhite.png")
    cache["icons/settings"] = p.image.load("./res/icons/settings.png")
    cache["icons/info"] = p.image.load("./res/icons/info.png")
    cache["textbox/background/menu"] = p.image.load("./res/textboxes/gray_rounded_playerSelectort.png")
    return cache
