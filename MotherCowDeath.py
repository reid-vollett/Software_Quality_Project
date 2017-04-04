from Circ import circ
from Particle import particle
from ezmath import *
from src import GlobalVariables


class motherCowDeath(particle):
    def __init__(this, pos, vel):
        particle.__init__(this, pos, vel, (255, 255, 0), 2)
        this.life = 25

    def update(this):
        if (this.life <= 0 or distance(p1.pos, this.pos) > 500):
            GlobalVariables.particles.remove(this)
            return
        if (this.life % 3 == 0):
            this.burst()
        this.life -= 1

    def burst(this):
        blast = circ(random.randrange(20, 35))
        if (randChance(50)):
            blast.color = (255, 150, 0)
        else:
            blast.color = (255, 255, 0)
        tpos = addPoints(this.pos, randPoint(20))
        blast.pos = tpos
        GlobalVariables.maincam.toDraw(blast)
        for p in range(6):
            part = particle(addPoints(tpos, randCirc(blast.scale / 2)), randCirc(5), blast.color, 3)
            part.life = randRange(30, 10)
            GlobalVariables.particles.append(part)

    def draw(this):
        0