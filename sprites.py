import pygame as pg

class player():
    def __init__(self, x, y):
        self.width = 20
        self.height = 40
        self.image = pg.transform.scale(pg.image.load('assets/images/player.png'), (self.width,self.height))
        self.x = x
        self.y = y
        self.vel = 3
    
    def draw(self, window):
        window.blit(self.image, (self.x - (self.width / 2), self.y - self.height))