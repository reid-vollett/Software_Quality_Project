# SpaceGame.py

# Software Quality Project - Refactoring / Unit Tests

# Game Author:
# Name: Isaiah Smith
# Github: https://github.com/Technostalgic/Asteroids-Too

import os
import sys
import time
import pygame

from Alien import alien
from Asteroid import asteroid
from Basher import basher
from Camera import camera
from Enemy import enemy
from EnemyBullet import enemyBullet
from Item import item
from MotherCow import motherCow
from Player import player
from Poly import poly
from Projectile import projectile
from gameFunctions import *
import GlobalVariables

# used for compiling with pyinstaller
fpath = '.'
if getattr(sys, 'frozen', False):
    fpath = os.path.abspath(os.curdir)
    os.chdir(sys._MEIPASS)

def handleInput():
    '''handles receiving input from the keyboard'''
    # pump() must be called before you attempt to get the keyboard state
    # this is due to the get_pressed function being called after the SDL_GetKeyState() in the
    # gamepy engine, which pump() resets
    pygame.event.pump()

    # stops the function if the game does not have focus
    if (not pygame.key.get_focused()):
        return
    #global activecontr
    #global lastactivec

    itr = 0
    for pressed in GlobalVariables.activecontr:
        GlobalVariables.lastactivec[itr] = pressed
        itr += 1
    keyspressed = pygame.key.get_pressed()
    GlobalVariables.activecontr[0] = keyspressed[GlobalVariables.controls[0]]
    GlobalVariables.activecontr[1] = keyspressed[GlobalVariables.controls[1]]
    GlobalVariables.activecontr[2] = keyspressed[GlobalVariables.controls[2]]
    GlobalVariables.activecontr[3] = keyspressed[GlobalVariables.controls[3]]
    GlobalVariables.activecontr[4] = keyspressed[GlobalVariables.controls[4]]
    GlobalVariables.activecontr[5] = keyspressed[GlobalVariables.controls[5]] or keyspressed[pygame.K_RETURN]

    handleGlobalControls(keyspressed)

def getTappedKeys():
    '''returns they keys that are being pressed on the first frame they are being pressed'''
    #global lastkeyspr
    if (GlobalVariables.lastkeyspr == None):
        # if lastkeyspr is not defined, it sets and returns it to avoid errors
        GlobalVariables.lastkeyspr = pygame.key.get_pressed()
        return GlobalVariables.lastkeyspr
    r = list()
    keyspr = pygame.key.get_pressed()
    itr = 0
    for key in keyspr:
        '''compares the new keypress list to the keys that were presed last frame and stores them in the return list if they are new keypresses'''
        if (key and not GlobalVariables.lastkeyspr[itr]):
            r.append(itr)
        itr += 1

    GlobalVariables.lastkeyspr = keyspr
    return r

def loadHiscore():
    '''loads the highscore from the score file into the global hi variable'''
    #global hi
    file = open(os.path.join(fpath, 'Scores/scores'), 'r')
    scs = file.read()
    GlobalVariables.hi = int(scs.split('\n')[0].split(':')[1])

def init():
    '''initializes the program'''
    print("initializing...", end="")
    #global screen
    global font
    global tinyfont

    # initializes pygame:
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    pygame.display.set_icon(pygame.image.load(compilePath(os.path.join("Graphics", "icon.png"))))
    pygame.display.set_caption("SPACEGAME.EXE")
    pygame.mouse.set_visible(False)
    GlobalVariables.screen = pygame.display.set_mode(GlobalVariables.size)
    font = pygame.font.Font(compilePath("font.ttf"), 32)
    tinyfont = pygame.font.Font(compilePath("font.ttf"), 16)
    loadSprites()
    loadSounds()
    loadHiscore()
    gotoMode(0)

    print("Done!")

