from ezmath import *

import particle
import circ

class motherCowDeath(particle):
    def __init__(this, pos, vel):
        particle.particle.__init__(this, pos, vel, (255, 255, 0), 2)
        this.life = 25

    def update(this, particles):
        if (this.life <= 0 or distance(p1.pos, this.pos) > 500):
            particles.remove(this)
            return
        if (this.life % 3 == 0):
            this.burst()
        this.life -= 1

    def burst(this, maincam, particles):
        blast = circ(random.randrange(20, 35))
        if (randChance(50)):
            blast.color = (255, 150, 0)
        else:
            blast.color = (255, 255, 0)
        tpos = addPoints(this.pos, randPoint(20))
        blast.pos = tpos
        maincam.toDraw(blast)
        for p in range(6):
            part = particle(addPoints(tpos, randCirc(blast.scale / 2)), randCirc(5), blast.color, 3)
            part.life = randRange(30, 10)
            particles.append(part)

    def draw(this):
        0