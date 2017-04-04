import math
import os
import random
import sys
import time
import pygame
from ezmath import *


from Poly import poly
from Img import img
#from OverShield import overShield
#from DeflectorShield import deflectorShield
#from QuadShooter import quadShooter
#from SpreadGun import spreadGun
#from IonCannon import ionCannon
#from RapidGun import rapidGun
#from MissileLauncher import missileLauncher



class item:
    def __init__(this, pos, power):
        '''initializes an item object'''
        this.overShield = importOverShield()
        this.deflectorShield = importDeflectorShield()
        this.quadShooter = importQuadShooter()
        this.spreadGun = importSpreadGun()
        this.ionCannon = importIonCannon()
        this.rapidGun = importRapidGun()
        this.missileLauncher = importMissileLauncher()

        this.pos = pos
        this.form = poly((10, 0), (7, 7), (0, 10), (-7, 7), (-10, 0), (-7, -7), (0, -10), (7, -7))
        this.form.color = (0, 0, 255)
        this.form.scale = 1.5
        this.life = 600
        this.pow = power
        this.radius = 20
        this.powersprite = power

    def randItem(this, pos):
        '''static: returns a random item'''
        rand = random.randrange(-3, 4)
        if (rand >= 0):
            return item(pos, rand)
        else:
            if (rand == -1):
                return this.overShield(pos)
            if (rand == -2):
                return this.deflectorShield(pos)
            if (rand == -3):
                return this.quadShooter(pos)

    def grab(this, items, sounds, p1):
        '''gives the item to the specified player'''
        if (this in items):
            items.remove(this)
            sounds[7].play()
        if (this.pow == -1):
            this.tryAddPower()
        if (this.pow == 0):
            p1.powerWep = this.spreadGun()
        if (this.pow == 1):
            p1.powerWep = this.ionCannon()
        if (this.pow == 2):
            p1.powerWep = this.rapidGun()
        if (this.pow == 3):
            p1.powerWep = this.missileLauncher()

    def tryAddPower(this, p1):
        for pow in p1.powerups:
            if (type(this) is type(pow)):
                pow.replenish()
                return
        p1.powerups.append(this)

    def update(this, items, p1):
        '''handles the logic step for the current instance'''
        if (this.life <= 0):
            if (this in items):
                items.remove(this)
        if (collision(this, p1)):
            this.grab()
        this.life -= 1

    def draw(this, maincam, powersprites):
        '''renders the item object'''
        col = (0, 0, 255)
        incol = (0, 0, 150)
        if (this.life % 10 < 5):  # makes the item blink
            incol = (0, 100, 70)
        if (this.life <= 200):
            if (this.life % 10 < 5):  # item blinking intensifies if it close to dissapearing
                col = (0, 0, 0)

        this.form.pos = this.pos
        this.form.fill = incol
        this.form.color = col
        this.form.thickness = 4
        maincam.toDraw(this.form)
        # the power's icon image
        vecimg = img(powersprites[this.powersprite])
        vecimg.pos = this.pos
        maincam.toDraw(vecimg)

    def doPower(this, event, params=[]):
        0

    def pDraw(this):
        0

    def pUpdate(this):
        0

    def replenish(this):
        0

def importOverShield():
    import OverShield
    return OverShield.overShield

def importDeflectorShield():
    import DeflectorShield
    return DeflectorShield.deflectorShield

def importQuadShooter():
    import QuadShooter
    return QuadShooter.quadShooter

def importSpreadGun():
    import SpreadGun
    return SpreadGun.spreadGun

def importIonCannon():
    import IonCannon
    return IonCannon.ionCannon

def importRapidGun():
    import RapidGun
    return RapidGun.rapidGun

def importMissileLauncher():
    import MissileLauncher
    return MissileLauncher.missileLauncher