from ezmath import *

from Projectile import projectile

class weapon:
    def __init__(this):
        '''initializes a weapon object'''
        this.fireDelay = 10
        this.firewait = 0
        this.ammo = 10

    def update(this):
        if (this.firewait > 0):
            this.firewait -= 1

    def draw(this):
        0

    def trigger(this, pos, aim, vel, sounds, projectiles):
        if (this.ammo <= 0):
            return False
        if (this.firewait <= 0):
            sounds[2].play()
            this.fire(pos, aim, vel, projectiles)
            this.firewait = this.fireDelay
            return True
        return False

    def fire(this, pos, aim, vel, projectiles):
        proj = projectile(True, pos, aim)
        proj.vel = addPoints(proj.vel, vel)
        projectiles.append(proj)