def startGame():
    '''starts a new round'''
    #global maincam
    #global p1
    #global mode
    #global score
    #global scoredrop
    #global scoredropper
    #global enemies
    #global stars
    #global projectiles
    #global items
    #global particles
    #global enemyspawndelay
    #global cowspawndelay

    GlobalVariables.enemies = list()
    GlobalVariables.stars = list()
    GlobalVariables.projectiles = list()
    GlobalVariables.items = list()
    GlobalVariables.particles = list()

    gotoMode(1)
    GlobalVariables.score = 0
    GlobalVariables.scoredrop = 500
    GlobalVariables.enemyspawndelay = 0
    GlobalVariables.cowspawndelay = 0
    GlobalVariables.scoredropper = None
    GlobalVariables.maincam = camera()
    GlobalVariables.p1 = player()

    # testpow = item((0, 40), 2)
    # items.append(testpow)
    # testbas = basher((100,100))
    # enemies.append(testbas)
    # testmtc = motherCow((100,100))
    # enemies.append(testmtc)

    # fills in the stars
    for i in range(200):
        GlobalVariables.stars.append(randPoint(500))

def scoreDrops():
    #global scoredropper
    if (GlobalVariables.scoredropper == None):
        return
    ppos = multPoint(xyComponent(GlobalVariables.p1.angle), 100)
    ppos = addPoints(ppos, GlobalVariables.p1.pos)
    if (GlobalVariables.scoredropper <= 0):
        GlobalVariables.scoredropper = None
        print(ppos)
        bonus = item.randItem(ppos)
        GlobalVariables.items.append(bonus)
    else:
        col = (255, 255, 255)
        if (GlobalVariables.scoredropper % 8 > 3):
            col = (100, 100, 100)
        pdraw = poly.circleGon(8, 15)
        pdraw.thickness = 3
        pdraw.color = col
        pdraw.pos = ppos
        GlobalVariables.maincam.toDraw(pdraw)
        GlobalVariables.scoredropper -= 1

def lose():
    '''goes to the endgame screen'''
    gotoMode(2)

def loadSprites():
    '''loads the item icon sprites'''

    GlobalVariables.powersprites.append(pygame.image.load(compilePath(os.path.join("Graphics", "power_spread.png"))))
    GlobalVariables.powersprites.append(pygame.image.load(compilePath(os.path.join("Graphics", "power_ioncannon.png"))))
    GlobalVariables.powersprites.append(pygame.image.load(compilePath(os.path.join("Graphics", "power_rapid.png"))))
    GlobalVariables.powersprites.append(pygame.image.load(compilePath(os.path.join("Graphics", "power_missiles.png"))))
    GlobalVariables.powersprites.append(pygame.image.load(compilePath(os.path.join("Graphics", "power_overshield.png"))))
    GlobalVariables.powersprites.append(pygame.image.load(compilePath(os.path.join("Graphics", "power_deflectorshield.png"))))
    GlobalVariables.powersprites.append(pygame.image.load(compilePath(os.path.join("Graphics", "power_quadshooter.png"))))

