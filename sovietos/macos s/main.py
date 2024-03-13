import pygame as pg, sys, time, pygame.mixer as mixer, os, random

def create_rect(width, height, border, color, border_color):
    surf = pg.Surface((width+border*2, height+border*2), pg.SRCALPHA)
    pg.draw.rect(surf, color, (border, border, width, height), 0)
    for i in range(1, border):
        pg.draw.rect(surf, border_color, (border-i, border-i, width+5, height+5), 1)
    return surf

pg.init()
w, h = 1920, 1080
screen = pg.display.set_mode((w, h), pg.FULLSCREEN)
surface = pg.display.get_surface()
w, h = size = surface.get_width(), surface.get_height()
pg.display.set_caption("MacOS S soviet")
pg.mouse.set_visible(False)
clock = pg.time.Clock()
mixer.init()


# images
logo = pg.image.load("assets/img/logo.png")
logo = pg.transform.scale(logo, (121, 145))
logo_rect = logo.get_rect(center=(w/2, h/2-200))

bg = pg.image.load("assets/img/bg.png")
bg = pg.transform.scale(bg, (w, h))
bgblur = pg.transform.gaussian_blur(bg, 20)
bg_rect = bg.get_rect(center=(w/2, h/2))

user = pg.image.load("assets/img/user.png")
user = pg.transform.scale(user, (200, 200))
user_rect = user.get_rect(center=(w/2, h/2-100))
password = create_rect(400, 50, 3, (220, 220, 220), (255, 255, 255))
password_rect = password.get_rect(center=(w/2, h/2+100))

icon = pg.image.load("assets/img/ussrlogo.png")
icon = pg.transform.scale(icon, (30, 30))
icon_rect = icon.get_rect(topleft=(20, 10))

batterylogo = pg.image.load("assets/img/batterylogo.png")
batterylogo = pg.transform.scale(batterylogo, (60, 35))
batterylogo_rect = batterylogo.get_rect(topleft=(w-425, 10))

okbutton = pg.image.load("assets/img/okbutton.png")
okbutton = pg.transform.scale(okbutton, (150, 50))

mac = pg.image.load("assets/img/mac.png")
mac_rect = mac.get_rect(center=(w/2, h/2-150))

warnicon = pg.image.load("assets/img/warn.png")
warnicon = pg.transform.scale(warnicon, (100, 100))
warnicon_safari_rect = warnicon.get_rect(center=(w/2-200, h/2-100))

settingsicon = pg.image.load("assets/img/settings.png")
settingsicon = pg.transform.scale(settingsicon, (100, 100))
settingsicon_rect = settingsicon.get_rect(topleft=(w/4+190, h-100))
settingsicon_error_rect = settingsicon.get_rect(center=(w/2-200, h/2-100))

windowbuttons = pg.image.load("assets/img/buttons.png")
windowbuttons = pg.transform.scale(windowbuttons, (160, 80))
windowbuttons_finder_rect = windowbuttons.get_rect(topleft=(w/2-340, h/2-220))

findericon = pg.image.load("assets/img/finder.png")
findericon = pg.transform.scale(findericon, (80, 80))
findericon_rect = findericon.get_rect(topleft=(w/4+10, h-90))

safariicon = pg.image.load("assets/img/safari.png")
safariicon = pg.transform.scale(safariicon, (80, 80))
safariicon_rect = safariicon.get_rect(topleft=(w/4+100, h-90))

# fonts
normalsmallfont = pg.font.Font("assets/fonts/normal.otf", 20)
normalmediumfont = pg.font.Font("assets/fonts/normal.otf", 35)
normalbigfont = pg.font.Font("assets/fonts/normal.otf", 50)
boldbigfont = pg.font.Font("assets/fonts/bold.otf", 50)

