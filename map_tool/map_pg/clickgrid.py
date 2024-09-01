import pygame as p

class ClickGrid():
    def __init__(self, size, pos_and_size):
        self.x_grid, self.y_grid = size
        self.x_pos, self.y_pos, self.x_end, self.y_end = pos_and_size
        self.activate_rect = p.Rect(pos_and_size)
        self.create_grid()
    
    def create_grid(self):
        self.x_rects = []
        self.y_rects = []
        x_ending = self.x_end / self.x_grid
        y_ending = self.y_end / self.y_grid
        for pos_x in range(self.x_grid):
            self.x_rects.append(p.Rect(((x_ending * pos_x) + self.x_pos, self.y_pos, x_ending, self.y_end)))
        
        for pos_y in range(self.y_grid):
            self.y_rects.append(p.Rect((self.x_pos, (y_ending * pos_y) + self.y_pos, self.x_end, y_ending)))
    
    def get_click(self, mpos):
        return_cor = (-1,-1)
        x = 0
        y = 0
        if self.activate_rect.collidepoint(mpos):
            for _ in range(self.x_grid):
                if self.x_rects[_].collidepoint(mpos):
                    break
                x += 1
            
            for _ in range(self.y_grid):
                if self.y_rects[_].collidepoint(mpos):
                    break
                y += 1
            return (x,y)
        return return_cor
    
    def return_number(self,mpos):
        coords = self.get_click(mpos)
        x, y = coords
        return y * self.x_grid + x
    
    def debug(self, win):
        vertcol = (255,255,0)
        horicol = (255,0,255)
        for xs in self.x_rects:
            p.draw.rect(win, horicol, xs, width=3)
        for ys in self.y_rects:
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
            
                
    