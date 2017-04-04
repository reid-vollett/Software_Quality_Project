import GlobalVariables
from Projectile import projectile
from ezmath import *


# weapons store data relevant to what the player's fire control will do
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

    def trigger(this, pos, aim, vel):
        if (this.ammo <= 0):
            return False
        if (this.firewait <= 0):
            GlobalVariables.sounds[2].play()
            this.fire(pos, aim, vel)
            this.firewait = this.fireDelay
            return True
        return False

    def fire(this, pos, aim, vel):
        proj = projectile(True, pos, aim)
        proj.vel = addPoints(proj.vel, vel)
        GlobalVariables.projectiles.append(proj)
