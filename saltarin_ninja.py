import pygame as pg
from classes.bird import Bird
from classes.clouds import Clouds
from classes.bricks import Bricks

pg.init()
SIZE = WIDTH, HEIGHT = 700, 400
HORIZON = 200
NCLOUDS = 8
nubes_file = r"C:\Users\JoseAlfredo\Desktop\lucas_python\MI_PRIMER_VIDEOJUEGO\sprites\nubes_sprite_2x50x50.png"
bricks_file = r"C:\Users\JoseAlfredo\Desktop\lucas_python\MI_PRIMER_VIDEOJUEGO\sprites\big_brick.png"
screen = pg.display.set_mode(SIZE)
FPS = 20
clock = pg.time.Clock()
bird_1 = Bird(pos=(WIDTH // 2, HEIGHT // 4), r=20, v=(0, 0), g=(0, 1))
clouds = Clouds(nubes_file, screen_shape=SIZE, horizon=HORIZON, n=NCLOUDS)
bricks = Bricks(bricks_file, screen_shape=SIZE,  p=30)
finish = False
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
    bird_1.wrap(screen, bricks)
    pg.display.update()
    clock.tick(FPS)
print('hemos terminado')
pg.quit()
quit()