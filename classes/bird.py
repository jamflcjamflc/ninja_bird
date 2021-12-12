import pygame as pg
from bricks import Bricks
from bricks import Brick
class Bird:

    def __init__(self, pos=(0, 0), r=10, v=(1, 0), g=(0, 2)):
        self.pos = pg.math.Vector2(pos)
        self.ala = 'up'
        self.v = pg.math.Vector2(v)
        self.g = pg.math.Vector2(g)
        self.r = r

    def _move(self, screen, aleteo=False):
        self.v = self.v + self.g
        self.pos = self.pos + self.v


    def _draw(self, screen):
        _, _, width, height = screen.get_rect()
        pg.draw.circle(screen, (255, 0, 0), (int(self.pos.x), int(self.pos.y)), self.r, 0)
        pg.draw.circle(screen, (0, 0, 0), (int(self.pos.x + 10), int(self.pos.y - 5)), 2, 0)
        pg.draw.polygon(screen, (255, 255, 0), [(int(self.pos.x + 16), int(self.pos.y)),
                                               (int(self.pos.x + 20), int(self.pos.y - 2)),
                                               (int(self.pos.x + 24), int(self.pos.y)),
                                               (int(self.pos.x + 20), int(self.pos.y + 2))], 0)

        pg.draw.polygon(screen, (255, 255, 0), [(int(self.pos.x - 20), int(self.pos.y)),
                                                (int(self.pos.x - 28), int(self.pos.y - 4)),
                                                (int(self.pos.x - 24), int(self.pos.y + 2))], 0)

        if self.ala == "up":
            pg.draw.polygon(screen, (255, 255, 0), [(int(self.pos.x - 14), int(self.pos.y + 6)),
                                                    (int(self.pos.x + 5), int(self.pos.y - 0)),
                                                    (int(self.pos.x - 23), int(self.pos.y - 4))], 0)

        else:
            pg.draw.polygon(screen, (255, 255, 0), [(int(self.pos.x - 14), int(self.pos.y + 6)),
                                                    (int(self.pos.x + 5), int(self.pos.y - 0)),
                                                    (int(self.pos.x - 23), int(self.pos.y + 16))], 0)

    def _screen_colision(self, screen, bricks):
        _, _, width, height = screen.get_rect()
        #choque horizontal
        """if self.pos.x >= width - self.r and self.v.x > 0:
            self.pos = pg.math.Vector2((width - self.r, self.pos.y))
            self.v = pg.math.Vector2(-self.v.x, self.v.y)
        elif self.pos.x <= self.r and self.v.x < 0:
            self.pos = pg.math.Vector2((self.r, self.pos.y))
            self.v = pg.math.Vector2(-self.v.x, self.v.y)"""
        #choque vertical
        if self.pos.y >= height - self.r and self.v.y > 0:
            self.pos = pg.math.Vector2((self.pos.x, height - self.r))
            self.v = pg.math.Vector2(self.v.x, 0)
            """self.v = pg.math.Vector2(self.v.x, -self.v.y)"""
        elif self.pos.y <= self.r and self.v.y < 0:
            self.pos = pg.math.Vector2((self.pos.x, self.r))
            self.v = pg.math.Vector2(self.v.x, 0)
            """self.v = pg.math.Vector2(self.v.x, -self.v.y)"""
        #colision con bricks
        for brick in bricks.bricks:
            #colision de pared izquierda
            condition_1 = brick.pos.x - self.pos.x < self.r
            condition_2 = self.pos.x - self.r < brick.pos.x + brick.brick_shape.x
            condition_3 = brick.pos.y - self.pos.y < self.r
            condition_4 = self.pos.y - self.r < brick.pos.y + brick.brick_shape.y
            condition_5 = brick.pos.y > self.pos.y + self.r / 7.0
            condition_6 = brick.pos.y + brick.brick_shape.y + self.r / 7.0 < self.pos.y
            colision = condition_1 and condition_2 and condition_3 and condition_4
            if colision:
                if condition_5:
                    self.pos.y = brick.pos.y - self.r
                    self.v.y = 0
                elif condition_6:
                    self.pos.y = brick.pos.y + brick.brick_shape.y + self.r
                    self.v.y = 0
                else:
                    self.pos.x = brick.pos.x - self.r
                break

    def wrap(self, screen, bricks):
        self._move(screen)
        self._screen_colision(screen, bricks)
        self._draw(screen)


if __name__ == "__main__":
    print("bird")