# text
username = boldbigfont.render("Blyat", True, (255, 255, 255))
username_rect = username.get_rect(center=(w/2, h/2+35))
printpass = boldbigfont.render("", True, (255, 255, 255))
printpass_rect = printpass.get_rect(topleft=(w/2-205, h/2+105))
passwordincorrect = normalmediumfont.render("Incorrect password", True, (170, 170, 170))
passwordincorrect_rect = passwordincorrect.get_rect(center=(w/2, h/2+160))
file = normalmediumfont.render("File", True, (0, 0, 0))
file_rect = file.get_rect(topleft=(100, 5))
edit = normalmediumfont.render("Edit", True, (0, 0, 0))
edit_rect = edit.get_rect(topleft=(200, 5))
view = normalmediumfont.render("View", True, (0, 0, 0))
view_rect = view.get_rect(topleft=(300, 5))
cyka = normalmediumfont.render("Cyka", True, (0, 0, 0))
cyka_rect = cyka.get_rect(topleft=(400, 5))
window = normalmediumfont.render("Window", True, (0, 0, 0))
window_rect = window.get_rect(topleft=(500, 5))
help = normalmediumfont.render("Help", True, (0, 0, 0))
help_rect = help.get_rect(topleft=(660, 5))
clocko = normalmediumfont.render("Mon 40 May  69:420", True, (0, 0, 0))
clocko_rect = clocko.get_rect(topleft=(w-350, 5))

dropdown_logo_about = normalmediumfont.render("About This Mac", True, (0, 0, 0))
dropdown_logo_about_rect = dropdown_logo_about.get_rect(topleft=(10, 50))
dropdown_logo_pref = normalmediumfont.render("System Preferences", True, (0, 0, 0))
dropdown_logo_pref_rect = dropdown_logo_pref.get_rect(topleft=(10, 100))
dropdown_logo_shutdown = normalmediumfont.render("Shutdown", True, (120, 120, 120))
dropdown_logo_shutdown_rect = dropdown_logo_shutdown.get_rect(topleft=(10, 150))
dropdown_logo_lock = normalmediumfont.render("Lock Screen", True, (0, 0, 0))
dropdown_logo_lock_rect = dropdown_logo_lock.get_rect(topleft=(10, 200))
dropdown_logo_logout = normalmediumfont.render("Log Out Blyat...", True, (0, 0, 0))
dropdown_logo_logout_rect = dropdown_logo_logout.get_rect(topleft=(10, 250))

dropdown_edit_expired1 = normalmediumfont.render("Your KGB+ Subscription", True, (0, 0, 0))
dropdown_file_expired1_rect = dropdown_edit_expired1.get_rect(topleft=(110, 50))
dropdown_edit_expired1_rect = dropdown_edit_expired1.get_rect(topleft=(210, 50))
dropdown_edit_expired2 = normalmediumfont.render("has expired.", True, (0, 0, 0))
dropdown_file_expired2_rect = dropdown_edit_expired2.get_rect(topleft=(110, 100))
dropdown_edit_expired2_rect = dropdown_edit_expired2.get_rect(topleft=(210, 100))
dropdown_edit_expired3 = normalmediumfont.render("Since we cannot verify if", True, (0, 0, 0))
dropdown_file_expired3_rect = dropdown_edit_expired3.get_rect(topleft=(110, 150))
dropdown_edit_expired3_rect = dropdown_edit_expired3.get_rect(topleft=(210, 150))
dropdown_edit_expired4 = normalmediumfont.render("you are not a capitalist pig,", True, (0, 0, 0))
dropdown_file_expired4_rect = dropdown_edit_expired4.get_rect(topleft=(110, 200))
dropdown_edit_expired4_rect = dropdown_edit_expired4.get_rect(topleft=(210, 200))
dropdown_edit_expired5 = normalmediumfont.render("the option to create or edit", True, (0, 0, 0))
dropdown_file_expired5_rect = dropdown_edit_expired5.get_rect(topleft=(110, 250))
dropdown_edit_expired5_rect = dropdown_edit_expired5.get_rect(topleft=(210, 250))
dropdown_edit_expired6 = normalmediumfont.render("files has been disabled.", True, (0, 0, 0))
dropdown_file_expired6_rect = dropdown_edit_expired6.get_rect(topleft=(110, 300))
dropdown_edit_expired6_rect = dropdown_edit_expired6.get_rect(topleft=(210, 300))

