#! /usr/bin/python3

"""
    main class to run a pyr_pg based rpg
    Copyright (C) 2024-2025 Spyro24

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

from random import randint
import subprocess
import os
from pathlib import Path
import pygame as p
import pyr_pg
#import time
import runtime_store as rs
import modding

class main_class():
    def __init__(self, LogSystem=print, debug=False):
        self.runtimeStore = {}
        self.cache        = {}
        self.modSupport   = modding.mod(self.runtimeStore)
        #----modify this section for your game if you use this runner----
        self.runtimeStore[rs.PlayerSpeed]  = 8
        self.runtimeStore[rs.DefaultFps]   = 60
        self.runtimeStore[rs.LogSystem]    = LogSystem
        #----------------------------------------------------------------
        self.autoSave                       = False
        self.runtimeStore[rs.PlayerName]    = "Default"
        self.random_title_text              = True #Set it to false if you don't want to use a sufix for the tiitle
        self.player_speed                   = self.runtimeStore[rs.PlayerSpeed]
        self.debug                          = debug
        self.runtimeStore[rs.MicroTiling]   = 16
        self.default_FPS                    = 30
        self.runtimeStore[rs.TileSheetSize] = "6x12"
        self.fpsCounter                     = True
        self.debug_console                  = True
        self.standard_player_sprite         = "blue_cube"
        self.character_path                 = "./res/characters/"
        self.main_FPS_count                 = 0
        self.rendered_FPS_count             = 0
        self.global_config = {"pg_window":None,
                              "options"  :None}
        self.debug_colors  = {"player_hitbox":(0, 0, 255),
                              "map_hitbox":(0,127,255)}
        self.map_config    = {"bg_tiles":pyr_pg.tile_handler.load_tiles("./tiles/ground/",    {"size":self.runtimeStore[rs.TileSheetSize]}),
                              "gd_tiles":pyr_pg.tile_handler.load_tiles("./tiles/overlay/",   {"size":self.runtimeStore[rs.TileSheetSize]}),
                              "ov_tiles":pyr_pg.tile_handler.load_tiles("./tiles/p_overlay/", {"size":self.runtimeStore[rs.TileSheetSize]}),
                              "debug_col":self.debug_colors}
        self.main_config   = {"tiles_xy":(16,16),
                              "player_start_pos_xy":(0,0),
                              "debug_colors":self.debug_colors,
                              "micro_tiling":self.runtimeStore[rs.MicroTiling],
                              "character_path":self.character_path,
                              "player_sprite":self.standard_player_sprite}
        self.player_speed = 1 / ((self.main_config["micro_tiling"] * self.player_speed))
        self.platform     = os.name
        info              = open("./res/main_menu/info_box", "r")
        self.info_text    = info.readlines(); info.close()
        inf               = ""
        for line in self.info_text:
            inf += line
        self.info_text    = inf
        self.game_config  = pyr_pg.config.config("./game.rpg")
        self.game_name    = self.game_config.get("name")
        self.game_version = self.game_config.get("version")
        self.NPCs         = []
        is_ready          = False
        print("try to init game: " + self.game_name)
        print("[PYR-PG][Info] version " + pyr_pg.version)
        print(self.info_text)
        self.conf_path = p.system.get_pref_path("pyr-pg","makend")
        try:
            is_configured = open(self.conf_path + "/CONFIGURED", "r")
            is_ready = True
            is_configured.close()
        except:
            try:
                is_configured = open(self.conf_path + "/CONFIGURED", "w")
                is_configured.close()
            except BaseException as err:
                print("---Error---")
                print("cannot configure the game.\nHere the Error: [ " + str(err) + " ]")
                print("---Error---")
        self.global_config_file = pyr_pg.config.config(self.conf_path + "/global_config")
        if not is_ready:
            get_wh = p.display.set_mode((0,0))
            w,h = get_wh.get_size()
            self.global_config_file.add("win_w", w / 1.5)
            self.global_config_file.add("win_h", h / 1.5)
        self.global_config_file.save()
        self.modSupport._on_ready()
        self.setupBeforeStartup()
         #---Setup Menu Objects---
        self.playerCharacterSelector = pyr_pg.characterSelector.characterSelector("./res/characters", self.runtimeStore, debug=debug)
        #------------------------
    
    def setupBeforeStartup(self) -> None:
        self.runtimeStore[rs.WindowProperties]            = {}
        self.runtimeStore[rs.WindowProperties][rs.Window] = p.display.set_mode((int(float(self.global_config_file.get("win_w"))),int(float(self.global_config_file.get("win_h")))))
        self.runtimeStore[rs.FontSystem]    = pyr_pg.font.font(self.runtimeStore[rs.WindowProperties][rs.Window], "./res/fonts/standard")
        
    def loadInCacheOnStartup(self) -> None:
        pass
    
    def play(self):
        self.game_win             = self.runtimeStore[rs.WindowProperties][rs.Window]
        self.font                 = self.runtimeStore[rs.FontSystem]
        self.map_config["window"] = self.game_win
        if self.random_title_text:
            text_list     = open("./pyr_pg/random_tittle_texts","r")
            random_line   = text_list.readlines() #read every line from the random tiltle text file
            random_line   = [line.strip() for line in random_line]
            chosen_tiitle = randint(0, len(random_line) - 1)
            text_list.close() #close the configuration nfile
            p.display.set_caption(self.game_config.get("display_name") + ": " + random_line[chosen_tiitle])
        else:
            p.display.set_caption(self.game_config.get("display_name"))
        pyr_pg.splash(self.game_win, 1.2)
        self.setup_env()
        #---Export important vars to self.global_config---
        self.global_config["pg_window"] = self.game_win
        self.global_config["font"]      = self.font
        #-------------------------------------------------
        #This has to be configured after the env--------------
        self.info_box = pyr_pg.infobox.InfoBox(self.game_win, self.font, int(self.menuSize / 2), (self.b_pos_x, self.b_pos_y), (20,20))
        self.options  = pyr_pg.options_menu.options_menu(self.global_config)
        self.options.create("./res/menus/options_menu.png")
        #-----------------------------------------------------
        #---Export all other important vars to self.global_config---
        self.global_config['options']   = self.options
        #-----------------------------------------------------
        self.cacheImages()
        self.main_menu() #Open the main menu and start the game
    
    def cacheImages(self) -> None:
        self.cache["mainMenu"]       = {}
        self.cache["mainMenu"]["bg"] = p.image.load("./images/main_menu/back.png")
    
    def main_menu(self) -> None:
        render = True
        run = True
        redraw = True
        #all main menu images
        background = p.transform.scale(self.cache["mainMenu"]["bg"],(self.lowestSize,self.lowestSize))
        title      = p.transform.scale(p.image.load("./images/main_menu/title.png"),(self.menuSize * 4,self.menuSize * 2))
        settings   = p.transform.scale(p.image.load("./images/main_menu/settings.png"),(self.menuSize,self.menuSize))
        start_newg = p.transform.scale(p.image.load("./images/main_menu/new.png"),(self.menuSize*3,self.menuSize))
        continue_g = p.transform.scale(p.image.load("./images/main_menu/load.png"),(self.menuSize*3,self.menuSize))
        info       = p.transform.scale(p.image.load("./images/main_menu/info.png"),(self.menuSize,self.menuSize))
        #button rectangles
        set_rect  = self.game_win.blit(settings, (self.b_pos_x + (self.menuSize * 9), self.b_pos_y + (self.menuSize *9)))
        load_rect = self.game_win.blit(continue_g, (self.b_pos_x + (self.menuSize * 3.33), self.b_pos_y + (self.menuSize * 8)))
        new_rect  = self.game_win.blit(start_newg, (self.b_pos_x + (self.menuSize * 3.33), self.b_pos_y + (self.menuSize * 6.5)))
        info_rect = self.game_win.blit(info, (self.b_pos_x, self.b_pos_y + (self.menuSize * 9)))
        #setup button vars
        start_new_game = False
        while run: #main menu loop
            for event in p.event.get():
                if event.type == p.QUIT:
                    run = False
                    self.close_game()
                if event.type == p.MOUSEBUTTONDOWN:
                    m_click = p.mouse.get_pressed()
                    m_pos = p.mouse.get_pos()            
                    if m_click[0]:
                        if set_rect.collidepoint(m_pos):
                            print("open settings menu")
                            self.audioSetup.play("sfx_1", "menu_click")
                            self.menu_settings()
                            redraw = True                
                        if new_rect.collidepoint(m_pos):
                            self.audioSetup.play("sfx_1", "menu_click")
                            run = False
                            start_new_game = True
                        if info_rect.collidepoint(m_pos):
                            self.info_box.show(self.info_text)
                            redraw = True
            if redraw:
                self.game_win.blit(background, (self.b_pos_x, self.b_pos_y))
                self.game_win.blit(title, (self.b_pos_x + (self.menuSize * 3), self.b_pos_y + self.menuSize))
                set_rect = self.game_win.blit(settings, (self.b_pos_x + (self.menuSize * 9), self.b_pos_y + (self.menuSize *9)))
                info_rect = self.game_win.blit(info, (self.b_pos_x, self.b_pos_y + (self.menuSize * 9)))
                self.game_win.blit(continue_g, (self.b_pos_x + (self.menuSize * 3.33), self.b_pos_y + (self.menuSize * 8)))
                self.game_win.blit(start_newg, (self.b_pos_x + (self.menuSize * 3.33), self.b_pos_y + (self.menuSize * 6.5)))
                redraw = False
                render = True                
            if render:
                p.display.flip()
                render = False
        if start_new_game:
            self.menu_create_character()
    
    def menu_settings(self):
        render = True
        menu__setting__ = True
        redraw = True
        back_button = p.transform.scale(p.image.load("./images/main_menu/settings/back.png"),(self.menuSize, self.menuSize))
        background = p.transform.scale(p.image.load("./images/main_menu/back.png"),(self.lowestSize,self.lowestSize))
        seting_background = p.transform.scale(p.image.load("./images/main_menu/settings/settings_back.png"),(self.menuSize * 8, self.menuSize * 8))
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
                self.game_win.blit(seting_background,(self.b_pos_x + self.menuSize, self.b_pos_y + self.menuSize))
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
        back_button = p.transform.scale(p.image.load("./images/main_menu/settings/back.png"),(self.menuSize, self.menuSize))
        background  = p.transform.scale(p.image.load("./images/main_menu/back.png"),(self.lowestSize,self.lowestSize))
        arow_left   = p.image.load("./images/main_menu/char_selector/chose.png")
        arow_right  = p.transform.rotate(arow_left, 180)
        ready  = p.transform.scale(p.image.load("./images/main_menu/char_selector/start.png"),(self.menuSize, self.menuSize))
        #setup rectangle buttons
        back = self.game_win.blit(back_button, (self.b_pos_x, self.b_pos_y + (self.menuSize * 9)))
        decrease_char_value = self.game_win.blit(arow_left, (self.b_pos_x, self.b_pos_y + (self.menuSize * 4)))
        start_b = self.game_win.blit(back_button, (self.b_pos_x + (self.menuSize * 9), self.b_pos_y + (self.menuSize * 9)))
        #setup button vars
        chosenPlayer = self.playerCharacterSelector.openSelector({"bg": background, "forward": p.image.load("./images/main_menu/char_selector/start.png"), "back": arow_left})
        
        if chosenPlayer[2]:
            self.close_game()
        if not chosenPlayer[1]:
            self.main_menu()
        else:
            self.setup_player([chosenPlayer[0]])
    
    def setup_player(self, option):
        self.player_env           = {"player":"Test", "player_sprite":option[0]}
        self.main_config['player_sprite'] = self.player_env['player_sprite']
        self.map_config["window"] = self.game_win
        self.map                  = pyr_pg.map_.map(self.map_config)
        self.main_config["map"]   = self.map
        self.dialog               = pyr_pg.DialogHandler.DialogScript(self.runtimeStore)
        self.player               = pyr_pg.player.player(self.game_win, self.main_config)
        self.map.load()
        self.play_game()
        
    def play_game(self):
        mb_pressed = False
        debug_console = self.debug_console
        from time import time as time_get
        FPS_get = time_get()
        FPSmax = self.runtimeStore[rs.DefaultFps]
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
            if (cur_frame_time - self.player_speed) > KT:
                if key_ar[p.K_w]:
                    self.player.set_facing("UP")
                    self.player.move(0,-1)
                if key_ar[p.K_d]:
                    self.player.set_facing("RIGHT")
                    self.player.move(1,0)              
                if key_ar[p.K_s]:
                    self.player.set_facing("DOWN")
                    self.player.move(0,1)
                if key_ar[p.K_a]:
                    self.player.set_facing("LEFT")
                    self.player.move(-1,0)
                if self.player.get_state(0):
                    KT = time_get()
                    self.player.reset_state(0)
            #put here the DEV menu code
            if key_ar[p.K_ESCAPE]:
                if not mb_pressed:
                    self.options.open()
                mb_pressed = True
            else:
                mb_pressed = False
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
            if self.fpsCounter:
                if (FPS_get + 1) < cur_frame_time:
                    FPS_get = cur_frame_time
                    print("FPS:", self.main_FPS_count, "RFPS:",self.rendered_FPS_count)
                    self.main_FPS_count = 0
                    self.rendered_FPS_count = 0                    
        
    def resume(self, player_save_file):
        pass
    
    def key_config(self):
        self.set_keys = ["UP","DOWN","LEFT","RIGHT"]
    
    def setup_env(self):
        w, h = self.game_win.get_size()
        self.lowestSize = w
        if w > h: self.lowestSize = h
        self.b_pos_x = (w / 2) - (self.lowestSize / 2)
        self.b_pos_y = (h / 2) - (self.lowestSize / 2)
        self.menuSize   = self.lowestSize / 10
        self.audioSetup = pyr_pg.sound.sound(self.game_win, "./res/music/")
                
    def close_game(self) -> None:
        p.quit()
    
    
if __name__ == "__main__":
    logsys = pyr_pg.log_system.log()
    runner = "User"
    if runner == "User":
        try:
            game = main_class(LogSystem=logsys.insert)
            game.play()
        except BaseException as err:
            try:
                import datetime
                log_time = datetime.datetime.now()
            except ImportError as errTime:
                log_time = errTime
            
            log = game.runtimeStore[rs.LogSystem]
            log(1, "-----Fatal Error-----",
                   "Crash Time: "       + str(log_time),
                   "Operating System: " + str(os.name),
                   "Game Name: "        + str(game.game_name),
                   "Game Version: "     + str(game.game_version),
                   "pyr_pg Version: "   + str(pyr_pg.version),
                   "Error: "            + str(err),
                   "------Error end------",
                   "\nplease report this to the developers if this is not a filepath error")
            logsys.WriteLog(path="./logs/")
        p.quit()
    elif runner == "Dev":
        game = main_class(debug=True)
        game.play()
        p.quit()
    else:
        print("Your are not a valid user for this programm")