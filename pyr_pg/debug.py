import pygame as p

class debug():
    def __init__(self, game_win, player, map_, fs):
        self.gw = game_win
        self.player = player
        self.map_ = map_
        self.fs= fs
        self.font = p.font.SysFont(p.font.get_default_font(),int(fs))
        self.colors = [(255,255,255),(0,0,255),(0,255,0)]
        
    def render(self):
        pi = self.player._debug()
        self.gw.blit(self.font.render("Player pos", False, self.colors[0]),(3,0))
        self.gw.blit(self.font.render("X=" + str(pi[1]), False, self.colors[1]),(3, self.fs))
        self.gw.blit(self.font.render("  A=" + str(pi[3]), False, self.colors[1]),(self.fs * 1.3, self.fs))
        self.gw.blit(self.font.render("Y=" + str(pi[2]), False, self.colors[2]),(3, self.fs * 2))
        self.gw.blit(self.font.render("  A=" + str(pi[4]), False, self.colors[2]),(self.fs * 1.3, self.fs * 2))