dropdown_view_window = create_rect(w/2, h/2, 5, (70, 70, 70), (0, 0, 0))
dropdown_view_windowtitle = boldbigfont.render("Blyat.", True, (255, 255, 255))
dropdown_view_windowtitle_rect = dropdown_view_windowtitle.get_rect(center=(w/2, h/2-270))
dropdown_view_row1 = normalmediumfont.render("Since we determined that you are propably an american spy,", True, (255, 255, 255))
dropdown_view_row1_rect = dropdown_view_row1.get_rect(topleft=(w/2-470, h/2-200))
dropdown_view_row2 = normalmediumfont.render("your access has been blocked.", True, (255, 255, 255))
dropdown_view_row2_rect = dropdown_view_row2.get_rect(topleft=(w/2-470, h/2-150))
dropdown_view_row3 = normalmediumfont.render("To avoid further damages, your mac will explode in:", True, (255, 255, 255))
dropdown_view_row3_rect = dropdown_view_row3.get_rect(topleft=(w/2-470, h/2-100))
explodetimer = 10
dropdown_view_timer = boldbigfont.render(str(explodetimer), True, (255, 255, 255))
dropdown_view_timer_rect = dropdown_view_timer.get_rect(center=(w/2, h/2+20))
dropdown_view_okbutton = boldbigfont.render("OK", True, (255, 255, 255))
dropdown_view_okbutton_rect = dropdown_view_okbutton.get_rect(center=(w/2, h/2+230))

findertitle = normalbigfont.render("Capitalist files finder", True, (0, 0, 0))
findertitle_rect = findertitle.get_rect(center=(w/2, h/2-150))
findersubtitle = normalsmallfont.render("Finding capitalist files and deleting them...", True, (0, 0, 0))
findersubtitle_rect = findersubtitle.get_rect(topleft=(w/2-280, h/2-100))
finderprogressbar = create_rect(560, 15, 3, (0, 0, 0), (255, 255, 255))
finder2title = normalmediumfont.render("ALL "+str(random.randint(50, 2500))+" CAPITALIST FILES", True, (0, 0, 0))
finder2title_rect = finder2title.get_rect(topleft=(w/2-150, h/2-150))
finder2title2 = normalmediumfont.render("ARE NOW DELETED!!!", True, (0, 0, 0))
finder2title2_rect = finder2title2.get_rect(topleft=(w/2-150, h/2-100))
okbutton_finder2_rect = okbutton.get_rect(center=(w/2+150, h/2+50))

dropdown_cyka_blyat = normalmediumfont.render("Blyat", True, (0, 0, 0))
dropdown_cyka_blyat_rect = dropdown_cyka_blyat.get_rect(topleft=(410, 50))

dropdown_window_row1 = normalmediumfont.render("This is not windows", True, (0, 0, 0))
dropdown_window_row1_rect = dropdown_window_row1.get_rect(topleft=(510, 50))
dropdown_window_row2 = normalmediumfont.render("you capitalist dog!!!", True, (0, 0, 0))
dropdown_window_row2_rect = dropdown_window_row2.get_rect(topleft=(510, 100))

taskbar = create_rect(w/2, 100, 3, (225, 225, 225), (225, 225, 225))
taskbar_rect = (w/4, h-100)

safarierrortext1 = normalmediumfont.render("Safari has crashed for no", True, (0, 0, 0))
safarierrortext1_rect = safarierrortext1.get_rect(topleft=(w/2-120, h/2-150))
safarierrortext2 = normalmediumfont.render("f**king reason, you blyat! ", True, (0, 0, 0))
safarierrortext2_rect = safarierrortext2.get_rect(topleft=(w/2-120, h/2-100))
okbutton_safarierror_rect = okbutton.get_rect(center=(w/2+250, h/2+50))
windowbuttons_safari_rect = windowbuttons.get_rect(topleft=(w/2-620, h/2-410))
windowbuttons_safarierror_rect = windowbuttons.get_rect(topleft=(w/2-340, h/2-220))