def loadSounds():
    '''loads the sound files'''
    GlobalVariables.sounds.append(pygame.mixer.Sound(os.path.join("Sounds", "MenuNavigate.wav")))
    GlobalVariables.sounds.append(pygame.mixer.Sound(os.path.join("Sounds", "MenuSelect.wav")))
    GlobalVariables.sounds.append(pygame.mixer.Sound(os.path.join("Sounds", "Shoot_Default.wav")))  # 2) weapon firing
    GlobalVariables.sounds.append(pygame.mixer.Sound(os.path.join("Sounds", "Shoot_RapidGun.wav")))
    GlobalVariables.sounds.append(pygame.mixer.Sound(os.path.join("Sounds", "Shoot_IonCannon.wav")))
    GlobalVariables.sounds.append(pygame.mixer.Sound(os.path.join("Sounds", "Shoot_SpreadGun.wav")))
    GlobalVariables.sounds.append(pygame.mixer.Sound(os.path.join("Sounds", "Shoot_MissileLauncher.wav")))
    GlobalVariables.sounds.append(pygame.mixer.Sound(os.path.join("Sounds", "PowerUp.wav")))
    GlobalVariables.sounds.append(pygame.mixer.Sound(os.path.join("Sounds", "Death_LargeAsteroid.wav")))  # 8) deaths
    GlobalVariables.sounds.append(pygame.mixer.Sound(os.path.join("Sounds", "Death_SmallAsteroid.wav")))
    GlobalVariables.sounds.append(pygame.mixer.Sound(os.path.join("Sounds", "Death_Alien.wav")))
    GlobalVariables.sounds.append(pygame.mixer.Sound(os.path.join("Sounds", "Death_MotherCow.wav")))
    GlobalVariables.sounds.append(pygame.mixer.Sound(os.path.join("Sounds", "Hit_Default.wav")))  # 12) weapon hits
    GlobalVariables.sounds.append(pygame.mixer.Sound(os.path.join("Sounds", "Hit_MissileLauncher.wav")))
    GlobalVariables.sounds.append(pygame.mixer.Sound(os.path.join("Sounds", "Hit_RapidGun.wav")))
    GlobalVariables.sounds.append(pygame.mixer.Sound(os.path.join("Sounds", "Attack_Alien.wav")))  # 15) enemy attacks
    GlobalVariables.sounds.append(pygame.mixer.Sound(os.path.join("Sounds", "Attack_MotherCow.wav")))
    GlobalVariables.sounds.append(pygame.mixer.Sound(os.path.join("Sounds", "TakeDamage.wav")))
    GlobalVariables.sounds.append(pygame.mixer.Sound(os.path.join("Sounds", "ShieldDeflect.wav")))

def handleGlobalControls(keys):
    '''handles the global controls that work anywhere in the gameloop'''
    if (keys[pygame.K_ESCAPE]):
        pygame.quit()

def handleMenuControls():
    '''handles GUI navigation in the menu screens'''
    #global selection
    if (GlobalVariables.activecontr[5] and (not GlobalVariables.lastactivec[5])):
        select(GlobalVariables.selection)
        GlobalVariables.sounds[1].play()
        GlobalVariables.sounds[1].play()
    if (GlobalVariables.activecontr[1] and (not GlobalVariables.lastactivec[1])):
        GlobalVariables.selection += 1
        GlobalVariables.sounds[0].play()
    if (GlobalVariables.activecontr[0] and (not GlobalVariables.lastactivec[0])):
        GlobalVariables.selection -= 1
        GlobalVariables.sounds[0].play()
    if (GlobalVariables.selection < 0):
        GlobalVariables.selection = 0

def select(selection):
    '''performs an action depending on the currently selected option in the menu'''
    if (GlobalVariables.mode == 0):
        if (selection == 0):
            startGame()
        if (selection == 1):
            gotoMode(3)
        if (selection == 2):
            pygame.mixer.stop()
            pygame.quit()
            raise ()
    elif (GlobalVariables.mode == 3):
        if (selection == 0):
            startGame()
        if (selection == 1):
            gotoMode(0)

def saveScore(name, points):
    '''saves a score under a specified name to the scoreboard'''
    scores = loadScoreboard()
    newscores = list()
    itr = 0
    pt = points
    for scor in scores:
        if (pt >= scor[1]):
            newscores.append((name, pt))
            pt = 0
        newscores.append(scor)
        itr += 1

    while (True):
        try:
            newscores.remove(newscores[5])
        except:
            break

    sbfile = open(os.path.join(fpath, 'Scores/scores'), 'w')
    for scor in newscores:
        sbfile.write(scor[0] + ':' + str(scor[1]) + '\n')

def gotoMode(modenum):
    '''goes to a specified mode and performs necessary actions before and after'''
    #global mode
    #global iteration
    #global selection

    if (modenum == 0):
        loadTitlesprite()
    if (GlobalVariables.mode == 0):
        disposeTitlesprite()

    GlobalVariables.selection = 0
    GlobalVariables.mode = modenum
    GlobalVariables.iteration = 0

def loadTitlesprite():
    '''loads the title screen background image'''
    #global titlesprite
    GlobalVariables.titlesprite = pygame.image.load(compilePath(os.path.join("Graphics", "title.png")))

