import pygame as pg
from pygame.locals import *
import time
import json
import os
import sys
import random
import math

def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    # Két egyenes metszéspontjának kiszámítása
    x = (x1*y2 - y1*x2) * (x3-x4) - (x1-x2) * (x3*y4 - y3*x4)
    y = (x1*y2 - y1*x2) * (y3-y4) - (y1-y2) * (x3*y4 - y3*x4)
    det = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
    if det == 0:
        return "NaN", "NaN"
    x /= det
    y /= det
    if x < min(x1, x2) or x > max(x1, x2) or x < min(x3, x4) or x > max(x3, x4):
        return "NaN", "NaN"
    if y < min(y1, y2) or y > max(y1, y2) or y < min(y3, y4) or y > max(y3, y4):
        return "NaN", "NaN"
    return x, y

pg.init()

# Képernyő beállítása
screen = pg.display.set_mode((800, 800))
surface = pg.display.get_surface()
w, h = size = surface.get_width(), surface.get_height()
pg.display.set_caption("Hlidar-Radar")
clock = pg.time.Clock()

# Program változók
rot = 0
rotspd = 0.03
playerx = 0
playery = 0
obstaclepoints = []
rotated = 0
dir = "None"

# Feliratok
font = pg.font.Font("font.ttf" , 28)

startup1 = font.render("Hlidar-Radar systems v0.1.5", True, (255, 255, 255))
startup1_rect = startup1.get_rect(topleft=(0, 0))
startup2 = font.render("----- Initializing system -----", True, (255, 255, 255))
startup2_rect = startup2.get_rect(topleft=(0, 30))
startup3 = font.render("Checking sensors...", True, (255, 255, 255))
startup3_rect = startup3.get_rect(topleft=(0, 60))
startup4 = font.render("LiDAR sensor............ [OK]", True, (255, 255, 255))
startup4_rect = startup4.get_rect(topleft=(0, 90))
startup5 = font.render("Radar sensor............ [OK]", True, (255, 255, 255))
startup5_rect = startup5.get_rect(topleft=(0, 120))
startup6 = font.render("Calibrating...", True, (255, 255, 255))
startup6_rect = startup6.get_rect(topleft=(0, 150))
startup7 = font.render("Calibration............. [OK]", True, (255, 255, 255))
startup7_rect = startup7.get_rect(topleft=(0, 180))
startup8 = font.render("Checking servos...", True, (255, 255, 255))
startup8_rect = startup8.get_rect(topleft=(0, 210))
startup9 = font.render("Servo-LiDAR............. [OK]", True, (255, 255, 255))
startup9_rect = startup9.get_rect(topleft=(0, 240))
startup10 = font.render("Servo-RDR.............. [OK]", True, (255, 255, 255))
startup10_rect = startup10.get_rect(topleft=(0, 270))
startup11 = font.render("Checking motors...", True, (255, 255, 255))
startup11_rect = startup11.get_rect(topleft=(0, 300))
startup12 = font.render("Motor-FL............... [OK]", True, (255, 255, 255))
startup12_rect = startup12.get_rect(topleft=(0, 330))
startup13 = font.render("Motor-FR............... [OK]", True, (255, 255, 255))
startup13_rect = startup13.get_rect(topleft=(0, 360))
startup14 = font.render("Motor-BL............... [OK]", True, (255, 255, 255))
startup14_rect = startup14.get_rect(topleft=(0, 390))
startup15 = font.render("Motor-BR............... [OK]", True, (255, 255, 255))
startup15_rect = startup15.get_rect(topleft=(0, 420))
startup16 = font.render("Checking boot files...", True, (255, 255, 255))
startup16_rect = startup16.get_rect(topleft=(0, 450))
startup17 = font.render("Booting...", True, (255, 255, 255))
startup17_rect = startup17.get_rect(topleft=(0, 480))
startup18 = font.render("System ready", True, (255, 255, 255))
startup18_rect = startup18.get_rect(topleft=(0, 510))




playerxtxt = font.render("Player X: "+str(playerx), True, (255, 255, 255))
playerxtxt_rect = playerxtxt.get_rect(topleft=(0, 30))
playerytxt = font.render("Player Y: "+str(playery), True, (255, 255, 255))
playerytxt_rect = playerytxt.get_rect(topleft=(0, 60))
dirtxt = font.render("Movement: "+dir, True, (255, 255, 255))
dirtxt_rect = dirtxt.get_rect(topleft=(0, 0))
clearinfo = font.render("C: Reset LIDAR", True, (255, 255, 255))
clearinfo_rect = clearinfo.get_rect(topleft=(0, h-30))

