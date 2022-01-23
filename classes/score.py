import pygame as pg

class Score:
    def __init__(self, pos=None, font=8):
        self.pos = pos
        self.font = font
        self.style = pg.font.SysFont("comicsans", 30)
        self.exp = 0

    def draw(self, screen):
        text = self.style.render("EXP {exp}".format(exp=self.exp), False, (255, 255, 255))
        screen.blit(text, self.pos)