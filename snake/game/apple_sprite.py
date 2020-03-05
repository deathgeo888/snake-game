import random

import pygame as pg

from . import tile
from constants import *


class Apple(tile.Tile):

    def __init__(self):
        tile.Tile.__init__(self)

        self.apple_tile = pg.Surface((self.size, self.size))
        self.apple_tile.fill(APPLE_COLOR)
        self.apple_rect = self.apple_tile.get_rect()

        self.place_apple()


    def move_apple(self, pos):
        self.apple_rect.x = pos[0]
        self.apple_rect.y = pos[1]

    def place_apple(self):
        while True:
            x = random.randint(0, self.screen_size[0])
            y = random.randint(0, self.screen_size[1])

            x = x - x % self.size
            y = y - y % self.size

            self.move_apple((x, y))

            if self.check_color(self.apple_rect, BLACK):
                self.screen.blit(self.apple_tile, self.apple_rect)
                return [self.apple_rect]
