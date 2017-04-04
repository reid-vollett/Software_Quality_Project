from ezmath import *

from Weapon import weapon
from Poly import poly
from IonBullet import ionBullet

class ionCannon(weapon):
    def __init__(this):
        '''initializes the ion cannon'''
        weapon.__init__(this)
        this.fireDelay = 1
        this.ammo = 300

    def draw(this, p1, maincam):
        '''draws the ion cannon's reticle'''
        thick = 3
        col = (0, 255, 255)

        ret1 = poly((0, 0), (1, 0))
        tpos = transform((20, 5), (0, 0), p1.angle)
        ret1.pos = addPoints(tpos, p1.pos)
        ret1.thickness = thick
        ret1.color = col
        ret1.scale = this.ammo / 10
        ret1.angle = p1.angle
        ret2 = poly((0, 0), (1, 0))
        tpos = transform((20, -5), (0, 0), p1.angle)
        ret2.pos = addPoints(tpos, p1.pos)
        ret2.thickness = thick
        ret2.color = col
        ret2.scale = this.ammo / 10
        ret2.angle = p1.angle

        maincam.toDraw(ret1)
        maincam.toDraw(ret2)

    def fire(this, pos, aim, vel, projectiles):
        '''fires a part of the beam'''
        this.ammo -= 1
        proj = ionBullet(pos, aim, 25)
        proj.vel = addPoints(proj.vel, vel)
        proj.life = 20
        proj.damage = .4
        proj.radius = 20
        proj.color = (0, 255, 155)
        proj.thickness = 4
        projectiles.append(proj)

    def trigger(this, pos, aim, vel, sounds):
        if (this.ammo <= 0):
            return False
        if (this.firewait <= 0):
            sounds[4].play()
            this.fire(pos, aim, vel)
            this.firewait = this.fireDelay
            return True
        return False