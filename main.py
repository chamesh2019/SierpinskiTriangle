import pygame as pg
from utils import update, draw_basics

pg.init()

# use full screen
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)

running = True
start_point, base_triangle = draw_basics(screen)

update(screen, start_point, base_triangle)
for event in pg.event.get():
    if event.type == pg.QUIT:
        pg.quit()
    
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_RETURN:
            pg.quit()
