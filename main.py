import pygame as pg
from world import *
from sprites import *

class Game():
    def __init__(self, winWidth, winHeight):
        self._init_pygame()
        self.window = pg.display.set_mode((winWidth, winHeight))
        self.map = map(0, winWidth, winHeight)
        self.clock = pg.time.Clock()
        self.player = player(100, 100)
        self.winWidth = winWidth
        self.winHeight = winHeight

    def main_loop(self):
        while True:
            self.clock.tick(60)
            self.handle_input()
            self.process_game_logic()
            self.draw()

    def draw(self):
        self.map.draw(self.window, self.winHeight, self.winWidth)
        self.player.draw(self.window)
        
        pg.display.update()

    def handle_input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()

        keys = pg.key.get_pressed()  # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.

        if keys[pg.K_LEFT] and self.player.x > 0: # We can check if a key is pressed like this
            self.player.x -= self.player.vel
        if keys[pg.K_RIGHT] and self.player.x < self.winWidth:
            self.player.x += self.player.vel
        if keys[pg.K_UP] and self.player.y > 0: # We can check if a key is pressed like this
            self.player.y -= self.player.vel
        if keys[pg.K_DOWN] and self.player.y < self.winHeight:
            self.player.y += self.player.vel

        if keys[pg.K_SPACE]:
            self.map.interact_with_tile(self.player.x, self.player.y, self.winHeight, self.winWidth)


    def _init_pygame(self):
        pg.init()
        pg.display.set_caption("Stardew")

    def process_game_logic(self):
        pass


if __name__ == "__main__":
    winWidth, winHeight = 560, 352
    game_instance = Game(winWidth, winHeight)
    game_instance.main_loop()