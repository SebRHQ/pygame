import pygame as pg, time, sys, os, random, math, json, pygame.mixer as mixer

def create_rect(width, height, border, color, border_color):
    surf = pg.Surface((width+border*2, height+border*2), pg.SRCALPHA)
    pg.draw.rect(surf, color, (border, border, width, height), 0)
    for i in range(1, border):
        pg.draw.rect(surf, border_color, (border-i, border-i, width+5, height+5), 1)
    return surf

def shutdown():
    screen.fill((0, 0, 0))
    screen.blit(shutdownbg, shutdownbg_rect)
    pg.display.flip()
    pg.mixer.Channel(6).play(pg.mixer.Sound("assets/sfx/anthem.mp3"))
    time.sleep(205)
    screen.fill((0, 0, 0))
    pg.mixer.Channel(7).play(pg.mixer.Sound("assets/sfx/shutdown.mp3"))
    pg.display.flip()
    time.sleep(4)
    pg.quit()
    sys.exit()
    


pg.init()
w, h = 1920, 1080
screen = pg.display.set_mode((w, h), pg.FULLSCREEN)
surface = pg.display.get_surface()
w, h = size = surface.get_width(), surface.get_height()
pg.display.set_caption("WINSOVIET")
clock = pg.time.Clock()
pg.mouse.set_visible(False)
mixer.init()
pg.mixer.Channel(7).play(pg.mixer.Sound("assets/sfx/oldpc.mp3"))
pg.mixer.Channel(7).set_volume(0.15)

# Load images
cursor = pg.image.load("assets/img/cursor.png")
cursor = pg.transform.scale(cursor, (32, 45))
amilogo = pg.image.load("assets/img/ami.png").convert_alpha()
amilogo_rect = amilogo.get_rect(topleft=(0, 0))


# Load sounds

# Load fonts
biosfont = pg.font.Font("assets/fonts/biosfont.ttf", 32)
winloadfont_big = pg.font.Font("assets/fonts/tahoma.ttf", 132)
winloadfont_small = pg.font.Font("assets/fonts/tahoma.ttf", 36)
normalfont = pg.font.SysFont("Calibri", 48)

biosline1 = biosfont.render("AMIBIOS(C)2007 American Megatrends Inc.", True, (255, 255, 255))
biosline1_rect = biosline1.get_rect(topleft=(0, 280))
biosline2 = biosfont.render("ASUS P5KPL ACPI BIOS Revision 0603", True, (255, 255, 255))
biosline2_rect = biosline2.get_rect(topleft=(0, 320))
biosline3 = biosfont.render("CPU : Intel(R) Pentium(R) Dual CPU E2180 @ 2.00GHz", True, (255, 255, 255))
biosline3_rect = biosline3.get_rect(topleft=(0, 360))
biosline4 = biosfont.render("   Speed : 2.51GHz     Count : 2", True, (255, 255, 255))
biosline4_rect = biosline4.get_rect(topleft=(0, 400))
biosline5 = biosfont.render("Press DEL to run Setup", True, (255, 255, 255))
biosline5_rect = biosline5.get_rect(topleft=(0, 480))
biosline6 = biosfont.render("Press F8 for BBS POPUP", True, (255, 255, 255))
biosline6_rect = biosline6.get_rect(topleft=(0, 520))
biosline7 = biosfont.render("DDR2-667 in Dual-Channel Interleaved Mode", True, (255, 255, 255))
biosline7_rect = biosline7.get_rect(topleft=(0, 560))
biosline8 = biosfont.render("Initializing USB Controllers .. Done.", True, (255, 255, 255))
biosline8_rect = biosline8.get_rect(topleft=(0, 600))
biosline9 = biosfont.render("1024MB OK", True, (255, 255, 255))
biosline9_rect = biosline9.get_rect(topleft=(0, 640))
biosline10 = biosfont.render("Auto-Detecting Pri Master..ATAPI CD-ROM", True, (255, 255, 255))
biosline10_rect = biosline10.get_rect(topleft=(0, 720))
biosline11 = biosfont.render("Pri Slave..ATA HDD0", True, (255, 255, 255))
biosline11_rect = biosline11.get_rect(topleft=(0, 780))
biosline12 = biosfont.render("Sec Master..None", True, (255, 255, 255))
biosline12_rect = biosline12.get_rect(topleft=(0, 820))
biosline01 = biosfont.render("(C) American Megatrends, Inc.", True, (255, 255, 255))
biosline01_rect = biosline01.get_rect(topleft=(0, h-40))
biosline02 = biosfont.render("64-0603-000001-00101111-022908-Bearlake-A0820000-Y2KC", True, (255, 255, 255))
biosline02_rect = biosline02.get_rect(topleft=(0, h-80))

