from ezmath import *
import GlobalVariables
from Weapon import weapon
from Poly import poly
from Projectile import projectile

# a gun that shoots 5 fast moving projectiles that spread out and hit multiple targets
class spreadGun(weapon):
    def __init__(this):
        '''initializes the spreadgun'''
        weapon.__init__(this)
        this.fireDelay = 15
        this.ammo = 50

    def draw(this):
        '''draws the spreadgun reticle'''
        thick = 4
        col = (0, 100, 255)

        ret1 = poly((0, 0), (1, .6))
        tpos = transform((20, 10), (0, 0), GlobalVariables.p1.angle)
        ret1.pos = addPoints(tpos, GlobalVariables.p1.pos)
        ret1.thickness = thick
        ret1.color = col
        ret1.scale = this.ammo / 3
        ret1.angle = GlobalVariables.p1.angle
        ret2 = poly((0, 0), (1, -.6))
        tpos = transform((20, -10), (0, 0), GlobalVariables.p1.angle)
        ret2.pos = addPoints(tpos, GlobalVariables.p1.pos)
        ret2.thickness = thick
        ret2.color = col
        ret2.scale = this.ammo / 3
        ret2.angle = GlobalVariables.p1.angle

        GlobalVariables.maincam.toDraw(ret1)
        GlobalVariables.maincam.toDraw(ret2)

    def fire(this, pos, aim, vel):
        '''releases 5 evenly spread projectiles'''
        this.ammo -= 1
        for i in range(5):
            spr = (i - 2) * 0.2
            proj = projectile(True, pos, aim + spr, 15)
            proj.life = 20
            proj.damage = 0.5
            proj.vel = addPoints(proj.vel, vel)
            proj.form = poly((0, -3), (0, 3))
            proj.form.color = (0, 200, 255)
            proj.form.thickness = 4
            GlobalVariables.projectiles.append(proj)

    def trigger(this, pos, aim, vel):
        if (this.ammo <= 0):
            return False
        if (this.firewait <= 0):
            GlobalVariables.sounds[5].play()
            this.fire(pos, aim, vel)
            this.firewait = this.fireDelay
            return True
        return False
