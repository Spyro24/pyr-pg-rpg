"""
How to use the pygame keyboard input:
make 4 vars: key, mod, arrow, action
than use the keyboard like this: key, mod, arrow, action = get_k_key.

"key" is for the kb key
"mod" is a modifier like shift
"arrow" is for the arrow keys
"action" is for the action keys like ESC or Backspace
"""




import pygame as p

def get_k_key():
    key = None
    mod = None
    arrow = None
    action = None
    for event in p.event.get():
        if event.type == p.KEYDOWN:
                if event.key == p.K_LSHIFT or event.key == p.K_RSHIFT:
                    mod = "uppercase"
                # Check for all the letter
                elif event.key == p.K_a:
                    key = "a"
                elif event.key == p.K_b:
                    key = "b"
                elif event.key == p.K_c:
                    key = "c"
                elif event.key == p.K_d:
                    key = "d"
                elif event.key == p.K_e:
                    key = "e"
                elif event.key == p.K_f:
                    key = "f"
                elif event.key == p.K_g:
                    key = "g"
                elif event.key == p.K_h:
                    key = "h"
                elif event.key == p.K_i:
                    key = "i"
                elif event.key == p.K_j:
                    key = "j"
                elif event.key == p.K_k:
                    key = "k"
                elif event.key == p.K_l:
                    key = "l"
                elif event.key == p.K_m:
                    key = "m"
                elif event.key == p.K_n:
                    key = "n"
                elif event.key == p.K_o:
                    key = "o"
                elif event.key == p.K_p:
                    key = "p"
                elif event.key == p.K_q:
                    key = "q"
                elif event.key == p.K_r:
                    key = "r"
                elif event.key == p.K_s:
                    key = "s"
                elif event.key == p.K_t:
                    key = "t"
                elif event.key == p.K_u:
                    key = "u"
                elif event.key == p.K_v:
                    key = "v"
                elif event.key == p.K_w:
                    key = "w"
                elif event.key == p.K_x:
                    key = "x"
                elif event.key == p.K_y:
                    key = "y"
                elif event.key == p.K_z:
                    key = "z"
                # Check for space
                elif event.key == p.K_SPACE:
                    key = " "
                # Check for period
                elif event.key == p.K_PERIOD:
                    key = "."
                # Check for comma
                elif event.key == p.K_COMMA:
                    key = ","
                # Check for numbers
                elif event.key == p.K_0:
                    key = "0"
                elif event.key == p.K_1:
                    key = "1"
                elif event.key == p.K_2:
                    key = "2"
                elif event.key == p.K_3:
                    key = "3"
                elif event.key == p.K_4:
                    key = "4"
                elif event.key == p.K_5:
                    key = "5"
                elif event.key == p.K_6:
                    key = "6"
                elif event.key == p.K_7:
                    key = "7"
                elif event.key == p.K_8:
                    key = "8"
                elif event.key == p.K_9:
                    key = "9"
                elif event.key ==  p.K_MINUS :
                    key = "-"
                elif event.key == p.K_UP :
                    arrow = "UP"
                elif event.key == p.K_DOWN :
                    arrow = "DOWN"
                elif event.key == p.K_LEFT :
                    arrow = "LEFT"
                elif event.key == p.K_RIGHT :
                    arrow = "RIGHT"
                # check for action Keys
                elif event.key == p.K_BACKSPACE:
                    action = "BACKSPACE"
                elif event.key == p.K_RETURN:
                    action = "ENTER"
                elif event.key == p.K_ESCAPE:
                    action = "ESC"
                
                
        elif event.type == p.KEYUP:
                if event.key == p.K_LSHIFT or event.key == p.K_RSHIFT:
                    mod = "lowercase"
    arow = 0
    return key, mod, arrow, action