def disposeTitlesprite():
    '''disposes the title screen background image'''
    titlesprite = None

def loop():
    '''defines the call order of the game loop'''
    #global GlobalVariables.lagcatch
    start = time.time()  # stores the time at the beginning if the step
    # lagcatch dissipates over time
    if (GlobalVariables.lagcatch > 0):
        GlobalVariables.lagcatch -= 0.01
    elif (GlobalVariables.lagcatch < 0):
        GlobalVariables.lagcatch = 0
    handleInput()
    update()
    draw()
    elapsed = time.time() - start  # compares the time at the beginning of the step to now
    sltime = GlobalVariables.framerate - elapsed  # calculates how much time is left before the next step is called
    if (sltime >= 0):  # if that time is above zero, it suspends the thread until the next step is to be called
        time.sleep(sltime)
    else:  # if that time is below zero, a lag has occured, this is where the lag is handled
        # print("lag" + str(sltime) + "s")
        GlobalVariables.lagcatch -= sltime
        handleLag()

def update():
    '''main game logic is handled here'''
    #global iteration
    updateMode()
    GlobalVariables.iteration += 1

def updateNoCol():
    #global iteration
    updateModeNoCol()
    GlobalVariables.iteration += 1

def updateMode():
    '''handles update logic based on the current game mode'''
    if (GlobalVariables.mode == 0):  # main menu
        updateMenu()
    elif (GlobalVariables.mode == 1):  # gameplay
        updateGameplay()
    elif (GlobalVariables.mode == 2):  # name entry
        updateNameEntry()
    elif (GlobalVariables.mode == 3):  # scoreboard
        updateScoreboard()

def updateModeNoCol():
    '''handles update logic based on the current game mode'''
    if (GlobalVariables.mode == 0):  # main menu
        updateMenu()
    elif (GlobalVariables.mode == 1):  # gameplay
        updateGameplayNoCol()
    elif (GlobalVariables.mode == 2):  # name entry
        updateNameEntry()
    elif (GlobalVariables.mode == 3):  # scoreboard
        updateScoreboard()

def updateMenu():
    '''handles update logic for the main menu'''
    #global selection
    handleMenuControls()
    if (GlobalVariables.selection > 2):
        GlobalVariables.selection = 2

def updateGameplay():
    '''handles the update logic for in-game'''
    for part in GlobalVariables.particles:
        part.update()  # updates all the particles
    for proj in GlobalVariables.projectiles:
        proj.update()  # updates all the projectiles
    for en in GlobalVariables.enemies:
        en.update()  # updates all the enemies
    for power in GlobalVariables.items:
        power.update()  # updates all the items
    GlobalVariables.p1.update()  # updates the player
    handleCollisions()
    scoreDrops()
    GlobalVariables.maincam.orient(GlobalVariables.p1.pos, GlobalVariables.p1.angle + math.pi / 2)  # orients the camera to follow the player
    # removes necessary projectiles. they are not removed as the projectile list is updating because it causes an iteration skip which results in some projectiles not getting updated
    for proj in GlobalVariables.projectiles:
        proj.removeCheck()
    spawnEnemies()  # spawns/despawns enemies into the world
    spawnStars()  # spawns/despawns stars around the player as they move
    if (
            GlobalVariables.p1.health == None and GlobalVariables.iteration > 60):  # acts as a makeshift timer to tell the screen to transition to the end screen after the player has been dead for a second
        lose()

def updateGameplayNoCol():
    for part in GlobalVariables.particles:
        part.update()  # updates all the particles
    for proj in GlobalVariables.projectiles:
        proj.update()  # updates all the projectiles
    for en in GlobalVariables.enemies:
        en.update()  # updates all the enemies
    for power in GlobalVariables.items:
        power.update()  # updates all the items
    GlobalVariables.p1.update()  # updates the player
    # handleCollisions()
    scoreDrops()
    GlobalVariables.maincam.orient(GlobalVariables.p1.pos, GlobalVariables.p1.angle + math.pi / 2)  # orients the camera to follow the player
    # removes necessary projectiles. they are not removed as the projectile list is updating because it causes an iteration skip which results in some projectiles not getting updated
    for proj in GlobalVariables.projectiles:
        proj.removeCheck()
    spawnEnemies()  # spawns/despawns enemies into the world
    spawnStars()  # spawns/despawns stars around the player as they move
    if (GlobalVariables.p1.health == None and GlobalVariables.iteration > 60):  # acts as a makeshift timer to tell the screen to transition to the end screen after the player has been dead for a second
        lose()