wintitle = winloadfont_big.render("Windows", True, (255, 255, 255))
wintitle_rect = wintitle.get_rect(center=(w/2, h/2))
winsubtitle = winloadfont_small.render("Stalinsoft", True, (255, 255, 255))
winsubtitle_rect = winsubtitle.get_rect(topleft=(wintitle_rect.left, h/2-100))
winsubtitle2 = normalfont.render("SOVIET", True, (197, 90, 17))
winsubtitle2_rect = winsubtitle2.get_rect(topleft=(wintitle_rect.right, h/2-70))
winlogo = pg.image.load("assets/img/winlogo.png").convert_alpha()
winlogo_rect = winlogo.get_rect(center=(w/2+130, h/2-170))
winloadline1 = normalfont.render("Copyright © Stalinsoft corporation", True, (255, 255, 255))
winloadline1_rect = winloadline1.get_rect(topleft=(0, h-100))
winloadline2 = normalfont.render("1922-1991", True, (255, 255, 255))
winloadline2_rect = winloadline2.get_rect(topleft=(0, h-50))
winloadline3 = normalfont.render("STALINSOFT", True, (255, 255, 255))
winloadline3_rect = winloadline3.get_rect(topleft=(w-300, h-50))

loginbg = pg.image.load("assets/img/loginbg.jpg").convert_alpha()
loginbg = pg.transform.scale(loginbg, (w-300, h))
loginbg_rect = loginbg.get_rect(center=(w/2, h/2))

shutdownbg = pg.image.load("assets/img/shutdownbg.png").convert_alpha()
shutdownbg = pg.transform.scale(shutdownbg, (w-300, h))
shutdownbg_rect = shutdownbg.get_rect(center=(w/2, h/2))

shutdownrect = pg.Rect(175, 1165, 50, 55)
typeboxrect = pg.Rect(1170, 642, 240, 40)
continuerect = pg.Rect(1452, 642, 40, 40)
questionrect = pg.Rect(1502, 642, 40, 40)

login2bg = pg.image.load("assets/img/login2bg.png").convert_alpha()
login2bg = pg.transform.scale(login2bg, (w-300, h))
login2bg_rect = login2bg.get_rect(center=(w/2, h/2))

mainbg = pg.image.load("assets/img/mainbg.png").convert_alpha()
mainbg = pg.transform.scale(mainbg, (w-300, h))
mainbg_rect = mainbg.get_rect(center=(w/2, h/2))

chromeicon = pg.image.load("assets/img/chrome.png").convert_alpha()
chromeicon = pg.transform.scale(chromeicon, (150, 150))
chromeicon_rect = chromeicon.get_rect(topleft=(250, 50))
chrometext = normalfont.render("CHROME", True, (255, 255, 255))
chrometext_rect = chrometext.get_rect(center=(325, 250))

musicicon = pg.image.load("assets/img/folder.png").convert_alpha()
musicicon = pg.transform.scale(musicicon, (150, 150))
musicicon_rect = musicicon.get_rect(topleft=(250, 300))
musictext = normalfont.render("MUSIC", True, (255, 255, 255))
musictext_rect = musictext.get_rect(center=(325, 500))

