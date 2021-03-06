import GlobalVariables
from Enemy import enemy
from Particle import particle
from Poly import poly
from Projectile import projectile
from gameFunctions import *


# the basher is a bogey that charges the player
class basher(enemy):
    def __init__(this, pos):
        enemy.__init__(this, pos)
        this.form = poly((5, 0), (3, 3), (0, 5), (-5, 4), (-2, 0), (-5, -4), (0, -5), (3, -3))
        this.form.scale = 3
        this.health = 6

    def kill(this):
        enemy.kill(this)
        GlobalVariables.sounds[10].play()
        getPoints(200)
        this.burst()

    def burst(this):
        for i in range(20):
            if (randChance(50)):
                vel = multPoint(xyComponent(direction(this.vel) - (math.pi / 2) * randRange(1)), randRange(4, 1))
            else:
                vel = multPoint(xyComponent(direction(this.vel) + (math.pi / 2) * randRange(1)), randRange(4, 1))
            if (randChance(50)):
                col = (255, 150, 0)
            else:
                col = (255, 255, 0)
            part = particle(this.pos, vel, col, 4)
            part.life = randRange(30, 10)
            GlobalVariables.particles.append(part)

    def update(this):
        enemy.update(this)
        acc = 0.3
        if (distance(this.pos, GlobalVariables.p1.pos) > 300):
            acc = 0.1
        this.vel = multPoint(this.vel, 0.94)
        this.vel = addPoints(this.vel, multPoint(normal(this.pos, GlobalVariables.p1.pos), acc))

    def draw(this):
        '''renders the basher'''
        this.form.pos = this.pos
        this.form.angle = direction(this.vel)
        this.form.fill = (100, 20, 0)
        this.form.color = (255, 50, 0)
        this.form.thickness = 2
        GlobalVariables.maincam.toDraw(this.form)

    def hit(this, ob):
        enemy.hit(this, ob)
        if (not baseIs(ob, projectile)):
            this.kill()