def updateNameEntry():
    '''updates the name entry screen'''
    #global p1
    # turns the player object into a string that the name on the scoreboard will be saved as so we don't have to create a new variable
    if (not type(GlobalVariables.p1) is str):
        GlobalVariables.scores = loadScoreboard()
        if (GlobalVariables.score < GlobalVariables.scores[4][1]):
            gotoMode(3)
            return
        GlobalVariables.p1 = ""
    tkeys = getTappedKeys()
    # parses the keyboard input into ascii characterss
    for k in tkeys:
        if (k == pygame.K_BACKSPACE):
            GlobalVariables.p1 = GlobalVariables.p1[:len(GlobalVariables.p1) - 1]
        if (k == pygame.K_SPACE):
            GlobalVariables.p1 += ' '
        if (k >= 48 and k <= 57):
            num = "0123456789"
            GlobalVariables.p1 += num[k - 48]
        if (k >= 97 and k <= 122):
            alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            GlobalVariables.p1 += alph[k - 97]

    # limits the name length to 12 characters
    if (len(GlobalVariables.p1) > 12):
        GlobalVariables.p1 = GlobalVariables.p1[:12]

    # if enter is pressed, finish name entry
    if (pygame.K_RETURN in tkeys):
        saveScore(GlobalVariables.p1, GlobalVariables.score)
        gotoMode(3)

def updateScoreboard():
    '''updates the scoreboard menu screen'''
    #global selection
    handleMenuControls()
    if (GlobalVariables.selection > 1):
        GlobalVariables.selection = 1

def draw():
    '''rendering logic handled here'''
    if (GlobalVariables.screen == None):
        print("Cannot draw to screen because screen is not initialized!")
        return
    GlobalVariables.screen.fill((0, 0, 0))
    drawMode()
    pygame.display.flip()

def drawMode():
    '''renders certain ways depending on the game mode'''
    if (GlobalVariables.mode == 0):  # mainmenu
        drawMenu()
    elif (GlobalVariables.mode == 1):  # in game
        drawGameplay()
    elif (GlobalVariables.mode == 2):  # name entry
        drawNameEntry()
    elif (GlobalVariables.mode == 3):  # score board
        drawScoreboard()

def drawMenu():
    '''draws the main title screen'''
    buttonpos = (200, 450)
    selcol = (0, 255, 0)
    if (GlobalVariables.iteration % 10 >= 5):  # selcol flashes btween green and dark green every 5 frames
        selcol = (0, 100, 0)

    # creates the selectable buttons, the flash if they are selcted
    if (GlobalVariables.selection == 0):
        startButton = font.render("START GAME", False, selcol)
    else:
        startButton = font.render("START GAME", False, (255, 255, 255))
    if (GlobalVariables.selection == 1):
        scoresButton = font.render("SCOREBOARD", False, selcol)
    else:
        scoresButton = font.render("SCOREBOARD", False, (255, 255, 255))
    if (GlobalVariables.selection == 2):
        exitButton = font.render("EXIT", False, selcol)
    else:
        exitButton = font.render("EXIT", False, (255, 255, 255))
    selector = font.render(">", False, (255, 255, 255))

    # renders the background
    GlobalVariables.screen.blit(GlobalVariables.titlesprite, (0, 0))
    GlobalVariables.screen.blit(selector, addPoints(buttonpos, (-15, GlobalVariables.selection * 40)))
    GlobalVariables.screen.blit(startButton, addPoints(buttonpos, (0, 0)))
    GlobalVariables.screen.blit(scoresButton, addPoints(buttonpos, (0, 40)))
    GlobalVariables.screen.blit(exitButton, addPoints(buttonpos, (0, 80)))

