import pygame as pg

class Score:
    def __init__(self, pos=None, font=8):
        self.pos = pos
        self.font = font
        self.exp = 0

    def draw(self, screen):
        lv = int(self.l * self.life)
        lr = int(self.l -lv)
        if self.life > 0:
            pg.draw.rect(screen, (0, 255, 0), (self.pos.x, self.pos.y, lv, self.h))
        if self.life < 1:
            pg.draw.rect(screen, (255, 0, 0), (self.pos.x + lv, self.pos.y, lr, self.h))