# Intro
if True == False:
    screen.fill((0, 0, 0))
    screen.blit(startup1, startup1_rect)
    pg.display.flip()
    time.sleep(1)
    screen.blit(startup2, startup2_rect)
    pg.display.flip()
    time.sleep(3)
    screen.blit(startup3, startup3_rect)
    pg.display.flip()
    time.sleep(2)
    screen.blit(startup4, startup4_rect)
    pg.display.flip()
    time.sleep(1)
    screen.blit(startup5, startup5_rect)
    pg.display.flip()
    time.sleep(2)
    screen.blit(startup6, startup6_rect)
    pg.display.flip()
    time.sleep(2)
    screen.blit(startup7, startup7_rect)
    pg.display.flip()
    time.sleep(1)
    screen.blit(startup8, startup8_rect)
    pg.display.flip()
    time.sleep(2)
    screen.blit(startup9, startup9_rect)
    pg.display.flip()
    time.sleep(2)
    screen.blit(startup10, startup10_rect)
    pg.display.flip()
    time.sleep(1)
    screen.blit(startup11, startup11_rect)
    pg.display.flip()
    time.sleep(1)
    screen.blit(startup12, startup12_rect)
    pg.display.flip()
    time.sleep(1)
    screen.blit(startup13, startup13_rect)
    pg.display.flip()
    time.sleep(1)
    screen.blit(startup14, startup14_rect)
    pg.display.flip()
    time.sleep(1)
    screen.blit(startup15, startup15_rect)
    pg.display.flip()
    time.sleep(2)
    screen.blit(startup16, startup16_rect)
    pg.display.flip()
    time.sleep(1)
    screen.blit(startup17, startup17_rect)
    pg.display.flip()
    time.sleep(2)
    screen.blit(startup18, startup18_rect)
    pg.display.flip()
    time.sleep(2)
    screen.fill((0, 0, 0))
