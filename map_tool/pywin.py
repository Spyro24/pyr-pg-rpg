import pygame as p
import random
p.init()


def icon_grid(win, fx, fy, size, x_rows, y_rows, icons, page, layer):
    iter_ = 0
    try:
        for y in range(0, int(y_rows)):
            for x in range(0, int(x_rows)):
                if icons[layer][iter_] == 0:
                    iter_ += 1
                else:
                    icon_ = icons[layer][iter_ + (x_rows * y_rows * page)]
                    transform_ = p.transform.scale(icon_, (size - 4, size - 4))
                    win.blit(transform_, (fx + (size * x),fy + (size *y)))
                    iter_ += 1
    except BaseException as err:
        print(err)
            
def button_grid(x,y,size,xrow,yrow):
    iter_ = 0
    m_x, m_y = p.mouse.get_pos()
    if p.mouse.get_pressed() == (1, 0, 0):
        for y_r in range(1, int(yrow) + 1):
            for x_r in range(1, int(xrow) + 1):
                if m_x >= ((x + x_r * size) - size) and m_x < (x + x_r * size):
                    if m_y >= ((y + y_r * size) - size) and m_y < (y + y_r  * size):
                        return (x_r -1, y_r - 1), iter_
                iter_ += 1
        
    
    return None, None

def draw_rect(win,x,y,tox,toy,col):
    rect_ = p.Rect(x, y, tox, toy)
    p.draw.rect(win, col, rect_)
    
def redraw_rect(x,y,size,x_y,col,win):
    rect_ = p.Rect(x + x_y[0]* size, y + x_y[1] * size, size, size)
    p.draw.rect(win, col, rect_)
    
def courser(x,y,size,x_y,col,win):
    rect_ = p.Rect(x + x_y[0]* size, y + x_y[1] * size, size, size)
    p.draw.rect(win, col, rect_, width=int(size / 10))

def draw_box(x,y,tox,toy,size,col,win):
    rect_ = p.Rect(x, y, tox, toy)
    p.draw.rect(win, col, rect_, width=int(size / 10))
    
def draw_font(win, size, x, y, text, col):
    font = p.font.Font(p.font.get_default_font(), int(size))
    ren = font.render(text, 0, col)
    win.blit(ren,(x,y))
    return font.size(text)

def p_push_button(x, y, tx, ty):
    mx, my = p.mouse.get_pos()
    left, void, void = p.mouse.get_pressed()
    if left == True:
        if mx >= x and my >= y:
            if mx <= x + tx and my <= y + ty:
                return True
    return False

def p_push_button2(x, y, tx, ty):
    p.event.get()
    mx, my = p.mouse.get_pos()
    left, void, void = p.mouse.get_pressed()
    if left == True:
        if mx >= x and my >= y:
            if mx <= (tx + x) and my <= (ty + y):
                return True
    return False
def draw_x(win, pos, size, x_y): #This function load the X.png and draw it
    path = "./symbols/X.png"
    img = p.transform.scale(p.image.load(path),(size,size))
    win.blit(img,(pos[0] + (x_y[0] * size), pos[1] + ( x_y[1] * size)))

def draw_tile(win, pos, ov, size, x_y, no):
    size = int(size)
    if ov == False:
        if True:
            print("DEBUG: running draw_tile")
            if no != 0:
                load_ = p.transform.scale(p.image.load("../tiles/" + str(no) + ".png"),(size, size))
                win.blit(load_,(pos[0] + (x_y[0] * size), pos[1] + ( x_y[1] * size)))
            else:
                draw_rect(win,pos[0] + (x_y[0] * size),pos[1] + ( x_y[1] * size),size,size,(0,0,0))
        else:
            draw_rect(win,pos[0] + (x_y[0] * size), pos[1] + (x_y[1] * size), pos[0] + ((x_y[0] + 1) * size), pos[1] + ((x_y[1] + 1) * size), (0,0,0))
    else:
        if no != 0:
            load_ =p.transform.scale(p.image.load("../tiles/overlay/" + str(no) + ".png"),(size,size))
            win.blit(load_,(pos[0] + (x_y[0] * size), pos[1] + ( x_y[1] * size)))

#dev comment: remove this function before release
def draw_map(win, pos, scale, map_, h_w, *opn):
    xp = int(pos[0])
    yp = int(pos[1])
    size = (int(scale), int(scale))
    iter_ = 0
    if opn == ():
        opn = ("","")
    if opn[0] == "X":
        for h in range(0, int(h_w[0])):
            for w in range(0, int(h_w[0])):
                if map_[iter_] != 0:
                    img_ = p.transform.scale(p.image.load("./symbols/X.png"),size)
                    win.blit(img_,(xp + w * size[0], yp + h * size[1]))
                iter_ += 1
    elif opn[0] == "ov":
        for h in range(0, int(h_w[0])):
            for w in range(0, int(h_w[0])):
                if map_[iter_] != 0:
                    img_ = p.transform.scale(p.image.load("../tiles/overlay/" + str(map_[iter_]) + ".png"),size)
                    win.blit(img_,(xp + w * size[0], yp + h * size[1]))
                iter_ += 1
    else:
        for h in range(0, int(h_w[0])):
            for w in range(0, int(h_w[0])):
                if map_[iter_] != 0:
                    img_ = p.transform.scale(p.image.load("../tiles/" + str(map_[iter_]) + ".png"),size)
                    win.blit(img_,(xp + w * size[0], yp + h * size[1]))
                iter_ += 1
                
def load_iconset(path, icons):
    iconset = []
    for element in icons:
        iconset.append(p.image.load(path + "/" + str(element) + ".png"))
    return iconset
    
def blit_icon(win, x, y, icon_frm_set, size):
    win.blit(p.transform.scale(icon_frm_set, (size,size)),(x,y))