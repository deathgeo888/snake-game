import pygame as pg

from constants import *


class Tile(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.screen = pg.display.get_surface()
        self.screen_size = self.screen.get_size()

        self.background = pg.Surface((TILE_SIZE, TILE_SIZE))
        self.background.fill(BLACK)
