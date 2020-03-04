import math

import pygame as pg
from pygame.locals import *

from constants import *


class Snake(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.screen = pg.display.get_surface()
        self.screen_size = self.screen.get_size()
        self.size = math.floor(self.screen_size[0] / 32) # Size of a single part

        self.snake_size = 3 # Size of the whole snake (number of parts)

        self.speed = (0, self.size)
        self.speed_tail = (0, self.size)
        self.tails_speeds = [[self.snake_size - 2, self.speed_tail]]

        self.background = pg.Surface((self.size, self.size))
        self.background.fill(BLACK)

        self.head = pg.Surface((self.size, self.size))
        self.head.fill(SNAKE_COLOR)
        self.head_rect = self.head.get_rect()

        posx, posy = (self.screen_size[0] / 2) - (self.screen_size[0] % self.size), (self.screen_size[1] / 4) - (self.screen_size[1] % self.size)
        self.head_rect.x = posx
        self.head_rect.y = posy
        self.tail_rect = self.head_rect.copy()

        self.screen.blit(self.head, self.head_rect)
        for i in range(2):
            self.move_rect(self.head_rect, self.speed)
            self.screen.blit(self.head, self.head_rect)

    def update(self, ate):
        if not ate:
            prev_tail = self.tail_rect.copy()
            self.screen.blit(self.background, prev_tail)

            hit_tail = self.hit_boundaries(self.tail_rect, self.speed_tail)
            self.move_rect(self.tail_rect, self.speed_tail, hit_tail)

        else:
            prev_tail = None
            self.snake_size += 1

        hit_head = self.hit_boundaries(self.head_rect, self.speed)
        self.move_rect(self.head_rect, self.speed, hit_head)
        self.screen.blit(self.head, self.head_rect)

        return [prev_tail, self.tail_rect, self.head_rect]

    def move_rect(self, rect, vector, hit=False):
        if hit == False:
            rect.x += vector[0]
            rect.y += vector[1]

        else:
            if vector[0] > 0: # Going right
                rect.x = 0

            elif vector[0] < 0: # Going left
                rect.x = self.screen_size[0]

            elif vector[1] > 0: # Going up
                rect.y = 0

            else: # Going down
                rect.y = self.screen_size[1]

    def hit_boundaries(self, rect, vector):
        if (rect.x >= (self.screen_size[0] - self.size) and vector[0] > 0) or (rect.x <= self.size and vector[0] < 0):
            return True

        if (rect.y >= (self.screen_size[1] - self.size) and vector[1] > 0) or (rect.y <= self.size and vector[1] < 0):
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