settingserrortext1 = normalmediumfont.render("You can't change the settings, only our", True, (0, 0, 0))
settingserrortext1_rect = settingserrortext1.get_rect(topleft=(w/2-120, h/2-150))
settingserrortext2 = normalmediumfont.render("glorious leader Stalin can change them! ", True, (0, 0, 0))
settingserrortext2_rect = settingserrortext2.get_rect(topleft=(w/2-120, h/2-100))
okbutton_settingserror_rect = okbutton.get_rect(center=(w/2+350, h/2+50))
windowbuttons_settingserror_rect = windowbuttons.get_rect(topleft=(w/2-340, h/2-220))


about_title = boldbigfont.render("Macintosh SOVIET", True, (0, 0, 0))
about_title_rect = about_title.get_rect(center=(w/2, h/2-320))
about_chip = normalsmallfont.render("         chip   M69              ", True, (0, 0, 0))
about_chip_rect = about_chip.get_rect(center=(w/2, h/2-20))
about_memory = normalsmallfont.render("   Memory   420TB            ", True, (0, 0, 0))
about_memory_rect = about_memory.get_rect(center=(w/2, h/2))
about_serial = normalsmallfont.render("Serial Number   1L0V3ST4L1N      ", True, (0, 0, 0))
about_serial_rect = about_serial.get_rect(center=(w/2, h/2+20))
about_os = normalsmallfont.render("                  MacOS   S SOVIET 69.420.1", True, (0, 0, 0))
about_os_rect = about_os.get_rect(center=(w/2, h/2+40))
windowbuttons_about_rect = windowbuttons.get_rect(topleft=(w/2-285, h/2-420))

userinput = True
while userinput:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            userinput = False
        if event.type == pg.MOUSEBUTTONDOWN:
            userinput = False

# startup
pg.mixer.Channel(7).play(pg.mixer.Sound("assets/sfx/oldanthem.mp3"))
screen.blit(logo, logo_rect)
pg.display.flip()
time.sleep(3.5)
pg.mixer.Channel(7).stop()
screen.blit(create_rect(400, 15, 3, (0, 0, 0), (255, 255, 255)), (w/2-200, h/2+300))
pg.display.flip()
time.sleep(3)

progressbar = 0

load = True
while load:
    screen.fill((0, 0, 0))
    screen.blit(logo, logo_rect)
    screen.blit(create_rect(400, 15, 3, (0, 0, 0), (255, 255, 255)), (w/2-200, h/2+300))
    if progressbar < 150:
        progressbar += 1
    elif progressbar < 400:
        progressbar += 5
    else:
        progressbar += 80
    if progressbar > w-(w/2-200):
        load = False
    screen.blit(create_rect(progressbar, 15, 3, (255, 255, 255), (255, 255, 255)), (w/2-200, h/2+300))
    pg.display.flip()
    clock.tick(20)

screen.fill((0, 0, 0))
pg.display.flip()
time.sleep(4)

