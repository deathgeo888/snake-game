import pygame as pg

from constants import *


class Tile(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.screen = pg.display.get_surface()
        self.screen_size = self.screen.get_size()

        self.size = TILE_SIZE

        self.background = pg.Surface((self.size, self.size))
        self.background.fill(BLACK)


    def check_color(self, rect, tile_color):
        pixel = rect.center
        color = self.screen.get_at(pixel)

        if color == tile_color:
            return True

        return False
