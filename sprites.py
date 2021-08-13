import pygame as pg

class player():
    def __init__(self, x, y):
        self.width = 20
        self.height = 40
        self.image = pg.transform.scale(pg.image.load('assets/images/playerPos.png'), (16,16))
        self.x = x
        self.y = y
        self.vel = 3
    
    def draw(self, window):
        window.blit(self.image, (self.x - 8, self.y - 8))

    def move(self, x_change, y_change):
        self.x += x_change
        self.y += y_change