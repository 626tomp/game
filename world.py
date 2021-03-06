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
        self.winHeight = winHeight
        self.winWidth = winWidth

    
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
        gridX, gridY = self.convert_coord_to_tile(playerX, playerY)
        if gridX == 35:
            gridX -= 1
        if gridY == 22:
            gridY -=1
        # the bottom and right edges are actually part of the previous tile. 
        # need to push it back so we dont get an index error
        print ("Youre on tile: ", gridX, gridY)
        print ("it is of type: ", self.grid[gridX][gridY])
        

        if self.grid[gridX][gridY] == 1:
            self.grid[gridX][gridY] = 2
        
    def get_tile_type(self, x, y):
        gridX, gridY = self.convert_coord_to_tile(x, y)

        return self.grid[gridX][gridY] 

    def convert_coord_to_tile(self, x, y):
        gridX = int((x / self.winWidth ) * self.width)
        gridY = int((y / self.winWidth) * self.height)

        return gridX, gridY

    # takes a sprite, checks whether its requested move is valid
    # moves the sprite if it is valid
    def move_sprite(self, sprite, x_change, y_change):
        tile_type = self.get_tile_type(sprite.x + x_change, sprite.y + y_change)
        # move sprite
        if tile_type != 3:
            sprite.move(x_change, y_change)

farmGrid = np.ones((35, 22))

for x in range(17, 35):
    for y in range(0, 9):
        farmGrid[x][y] = 0
    
farmGrid[0,:] = 3
farmGrid[:,0] = 3
farmGrid[34,:] = 3
farmGrid[:,21] = 3
farmGrid[18:22,7] = 3
farmGrid[25:27,7] = 3
farmGrid[18:27,2:7] = 3 # house

print(farmGrid.transpose())
print(farmGrid[34][0])

mapList = [{'name' : 'farm', 'image' : 'assets/images/farm.jpg', 'height' : 22, 'width' : 35, 'grid' : farmGrid}]