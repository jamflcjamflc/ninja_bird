import pygame as pg

class Intro:

    def __init__(self, picture_file):
        self.background = pg.image.load(picture_file)

    def run(self, screen, clock, FPS):
        finish = False
        exit_while = False
        while not exit_while:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    finish = True
                    exit_while = True
                elif event.type == pg.KEYDOWN:
                    exit_while = True
            screen.fill((0, 150, 0))
            screen.blit(self.background, (0, 0))
            pg.display.update()
            clock.tick(FPS)
        return finish

if __name__ == "__main__":
    print("intro")