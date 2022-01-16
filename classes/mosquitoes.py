import pygame as pg
import random

class Mosquitoes:

    def __init__(self, ifile, screen_shape=(700, 400), p=100, v=7):
        self.p = p
        self.ifile = ifile
        self.t = 0
        self.v = v
        self.screen_shape = screen_shape
        self.width, self.height = self.screen_shape
        self.sprite = pg.image.load(self.ifile)
        _, _, self.sprite_width, self.sprite_height = self.sprite.get_rect()
        self.sprite = pg.Surface.convert_alpha(self.sprite)
        for i in range(self.sprite_width):
            for j in range(self.sprite_height):
                color = self.sprite.get_at((i, j))
                if color == (255, 255, 255, 255):
                    self.sprite.set_at((i, j), (255, 255, 255, 0))
        self.mosquitoes = []

    def _create(self):
        if self.t % self.p == 0:
            y = random.randint(0, self.screen_shape[1])
            pos = (self.screen_shape[0], y)
            print("mosquito created")
            self.mosquitoes.append(Mosquito(sprite=self.sprite, shape=self.screen_shape, pos=pos, v=self.v))

    def _destroy(self):
        for i, mosquito in enumerate(self.mosquitoes):
            if mosquito.pos.x < -self.sprite.get_rect()[2]:
                self.mosquitoes[i].alive = False
        self.mosquitoes = [mosquito for mosquito in self.mosquitoes if mosquito.alive]


    def _draw(self, screen):
        for mosquito in self.mosquitoes:
            mosquito.draw(screen)

    def _move(self):
        for i, mosquito in enumerate(self.mosquitoes):
            self.mosquitoes[i].move()

    def wrap(self, screen):
        self.t += 1
        self._destroy()
        self._create()
        self._move()
        self._draw(screen)


class Mosquito:

    def __init__(self, sprite=None, shape=(0, 0), pos=(0, 0), v=3):
        self.shape = shape
        self.sprite = sprite
        self.alive = True
        self.pos = pg.math.Vector2(pos)
        self.v = pg.math.Vector2((-v, 0))
        self.mosquito_shape = pg.math.Vector2((30, 20))
        self.t = 0


    def draw(self, screen):
        screen.blit(self.sprite, (int(self.pos.x), int(self.pos.y)), area=(0, 20*(self.t%4), 30, 20))
        self.t += 1


    def move(self):
        self.pos = self.pos + self.v