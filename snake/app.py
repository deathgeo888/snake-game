import sys

import pygame as pg
from pygame.locals import *

from display import window
from game import snake_sprite, apple_sprite
from constants import *

pg.init()


def run():
    screen= window.createWindow()
    clock = pg.time.Clock()

    snake = snake_sprite.Snake()
    apple = apple_sprite.Apple()

    pg.display.flip()

    while True:
        clock.tick(15)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    sys.exit()

                elif event.key >= pg.K_UP and event.key <= pg.K_LEFT:
                    snake.change_dir(event.key)

                break

        snake_updates = snake.update()
        ate = snake_updates.pop(0)

        apple_rect = []
        if ate:
            apple_rect = apple.place_apple()

        pg.display.update(snake_updates + apple_rect)
