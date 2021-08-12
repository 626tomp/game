import pygame as pg
import numpy as np

# map tiles
EMPTY_TILE = 0
FARM_TILE = 1
WORKED_TILE = 2
WALL_TILE = 3


WORKED_TILE_IMAGE = pg.transform.scale(pg.image.load('assets/images/workedTile.png'), (int(560/35), int(352/22)))
FARM_TILE_IMAGE = pg.transform.scale(pg.image.load('assets/images/farmTile.png'), (int(560/35), int(352/22)))
WALL_TILE_IMAGE = pg.transform.scale(pg.image.load('assets/images/boulder.png'), (int(560/35), int(352/22)))

class map():
    def __init__(self, mapIndex, winWidth, winHeight):
        self.index = mapIndex
        self.grid = mapList[mapIndex]['grid']
        self.file = mapList[mapIndex]['image']
        self.image = pg.image.load(self.file)
        self.height = mapList[mapIndex]['height']
        self.width = mapList[mapIndex]['width']
        self.name = mapList[mapIndex]['name']
        self.tileWidth = winWidth / self.width
        self.tileHeight = winHeight / self.height
    
    def draw(self, window, winHeight, winWidth):
        window.blit(self.image, (0,0))

        # render worked tiles
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                if self.grid[x][y] == 2:
                    x_coord = self.tileWidth * x
                    y_coord = self.tileHeight * y
                    window.blit(WORKED_TILE_IMAGE, (x_coord, y_coord))
                if self.grid[x][y] == 1:
                    x_coord = self.tileWidth * x
                    y_coord = self.tileHeight * y
                    window.blit(FARM_TILE_IMAGE, (x_coord, y_coord))
                if self.grid[x][y] == 3:
                    x_coord = self.tileWidth * x
                    y_coord = self.tileHeight * y
                    window.blit(WALL_TILE_IMAGE, (x_coord, y_coord))

    def interact_with_tile(self, playerX, playerY, winHeight, winWidth):
        gridX = int((playerX / winWidth ) * self.width)
        gridY = int((playerY / winHeight) * self.height)

        if gridX == 35:
            gridX -= 1
        if gridY == 22:
            gridY -=1

        if self.grid[gridX][gridY] == 1:
            self.grid[gridX][gridY] = 2


farmGrid = np.ones((35, 22))

for x in range(17, 35):
    for y in range(0, 9):
        farmGrid[x][y] = 0
    
farmGrid[0,:] = 3
farmGrid[:,0] = 3
farmGrid[34,:] = 3
farmGrid[:,21] = 3

print(farmGrid.transpose())
print(farmGrid[34][0])

mapList = [{'name' : 'farm', 'image' : 'assets/images/farm.jpg', 'height' : 22, 'width' : 35, 'grid' : farmGrid}]