import pygame as pg

class Tile(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.screen = pg.display.get_surface()
        self.screen_size = self.screen.get_size()

        self.background = pg.Surface()
        self.background.fill(BLACK)
