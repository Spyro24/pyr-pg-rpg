'''
    Tile map maker
    Copyright (C) 2025 Spyro24

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
'''
import pygame as p

def load_tiles(path, config, *font, mode="new"):
    tmp = config["size"].split("x")
    tmx = int(tmp[0])
    tmy = int(tmp[1])
    draw_font = False
    tile_maps = []
    tiles = []
    tile_maps.append(p.image.load(path))
    
    max_tile_maps = len(tile_maps)
    
    for tmap in range(max_tile_maps):
        cur_tmap = tile_maps[tmap]
        tw, th = cur_tmap.get_size()
        sx, sy = tw / tmx, th / tmy
        for h in range(tmy):
            for w in range(tmx):
                tmp = p.Surface((sy, sy), flags=p.SRCALPHA)
                tmp.blit(cur_tmap,(0,0),(sx * w, sy * h, sx, sy))
                tiles.append(tmp)
    
    return tiles
                

#Unit test of the modul
if __name__ == "__main__":
    pathToTileseSet = input("Input path for the tileset to split")
    sizeXY = input("Tileset size in XTiles x YTiles")
    tileSize = 64
    tileNumber = 0
    sheetNumber = 0
    curSurface = p.Surface((tileSize * 6, tileSize * 12), flags=p.SRCALPHA)
    tileSet = load_tiles(pathToTileseSet, {"size":sizeXY})
    while True:
        try:
            for y in range(12):
                for x in range(6):
                    curSurface.blit(p.transform.scale(tileSet[tileNumber],(tileSize, tileSize)),(x * tileSize, y * tileSize))
                    tileNumber += 1
            p.image.save(curSurface, str(sheetNumber) + ".png")
            curSurface = p.Surface((tileSize * 6, tileSize * 12), flags=p.SRCALPHA)
            sheetNumber += 1
        except IndexError:
            p.image.save(curSurface, str(sheetNumber) + ".png")
            break
    print("Finish. you can now use your tiles in pyr_pg")