wardeclarer = pg.image.load("assets/img/winlogo.png").convert_alpha()
wardeclarer = pg.transform.scale(wardeclarer, (150, 150))
wardeclarer_rect = wardeclarer.get_rect(topleft=(250, 550))
wardeclarertext = normalfont.render("DECLARE", True, (255, 255, 255))
wardeclarertext_rect = wardeclarertext.get_rect(center=(325, 750))
wardeclarertext2 = normalfont.render("A WAR !!", True, (255, 255, 255))
wardeclarertext2_rect = wardeclarertext2.get_rect(center=(325, 800))

popup1 = pg.image.load("assets/img/popupremoving.png").convert_alpha()
popup1 = pg.transform.scale(popup1, (450, 320))
popup1_rect = popup1.get_rect(center=(w/2, h/2))
popup2 = pg.image.load("assets/img/popupremoved.png").convert_alpha()
popup2 = pg.transform.scale(popup2, (450, 320))
popup2_rect = popup2.get_rect(center=(w/2, h/2))

chromepopup = pg.image.load("assets/img/popupchromeerror.png").convert_alpha()
chromepopup = pg.transform.scale(chromepopup, (450, 320))
chromepopup_rect = chromepopup.get_rect(center=(w/2, h/2))

musicfolder = pg.image.load("assets/img/musicfolder.png").convert_alpha()
musicfolder_rect = musicfolder.get_rect(center=(w/2, h/2))
musicpopup = pg.image.load("assets/img/popupmusicerror.png").convert_alpha()
musicpopup = pg.transform.scale(musicpopup, (450, 320))
musicpopup_rect = musicpopup.get_rect(center=(w/2, h/2))
winamp = pg.image.load("assets/img/winamp.png").convert_alpha()
winamp = pg.transform.scale(winamp, (800, 318))
winamp_rect = winamp.get_rect(center=(w/2, h/2))

wardeclarerwarn = pg.image.load("assets/img/wardeclarerwarn.png").convert_alpha()
wardeclarerwarn = pg.transform.scale(wardeclarerwarn, (450, 450))
wardeclarerwarn_rect = wardeclarerwarn.get_rect(center=(w/2, h/2))
wardeclarererror = pg.image.load("assets/img/wardeclarererror.png").convert_alpha()
wardeclarererror = pg.transform.scale(wardeclarererror, (450, 450))
wardeclarererror_rect = wardeclarererror.get_rect(center=(w/2, h/2))
wardeclarerbg = pg.image.load("assets/img/wardeclarerbg.jpg").convert_alpha()
wardeclarerbg = pg.transform.scale(wardeclarerbg, (w-300, h))
wardeclarerbg_rect = wardeclarerbg.get_rect(center=(w/2, h/2))

wardeclarerline1 = normalfont.render("Hello comrade", True, (255, 255, 255))
wardeclarerline1_rect = wardeclarerline1.get_rect(center=(w/2, h-200))
wardeclarerline2 = normalfont.render("Which country do you wanna destroy today?", True, (255, 255, 255))
wardeclarerline2_rect = wardeclarerline2.get_rect(center=(w/2, h-200))
wardeclarerline3 = normalfont.render("a:) USA [imperialists]", True, (255, 255, 255))
wardeclarerline3_rect = wardeclarerline3.get_rect(center=(w/2, h-200))
wardeclarerline4 = normalfont.render("b:) Germany [Nazis]", True, (255, 255, 255))
wardeclarerline4_rect = wardeclarerline4.get_rect(center=(w/2, h-150))
wardeclarerline5 = normalfont.render("ok", True, (255, 255, 255))
wardeclarerline5_rect = wardeclarerline5.get_rect(center=(w/2, h-200))

rocket = pg.image.load("assets/img/rocket.png").convert_alpha()
rocket.set_colorkey((0, 0, 0))
rocketx, rockety = 1420, 338
rocket_rect = rocket.get_rect(center=(w/2, h/2))

boom = pg.image.load("assets/img/nuc.png").convert_alpha()
boom = pg.transform.scale(boom, (400, 300))

okbutton = pg.Rect(962, 686, 127, 37)
playmusicrect = pg.Rect(877, 447, 470, 100)
musicclose = pg.Rect(1418, 264, 32, 32)
winampclose = pg.Rect(1407, 480, 13, 13)

