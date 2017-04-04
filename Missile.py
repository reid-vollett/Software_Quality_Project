import GlobalVariables
from gameFunctions import *

from Projectile import projectile
from Poly import poly
from Particle import particle
from Enemy import enemy
from Circ import circ

class missile(projectile):
    def __init__(this, pos, aim, speed):
        '''initializes a missile projectile, used for the missileLauncher weapon'''
        projectile.__init__(this, True, pos, aim, speed)
        this.form = poly((10, 0), (-5, 5), (-5, -5))
        this.form.color = (255, 180, 0)
        this.form.thickness = 2
        this.life = 110
        this.lock = None

    def update(this):
        '''handles the logic step for the current instance'''
        projectile.update(this)
        if (this.life <= 100):
            if (this.lock == None):
                this.search()
            else:
                this.seek(this.lock)
            if (not this.lock in GlobalVariables.enemies):
                this.lock = None

    def search(this):
        '''seeks out an enemy to lock onto'''
        for en in GlobalVariables.enemies:
            if (distance(en.pos, this.pos) <= 150):
                this.lock = en

    def seek(this, en):
        '''homes in to an enemy'''
        if (not en in GlobalVariables.enemies):
            return
        # dampens the velocity to account for course readjustment
        this.vel = multPoint(this.vel, 0.92)
        # adds velocity toward the target
        this.vel = addPoints(this.vel, multPoint(normal(this.pos, en.pos), 1))
        this.thrustParticle()

    def thrustParticle(this):
        '''emits particles to show that it is seeking an enemy'''
        force = multPoint(xyComponent(this.form.angle - math.pi), 0.7)
        part = particle(addPoints(this.pos, randPoint(randRange(4, 6))), multPoint(force, 5), (255, 255, 0))
        part.vel = addPoints(part.vel, this.vel)
        part.life = random.randrange(5, 10)
        part.damping = 0.8
        if (randChance(50)):
            part.color = (200, 200, 0)
        part.thickness = 2
        GlobalVariables.particles.append(part)

    def hit(this, en):
        '''collides with the specified enemy'''
        projectile.hit(this, en)
        for cols in collidingColchecks(this.pos, 30):
            for en in cols:
                if (not baseIs(en, enemy) or en.dead()):
                    continue
                    # damages other enemies in within a radius, acts as splash damage
                if (distance(this.pos, en.pos) < 30):
                    en.health -= 2
                if (en.health <= 0):
                    en.kill()

    def burst(this):
        '''creates a small flash and emits some explosion particles'''
        GlobalVariables.sounds[13].play()
        for i in range(random.randrange(5, 10)):
            part = particle(this.pos, randCirc(5), (255, 255, 0))
            GlobalVariables.particles.append(part)
        blast = circ()
        blast.pos = this.pos
        blast.scale = 30
        blast.color = (255, 255, 100)
        GlobalVariables.maincam.toDraw(blast)