import pygame as pg
import random

class Clouds:

    def __init__(self, ifile, screen_shape=(700, 400), horizon=300, n=8):
        self.horizon = horizon
        self.n = n
        self.ifile = ifile
        self.screen_shape = screen_shape
        self.width, self.height = self.screen_shape
        self.sprite = pg.image.load(self.ifile)
        _, _, self.sprite_width, self.sprite_height = self.sprite.get_rect()
        self.sprite = pg.Surface.convert_alpha(self.sprite)
        for i in range(self.sprite_width):
            for j in range(self.sprite_height):
                color = self.sprite.get_at((i, j))
                if color == (255, 255, 255, 0):
                    self.sprite.set_at((i, j), (255, 255, 255, 255))
        self.clouds = [Cloud(ctype=random.randint(0, 2),
                             sprite=self.sprite,
                             width=self.width,
                             pos=(random.randint(0, self.width), random.randint(0, self.horizon - 50))) for _ in range(self.n)]

    def _create(self):
        for _ in range(len(self.clouds), self.n):
            self.clouds.append(Cloud(ctype=random.randint(0, 2),
                                     sprite=self.sprite,
                                     width=self.width,
                                     pos=(self.width, random.randint(0, self.horizon - 50))))

    def _destroy(self):
        for i, cloud in enumerate(self.clouds):
            if cloud.pos.x < -self.sprite.get_rect()[2]:
                self.clouds[i].alive = False
        self.clouds = [cloud for cloud in self.clouds if cloud.alive]


    def _draw(self, screen):
        for cloud in self.clouds:
            cloud.draw(screen)

    def _move(self):
        for i, cloud in enumerate(self.clouds):
            self.clouds[i].move()

    def wrap(self, screen):
        self._destroy()
        self._create()
        self._move()
        self._draw(screen)


class Cloud:

    def __init__(self, ctype=0, sprite=None, width=None, pos=(0,0)):
        self.ctype = ctype
        self.sprite = sprite
        self.alive = True
        self.pos = pg.math.Vector2(pos)
        self.v = pg.math.Vector2((-0.4, 0))


    def draw(self, screen):
        if self.ctype == 0:
            screen.blit(self.sprite, (int(self.pos.x), int(self.pos.y)), area=(0, 0, 50, 50))
        elif self.ctype == 1:
            screen.blit(self.sprite, (int(self.pos.x), int(self.pos.y)), area=(0, 0, 50, 50))
        elif self.ctype == 2:
            screen.blit(self.sprite, (int(self.pos.x), int(self.pos.y)), area=(0, 50, 50, 50))
        elif self.ctype == 3:
            screen.blit(self.sprite, (int(self.pos.x), int(self.pos.y)), area=(0, 50, 50, 50))

    def move(self):
        self.pos = self.pos + self.v