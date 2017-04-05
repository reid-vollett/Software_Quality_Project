from ezmath import *

import GlobalVariables
from Circ import circ
from Particle import particle
from Projectile import projectile



class ionBullet(projectile):
    def __init__(this, pos, aim, speed):
        '''initializes an ionBullet projectile, used for the ionCannon weapon'''
        projectile.__init__(this, True, pos, aim, speed)

    def burst(this):
        '''the bullet produces a small green flash when it collides'''
        for i in range(2):
            part = particle(this.pos, randPoint(30), (0, 255, 50))
            part.damping = 0.8
            part.thickness = 4
            GlobalVariables.particles.append(part)
        blast = circ()
        blast.pos = this.pos
        blast.scale = 10
        blast.color = (0, 255, 100)
        GlobalVariables.maincam.toDraw(blast)
