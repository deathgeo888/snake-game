import pygame as pg
from constants import *


def createWindow(width=800, height=600):
    """Initialize the main window and fill it with black"""

    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("The Classic Snake Game!")

    background = pg.Surface(screen.get_size())
    background.convert()
    background.fill(BLACK)

    return screen
