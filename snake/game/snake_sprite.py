import math
import sys

import pygame as pg
from pygame.locals import *

from . import tile
from constants import *


class Snake(tile.Tile):

    def __init__(self):
        tile.Tile.__init__(self)

        self.snake_size = 3 # Size of the whole snake (number of parts)

        self.speed = (0, self.size) # The direction of the snake
        self.speed_tail = self.speed # The direction of the tail

        self.edges = [] # Each time the snake steers we will append the rect where the change happened and save the way of the direction the tail must have

        self.snake_tile = pg.Surface((self.size, self.size))
        self.snake_tile.fill(SNAKE_COLOR)
        self.head_rect = self.snake_tile.get_rect()

        posx, posy = (self.screen_size[0] / 2) - (self.screen_size[0] % self.size), (self.screen_size[1] / 4) - (self.screen_size[1] % self.size)
        self.head_rect.x = posx
        self.head_rect.y = posy
        self.tail_rect = self.head_rect.copy()

        self.screen.blit(self.snake_tile, self.head_rect)

        for i in range(2):
            self.move_rect(self.head_rect, self.speed)
            self.screen.blit(self.snake_tile, self.head_rect)


    def update(self):
        self.move_rect(self.head_rect, self.speed)

        if self.check_color(self.head_rect, SNAKE_COLOR):
            print("You lost!")
            sys.exit()

        ate = self.check_color(self.head_rect, APPLE_COLOR)

        self.screen.blit(self.snake_tile, self.head_rect)

        if not ate:
            prev_tail = self.tail_rect.copy()
            self.screen.blit(self.background, prev_tail)

            if self.edges:
                if prev_tail == self.edges[0][0]:
                    self.speed_tail = self.edges[0][1]
                    self.edges.pop(0)

            self.move_rect(self.tail_rect, self.speed_tail)

        else:
            prev_tail = None
            self.snake_size += 1

        return [ate, prev_tail, self.head_rect]

    def move_rect(self, rect, vector):
        hit = self.hit_boundaries(rect, vector)

        if hit == False:
            rect.x += vector[0]
            rect.y += vector[1]

        else:
            if vector[0] > 0: # Going right
                rect.x = 0

            elif vector[0] < 0: # Going left
                rect.x = self.screen_size[0] - self.size

            elif vector[1] > 0: # Going up
                rect.y = 0

            else: # Going down
                rect.y = self.screen_size[1] - self.size

    def hit_boundaries(self, rect, vector):
        if (rect.x >= (self.screen_size[0] - self.size) and vector[0] > 0) or (rect.x < self.size and vector[0] < 0):
            return True

        if (rect.y >= (self.screen_size[1] - self.size) and vector[1] > 0) or (rect.y < self.size and vector[1] < 0):
            return True

        return False

    def change_dir(self, key):
        speed = self.size

        if self.speed[1] == 0:
            if key == pg.K_UP:
                self.speed = [0, -speed]

            elif key == pg.K_DOWN:
                self.speed = [0, speed]

        if self.speed[0] == 0:
            if key == pg.K_RIGHT:
                self.speed = [speed, 0]

            elif key == pg.K_LEFT:
                self.speed = [-speed, 0]

        self.edges.append((self.head_rect.copy(), self.speed))
