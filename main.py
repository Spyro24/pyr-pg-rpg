#! /usr/bin/python3

"""
    main class to run a pyr_pg based rpg
    Copyright (C) 2024 Spyro24

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.
"""

import pygame as p
import os
from pathlib import Path
import subprocess
import pyr_pg
from random import randint
import time

class main_class():
    def __init__(self):
        #----modify this section for your game if you use this runner----
        self.random_title_text = True #Set it to false if you don't want to use a sufix for the tiitle
        self.player_speed = 8
        self.debug = False
        self.object_lenght = 2
        self.micro_tiling = 16
        self.default_FPS = 30
        tilesheet_size = "12x6"
        self.FPS_COUNTER = True
        self.debug_console = True
        self.standard_player_sprite = "blue_cube"
        self.character_path = "./characters/"
        #----------------------------------------------------------------------
        self.main_FPS_count = 0
        self.rendered_FPS_count = 0
        self.debug_colors = {"player_hitbox":(0, 0, 255), "map_hitbox":(0,127,255)}
        self.map_config = {"bg_tiles":pyr_pg.tile_handler.load_tiles("./tiles/ground/", {"size":tilesheet_size}),
                           "gd_tiles":pyr_pg.tile_handler.load_tiles("./tiles/overlay/", {"size":tilesheet_size}),
                           "ov_tiles":pyr_pg.tile_handler.load_tiles("./tiles/p_overlay/", {"size":tilesheet_size}),
                           "debug_col":self.debug_colors}
        self.main_config = {"tiles_xy":(16,16), "player_start_pos_xy":(0,0), "debug_colors":self.debug_colors, "micro_tiling":self.micro_tiling,
                            "character_path":self.character_path, "player_sprite":self.standard_player_sprite}
        self.player_speed = 1 / ((self.main_config["micro_tiling"] * self.player_speed))
        self.platform = os.name
        info = open("./res/main_menu/info_box", "r")
        self.info_text = info.readlines()
        info.close()
        print(self.info_text)
        inf = ""
        for line in self.info_text:
            inf += line
        self.info_text = inf
        print(self.info_text)
        self.game_config = pyr_pg.config.config("./game.rpg")
        self.game_name = self.game_config.get("name")
        self.game_version = self.game_config.get("version")
        print("try to init game: " + self.game_name)
        is_ready = False
        
        
        if self.platform == "posix": # init for a linux system
            #----- This code need some optimisation ----
            self.conf_path = str(Path.home()) + "/.config/pyr-pg/" + self.game_name
            try:
                is_configured = open(self.conf_path + "/CONFIGURED", "r")
                is_ready = True
                is_configured.close()
            except:
                try:
                    test_if_pyr_pg_configured = subprocess.run(["ls", str(Path.home()) + "/.config/pyr-pg/"],stderr=subprocess.PIPE)
                    if test_if_pyr_pg_configured.stderr != b"":
                        print("[Missing the config dir]")
                        subprocess.run(["mkdir", str(Path.home()) + "/.config/pyr-pg/"])
                        print("[config dir created]")
                    subprocess.run(["mkdir", self.conf_path])
                    subprocess.run(["cp","-r","./config/.", self.conf_path])
                    is_configured = open(self.conf_path + "/CONFIGURED", "w")
                    is_configured.close()
                except BaseException as err:
                    print("---Error---")
                    print("cannot configure the game.\nHere the Error: [ " + str(err) + " ]")
                    print("---Error---")
        
        #I have outcomment this section because i have no windows tester
        #elif self.platform == "nt":
        #    self.conf_path = str(os.environ['APPDATA'] + "/config/pyr-pg/" + self.game_name)
        #    if not os.path.exists(self.conf_path):
        #        os.makedirs(self.conf_path)
        
        #general config if you use a generic system
        else:
            #----- You have to use linux in the 0.4 to 1.0
            #but a simple config is here
            #(Please use the next time linux to run the game)
            self.conf_path = "./main_conf"
            
        self.global_config = pyr_pg.config.config(self.conf_path + "/global_config")
        if not is_ready:
            get_wh = p.display.set_mode((0,0))
            w,h = get_wh.get_size()
            self.global_config.add("win_w", w / 1.5)
            self.global_config.add("win_h", h / 1.5)
        self.global_config.save()
        
    
    def play(self):
        self.game_win = p.display.set_mode((int(float(self.global_config.get("win_w"))),int(float(self.global_config.get("win_h")))))
        self.font = pyr_pg.font.font(self.game_win, "./res/fonts/standard")
        self.map_config["window"] = self.game_win
        if self.random_title_text:
            text_list = open("./pyr_pg/random_tittle_texts","r")
            random_line = text_list.readlines() #read every line from the configuration file
            text_list.close() #close the configuration nfile
            random_line = [line.strip() for line in random_line]
            chosen_tiitle = randint(0, len(random_line) - 1)
            p.display.set_caption(self.game_config.get("display_name") + ": " + random_line[chosen_tiitle])
        else:
            p.display.set_caption(self.game_config.get("display_name"))
        pyr_pg.splash(self.game_win, 1.2)
        self.setup_env()
        #This has to be configured after the env--------------
        self.info_box = pyr_pg.infobox.InfoBox(self.game_win, self.font, int(self.menu_size / 2), (self.b_pos_x, self.b_pos_y), (20,20))
        #-----------------------------------------------------
        self.main_menu() #Open the main menu and start the game
        
    def main_menu(self):
        render = True
        run = True
        redraw = True
        #all main menu images
        background = p.transform.scale(p.image.load("./images/main_menu/back.png"),(self.lowest_size,self.lowest_size))
        title = p.transform.scale(p.image.load("./images/main_menu/title.png"),(self.menu_size * 4,self.menu_size * 2))
        settings = p.transform.scale(p.image.load("./images/main_menu/settings.png"),(self.menu_size,self.menu_size))
        start_newg = p.transform.scale(p.image.load("./images/main_menu/new.png"),(self.menu_size*3,self.menu_size))
        continue_g = p.transform.scale(p.image.load("./images/main_menu/load.png"),(self.menu_size*3,self.menu_size))
        info = p.transform.scale(p.image.load("./images/main_menu/info.png"),(self.menu_size,self.menu_size))
        #button rectangles
        set_rect = self.game_win.blit(settings, (self.b_pos_x + (self.menu_size * 9), self.b_pos_y + (self.menu_size *9)))
        load_rect = self.game_win.blit(continue_g, (self.b_pos_x + (self.menu_size * 3.33), self.b_pos_y + (self.menu_size * 8)))
        new_rect = self.game_win.blit(start_newg, (self.b_pos_x + (self.menu_size * 3.33), self.b_pos_y + (self.menu_size * 6.5)))
        info_rect = self.game_win.blit(info, (self.b_pos_x, self.b_pos_y + (self.menu_size * 9)))
        #setup button vars
        start_new_game = False
        while run: #main menu loop
            for event in p.event.get():
                if event.type == p.QUIT:
                    run = False
                    self.close_game()                    
            m_click = p.mouse.get_pressed()
            m_pos = p.mouse.get_pos()            
            if m_click[0]:
                if set_rect.collidepoint(m_pos):
                    print("open settings menu")
                    self.audio_setup.play("sfx_1", "menu_click")
                    self.menu_settings()
                    redraw = True                
                if new_rect.collidepoint(m_pos):
                    self.audio_setup.play("sfx_1", "menu_click")
                    run = False
                    start_new_game = True
                if info_rect.collidepoint(mpos):
                    self.info_box.show(self.info_text)
                    redraw = True
            if redraw:
                self.game_win.blit(background, (self.b_pos_x, self.b_pos_y))
                self.game_win.blit(title, (self.b_pos_x + (self.menu_size * 3), self.b_pos_y + self.menu_size))
                set_rect = self.game_win.blit(settings, (self.b_pos_x + (self.menu_size * 9), self.b_pos_y + (self.menu_size *9)))
                info_rect = self.game_win.blit(info, (self.b_pos_x, self.b_pos_y + (self.menu_size * 9)))
                self.game_win.blit(continue_g, (self.b_pos_x + (self.menu_size * 3.33), self.b_pos_y + (self.menu_size * 8)))
                self.game_win.blit(start_newg, (self.b_pos_x + (self.menu_size * 3.33), self.b_pos_y + (self.menu_size * 6.5)))
                redraw = False
                render = True                
            if render:
                p.display.flip()
                render = False
        if start_new_game:
            self.menu_create_character()
            
    def show_info(self):
        pass
            
    def menu_settings(self):
        render = True
        menu__setting__ = True
        redraw = True
        back_button = p.transform.scale(p.image.load("./images/main_menu/settings/back.png"),(self.menu_size, self.menu_size))
        background = p.transform.scale(p.image.load("./images/main_menu/back.png"),(self.lowest_size,self.lowest_size))
        seting_background = p.transform.scale(p.image.load("./images/main_menu/settings/settings_back.png"),(self.menu_size * 8, self.menu_size * 8))
        #setup rectangle buttons
        back = 0
        while menu__setting__:
            for event in p.event.get():
                if event.type == p.QUIT:
                    menu__setting__ = False
                    self.close_game()            
            m_click = p.mouse.get_pressed()
            m_pos = p.mouse.get_pos()                    
            if redraw:
                self.game_win.blit(background,(self.b_pos_x, self.b_pos_y))
                back = self.game_win.blit(back_button, (self.b_pos_x, self.b_pos_y))
                self.game_win.blit(seting_background,(self.b_pos_x + self.menu_size, self.b_pos_y + self.menu_size))
                if self.debug:
                    pass
                render = True
                redraw = False            
            if render:
                p.display.flip()
                render = False                
            if m_click[0]:
                if back.collidepoint(m_pos):
                    menu__setting__ = False
                    
    def menu_create_character(self):
        menu__create_character__ = True
        render = True
        redraw = True
        back_button = p.transform.scale(p.image.load("./images/main_menu/settings/back.png"),(self.menu_size, self.menu_size))
        background = p.transform.scale(p.image.load("./images/main_menu/back.png"),(self.lowest_size,self.lowest_size))
        arow_left = p.transform.scale(p.image.load("./images/main_menu/char_selector/chose.png"),(self.menu_size,self.menu_size * 2))
        arow_right = p.transform.rotate(arow_left, 180)
        ready = p.transform.scale(p.image.load("./images/main_menu/char_selector/start.png"),(self.menu_size, self.menu_size))
        #setup rectangle buttons
        back = self.game_win.blit(back_button, (self.b_pos_x, self.b_pos_y + (self.menu_size * 9)))
        decrease_char_value = self.game_win.blit(arow_left, (self.b_pos_x, self.b_pos_y + (self.menu_size * 4)))
        start_b = self.game_win.blit(back_button, (self.b_pos_x + (self.menu_size * 9), self.b_pos_y + (self.menu_size * 9)))
        #setup button vars
        back_to_main = False
        start_game = False
        while menu__create_character__:
            for event in p.event.get():
                if event.type == p.QUIT:
                    menu__setting__ = False
                    self.close_game()            
            m_click = p.mouse.get_pressed()
            m_pos = p.mouse.get_pos()            
            if m_click[0]:
                if back.collidepoint(m_pos):
                    back_to_main = True
                    menu__create_character__ = False                
                if start_b.collidepoint(m_pos):
                    start_game = True
                    menu__create_character__ = False                    
            if redraw:
                self.game_win.blit(background,(self.b_pos_x, self.b_pos_y))
                back = self.game_win.blit(back_button, (self.b_pos_x, self.b_pos_y + (self.menu_size * 9)))
                decrease_char_value = self.game_win.blit(arow_left, (self.b_pos_x, self.b_pos_y + (self.menu_size * 4)))
                start_b = self.game_win.blit(back_button, (self.b_pos_x + (self.menu_size * 9), self.b_pos_y + (self.menu_size * 9)))
                render = True
                redraw = False            
            if render:
                p.display.flip()
                render = False
        
        if back_to_main:
            self.main_menu()
        
        if start_game:
            self.setup_player("create")
    
    def setup_player(self, option):
        self.player_env = {"player":"Test", "player_sprite":"synth"}
        self.map_config["window"] = self.game_win
        self.map = pyr_pg.map_.map(self.map_config)
        self.main_config["map"] = self.map
        self.map.load()
        self.dialog = pyr_pg.dialog_.dialog(self.game_win, "./dialog/", "./players/",  self.player_env, self.audio_setup)
        self.player = pyr_pg.player.player(self.game_win, self.main_config)
        self.play_game()
        
    def play_game(self):
        debug_console = self.debug_console
        from time import time as time_get
        FPS_get = time_get()
        FPSmax = 128
        FPS_c = 0
        KT = time_get()
        ms = 0.001
        run = True
        last_frame = time_get()
        while run:
            #---begin of the game loop---
            cur_frame_time = time_get()
            for event in p.event.get():
                if event.type == p.QUIT:
                    run = False            
            key_ar = p.key.get_pressed()            
            '''
            for n in range(0, len(key_ar)):
                if key_ar[n]:
                    print(n)
            '''            
            if (cur_frame_time - self.player_speed) > KT:
                if key_ar[119]:
                    self.player.set_facing("UP")
                    self.player.move(0,-1)
                if key_ar[100]:
                    self.player.set_facing("RIGHT")
                    self.player.move(1,0)              
                if key_ar[115]:
                    self.player.set_facing("DOWN")
                    self.player.move(0,1)
                if key_ar[97]:
                    self.player.set_facing("LEFT")
                    self.player.move(-1,0)
                if self.player.get_state(0):
                    KT = time_get()
                    self.player.reset_state(0)            
            if key_ar[60]:
                if debug_console:
                    console = input(">>> ")
                    console = console.split(" ")
                    print(console)
                    if console[0] == "set":
                        if console[1] == "player":
                            if console[2] == "speed":
                                self.player_speed = 1 / ((self.main_config["micro_tiling"] * float(console[3])))            
            if (cur_frame_time - (1/FPSmax)) > last_frame:
                last_frame = time_get()
                self.game_win.fill((0,0,0))
                self.player.reset_resetable_states()
                self.map.render()
                self.player.render()
                if self.debug:
                    self.player._debug()
                    self.map.debug()
                p.display.flip()
                render_win = False
                self.rendered_FPS_count += 1            
            #---end of game loop---
            self.main_FPS_count += 1 
            if self.FPS_COUNTER:
                if (FPS_get + 1) < cur_frame_time:
                    FPS_get = cur_frame_time
                    print("RFPS: " + str(self.rendered_FPS_count))
                    print(" FPS: " + str(self.main_FPS_count))
                    self.main_FPS_count = 0
                    self.rendered_FPS_count = 0                    
        
    def resume(self, player_save_file):
        pass
    
    def key_config(self):
        self.set_keys = ["UP","DOWN","LEFT","RIGHT"]
    
    def setup_env(self):
        w, h = self.game_win.get_size()
        self.lowest_size = 0
        if w > h:
            self.lowest_size = h
        else:
            self.lowest_size = w
        self.b_pos_x = (w / 2) - (self.lowest_size / 2)
        self.b_pos_y = (h / 2) - (self.lowest_size / 2)
        self.menu_size = self.lowest_size / 10
        self.audio_setup = pyr_pg.sound.sound(self.game_win, "./music/")
                
    def close_game(self):
        p.quit()
        exit(0)
    
    
if __name__ == "__main__":
    runner = "Dev"
    if runner == "User":
        try:
            game = main_class()
            game.play()
        except BaseException as err:
            try:
                import datetime
                log_time = datetime.datetime.now()
            except ImportError as err:
                log_time = err
            
            print("\n\n\n")
            print("-----Fatal Error-----")
            print("Crash Time: " + str(log_time))
            print("Operating System: " + str(os.name))
            print("Game Name: " + str(game.game_name))
            print("Game Version: " + str(game.game_version))
            print("pyr_pg Version: " + str(pyr_pg.version))
            print("Error: " + str(err))
            print("------Error end------")
            print("\nplease report this to the developers if this is not a filepath error")
        p.quit()
    elif runner == "Dev":
        game = main_class()
        game.play()
        p.quit()
    else:
        print("Your are not a valid user for this programm")