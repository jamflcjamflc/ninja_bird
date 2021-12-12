import pygame as pg
import random

class Bricks:

    def __init__(self, ifile, screen_shape=(700, 400), p=100):
        self.p = p
        self.ifile = ifile
        self.t = 0
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
        self.bricks = []

    def _create(self):
        if self.t % self.p == 0:
            y = random.randint(0, self.screen_shape[1] - 300)
            pos = (self.screen_shape[0], y)
            print("brick created")
            self.bricks.append(Brick(sprite=self.sprite, shape=self.screen_shape, pos=pos))
            pos = (self.screen_shape[0], y + 200)
            self.bricks.append(Brick(sprite=self.sprite, shape=self.screen_shape, pos=pos))

    def _destroy(self):
        for i, brick in enumerate(self.bricks):
            if brick.pos.x < -self.sprite.get_rect()[2]:
                self.bricks[i].alive = False
        self.bricks = [brick for brick in self.bricks if brick.alive]


    def _draw(self, screen):
        for brick in self.bricks:
            brick.draw(screen)

    def _move(self):
        for i, brick in enumerate(self.bricks):
            self.bricks[i].move()

    def wrap(self, screen):
        self.t += 1
        self._destroy()
        self._create()
        self._move()
        self._draw(screen)


class Brick:

    def __init__(self, sprite=None, shape=(0, 0), pos=(0, 0)):
        self.shape = shape
        self.sprite = sprite
        self.alive = True
        self.pos = pg.math.Vector2(pos)
        self.v = pg.math.Vector2((-5, 0))
        self.brick_shape = pg.math.Vector2((50, 100))


    def draw(self, screen):
        screen.blit(self.sprite, (int(self.pos.x), int(self.pos.y)))


    def move(self):
        self.pos = self.pos + self.v