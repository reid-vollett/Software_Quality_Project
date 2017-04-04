import GlobalVariables
from Asteroid import asteroid
from Player import player
from Poly import poly
from Projectile import projectile
from ezmath import *


class enemyBullet(projectile):
    def __init__(this, pos, aim, speed):
        '''initializes an enemy bullet instance, used by alien objects to fire at the player'''
        projectile.__init__(this, False, pos, aim, speed)
        this.form = poly((3, 0), (0, 3), (-5, 0), (0, -3))

    def update(this):
        '''handles the logic step for the current instance'''
        projectile.update(this)
        # this.checkAsteroidCollisions() #collides with asteroids, but not other enemies
        # if(collision(this, p1)):
        # checks for collision with the player
        # if(this in projectiles):
        # projectiles.remove(this)
        # p1.damage(1)
        # p1.powerEvent(0, this)

    def draw(this):
        '''handles the rendering logic for the current instance'''
        this.form.pos = this.pos
        this.form.angle = direction(this.vel)
        if (this.life % 6 > 2):  # flashes between yellow and red every 3 frames
            this.form.color = (255, 255, 0)
        else:
            this.form.color = (255, 0, 0)
            GlobalVariables.maincam.toDraw(this.form)

    def hit(this, en):
        if (type(en) is player):
            this.life = 0
            this.burst
            return
        elif (type(en) is asteroid):
            this.life = 0
            this.burst
        projectile.hit(this, en)