def drawGameplay():
    '''draws the gameplay'''
    drawStars()
    for part in GlobalVariables.particles:
        part.draw(poly)  # draws all the particles
    for power in GlobalVariables.items:
        power.draw()  # draws all the items
    for proj in GlobalVariables.projectiles:
        proj.draw()  # draws all the projectiles
    for en in GlobalVariables.enemies:
        en.draw()  # draws all the enemies
    GlobalVariables.p1.draw()  # renders the player
    GlobalVariables.maincam.render()  # renders the world objects throught the camera's point of view
    drawScore()

    ##
    # col0 = circ(200)
    # col0.pos = p1.pos
    # col0.thickness = 1
    # col1 = circ(300)
    # col1.pos = p1.pos
    # col1.thickness = 1
    # maincam.renderCirc(col0)
    # maincam.renderCirc(col1)
    ##

def drawNameEntry():
    '''draws the name entry screen'''
    #global p1
    if (not type(GlobalVariables.p1) is str):
        return
    sccol = (255, 255, 0)
    ncol = (0, 255, 255)
    if (GlobalVariables.iteration % 10 >= 5):
        sccol = (255, 150, 0)
        ncol = (0, 100, 255)
    title1 = font.render("YOU PLACED IN THE ", False, (255, 255, 255))
    title2 = font.render("SCOREBOARD!", False, sccol)
    title3 = font.render("ENTER YOUR NAME BELOW:", False, (255, 255, 255))

    GlobalVariables.screen.blit(title1, (10, 300))
    GlobalVariables.screen.blit(title2, (350, 300))
    GlobalVariables.screen.blit(title3, (85, 340))
    ntex = GlobalVariables.p1
    if (len(GlobalVariables.p1) < 12):
        ntex += '_'
    nametext = font.render(ntex, False, ncol)
    GlobalVariables.screen.blit(nametext, (180, 400))

def drawScoreboard():
    '''draws the scoreoard screen'''
    buttonpos = (200, 450)
    scores = loadScoreboard()
    col = (255, 150, 0)
    selcol = (0, 255, 0)
    ycol = (0, 255, 255)
    if (GlobalVariables.iteration % 10 >= 5):
        col = (255, 255, 0)
        selcol = (0, 100, 0)
        ycol = (0, 100, 255)
    title = font.render("---SCOREBOARD---", False, col)
    scoretext = font.render("YOU:                   " + str(GlobalVariables.score), False, ycol)
    if (GlobalVariables.selection == 0):
        startButton = font.render("START GAME", False, selcol)
    else:
        startButton = font.render("START GAME", False, (255, 255, 255))
    if (GlobalVariables.selection == 1):
        menuButton = font.render("MAIN MENU", False, selcol)
    else:
        menuButton = font.render("MAIN MENU", False, (255, 255, 255))

    selector = font.render(">", False, (255, 255, 255))

    itr = 0
    for scor in scores:
        scoreentry = font.render(str(itr + 1) + '. ' + scor[0], False, (0, 255, 0))
        GlobalVariables.screen.blit(scoreentry, (100, 150 + itr * 40))
        scoreentry = font.render(str(scor[1]), False, (0, 255, 0))
        GlobalVariables.screen.blit(scoreentry, (450, 150 + itr * 40))
        itr += 1

    GlobalVariables.screen.blit(title, (150, 50))
    GlobalVariables.screen.blit(selector, addPoints(buttonpos, (-15, GlobalVariables.selection * 40)))
    if (GlobalVariables.score > 0):
        GlobalVariables.screen.blit(scoretext, (150, 380))
    GlobalVariables.screen.blit(startButton, addPoints(buttonpos, (0, 0)))
    GlobalVariables.screen.blit(menuButton, addPoints(buttonpos, (0, 40)))


