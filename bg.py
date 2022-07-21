import pygame as pg
import random

from pygame import Surface

W = 20000
H = 20000
pg.init()
WIDTH = 1200
HEIGHT = 800
#screen = pg.display.set_mode((WIDTH, HEIGHT))
##pg.display.update()
def background():  

##    size = int(WIDTH * 10 // 1), int(HEIGHT * 10 // 1)
##    exsize = int(WIDTH * 20 // 1), int(HEIGHT * 20 // 1)


    sizex = int(W)
    sizey = int(H)
    exsize = (W, H)
    center_pos=(W/2, H/2)
    bg = pg.Surface(exsize)
   
    bg_rect = bg.get_rect()
    bg.set_colorkey((0, 0, 0))
    bg.fill((0, 0, 0))
    # Drawing a grid.
    for x in range(sizex):
        pg.draw.line(bg, (15, 20, 30), (x * 20, 0), (x * 20, sizey), 1)
    for y in range(sizey):
        pg.draw.line(bg, (15, 20, 30), (0, y * 20), (sizex, y * 20), 1)
    # Drawing Stars
    for stars in range(20000):
        starx = random.randint(10, sizex)
        stary = random.randint(10, sizey)
        star = starx, stary
        radius = random.randint(1, 3)
        pg.draw.circle(bg, pg.Color("white"), star, radius)
    bg.blit(bg, bg_rect)
##    for planets in range(100):
##        red = random.randint(0, 255)
##        green = random.randint(0, 255)
##        blue = random.randint(0, 255)
##        random_rgbcolor = (red, green, blue)
##
##        planetx = random.randint(0, sizex - 1)
##        planety = random.randint(0, sizey - 1)
##        pos = (planetx, planety)
##        radius = random.randint(1, 100)
##
##        pg.draw.circle(bg, random_rgbcolor, pos, radius)
    pg.display.flip
    return bg


