import pygame as p

class drop_down():
    def __init__(self, win, size, pos, lenght, font, color, activate, functs, mode="static"):
        self.win = win
        self.font = font
        self.font_size = size
        self.mode = mode
        self.advace_render = False
        self.set_mode()
        self.activate = p.Rect(activate)
        self.functions = functs
        self.function_keys = list(self.functions.keys())
        self.x_pos = pos[0]
        self.begin_pos = pos
        self.end_pos = (size * lenght, 0)
        self.expand_rect = p.Rect(pos, (size * lenght, size * len(self.function_keys)))
        self.bg_col = color[0]
        self.fg_col = color[1]
        self.option_grid = []
        self.create_option_grid()
    
    def set_mode(self):
        if self.mode == "static":
            self.advace_render = False
        elif self.mode == "advance":
            self.advace_render = True
        else:
            raise ValueError("Render modes are 'static' or 'advance'")
    
    def create_option_grid(self):
        x = self.begin_pos[0]
        y = self.begin_pos[1]
        x_end = self.end_pos[0]
        y_end = self.font_size
        for option in range(len(self.function_keys)):
            self.option_grid.append(p.Rect(x, y, x_end, y_end))
            y += self.font_size
        
    def expand(self):
        run = True
        redraw = True
        update = False
        while run:
            if redraw:
                self.draw_options()
                redraw = False
                update = True
            
            p.event.get()
            
            mpos = p.mouse.get_pos()
            mclick = p.mouse.get_pressed()
            
            if self.activate.collidepoint(mpos) or self.expand_rect.collidepoint(mpos):
                if self.advace_render:
                    self.draw_options()
                    for rect in self.option_grid:
                        if rect.collidepoint(mpos):
                            p.draw.rect(self.win, self.fg_col, rect)
                            self.draw_text()
                            update = True
                            
                if mclick[0]:
                    for rect in range(len(self.function_keys)):
                        if self.option_grid[rect].collidepoint(mpos):
                            self.functions[self.function_keys[rect]]()
                            run = False
                            self.close()
                
            else:
                run = False
                
            if update:
                p.display.flip()
                update = False
        
    def draw_text(self):
        x = self.begin_pos[0]
        y = self.begin_pos[1]
        for entry in self.function_keys:
            self.font.draw(entry, self.font_size - 2, (x + 1, y + 1))
            y += self.font_size
            
    def draw_options(self):
        p.draw.rect(self.win, self.bg_col, self.expand_rect)
        self.draw_text()
    
    
    def close(self):
        pass
    
    def open(self, mpos):
        if self.activate.collidepoint(mpos):
            self.expand()

if __name__ == "__main__":
    import font
    def print_hello():
        print("Hello World")
    
    ts = 20*3
    window = p.display.set_mode((ts * 15, ts * 15))
    main_font = font.font(window, "../symbols/standard")
    unit_test = drop_down(window, ts, (0, ts), 3, main_font, [(0, 128, 128),(128, 0, 128)], (0, 0,ts * 2, ts), {"Exit":p.quit, "Hello":print_hello}, mode="advance")
    run = True
    
    while run:
        p.event.get()
        
        mpos = p.mouse.get_pos()
        mclick = p.mouse.get_pressed()
        
        if mclick[0] == True:
            unit_test.open(mpos)
        
        window.fill((0,0,0))
        p.display.flip()