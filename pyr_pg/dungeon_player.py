import pygame as p
import time

class player():
    def __init__(self, game_window, settings_dict):
        self.settings = settings_dict
        self.gw = game_window
        gw_w, gw_h = self.gw.get_size()
        self.shortest_side = 0
        if gw_w > gw_h:
            self.shortest_side = gw_h
        else:
            self.shortest_side = gw_w
        ts_x, ts_y = self.shortest_side / self.settings["tiles"][0], self.shortest_side / self.settings["tiles"][1]
        self.hitbox = p.Rect((self.settings["start_pos"][0] * ts_x, self.settings["start_pos"][1] * ts_y), (self.settings["hitbox"][0] * ts_x, self.settings["hitbox"][1] * ts_y))
        self.color_table = self.settings["color_table"]
        self.move_ = ts_x / 16
        self.dir = "UP"
    
    def render(self):
        p.draw.rect(self.gw, self.color_table["player_col"], self.hitbox)
    
    def move(self, x, y):
        rp_x = 0
        rp_y = 0
        if y > 0:
            rp_y = y * self.move_
            self.dir = "DOWN"
        elif y < 0:
            rp_y = y * self.move_
            self.dir = "UP"
        
        if x > 0:
            rp_x = x * self.move_
            self.dir = "DOWN"
        elif x < 0:
            rp_x = x * self.move_
            self.dir = "UP"
        
        self.hitbox.move_ip(rp_x, rp_y)
        
        


if __name__ == "__main__":
    game_window = p.display.set_mode((16 * 50, 9 * 50))
    color_table = {"bg_col":(0,0,0), "player_col":(255,0,0)}
    d_player = player(game_window, {"tiles":(16,16), "hitbox":(1,1), "start_pos":(0,0), "color_table":color_table})
    d_player.render()
    p.display.flip()
    update = True
    run = True
    rtime = time.time()
    deley = 0.005
    while run:
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
                
        key_ar = p.key.get_pressed()
        n = 0
        
        '''
        for n in range(0, len(key_ar)):
                if key_ar[n]:
                    print(n)
        '''
        if time.time() > rtime + deley:
            move = False
            mo_x, mo_y = 0, 0
            if key_ar[115]:
                move = True
                mo_y = 1
            
            if move:
                rtime = time.time()
                update = True
                d_player.move(mo_x, mo_y)
                
        if update:
            game_window.fill(color_table["bg_col"])
            d_player.render()
            p.display.flip()
            update = False
        
    
    p.quit()