chromerect = pg.Rect(215, 50, 225, 220)
musicrect = pg.Rect(215, 300, 225, 220)
warrect = pg.Rect(215, 540, 225, 300)


# Boot up
screen.fill((0, 0, 0))

screen.blit(amilogo, amilogo_rect)
screen.blit(biosline1, biosline1_rect)
screen.blit(biosline2, biosline2_rect)
screen.blit(biosline01, biosline01_rect)
screen.blit(biosline02, biosline02_rect)
pg.display.flip()
time.sleep(1)
screen.blit(biosline3, biosline3_rect)
screen.blit(biosline4, biosline4_rect)
pg.display.flip()
time.sleep(2)
screen.blit(biosline5, biosline5_rect)
screen.blit(biosline6, biosline6_rect)
pg.display.flip()
time.sleep(0.5)
screen.blit(biosline7, biosline7_rect)
screen.blit(biosline8, biosline8_rect)
pg.display.flip()
time.sleep(1)
screen.blit(biosline9, biosline9_rect)
pg.display.flip()
time.sleep(1)
screen.blit(biosline10, biosline10_rect)
pg.display.flip()
time.sleep(1)
screen.blit(biosline11, biosline11_rect)
pg.display.flip()
time.sleep(0.5)
screen.blit(biosline12, biosline12_rect)
pg.display.flip()
pg.mixer.Channel(7).play(pg.mixer.Sound("assets/sfx/oldpcloop.mp3"), -1)
time.sleep(4)

frame = 0
tank = pg.image.load("assets/img/tank.png").convert_alpha()
tankx = w/2-240
tank_rect = tank.get_rect(center=(tankx, h/2+132))
pg.mixer.Channel(6).play(pg.mixer.Sound("assets/sfx/katyusha.mp3"), -1)

bootup = True
while bootup:
    screen.fill((0, 0, 0))
    screen.blit(wintitle, wintitle_rect)
    screen.blit(winsubtitle, winsubtitle_rect)
    screen.blit(winsubtitle2, winsubtitle2_rect)
    screen.blit(create_rect(300, 50, 3, (0, 0, 0), (100, 100, 100)), (w/2-150, h/2+100))
    screen.blit(winlogo, winlogo_rect)
    screen.blit(winloadline1, winloadline1_rect)
    screen.blit(winloadline2, winloadline2_rect)
    screen.blit(winloadline3, winloadline3_rect)
    tankx += 5
    tank_rect = tank.get_rect(center=(tankx, h/2+132))
    screen.blit(tank, tank_rect)
    screen.blit(create_rect(207, 100, 3, (0, 0, 0), (0, 0, 0)), (w/2-360, h/2+100))
    screen.blit(create_rect(200, 100, 3, (0, 0, 0), (0, 0, 0)), (w/2+155, h/2+100))
    frame += 1
    pg.display.flip()
    if tankx >= w/2+240:
        tankx = w/2-240
    if frame >= 600:
        bootup = False
    clock.tick(60)

showpointer = False
switchpointer = False

login = True
frame = 0
while login:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.MOUSEBUTTONDOWN:
            if shutdownrect.collidepoint(pg.mouse.get_pos()):
                shutdown()
            if typeboxrect.collidepoint(pg.mouse.get_pos()):
                showpointer = True
            if continuerect.collidepoint(pg.mouse.get_pos()):
                login = False
            if questionrect.collidepoint(pg.mouse.get_pos()):
                print("Okcs")
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN and showpointer:
                login = False

    frame += 1
    if frame % 10 == 0:
        switchpointer = not switchpointer
    screen.fill((0, 0, 0))
    screen.blit(loginbg, loginbg_rect)
    if showpointer and switchpointer:
        screen.blit(create_rect(2, 30, 0, (0, 0, 0), (0, 0, 0)), (1180, 648))

    
    screen.blit(cursor, pg.mouse.get_pos())
    pg.display.flip()
    clock.tick(60)

