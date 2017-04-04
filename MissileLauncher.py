from ezmath import *
import GlobalVariables
from Weapon import weapon
from Poly import poly
from Missile import missile


# a high-damage power weapon that locks onto nearby enemies
class missileLauncher(weapon):
    def __init__(this):
        '''initializes the missileLauncher'''
        weapon.__init__(this)
        this.fireDelay = 15
        this.ammo = 45

    def draw(this):
        # draws the reticle of the missileLauncher
        col = (255, 100, 0)
        verts1 = [(0, 0), (0, 1), (2, 0)]
        verts2 = [(0, 0), (0, -1), (2, 0)]
        ret1 = poly()
        tpos = transform((20, 10), (0, 0), GlobalVariables.p1.angle)
        ret1.pos = addPoints(tpos, GlobalVariables.p1.pos)
        ret1.angle = GlobalVariables.p1.angle
        ret1.verts = verts1
        ret1.scale = 7 * (this.ammo / 45)
        ret1.thickness = 3
        ret1.color = col
        ret2 = poly()
        tpos = transform((20, -10), (0, 0), GlobalVariables.p1.angle)
        ret2.pos = addPoints(tpos, GlobalVariables.p1.pos)
        ret2.angle = GlobalVariables.p1.angle
        ret2.verts = verts2
        ret2.scale = 7 * (this.ammo / 45)
        ret2.thickness = 3
        ret2.color = col
        GlobalVariables.maincam.toDraw(ret2)
        GlobalVariables.maincam.toDraw(ret1)

    def fire(this, pos, aim, vel):
        '''releases a missile projectile'''
        this.ammo -= 1
        proj = missile(pos, aim, 10)
        proj.vel = addPoints(proj.vel, vel)
        proj.damage = 3
        GlobalVariables.projectiles.append(proj)

    def trigger(this, pos, aim, vel):
        if (this.ammo <= 0):
            return False
        if (this.firewait <= 0):
            GlobalVariables.sounds[6].play()
            this.fire(pos, aim, vel)
            this.firewait = this.fireDelay
            return True
        return False