from ezmath import *

import weapon
import poly
import projectile

class rapidGun(weapon):
    def __init__(this):
        '''initializes the rapid gun'''
        weapon.__init__(this)
        this.fireDelay = 3
        this.ammo = 140

    def draw(this, p1, maincam):
        '''draws the reticle for the rapid gun'''
        thick = 2
        col = (255, 230, 20)
        ret1 = poly((0, 0), (1, 0))
        tpos = transform((20, 10), (0, 0), p1.angle)
        ret1.pos = addPoints(tpos, p1.pos)
        ret1.thickness = thick
        ret1.color = col
        ret1.scale = this.ammo / 7
        ret1.angle = p1.angle
        ret2 = poly((0, 0), (1, 0))
        tpos = transform((20, -10), (0, 0), p1.angle)
        ret2.pos = addPoints(tpos, p1.pos)
        ret2.thickness = thick
        ret2.color = col
        ret2.scale = this.ammo / 7
        ret2.angle = p1.angle
        maincam.toDraw(ret1)
        maincam.toDraw(ret2)

    def trigger(this, pos, aim, vel, sounds):
        if (this.ammo <= 0):
            return False
        if (this.firewait <= 0):
            sounds[3].play()
            this.fire(pos, aim, vel)
            this.firewait = this.fireDelay
            return True
        return False

    def fire(this, pos, aim, vel, projectiles):
        '''releases a projectile within a small radius'''
        this.ammo -= 1
        proj = projectile(True, pos, aim, 15)
        proj.vel = addPoints(proj.vel, vel)
        proj.pos = addPoints(proj.pos, randCirc(5))
        proj.damage = 0.7
        projectiles.append(proj)