screen.fill((0, 0, 0))
screen.blit(login2bg, login2bg_rect)
pg.display.flip()
mixer.Channel(6).play(mixer.Sound("assets/sfx/anthem.mp3"))
time.sleep(10.5)
mixer.Channel(6).stop()


# Main loop
frame = 0
currentframe = 0
popup1ok = False
popup2ok = False

chrome = False
music = False
war = False

playsound1 = True
playsound2 = True
playsound3 = True
playsound4 = True
chromesound = True
musicsound = True
playmusic = False
playmusic2 = False

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if war and event.key == pg.K_ESCAPE:
                war = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if chromerect.collidepoint(pg.mouse.get_pos()) and popup1ok and popup2ok and not chrome and not war and not music:
                chrome = True
            if musicrect.collidepoint(pg.mouse.get_pos()) and popup1ok and popup2ok and not chrome and not war and not music:
                music = True
            if warrect.collidepoint(pg.mouse.get_pos()) and popup1ok and popup2ok and not chrome and not war and not music:
                war = True
                playsound1 = True

            if not popup1ok and okbutton.collidepoint(pg.mouse.get_pos()) and frame >= 180:
                popup1ok = True
                popup2ok = False
                currentframe = frame
            if popup1ok and not popup2ok and okbutton.collidepoint(pg.mouse.get_pos()) and frame-currentframe >= 240:
                popup2ok = True
            
            if chrome and okbutton.collidepoint(pg.mouse.get_pos()):
                chrome = False
                chromesound = True

            if music and playmusicrect.collidepoint(pg.mouse.get_pos()):
                playmusic = True

            if music and playmusic and okbutton.collidepoint(pg.mouse.get_pos()):
                musicsound = True
                playmusic2 = True
                playmusic = False
                playsound3 = True

            if playmusic2 and winampclose.collidepoint(pg.mouse.get_pos()):
                playsound3 = True
                playsound4 = True
                playmusic = False
                playmusic2 = False
                mixer.Channel(6).stop()

            if music and musicclose.collidepoint(pg.mouse.get_pos()):
                music = False
                playmusic = False
                musicsound = False
                playsound3 = True
                playsound4 = True
                playmusic2 = False
                mixer.Channel(6).stop()
            
            if war and okbutton.collidepoint(pg.mouse.get_pos()):
                running = False



    
    frame += 1
    
    screen.fill((0, 0, 0))
    screen.blit(mainbg, mainbg_rect)
    screen.blit(chromeicon, chromeicon_rect)
    screen.blit(chrometext, chrometext_rect)
    screen.blit(musicicon, musicicon_rect)
    screen.blit(musictext, musictext_rect)
    screen.blit(wardeclarer, wardeclarer_rect)
    screen.blit(wardeclarertext, wardeclarertext_rect)
    screen.blit(wardeclarertext2, wardeclarertext2_rect)

    if frame >= 180 and not popup1ok:
        if playsound1:
            mixer.Channel(1).play(mixer.Sound("assets/sfx/nyeetoh.mp3"))
            playsound1 = False
        screen.blit(popup1, popup1_rect)

    if popup1ok and not popup2ok and frame-currentframe >= 240:
        if playsound2:
            mixer.Channel(1).play(mixer.Sound("assets/sfx/nyeetoh.mp3"))
            playsound2 = False
        screen.blit(popup2, popup2_rect)

    
    if chrome:
        if chromesound:
            mixer.Channel(1).play(mixer.Sound("assets/sfx/russian woman speaking.mp3"))
            chromesound = False
        screen.blit(chromepopup, chromepopup_rect)
    
    if music:
        screen.blit(musicfolder, musicfolder_rect)
        if playmusic:
            screen.blit(musicpopup, musicpopup_rect)
            if playsound3:
                mixer.Channel(6).play(mixer.Sound("assets/sfx/russian man speaking.mp3"))
                playsound3 = False
        if playmusic2:
            screen.blit(winamp, winamp_rect)
            if playsound4:
                mixer.Channel(6).play(mixer.Sound("assets/sfx/redalert.mp3"))
                playsound4 = False
            
    if war:
        screen.blit(wardeclarerwarn, wardeclarerwarn_rect)
        if playsound1:
            mixer.Channel(6).play(mixer.Sound("assets/sfx/nyeetoh.mp3"))
            playsound1 = False
        
    screen.blit(cursor, pg.mouse.get_pos())

    pg.display.flip()
    clock.tick(60)


