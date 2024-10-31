import pygame as p

class font():
    def __init__(self, game_win, font_png, font_color="white", font_table=[]):
        self.game_win = game_win
        self.font_table = {"w_and_h":(13,10), "space": 0.5, "A":(0, 0), "B":(1, 0), "C":(2, 0), "D":(3, 0), "E":(4, 0),
                           "F":(5, 0), "G":(6, 0), "H":(7, 0), "I":(8, 0), "J":(9, 0), "K":(10, 0), "L":(11, 0),
                           "M":(12, 0), "N":(0, 1), "O":(1, 1), "P":(2, 1), "Q":(3, 1), "R":(4, 1), "S":(5, 1),
                           "T":(6, 1), "U":(7, 1), "V":(8, 1), "W":(9, 1), "X":(10, 1), "Y":(11, 1), "Z":(12, 1),
                           "a":(0, 2), "b":(1, 2), "c":(2, 2), "d":(3, 2), "e":(4, 2), "f":(5, 2), "g":(6, 2), "h":(7, 2),
                           "i":(8, 2), "j":(9, 2), "k":(10, 2), "l":(11, 2), "m":(12, 2), "n":(0, 3), "o":(1, 3),
                           "p":(2, 3), "q":(3, 3), "r":(4, 3), "s":(5, 3), "t":(6, 3), "u":(7, 3), "v":(8, 3), "w":(9, 3),
                           "x":(10, 3), "y":(11, 3), "z":(12,3), "1":(0,5), "line_spacing":1} #The table with the positions of the letters
        
        self.spacing = {"A":(1, 0, 2, 0), "B":(1, 0, 2, 0), "C":(1, 0, 2, 0), "D":(1, 0, 2, 0), "E":(1, 0, 2, 0), "F":(1, 0, 2, 0),
                        "G":(1, 0, 1, 0), "H":(1, 0, 2, 0), "I":(2, 0,-1, 0), "J":(1, 0, 0, 0), "K":(1, 0, 0, 0), "L":(1, 0, 2, 0),
                        "M":(0, 0, 1, 0), "N":(0, 0, 1, 0), "O":(1, 0, 0, 0), "P":(1, 0, 0, 0), "Q":(0, 0, 1, 0), "R":(1, 0, 0, 0),
                        "S":(1, 0, 0, 0), "T":(1, 0, 0, 0), "U":(1, 0, 0, 0), "V":(1, 0, 0, 0), "W":(0, 0, 1, 0), "X":(1, 0, 0, 0),
                        "Y":(1, 0, 0, 0), "Z":(1, 0, 0, 0), "a":(1, 0, 1, 0), "b":(1, 0, 0, 0), "c":(1, 0, 0, 0), "d":(1, 0, 0, 0),
                        "e":(1, 0, 0, 0), "f":(1, 0, -1, 0), "g":(1, 0, 0, 0), "h":(1, 0, 0, 0), "i":(2, 0, -1, 0), "j":(1, 0, 0, 0),
                        "k":(1, 0, 0, 0), "l":(2, 0, 0, 0), "m":(0, 0, 0, 0), "n":(1, 0, 0, 0), "o":(1, 0, 0, 0), "p":(1, 0, 0, 0),
                        "q":(1, 0, 0, 0), "r":(1, 0, 0, 0), "s":(1, 0, 0, 0), "t":(2, 0, 1, 0), "u":(1, 0, 0, 0), "v":(1, 0, 0, 0),
                        "w":(0, 0, 1, 0), "x":(1, 0, 0, 0), "y":(2, 0, 2, 0), "z":(1, 0, 0, 0), "1":(1,0,2,0)} 
        
        if len(font_table) > 0:
            self.font_table = font_table[0]
        self.font_w, self.font_h = self.font_table["w_and_h"]
        self.font_img = p.image.load(font_png +"_"+font_color+".png")
        self.w, self.h = self.font_img.get_size()
        self.ts = self.w / self.font_w
        print(self.ts)
        
    def draw(self, string, size, dest):
        string_lenght = len(string)
        count_x = 0 #the counter for the letters to move the courser
        count_y = 0 #the line counter (not in use in this version)
        spacing = 0
        part_string = string.split("\n")
        lines = len(part_string)
        string_surface = p.Surface((string_lenght * self.ts, (self.ts)), flags=p.SRCALPHA)
        for letter in string:
            if letter == " ":
                spacing += int(self.ts * self.font_table["space"]) - self.ts
            else:
                source = self.font_table[letter]
                spacing -= self.spacing[letter][0]
                string_surface.blit(self.font_img, (count_x * self.ts + spacing,0), area=p.Rect((source[0] * self.ts, source[1] * self.ts),(self.ts, self.ts)))
                spacing -= self.spacing[letter][2] - 1
            count_x += 1
        self.game_win.blit(p.transform.scale(string_surface, (string_lenght * size, size)), dest)
        

if __name__ == "__main__":
    _test_win = p.display.set_mode((700,700))
    _test_font = font(_test_win, "./res/fonts/standard")
    _test_font.draw("Layer 1", 20, (5,5))
    p.display.flip()