login = True
mainloop = True
pg.mouse.set_visible(True)
while mainloop:
    if login:
        showcursor = False
        cursorblink = False
        loaduser = False
        tried = False

        usertext = ""
        printtext = ""

        frame = 0
        while login:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()
                    if showcursor == True:
                        if event.key == pg.K_BACKSPACE:
                            usertext = usertext[:-1]
                            printtext = printtext[:-1]
                        elif event.key == pg.K_RETURN:
                            if usertext == "stalin123":
                                progressbar = 0
                                while True:
                                    screen.blit(bgblur, bg_rect)
                                    screen.blit(user, user_rect)
                                    if progressbar < 400:
                                        progressbar += 10
                                    else:
                                        main = True
                                        break
                                    screen.blit(create_rect(400, 15, 3, (0, 0, 0), (255, 255, 255)), (w/2-200, h/2+100))
                                    screen.blit(create_rect(progressbar, 15, 3, (255, 255, 255), (255, 255, 255)), (w/2-200, h/2+100))
                                    pg.display.flip()
                                    clock.tick(20)
                                    
                                login = False
                            else:
                                tried = True
                        elif len(usertext) < 15 and event.key != pg.K_LSHIFT and event.key != pg.K_LCTRL and event.key != pg.K_RSHIFT and event.key != pg.K_RCTRL and event.key != pg.K_RALT and event.key != pg.K_LALT and event.key != pg.K_TAB and event.key != pg.K_CAPSLOCK and event.key != pg.K_RMETA and event.key != pg.K_LMETA and event.key != pg.K_LSUPER and event.key != pg.K_RSUPER and event.key != pg.K_MODE and event.key != pg.K_HELP and event.key != pg.K_PRINT and event.key != pg.K_SYSREQ and event.key != pg.K_BREAK and event.key != pg.K_MENU and event.key != pg.K_POWER and event.key != pg.K_EURO and event.key != pg.K_CLEAR and event.key != pg.K_INSERT and event.key != pg.K_HOME and event.key != pg.K_PAGEUP and event.key != pg.K_END and event.key != pg.K_PAGEDOWN and event.key != pg.K_UP and event.key != pg.K_DOWN and event.key != pg.K_LEFT and event.key != pg.K_RIGHT and event.key != pg.K_F1 and event.key != pg.K_F2 and event.key != pg.K_F3 and event.key != pg.K_F4 and event.key != pg.K_F5 and event.key != pg.K_F6 and event.key != pg.K_F7 and event.key != pg.K_F8 and event.key != pg.K_F9 and event.key != pg.K_F10 and event.key != pg.K_F11 and event.key != pg.K_F12 and event.key != pg.K_F13 and event.key != pg.K_F14 and event.key != pg.K_F15 and event.key != pg.K_NUMLOCK and event.key != pg.K_SCROLLOCK and event.key != pg.K_PAUSE and event.key != pg.K_PRINT and event.key != pg.K_KP0 and event.key != pg.K_KP1 and event.key != pg.K_KP2 and event.key != pg.K_KP3 and event.key != pg.K_KP4 and event.key != pg.K_KP5 and event.key != pg.K_KP6 and event.key != pg.K_KP7 and event.key != pg.K_KP8:
                            usertext += event.unicode
                            printtext += "*"
                        printpass = boldbigfont.render(printtext, True, (0, 0, 0))
                        printpass_rect = printpass.get_rect(topleft=(w/2-195, h/2+80))
                if event.type == pg.MOUSEBUTTONDOWN:
                    if password_rect.collidepoint(pg.mouse.get_pos()):
                        showcursor = True

            frame += 1
            screen.fill((0, 0, 0))
            if frame < 180:
                screen.blit(bg, bg_rect)
            else:
                screen.blit(bgblur, bg_rect)
                screen.blit(user, user_rect)
                screen.blit(password, password_rect)
                screen.blit(username, username_rect)
            
            if showcursor:
                if frame % 30 == 0:
                    cursorblink = not cursorblink
                if cursorblink:
                    screen.blit(boldbigfont.render("|", True, (0, 0, 0)), (w/2-200+len(printtext)*25, h/2+100-35))

            if tried:
                screen.blit(passwordincorrect, passwordincorrect_rect)

            screen.blit(printpass, printpass_rect)

            pg.display.flip()
            clock.tick(60)

    if main:
        dropdown_logo = False
        dropdown_file = False
        dropdown_edit = False
        dropdown_view = False
        dropdown_cyka = False
        dropdown_window = False
        dropdown_help = False
        finder = False
        finder2 = False
        safari = False
        setterror = False
        playsoundfinder2 = False
        playsoundsafarierror = False
        playsoundsetterror = False
        about = False
        setterror = False
        safarierror = False

        finderprogressbarval = 0
        
        frame = 0
        safariframe = 0
        explodetimer = 10
        while main:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if icon_rect.collidepoint(pg.mouse.get_pos()) and not dropdown_view:
                        dropdown_logo = not dropdown_logo
                        dropdown_file = dropdown_edit = dropdown_cyka = dropdown_window = dropdown_help = False
                    if file_rect.collidepoint(pg.mouse.get_pos()) and not dropdown_view:
                        dropdown_file = not dropdown_file
                        dropdown_logo = dropdown_edit = dropdown_cyka = dropdown_window = dropdown_help = False
                    if edit_rect.collidepoint(pg.mouse.get_pos()) and not dropdown_view:
                        dropdown_edit = not dropdown_edit
                        dropdown_file = dropdown_logo = dropdown_cyka = dropdown_window = dropdown_help = False
                    if view_rect.collidepoint(pg.mouse.get_pos()) and not dropdown_view:
                        dropdown_view = True
                        dropdown_file = dropdown_edit = dropdown_logo = dropdown_cyka = dropdown_window = dropdown_help = False
                        finder = False
                        finder2 = False
                        safari = False
                        setterror = False
                        playsoundfinder2 = False
                        playsoundsafarierror = False
                        playsoundsetterror = False
                        about = False
                        setterror = False
                        safarierror = False
                        mixer.Channel(7).play(pg.mixer.Sound("assets/sfx/explode.mp3"))
                        time.sleep(1)
                    if cyka_rect.collidepoint(pg.mouse.get_pos()) and not dropdown_view:
                        dropdown_cyka = not dropdown_cyka
                        dropdown_file = dropdown_edit = dropdown_logo = dropdown_window = dropdown_help = False
                    if window_rect.collidepoint(pg.mouse.get_pos()) and not dropdown_view:
                        dropdown_window = not dropdown_window
                        dropdown_file = dropdown_edit = dropdown_cyka = dropdown_logo = dropdown_help = False
                    if help_rect.collidepoint(pg.mouse.get_pos()) and not dropdown_view:
                        dropdown_help = not dropdown_help
                        dropdown_file = dropdown_edit = dropdown_cyka = dropdown_window = dropdown_logo = False
                    
                    if findericon_rect.collidepoint(pg.mouse.get_pos()):
                        finder = True
                        finder2 = False
                        finderprogressbarval = 0

                    if okbutton_finder2_rect.collidepoint(pg.mouse.get_pos()):
                        finder2 = False

                    if okbutton_safarierror_rect.collidepoint(pg.mouse.get_pos()):
                        safarierror = False

                    if safariicon_rect.collidepoint(pg.mouse.get_pos()):
                        safari = True
                        safariframe = frame
                        playsoundsafarierror = True

                    if settingsicon_rect.collidepoint(pg.mouse.get_pos()):
                        setterror = True
                        playsoundsetterror = True

                    if okbutton_settingserror_rect.collidepoint(pg.mouse.get_pos()) or windowbuttons_settingserror_rect.collidepoint(pg.mouse.get_pos()):
                        setterror = False

                    if dropdown_logo:
                        if dropdown_logo_about_rect.collidepoint(pg.mouse.get_pos()):
                            about = True
                        if dropdown_logo_pref_rect.collidepoint(pg.mouse.get_pos()):
                            setterror = True
                            playsoundsetterror = True
                        #if dropdown_logo_shutdown_rect.collidepoint(pg.mouse.get_pos()):
                            #pg.quit()
                            #sys.exit()
                        if dropdown_logo_lock_rect.collidepoint(pg.mouse.get_pos()):
                            usertext = ""
                            printtext = ""
                            printpass = boldbigfont.render("", True, (0, 0, 0))
                            main = False
                            login = True
                        if dropdown_logo_logout_rect.collidepoint(pg.mouse.get_pos()):
                            usertext = ""
                            printtext = ""
                            printpass = boldbigfont.render("", True, (0, 0, 0))
                            main = False
                            login = True
                        
                    if about:
                        if windowbuttons_about_rect.collidepoint(pg.mouse.get_pos()):
                            about = False

            screen.fill((0, 0, 0))
            screen.blit(bg, bg_rect)
            screen.blit(create_rect(w, 50, 3, (225, 225, 225), (225, 225, 225)), (0, 0))
            screen.blit(icon, icon_rect)
            screen.blit(batterylogo, batterylogo_rect)
            screen.blit(file, file_rect)
            screen.blit(edit, edit_rect)
            screen.blit(view, view_rect)
            screen.blit(cyka, cyka_rect)
            screen.blit(window, window_rect)
            screen.blit(help, help_rect)
            screen.blit(clocko, clocko_rect)
            screen.blit(taskbar, taskbar_rect)
            screen.blit(findericon, findericon_rect)
            screen.blit(safariicon, safariicon_rect)
            screen.blit(settingsicon, settingsicon_rect)

            if dropdown_logo:
                screen.blit(create_rect(400, 250, 3, (225, 225, 225), (0, 0, 0)), (0, 50))
                screen.blit(dropdown_logo_about, dropdown_logo_about_rect)
                pg.draw.line(screen, (0, 0, 0), (0, 100), (400, 100), 3)
                screen.blit(dropdown_logo_pref, dropdown_logo_pref_rect)
                pg.draw.line(screen, (0, 0, 0), (0, 150), (400, 150), 3)
                screen.blit(dropdown_logo_shutdown, dropdown_logo_shutdown_rect)
                screen.blit(dropdown_logo_lock, dropdown_logo_lock_rect)
                screen.blit(dropdown_logo_logout, dropdown_logo_logout_rect)

            if dropdown_file:
                screen.blit(create_rect(400, 300, 3, (225, 225, 225), (0, 0, 0)), (100, 50))
                screen.blit(dropdown_edit_expired1, dropdown_file_expired1_rect)
                screen.blit(dropdown_edit_expired2, dropdown_file_expired2_rect)
                screen.blit(dropdown_edit_expired3, dropdown_file_expired3_rect)
                screen.blit(dropdown_edit_expired4, dropdown_file_expired4_rect)
                screen.blit(dropdown_edit_expired5, dropdown_file_expired5_rect)
                screen.blit(dropdown_edit_expired6, dropdown_file_expired6_rect)
            
            if dropdown_edit:
                screen.blit(create_rect(400, 300, 3, (225, 225, 225), (0, 0, 0)), (200, 50))
                screen.blit(dropdown_edit_expired1, dropdown_edit_expired1_rect)
                screen.blit(dropdown_edit_expired2, dropdown_edit_expired2_rect)
                screen.blit(dropdown_edit_expired3, dropdown_edit_expired3_rect)
                screen.blit(dropdown_edit_expired4, dropdown_edit_expired4_rect)
                screen.blit(dropdown_edit_expired5, dropdown_edit_expired5_rect)
                screen.blit(dropdown_edit_expired6, dropdown_edit_expired6_rect)
            
            if dropdown_view:
                if explodetimer > 0 and frame % 60 == 0:
                    explodetimer -= 1
                elif explodetimer <= 0:
                    time.sleep(1)
                    screen.fill((0, 0, 0))
                    pg.display.flip()
                    time.sleep(1)
                    pg.quit()
                    sys.exit()
                screen.fill((35, 35, 35))
                screen.blit(dropdown_view_window, (w/2-w/4, h/2-h/4))
                screen.blit(dropdown_view_windowtitle, dropdown_view_windowtitle_rect)
                screen.blit(dropdown_view_row1, dropdown_view_row1_rect)
                screen.blit(dropdown_view_row2, dropdown_view_row2_rect)
                screen.blit(dropdown_view_row3, dropdown_view_row3_rect)
                dropdown_view_timer = boldbigfont.render(str(explodetimer), True, (255, 255, 255))
                screen.blit(dropdown_view_timer, dropdown_view_timer_rect)

            if dropdown_cyka:
                screen.blit(create_rect(100, 50, 3, (225, 225, 225), (0, 0, 0)), (400, 50))
                screen.blit(dropdown_cyka_blyat, dropdown_cyka_blyat_rect)

            if dropdown_window:
                screen.blit(create_rect(400, 200, 3, (225, 225, 225), (0, 0, 0)), (500, 50))
                screen.blit(dropdown_window_row1, dropdown_window_row1_rect)
                screen.blit(dropdown_window_row2, dropdown_window_row2_rect)

            if about:
                screen.blit(create_rect(500, 800, 3, (225, 225, 225), (0, 0, 0)), (w/2-250, h/2-400))
                screen.blit(about_title, about_title_rect)
                screen.blit(about_chip, about_chip_rect)
                screen.blit(about_memory, about_memory_rect)
                screen.blit(about_serial, about_serial_rect)
                screen.blit(about_os, about_os_rect)
                screen.blit(windowbuttons, windowbuttons_about_rect)
                screen.blit(mac, mac_rect)

            if finder:
                screen.blit(create_rect(600, 300, 3, (225, 225, 225), (0, 0, 0)), (w/2-300, h/2-200))
                screen.blit(findertitle, findertitle_rect)
                screen.blit(findersubtitle, findersubtitle_rect)
                screen.blit(finderprogressbar, (w/2-280, h/2-50))
                screen.blit(windowbuttons, windowbuttons_finder_rect)
                if finderprogressbarval < 560:
                    finderprogressbarval += 1
                else:
                    finder2 = True
                    finder = False
                    playsoundfinder2 = True
                screen.blit(create_rect(finderprogressbarval, 15, 0, (0, 200, 0), (255, 255, 255)), (w/2-280, h/2-50))

            if finder2:
                if playsoundfinder2:
                    mixer.Channel(7).play(pg.mixer.Sound("assets/sfx/br.mp3"))
                    playsoundfinder2 = False
                screen.blit(create_rect(600, 300, 3, (225, 225, 225), (0, 0, 0)), (w/2-300, h/2-200))
                screen.blit(findericon, (w/2-250, h/2-150))
                screen.blit(finder2title, finder2title_rect)
                screen.blit(finder2title2, finder2title2_rect)
                screen.blit(okbutton, okbutton_finder2_rect)
                screen.blit(windowbuttons, windowbuttons_finder_rect)

            if safari:
                screen.blit(create_rect(1200, 800, 3, (225, 225, 225), (0, 0, 0)), (w/2-600, h/2-400))
                screen.blit(windowbuttons, windowbuttons_safari_rect)
                if frame-safariframe > 120:
                    safarierror = True
                    safari = False

            if safarierror:
                if playsoundsafarierror:
                    mixer.Channel(7).play(pg.mixer.Sound("assets/sfx/blyat1.mp3"))
                    playsoundsafarierror = False
                screen.blit(create_rect(700, 300, 3, (225, 225, 225), (0, 0, 0)), (w/2-300, h/2-200))
                screen.blit(warnicon, warnicon_safari_rect)
                screen.blit(safarierrortext1, safarierrortext1_rect)
                screen.blit(safarierrortext2, safarierrortext2_rect)
                screen.blit(okbutton, okbutton_safarierror_rect)
                screen.blit(windowbuttons, windowbuttons_safarierror_rect)

            if setterror:
                if playsoundsetterror:
                    mixer.Channel(7).play(pg.mixer.Sound("assets/sfx/rage1.mp3"))
                    playsoundsetterror = False
                screen.blit(create_rect(800, 300, 3, (225, 225, 225), (0, 0, 0)), (w/2-300, h/2-200))
                screen.blit(settingsicon, settingsicon_error_rect)
                screen.blit(settingserrortext1, settingserrortext1_rect)
                screen.blit(settingserrortext2, settingserrortext2_rect)
                screen.blit(okbutton, okbutton_settingserror_rect)
                screen.blit(windowbuttons, windowbuttons_settingserror_rect)

            frame += 1


            pg.display.flip()
            clock.tick(60)


