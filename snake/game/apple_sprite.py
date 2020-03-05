import random

import pygame as pg

from . import tile
from constants import *


class Apple(tile.Tile):

    def __init__(self):
        tile.Tile.__init__(self)