def drawScore():
    '''draws the score and high score in the upper left of the screen'''
    pygame.sysfont
    text = font.render("SCORE: " + str(int(GlobalVariables.score)), False, (255, 255, 255))
    hitext = tinyfont.render("HI: " + str(GlobalVariables.hi), False, (200, 200, 200))
    GlobalVariables.screen.blit(text, (4, 4))
    GlobalVariables.screen.blit(hitext, (4, 40))

def loadScoreboard():
    '''loads the scores from the score file'''
    loadHiscore()
    r = list()
    file = open(os.path.join(fpath, 'Scores/scores'), 'r')
    dat = file.read()
    spldat = dat.split('\n')
    for scor in spldat:
        if (scor == ""):
            continue
        splscor = scor.split(':')
        r.append((splscor[0], int(splscor[1])))
    return r

def handleLag():
    '''handles the lag by removing non essential game assets'''
    if (GlobalVariables.mode != 1):
        return
    catchup()

    partsr = 0
    asterr = 0
    for part in GlobalVariables.particles:
        if (randChance(50)):
            part.life = 0
            partsr += 1
    for en in GlobalVariables.enemies:
        if (type(en) is asteroid):
            if (en.radius <= 10):
                if (distance(en.pos, GlobalVariables.p1.pos) > 400):
                    GlobalVariables.enemies.remove(en)
                    asterr += 1
                    # print("cleaned up " + str(partsr) + " particles, " +str(asterr) + " asteroids")

def catchup():
    '''updates the game without rendering to save time'''
    #global lagcatch
    itr = 0
    while (GlobalVariables.lagcatch >= GlobalVariables.framerate):
        GlobalVariables.lagcatch -= GlobalVariables.framerate
        start = time.time()
        updateNoCol()
        elapsed = time.time() - start
        GlobalVariables.lagcatch += elapsed
        itr += 1
    GlobalVariables.maincam.drawQuery = list()
    # print("caught up " + str(itr) + " frames")

def handleCollisions():
    handleColLists()
    itr = 0
    for op in GlobalVariables.colcheck0:
        typ = projectile
        if (baseIs(op, enemy)):
            typ = enemy
        opCheckColList(op, GlobalVariables.colcheck0, itr, typ)
        if (collision(GlobalVariables.p1, op)):
            if (baseIs(op, projectile)):
                if (not op.friendly):
                    GlobalVariables.p1.damage(1)
                    GlobalVariables.p1.powerEvent(0, op)
                    op.hit(GlobalVariables.p1)
            else:
                GlobalVariables.p1.damage(1)
                GlobalVariables.p1.powerEvent(0, op)
                op.hit(GlobalVariables.p1)
        itr += 1
    itr = 0
    for op in GlobalVariables.colcheck1:
        typ = projectile
        if (baseIs(op, enemy)):
            typ = enemy
        opCheckColList(op, GlobalVariables.colcheck1, itr, typ)
        itr += 1
    itr = 0
    for op in GlobalVariables.colcheck2:
        typ = projectile
        if (baseIs(op, enemy)):
            typ = enemy
        opCheckColList(op, GlobalVariables.colcheck2, itr, typ)
        itr += 1
    collectBodies()

def opCheckColList(op, clist, itr, optype):
    if (op.cck or op.dead()):
        return
    op.cck = True
    for i in range(itr + 1, len(clist)):
        if (clist[i].dead()):
            continue
        if (baseIs(clist[i], optype)):
            if (optype is projectile):
                if (clist[i].friendly == op.friendly):
                    continue
            else:
                continue
        if (collision(op, clist[i])):
            op.hit(clist[i])
            if (type(clist[i]) is enemyBullet):
                clist[i].hit(op)

def collectBodies():
    itr = 0
    while (itr < len(GlobalVariables.enemies)):
        if (GlobalVariables.enemies[itr].dead()):
            del GlobalVariables.enemies[itr]
            continue
        itr += 1
    itr = 0
    while (itr < len(GlobalVariables.projectiles)):
        if (GlobalVariables.projectiles[itr].dead()):
            del GlobalVariables.projectiles[itr]
            continue
        itr += 1

