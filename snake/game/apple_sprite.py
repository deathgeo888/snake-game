import random

import pygame as pg

from . import tile
from constants import *


class Apple(tile.Tile):

    def __init__(self):
        tile.Tile.__init__(self)

        self.screen = pg.display.get_surface()
        self.screen_size = self.screen.get_size()

        self.apple_tile = pg.Surface()
        self.apple_tile.fill(APPLE_COLOR)

        self.background = pg.Surface()