# Főciklus
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            if event.key == pg.K_c:
                rotated = 0
                obstaclepoints = []
        
        keys = pg.key.get_pressed()
    
    # Játék logika
    rot = rot + rotspd
    if rot > 2*3.1415:
        rot = 0
        rotated += 1
    linex2 = w/2 + h/2 * math.cos(rot)
    liney2 = h/2 + h/2 * math.sin(rot)

    if rotated == 5:
        rotated = 0
        obstaclepoints = []

    # Akadályok
    obstacles = [ # drawn lines
        (-100, 100, 100, 100), # Main room top
        (-100, 100, -100, -100), # Main room left
        (-100, -100, 100, -100), # Main room bootom
        (100, -100, 100, -20), # Main room right lower
        (100, 100, 100, 20), # Main room right upper

        (100, -20, 150, -20), # corridor 1 top
        (100, 20, 350, 20), # corridor 1 bottom, room 1 bottom
        (350, 20, 350, -260), # room 1 right
        (150, -20, 150, -300), # room 1 left
        (150, -300, 500, -300), # corridor 2 top, room 1 top
        (350, -260, 450, -260), # corridor 2 bottom
        (500, -300, 500, 100), # corridor 3 right
        (450, -260, 450, 100), # corridor 3 left
        (350, 100, 450, 100), # corridor 4 top left
        (500, 100, 600, 100), # corridor 4 top right
        (350, 140, 600, 140), # corridor 4 bottom

    ]

    obsrects = [ # collision rectangles
        
        Rect(-100, 100, 200, 5), # Main room top
        Rect(-100, -100, 5, 200), # Main room left
        Rect(-100, -100, 200, 5), # Main room bottom
        Rect(100, -100, 5, 80), # Main room right upper
        Rect(100, 20, 5, 80), # Main room right lower, not working for some reason
        Rect(100, -20, 50, 5), # corridor 1 top
        Rect(100, 20, 250, 5), # corridor 1 bottom, room 1 bottom
        Rect(150, -20, 5, -280), # room 1 left
        Rect(350, 20, 5, -280), # room 1 right
        Rect(150, -300, 350, 5), # corridor 2 top, room 1 top
        Rect(350, -260, 100, 5), # corridor 2 bottom
        Rect(450, -260, 5, 360), # corridor 3 left
        Rect(500, -300, 5, 400), # corridor 3 right
        Rect(350, 140, 250, 5), # corridor 4 bottom
        # corridor 4 top left
        # corridor 4 top right
        # room 2 left
        # room 2 top
        # room 2 right upper
        # room 2 right lower
        # room 2 bottom left
        # room 2 bottom right
        # room 3 left upper
        # room 3 left lower
        # room 3 right upper
        # room 3 right lower
        # room 3 top left
        # room 3 top right
        # room 3 bottom left
        # room 3 bottom right
        # corridor 5 left
        # corridor 5 right
        # corridor 5 top
        # corridor 6 top
        # corridor 6 bottom
        # corridor 7 left
        # corridor 7 right
        # corridor 7 bottom
        # corridor 8 left
        # corridor 8 right
        # corridor 9 left
        # corridor 9 right
        # corridor 10 right
        # corridor 10 bottom
        # corridor 10 top left
        # corridor 10 top right
        # corridor 11 left
        # corridor 11 right upper
        # corridor 11 right lower
        # corridor 12 top
        # corridor 12 bottom
        # room 4 left
        # room 4 right
        # room 4 top
        # room 4 bottom
        # corridor 13 bottom
        # corridor 13 top left
        # corridor 13 top right
        # room 5 left upper
        # room 5 left lower
        # room 5 right
        # room 5 top
        # room 5 bottom
        # corridor 14 left
        # corridor 14 right upper
        # corridor 14 right lower
        # room 6 left
        # room 6 right upper
        # room 6 right lower
        # room 6 top left
        # room 6 top middle
        # room 6 top right
        # room 6 bottom
        # room 7 left upper
        # room 7 left lower
        # room 7 right
        # room 7 top
        # room 7 bottom left
        # room 7 bottom right
        # corridor 15 top
        # corridor 15 bottom
        # room 8 left
        # room 8 right upper
        # room 8 right lower
        # room 8 top
        # room 8 bottom left
        # room 8 bottom right
        # corridor 16 left
        # corridor 16 right
        # corridor 17 top
        # corridor 17 bottom
        # corridor 18 left
        # corridor 18 right
        # corridor 19 top
        # corridor 19 bottom
        # corridor 20 left
        # corridor 20 right
        # room 9 left
        # room 9 right upper
        # room 9 right lower
        # room 9 top
        # room 9 bottom left
        # room 9 bottom right
        # corridor 21 top
        # corridor 21 bottom
        # exit left upper
        # exit left lower
        # exit right
        # exit top
        # exit bottom
    ]

    # Ütközés
    up = True
    down = True
    left = True
    right = True
    for obstacle in obsrects:
        obstop = obstacle[1] + playery
        obsbot = obstacle[1] - obstacle[3] + playery
        obsleft = obstacle[0] + playerx
        obsright = obstacle[0] + obstacle[2] + playerx
        if 0 == obsbot and obsleft < 0 < obsright:
            down = False
        if 0 == obstop and obsleft < 0 < obsright:
            up = False
        if 0 == obsright and obsbot + 200 < 0 < obstop + 200:
            left = False
        if 0 == obsleft and obsbot + 200 < 0 < obstop + 200:
            right = False

    # Mozgásirány kiszámítása
    if keys[pg.K_w] and keys[pg.K_a]:
        dir = "UL"
    elif keys[pg.K_w] and keys[pg.K_d]:
        dir = "UR"
    elif keys[pg.K_s] and keys[pg.K_a]:
        dir = "DL"
    elif keys[pg.K_s] and keys[pg.K_d]:
        dir = "DR"
    elif keys[pg.K_w]:
        dir = "U"
    elif keys[pg.K_a]:
        dir = "L"
    elif keys[pg.K_d]:
        dir = "R"
    elif keys[pg.K_s]:
        dir = "D"
    else:
        dir = "None"



    # Játékos mozgatása

    if keys[pg.K_w] and up:
        playery += 0.5
    if keys[pg.K_s] and down:
        playery -= 0.5
    if keys[pg.K_a] and left:
        playerx += 0.5
    if keys[pg.K_d] and right:
        playerx -= 0.5

    # Rajzolás
    screen.fill((0, 0, 0))
    pg.draw.circle(surface, (255, 255, 255), (w/2, h/2), h/2)
    pg.draw.circle(surface, (0, 0, 0), (w/2, h/2), h/2-6)
    pg.draw.circle(surface, (255, 255, 255), (w/2, h/2), 5)
    pg.draw.line(surface, (255, 255, 255), (w/2, h/2), (linex2, liney2), 5)
    dirtxt = font.render("Movement: "+dir, True, (255, 255, 255))
    playerxtxt = font.render("Player X: "+str(playerx), True, (255, 255, 255))
    playerytxt = font.render("Player Y: "+str(playery), True, (255, 255, 255))
    screen.blit(dirtxt, dirtxt_rect)
    screen.blit(playerxtxt, playerxtxt_rect)
    screen.blit(playerytxt, playerytxt_rect)
    screen.blit(clearinfo, clearinfo_rect)
    for obstacle in obstacles:
        x1, y1, x2, y2 = obstacle[0] + playerx, obstacle[1] + playery, obstacle[2] + playerx, obstacle[3] + playery
        x, y = intersect(w/2, h/2, linex2, liney2, x1 + w/2, y1 + h/2, x2 + w/2, y2 + h/2)
        if (x, y) != ("NaN", "NaN"):
            obstaclepoints.append((x, y, rot))
    for item in obstaclepoints:
        if item[2] != rot+rotspd:
            pg.draw.circle(surface, (0, 0, 255), (item[0], item[1]), 5)
        if item[2] == rot+rotspd:
            obstaclepoints.remove(item)

    pg.display.flip()
    clock.tick(120)