def handleColLists():
    #global colcheck0
    #global colcheck1
    #global colcheck2
    GlobalVariables.colcheck0 = list()
    GlobalVariables.colcheck1 = list()
    GlobalVariables.colcheck2 = list()
    for en in GlobalVariables.enemies:
        sortToColList(en)
    for proj in GlobalVariables.projectiles:
        sortToColList(proj)

def sortToColList(obj):
    dist = distance(obj.pos, GlobalVariables.p1.pos)
    if (dist <= 200):
        GlobalVariables.colcheck0.append(obj)
        if (dist + obj.radius > 200):
            GlobalVariables.colcheck1.append(obj)
    elif (dist <= 300):
        GlobalVariables.colcheck1.append(obj)
        if (dist - obj.radius <= 200):
            GlobalVariables.colcheck0.append(obj)
        if (dist + obj.radius > 300):
            GlobalVariables.colcheck2.append(obj)
    else:
        GlobalVariables.colcheck2.append(obj)
        if (dist - obj.radius <= 300):
            GlobalVariables.colcheck1.append(obj)

def spawnStars():
    '''spawns/despawns the stars around the player'''
    for star in GlobalVariables.stars:
        if (distance(subtractPoints(star, GlobalVariables.p1.pos)) > 405):
            GlobalVariables.stars.remove(star)

    while (len(GlobalVariables.stars) < 200):
        GlobalVariables.stars.append(addPoints(multPoint(xyComponent(random.random() * math.pi * 2), 400), GlobalVariables.p1.pos))

def spawnEnemies():
    # spawns/despawns the enemies around the player
    #global enemyspawndelay
    #global cowspawndelay

    for en in GlobalVariables.enemies:
        if (distance(subtractPoints(GlobalVariables.p1.pos, en.pos)) > 800):
            GlobalVariables.enemies.remove(en)

    # astsize = iteration / 10000
    astsize = 1
    aliencount = (GlobalVariables.iteration - 1800) / 1800 + 1
    bashercount = (GlobalVariables.iteration - 2000) / 2500 + 1
    if (aliencount < 0):
        aliencount = 0

    if (GlobalVariables.enemyspawndelay <= 0):
        GlobalVariables.enemyspawndelay = 300
        for i in range(3):
            en = asteroid(addPoints(randCirc(500), GlobalVariables.p1.pos), randRange(randRange(randRange(120 * astsize + 10))) + 8)
            en.vel = randPoint(3)
            GlobalVariables.enemies.append(en)

        for i in range(int(aliencount)):
            en = alien(addPoints(randCirc(500), GlobalVariables.p1.pos))
            GlobalVariables.enemies.append(en)

        if (int(bashercount) > 0):
            for i in range(random.randrange(int(bashercount))):
                bs = basher(addPoints(randCirc(randRange(600, 500)), GlobalVariables.p1.pos))
                GlobalVariables.enemies.append(bs)
    GlobalVariables.enemyspawndelay -= 1
    #testing 3500 -> 350
    if (GlobalVariables.iteration > 3500):
        GlobalVariables.cowspawndelay -= 1
        if (GlobalVariables.cowspawndelay <= 0):
            #testing 1200 -> 200
            GlobalVariables.cowspawndelay = 1200
            cow = motherCow(addPoints(randCirc(500), GlobalVariables.p1.pos))
            GlobalVariables.enemies.append(cow)

def compilePath(path):
    '''ignore, used for compiling to a standalone exe with pyinstaller, ended up not doing it'''
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, path)
    return os.path.join(os.path.abspath('.'), path)

def drawStars():
    '''draws the stars'''
    itr = 0
    for star in GlobalVariables.stars:
        pol = poly()
        pol.color = (140, 140, 140)
        pol.verts = [(0, 0)]
        pol.verts.append((0, 1))
        pol.pos = star
        pol.thickness = 2
        verts = GlobalVariables.maincam.renderPoly(pol)
        itr += 1

def main():
    '''main entry point of the gameloop'''
    while (True):
        loop()

init()
# raise Exception()
main()
