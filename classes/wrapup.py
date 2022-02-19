import pygame as pg
import os


class Wrapup:

    def __init__(self, score_file):
        self.score_file = score_file
        self.style = pg.font.SysFont("comicsans", 40)
        if os.path.isfile(self.score_file):
            with open(self.score_file, "r") as f:
                lines = f.readlines()
                self.high_score = int(lines[-1].strip("\r\n"))
        else:
            self.high_score = 0

    def run(self, screen, clock, FPS, score):
        if score > self.high_score:
            with open(self.score_file, "a") as f:
                f.write(str(score) + "\n")
        finish = False
        exit_while = False
        while not exit_while:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    finish = True
                    exit_while = True
                elif event.type == pg.KEYDOWN:
                    exit_while = True
            text = self.style.render("You lose", False, (255, 255, 255))
            screen.blit(text, (300, 130))
            text = self.style.render("Your score {score}".format(score=score), False, (255, 255, 255))
            screen.blit(text, (300, 170))
            text = self.style.render("High score {score}".format(score=self.high_score), False, (255, 255, 255))
            screen.blit(text, (300, 210))
            text = self.style.render("Press a key", False, (255, 255, 255))
            screen.blit(text, (300, 250))
            pg.display.update()
            clock.tick(FPS)
        return finish


if __name__ == "__main__":
    print("wrapup")
