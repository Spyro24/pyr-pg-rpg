import pygame as p
import random
            
def button_grid(x,y,size,xrow,yrow):
    iter_ = 0
    p.event.get()
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
    p.event.get()
    mx, my = p.mouse.get_pos()
    left, void, void = p.mouse.get_pressed()
    if left == True:
        if mx >= x and my >= y:
            if mx <= (tx + x) and my <= (ty + y):
                return True
    return False