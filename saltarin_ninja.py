import pygame as pg
import os
import sys
import time
from classes.bird import Bird
from classes.clouds import Clouds
from classes.bricks import Bricks
from classes.mosquitoes import Mosquitoes
from classes.score import Score
from classes.intro import Intro
from classes.wrapup import Wrapup

pg.init()
pg.font.init()
pg.mixer.init()

SIZE = WIDTH, HEIGHT = 700, 400
HORIZON = 200
NCLOUDS = 8
path, _ = os.path.split(os.path.abspath(sys.argv[0]))
nubes_file = os.path.join(path, "sprites", "nubes_sprite_2x50x50.png")
bricks_file = os.path.join(path, "sprites", "big_brick.png")
mosquitoes_file = os.path.join(path, "sprites", "mosquito.png")
intro_file = os.path.join(path, "sprites", "Intro.png")
score_file = os.path.join(path, "resources", "high_score.txt")
background_music = os.path.join(path, "sounds", "172561__djgriffin__video-game-7.wav")
background = pg.mixer.Sound(background_music)
background.play(loops=-1)
background.set_volume(0.5)
screen = pg.display.set_mode(SIZE)
FPS = 20
clock = pg.time.Clock()
score = Score(pos=(10, HEIGHT - 20))
bird_1 = Bird(pos=(WIDTH // 2, HEIGHT // 4), r=20, v=(0, 0), g=(0, 1), score=score)
clouds = Clouds(nubes_file, screen_shape=SIZE, horizon=HORIZON, n=NCLOUDS)
bricks = Bricks(bricks_file, screen_shape=SIZE,  p=30, v=(-5, 1))
mosquitoes = Mosquitoes(mosquitoes_file, screen_shape=SIZE, p=20, v=7)
intro = Intro(intro_file)
wrapup = Wrapup(score_file)
finish = intro.run(screen, clock, FPS)
while not finish:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finish = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                bird_1.v = bird_1.v + pg.math.Vector2((0, -10))
                bird_1.ala = "down"
        elif event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                bird_1.ala = "up"

    screen.fill((0, 150, 0))
    pg.draw.rect(screen, (0, 0, 200), (0, 0, WIDTH, HORIZON), 0)
    pg.draw.circle(screen, (255, 255, 0), (5 * WIDTH // 7, HORIZON // 2), 20, 0)
    clouds.wrap(screen)
    bricks.wrap(screen)
    mosquitoes.wrap(screen)
    bird_1.wrap(screen, bricks, mosquitoes)
    if not bird_1.alive:
        finish = True
    pg.display.update()
    clock.tick(FPS)
print('hemos terminado')
time.sleep(1)
wrapup.run(screen, clock, FPS, bird_1.score.exp)
pg.mixer.stop()
pg.quit()
quit()