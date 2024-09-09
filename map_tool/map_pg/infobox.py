import pygame as p
import time

#Info: the Info box need a min size from (9,4) to show up corectly
class InfoBox():
    def __init__(self, win, font, grid_size, pos, outer_size, col=[(0, 128, 128),(128, 0, 128),(128,128,0),(100,100,100)], action=False):
        self.window = win
        self.font = font
        self.size = grid_size
        self.init_pos = pos
        self.outer_size = outer_size
        self.colors = col
        self.action = action
        self.rect_list = []
        self.create_rects()
        
    def show(self, text):
        #text parsing
        showable_text = text.split("\n")
        print(showable_text)
        #setup textscroller
        rect_size = self.rect_list[1][3]
        lines = int(rect_size / self.size)
        print(lines)
        #setup local vars
        x_init = self.init_pos[0] + self.size
        y_init = self.init_pos[1] + self.size 
        x = x_init
        y = y_init
        scroll = 0
        scrollock = 0
        len_text = len(showable_text)
        #setup runtime vars
        run = True
        redraw = True
        update = True
        #execute
        while run:
            if redraw:
                p.draw.rect(self.window, self.colors[0], self.rect_list[0])
                p.draw.rect(self.window, self.colors[3], self.rect_list[1])
                x = x_init
                y = y_init
                for line in range(lines):
                    if (line + scroll) >= len_text:
                        break 
                    self.font.draw(showable_text[line + scroll], self.size - 2, (x + 1, y + 1))
                    y += self.size
                redraw = False
                update = True

            for event in p.event.get():
                if event.type == p.MOUSEWHEEL:
                    scroll_dir = event.y
                    if scroll_dir == -1:
                        scroll += 1
                    elif scroll_dir == 1:
                        scroll -= 1
                    
                    if scroll < 0:
                        scroll = 0
                    
                    if (scroll + lines) > len_text:
                        scroll -= 1
                    redraw = True
            
            mpos = p.mouse.get_pos
            mclick = p.mouse.get_pressed
            
            if update:
                p.display.flip()
                update = False
                
    def create_rects(self):
        outer_rect = p.Rect(self.init_pos, (self.outer_size[0] * self.size, self.outer_size[1] * self.size))
        self.rect_list.append(outer_rect)
        text_rect = p.Rect((self.init_pos[0] + self.size, self.init_pos[1] + self.size), ((self.outer_size[0] - 2) * self.size, (self.outer_size[1] - 3) * self.size))
        self.rect_list.append(text_rect)
        
    def on_end(self, clicked):
        if clicked == 2:
            if self.action:
                return True
        
#Unit test
if __name__ == "__main__":
    import font
    ts = 30
    window = p.display.set_mode((ts * 50, ts * 30))
    font = font.font(window, "../symbols/standard")
    infotext = "A\nB\nC\nD\nE\nF\nG"
    infobox = InfoBox(window, font, ts, (ts *3, ts * 4), (9,7))
    infobox.show(infotext)
    