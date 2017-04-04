import GlobalVariables
from IonBullet import ionBullet
from Poly import poly
from Weapon import weapon
from ezmath import *


# the ion cannon fires a fast traveling steady beam of projectiles
class ionCannon(weapon):
    def __init__(this):
        '''initializes the ion cannon'''
        weapon.__init__(this)
        this.fireDelay = 1
        this.ammo = 300

    def draw(this):
        '''draws the ion cannon's reticle'''
        thick = 3
        col = (0, 255, 255)

        ret1 = poly((0, 0), (1, 0))
        tpos = transform((20, 5), (0, 0), GlobalVariables.p1.angle)
        ret1.pos = addPoints(tpos, GlobalVariables.p1.pos)
        ret1.thickness = thick
        ret1.color = col
        ret1.scale = this.ammo / 10
        ret1.angle = GlobalVariables.p1.angle
        ret2 = poly((0, 0), (1, 0))
        tpos = transform((20, -5), (0, 0), GlobalVariables.p1.angle)
        ret2.pos = addPoints(tpos, GlobalVariables.p1.pos)
        ret2.thickness = thick
        ret2.color = col
        ret2.scale = this.ammo / 10
        ret2.angle = GlobalVariables.p1.angle

        GlobalVariables.maincam.toDraw(ret1)
        GlobalVariables.maincam.toDraw(ret2)

    def fire(this, pos, aim, vel):
        '''fires a part of the beam'''
        this.ammo -= 1
        proj = ionBullet(pos, aim, 25)
        proj.vel = addPoints(proj.vel, vel)
        proj.life = 20
        proj.damage = .4
        proj.radius = 20
        proj.color = (0, 255, 155)
        proj.thickness = 4
        GlobalVariables.projectiles.append(proj)

    def trigger(this, pos, aim, vel):
        if (this.ammo <= 0):
            return False
        if (this.firewait <= 0):
            GlobalVariables.sounds[4].play()
            this.fire(pos, aim, vel)
            this.firewait = this.fireDelay
            return True
        return False