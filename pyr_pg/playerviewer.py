"""
    playerviewer - A Tool to view player files from pyr-pg
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
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
class PlayerDataViewer():
    def __init__(self):
        self.player_data = {"PlayerName":"", "fileversion":"", "Position":[]}
        self.version = "0.0.1"
        
    def run(self):
        print("pyr-pg player save viewer - A Tool to view player files")
        file = input("Path to Player file >>> ")
        self.extract_data(file)
        run = True
        while run:
            self.main_menu()
            
    def main_menu(self):
        print("\n\n\n")
        print("+----Main menu---------+")
        print("| 1) Show basic info   |")
        print("| 2) Exit              |")
        print("+----------------------+")
        chose = input("chose a number (1-2) >>>")
        if chose == "1":
            self.basic_info()
        elif chose == "2":
            exit(0)
        else:
            print("This Number is not valid")
    
    def basic_info(self):
        print("\n\n\n")
        print("+----Player Info---->")
        print("| Player name : " + self.player_data['PlayerName'])
        print("| File version: " + self.player_data['fileversion'])
        print("+------------------->")
        input("press [Enter]") 
        
    
    def extract_data(self, file):
        version = ""
        data = open(file, "br")
        for n in range(3):
            version += str(int.from_bytes(data.read(1), "little"))
            if n == 2:
                break
            version += "."
        self.player_data['fileversion'] = version
        player_name = ""
        while True:
            byte = data.read(1)
            if int.from_bytes(byte, "little") == 255:
                break
            else:
                player_name += byte.decode("UTF8")
        self.player_data['PlayerName'] = player_name
        position = []
        for n in range(6):
            cur_pos = ""
            while True:
                byte = data.read(1)
                if int.from_bytes(byte, "little") == 255:
                    position.append(int(cur_pos))
                    break
                else:
                    cur_pos += byte.decode("UTF8")
        self.player_data['Position'] = position
        

if __name__ == "__main__":
    PlayerDataViewer().run()
else:
    raise BaseException()