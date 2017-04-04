from ezmath import*

from Projectile import projectile
from Particle import particle
from Circ import circ

class ionBullet(projectile):
    def __init__(this, pos, aim, speed):
        '''initializes an ionBullet projectile, used for the ionCannon weapon'''
        projectile.__init__(this, True, pos, aim, speed)

    def burst(this, particles, maincam):
        '''the bullet produces a small green flash when it collides'''
        for i in range(2):
            part = particle(this.pos, randPoint(30), (0, 255, 50))
            part.damping = 0.8
            part.thickness = 4
            particles.append(part)
        blast = circ()
        blast.pos = this.pos
        blast.scale = 10
        blast.color = (0, 255, 100)
        maincam.toDraw(blast)