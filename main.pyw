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

import pygame as p
import manor
import pyr_pg
import runtime_store as rs
import modding

from random import randint
import os
import sys
#import time

if __name__ == "__main__":
    logsys = pyr_pg.log_system.log()
    runner = "User"
    if sys.argv.__contains__("-d"):
        runner = "Dev"
        logsys.printOut = True
    if runner == "User":
        try:
            manor.start(log=logsys.insert)
            p.quit()
        except BaseException as err:
            try:
                import datetime
                log_time = datetime.datetime.now()
            except ImportError as errTime:
                log_time = errTime
            log = game.runtimeStore[rs.LogSystem]
            log(1, "-----Fatal Error-----",
                   f"Crash Time: {str(log_time)}",
                   f"Operating System: {str(os.name)}",
                   f"Game Name: {str(game.game_name)}",
                   f"Game Version: {str(game.game_version)}",
                   f"pyr_pg Version: {str(pyr_pg.version)}",
                   f"Error: {str(err)}",
                   f"------Error end------",
                   "\nplease report this to the developers if this is not a filepath error")
            logsys.WriteLog(path="./logs/")
        p.quit()
        sys.exit(1)
    elif runner == "Dev":
        manor.start(log=logsys.insert, entry="main_game")
        p.quit()
    else:
        print("Your are not a valid user for this programm")