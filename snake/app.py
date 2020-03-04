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
        ate = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit(0)

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_h:
                    ate = True

                elif event.key >= pg.K_UP and event.key <= pg.K_LEFT:
                    snake.change_dir(event.key)
                break

        snake_updates = snake.update(ate)
        pg.display.update(snake_updates)
        pg.time.delay(500)
