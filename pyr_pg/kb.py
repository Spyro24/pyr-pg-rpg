import pygame as p

def wasd_arrow_2d():
    direction = None
    pressed = False
    key_ar = list(p.key.get_pressed())
    
    #This is the new control script
    if key_ar[3+23] and key_ar[3+1]:
        direction = "LUP"
    elif key_ar[3+23] and key_ar[3+4]:
        direction = "RUP"
    elif key_ar[3+1] and key_ar[3+19] :
        direction = "LWN"
    elif key_ar[3+4]  and key_ar[3+19]:
        direction = "RWN"
    
    #This was the Original control script
    elif key_ar[3+23]:
        direction = "UP"
    elif key_ar[3+1]:
        direction = "LEFT"
    elif key_ar[3+19]:
        direction = "DOWN"
    elif key_ar[3+4]:
        direction = "RIGHT"
        
    if direction != None:
        pressed = True
    
    return direction, pressed
