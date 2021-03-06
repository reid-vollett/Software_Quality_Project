

import GlobalVariables
from Img import img
from Poly import poly
from ezmath import *


# items are powerups that are dropped from enemies and the player can pick up
class item:
    def __init__(this, pos, power):
        '''initializes an item object'''
        this.pos = pos
        this.form = poly((10, 0), (7, 7), (0, 10), (-7, 7), (-10, 0), (-7, -7), (0, -10), (7, -7))
        this.form.color = (0, 0, 255)
        this.form.scale = 1.5
        this.life = 600
        this.pow = power
        this.radius = 20
        this.powersprite = power

    def randItem(pos):
        '''static: returns a random item'''
        overShield = importOverShield()
        quadShooter = importQuadShooter()
        deflectorShield = importDeflectorShield()
        rand = random.randrange(-3, 4)
        if (rand >= 0):
            return item(pos, rand)
        else:
            if (rand == -1):
                return overShield(pos)
            if (rand == -2):
                return deflectorShield(pos)
            if (rand == -3):
                return quadShooter(pos)

    def grab(this):
        '''gives the item to the specified player'''
        spreadGun = importSpreadGun()
        ionCannon = importIonCannon()
        rapidGun = importRapidGun()
        missileLauncher = importMissileLauncher()
        if (this in GlobalVariables.items):
            GlobalVariables.items.remove(this)
            GlobalVariables.sounds[7].play()
        if (this.pow == -1):
            this.tryAddPower()
        if (this.pow == 0):
            GlobalVariables.p1.powerWep = spreadGun()
        if (this.pow == 1):
            GlobalVariables.p1.powerWep = ionCannon()
        if (this.pow == 2):
            GlobalVariables.p1.powerWep = rapidGun()
        if (this.pow == 3):
            GlobalVariables.p1.powerWep = missileLauncher()

    def tryAddPower(this):
        for pow in GlobalVariables.p1.powerups:
            if (type(this) is type(pow)):
                pow.replenish()
                return
        GlobalVariables.p1.powerups.append(this)

    def update(this):
        '''handles the logic step for the current instance'''
        if (this.life <= 0):
            if (this in GlobalVariables.items):
                GlobalVariables.items.remove(this)
        if (collision(this, GlobalVariables.p1)):
            this.grab()
        this.life -= 1

    def draw(this):
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
        GlobalVariables.maincam.toDraw(this.form)
        # the power's icon image
        vecimg = img(GlobalVariables.powersprites[this.powersprite])
        vecimg.pos = this.pos
        GlobalVariables.maincam.toDraw(vecimg)

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