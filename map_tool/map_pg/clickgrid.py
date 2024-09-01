import pygame as p

class ClickGrid():
    def __init__(self, size, pos_and_size):
        self._x_grid, self._y_grid = size
        self._x_pos, self._y_pos, self._x_end, self._y_end = pos_and_size
        self.activate_rect = p.Rect(pos_and_size)
        self._create_grid()
    
    def _create_grid(self):
        self._x_rects = []
        self._y_rects = []
        x_ending = self._x_end / self._x_grid
        y_ending = self._y_end / self._y_grid
        for pos_x in range(self._x_grid):
            self._x_rects.append(p.Rect(((x_ending * pos_x) + self._x_pos, self._y_pos, x_ending, self._y_end)))
        
        for pos_y in range(self._y_grid):
            self._y_rects.append(p.Rect((self._x_pos, (y_ending * pos_y) + self._y_pos, self._x_end, y_ending)))
    
    def get_click(self, mpos): #-> tuple(x, y) 
        return_cor = (-1,-1)
        x = 0
        y = 0
        if self.activate_rect.collidepoint(mpos):
            for _ in range(self._x_grid):
                if self._x_rects[_].collidepoint(mpos):
                    break
                x += 1
            
            for _ in range(self._y_grid):
                if self._y_rects[_].collidepoint(mpos):
                    break
                y += 1
            return (x,y)
        return return_cor
    
    def return_number(self, mpos): #-> int
        coords = self.get_click(mpos)
        x, y = coords
        return y * self._x_grid + x
    
    def debug(self, win):
        vertcol = (255,255,0)
        horicol = (255,0,255)
        for xs in self._x_rects:
            p.draw.rect(win, horicol, xs, width=3)
        for ys in self._y_rects:
            p.draw.rect(win, vertcol, ys, width=3)
    
#unit test of the modul
if __name__ == "__main__":
    window = p.display.set_mode((300,300))
    click_rect = ClickGrid((5,5),(50,50,300,300))
    click_rect.debug(window)
    p.display.flip()
    run = True
    while run:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                
        mpos = p.mouse.get_pos()
        mclick = p.mouse.get_pressed()
        if mclick[0] == True:
            print(click_rect.get_click(mpos))
            print(click_rect.return_number(mpos))
            
                
    