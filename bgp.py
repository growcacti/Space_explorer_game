import pygame as pg
import random

from pygame import Surface


pg.init()

#reduced W an H to use less  memory
W = 10000 # size of space used for game background
H = 10000 # 2nd surface over screen
HW = W / 2 # Finding center of game world
HH = H / 2
WIDTH = 1200 # view screen settings
HEIGHT = 800
#screen = pg.display.set_mode((WIDTH, HEIGHT))
##pg.display.update()
def background():  

##    size = int(WIDTH * 10 // 1), int(HEIGHT * 10 // 1)
##    exsize = int(WIDTH * 20 // 1), int(HEIGHT * 20 // 1)


    sizex = int(W)
    sizey = int(H)
    exsize = (W, H)
    center_pos=(HW,  HH)
    bg = pg.Surface(exsize)
   
    bg_rect = bg.get_rect()
    # make black transparent using colorkey so I can do
    # a screen fill and not cover up everything in black
    # prevents trailing images which drove me crazy for a time
    
    bg.set_colorkey((0, 0, 0)) 
    bg.fill((0, 0, 0))
    # Drawing a grid map.
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
    def rc():
        randx = random.randint(20, 9800)
        randy = random.randint(20, 9800)
        randpos = (randx, randy)
        return randpos
    bg.blit(bg, bg_rect)

    p1 = pg.image.load("p1.png")
    p1_rect = p1.get_rect(center = rc())
     
    p2 = pg.image.load("p2.png")
     
    p3 = pg.image.load("p3.png")
     
    p4 = pg.image.load("p4.png")

    p6 = pg.image.load("p6.png")
     
    p7 = pg.image.load("p7.png")

    p8 = pg.image.load("p8.png")

    #p9 = pg.image.load("p9.png")

    p10 = pg.image.load("p10.png")
    p11 = pg.image.load("p11.png")

    p12 = pg.image.load("p12.png")

    p13 = pg.image.load("p13.png")
    p14 = pg.image.load("p14.png")

    p15 = pg.image.load("p15.png")

    p16 = pg.image.load("p16.png")




    p2_rect = p2.get_rect(center= rc())

    p3_rect = p3.get_rect(center = rc())

    p4_rect = p4.get_rect(center = rc())





    p8_rect = p8.get_rect(center = rc())

  

    p10_rect = p10.get_rect(center = rc())

    p11_rect = p11.get_rect(center = rc())

    p12_rect = p12.get_rect(center = rc())

    p13_rect = p13.get_rect(center = rc())

    p14_rect = p14.get_rect(center = rc())

    p15_rect = p15.get_rect(center = rc())

    p16_rect = p16.get_rect(center = rc())




    bg.blit(p1, p1_rect)
    bg.blit(p2, p2_rect)
    bg.blit(p3, p3_rect)
    bg.blit(p4, p4_rect)
  
   

    bg.blit(p8, p8_rect)

    bg.blit(p10, p10_rect)
    bg.blit(p11, p11_rect)
    bg.blit(p12, p12_rect)
    bg.blit(p13, p13_rect)
    bg.blit(p14, p14_rect)







    return bg        
def get_random_cor(x, y, objw, objh):
    cam_rect = pg.Rect(camx, camy, WIDTH, HEIGHT)
    newx = random.randint((camx - WIDTH), (camx + 2*WIDTH))
    newy = random.randint((camy - HEIGHT), (camy + 2*HEIGHT))
    obj_rect = pg.Rect(newx, newy, objW, objh)
    if not objRect.collderect(cam_rect):
        return newx, newy









    
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
    


