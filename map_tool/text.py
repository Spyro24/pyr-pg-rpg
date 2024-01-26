from pywin import *
import keyboard as kb

def text_field(win,size,x,y,tx,ty,col,*desc):
    #the col var is a list with the colors for [outer, inner, text, courser]
    rd = 0
    text_field = True
    size_ = int(size / 4)
    upper = False
    text = []
    last_cp = []
    last_cp.append(0)
    c_pos = 0
    init_t = 1
    cur_w = 3 * size
    cur_h = 1 * size
    bsize = size_ *2
    
    while text_field:
        p.display.flip()
        if rd or init_t:
            font = p.font.Font(p.font.get_default_font(), int(size))
            if len(desc) > 0:
                title = font.size(desc[0])
                x_t, y_t = title
                draw_rect(win, x - size_ , y - y_t - bsize ,tx + bsize, ty + y_t + size ,col[0])
                x_r = tx - x
                draw_font(win,size,x , (y - y_t - size_), desc[0], col[2])
            else:
                draw_rect(win, x - size_, y - size_, tx + bsize, ty + bsize, col[0])
            draw_rect(win,x,y,tx,ty,col[1])
            init_t = False
            rd = 0
        
        #Get the keyboard input
        key, mod, trash, action = kb.get_k_key()
        
        if mod != None or key != None or action != None:
            #Get the modifier
            if mod != None:
                print(mod)
                if mod == "uppercase":
                    upper = True
                elif mod == "lowercase":
                    upper = False
            
            if key != None:
                print(key)
                if upper == True:
                    if key == "-":
                        text.append("_")
                        cp, trash = draw_font(win,size,x + sum(last_cp),y,"_",col[2])
                        last_cp.append(cp)

                    else:
                        text.append(key.upper())
                        cp, trash = draw_font(win,size,x + sum(last_cp),y,key.upper(),col[2])
                        last_cp.append(cp)
                else:
                    text.append(key)
                    cp, trash = draw_font(win,size,x + sum(last_cp),y,key,col[2])
                    last_cp.append(cp)
                
                c_pos += 1
            
            if action == "BACKSPACE":
                if c_pos != 0:
                    x_c = x
                    remove = last_cp.pop()
                    draw_rect(win,x + sum(last_cp),y, tx - sum(last_cp),ty,col[1])
                    text.pop()
                    c_pos -= 1
            
            if len(desc) > 1:
                if c_pos > desc[1]:
                    x_c = x
                    remove = last_cp.pop()
                    draw_rect(win,x + sum(last_cp),y, tx - sum(last_cp),ty,col[1])
                    text.pop()
                    c_pos -= 1
            
            if action == "ESC":
                text_field = False
                return None
            #Look if pressed Enter
            if action == "ENTER":
                text_field = False
                return ''.join(text)
            