usa = False
nazi = False
frame = 0
currentframe = 0

mixer.Channel(6).play(mixer.Sound("assets/sfx/clearsky.mp3"), -1)
mixer.Channel(6).set_volume(0.5)

while war:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if frame >= 480:
                if wardeclarerline3_rect.collidepoint(pg.mouse.get_pos()):
                    usa = True
                    currentframe = frame
                if wardeclarerline4_rect.collidepoint(pg.mouse.get_pos()):
                    nazi = True
                    currentframe = frame

    frame += 1

    screen.fill((0, 0, 0))
    screen.blit(wardeclarerbg, wardeclarerbg_rect)

    if 240 >= frame >= 60:
        screen.blit(wardeclarerline1, wardeclarerline1_rect)
    if 480 >= frame >= 240:
        screen.blit(wardeclarerline2, wardeclarerline2_rect)
    if frame >= 480 and not usa and not nazi:
        screen.blit(wardeclarerline3, wardeclarerline3_rect)
        screen.blit(wardeclarerline4, wardeclarerline4_rect)

    if usa and frame-currentframe >= 60:
        screen.blit(wardeclarerline5, wardeclarerline5_rect)
        pg.display.flip()
        time.sleep(2)
        while rocketx > 274:
            screen.fill((0, 0, 0))
            screen.blit(wardeclarerbg, wardeclarerbg_rect)
            screen.blit(rocket, rocket_rect)
            rocketx -= 5
            if rockety < 427:
                rockety += 1
            rocket_rect = rocket.get_rect(center=(rocketx, rockety))
            screen.blit(cursor, pg.mouse.get_pos())
            pg.display.flip()
            clock.tick(60)
        screen.blit(boom, boom.get_rect(center=(274, 427)))
        mixer.Channel(5).play(mixer.Sound("assets/sfx/nuc.mp3"))
        pg.display.flip()
        time.sleep(2)
        war = False
    
    if nazi and frame-currentframe >= 60:
        screen.blit(wardeclarerline5, wardeclarerline5_rect)
        pg.display.flip()
        time.sleep(2)
        while rocketx > 900:
            screen.fill((0, 0, 0))
            screen.blit(wardeclarerbg, wardeclarerbg_rect)
            screen.blit(rocket, rocket_rect)
            rocketx -= 5
            if rockety < 340:
                rockety += 1
            rocket_rect = rocket.get_rect(center=(rocketx, rockety))
            screen.blit(cursor, pg.mouse.get_pos())
            pg.display.flip()
            clock.tick(60)
        screen.blit(boom, boom.get_rect(center=(900, 340)))
        mixer.Channel(5).play(mixer.Sound("assets/sfx/nuc.mp3"))
        pg.display.flip()
        time.sleep(2)
        war = False
    
    screen.blit(cursor, pg.mouse.get_pos())
    pg.display.flip()
    clock.tick(60)

mixer.Channel(6).play(mixer.Sound("assets/sfx/nyeetoh.mp3"))
while True:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if okbutton.collidepoint(pg.mouse.get_pos()):
                shutdown()

    screen.fill((0, 0, 0))
    screen.blit(mainbg, mainbg_rect)
    screen.blit(chromeicon, chromeicon_rect)
    screen.blit(chrometext, chrometext_rect)
    screen.blit(musicicon, musicicon_rect)
    screen.blit(musictext, musictext_rect)
    screen.blit(wardeclarer, wardeclarer_rect)
    screen.blit(wardeclarertext, wardeclarertext_rect)
    screen.blit(wardeclarertext2, wardeclarertext2_rect)
    screen.blit(wardeclarererror, wardeclarererror_rect)
    screen.blit(cursor, pg.mouse.get_pos())
    pg.display.flip()
    clock.tick(60)
