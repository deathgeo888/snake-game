import sys

import pygame as pg
from pygame.locals import *

from display import window
from game import snake_object
from constants import *

pg.init()


def run():
    screen= window.createWindow()

    snake = snake_object.Snake()
    pg.display.flip()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit(0)

        snake_updates = snake.update()
        pg.display.update(snake_updates)
        pg.time.delay(500)
