import pygame as p
import pywin as pw

class player:
    def __init__(self, win, max_h, pos_x, pos_y, player_set):
        self.hight = 0
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pg_win = win
        self.max_hight = max_h
        self.sprites = player_set

test = ["up"]
test_set = []
for element in test:
    test_set.append(p.image.load("./player/" + str(element) + ".png"))
test_win = p.display.set_mode((500,500))
def end_game(win,varlst):
    #varlist = [win_w,win_h]
    cube = player(win, 30, 0, 0,)
    run = True
    update = False
    while run:
    
        for event in p.event.get():
            if event == p.QUIT:
                pass
        
        if update:
            p.update()
            update = False
    
end_game(test_win,[500,500])
