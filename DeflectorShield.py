from ezmath import  *

import poly
from Circ import circ
import item

class deflectorShield(item):
    def __init__(this, pos):
        item.__init__(this, pos, -1)
        this.matrix = [True, True, True, True, True, True]
        this.powersprite = 5

    def pUpdate(this, p1, projectiles):
        if (
        not (this.matrix[0] or this.matrix[1] or this.matrix[2] or this.matrix[3] or this.matrix[4] or this.matrix[5])):
            if (this in p1.powerups):
                p1.powerups.remove(this)

        for i in range(6):
            if (not this.matrix[i]):
                continue
            fpos = multPoint(xyComponent(math.pi * 2 * (i / 6)), 30)
            fpos = addPoints(fpos, p1.pos)
            for bullet in projectiles:
                if (bullet.friendly):
                    continue
                if (distance(bullet.pos, fpos) <= 15):
                    bullet.life = 0
                    this.matrix[i] = False
                    this.burst(fpos)
                    break

    def burst(this, pos, sounds, maincam):
        sounds[18].play()
        tform = circ(20)
        tform.pos = pos
        tform.color = (0, 255, 200)
        maincam.toDraw(tform)

    def pDraw(this, maincam):
        itr = 0
        for field in this.matrix:
            if (field):
                anginc = math.pi * 2 * (itr / 6)
                tform = poly((30, -10), (30, 10), (30, 10))
                tform.angle = anginc
                tform.pos = p1.pos
                tform.color = (0, 0, 255)
                tform.thickness = 3
                maincam.toDraw(tform)
            itr += 1

    def replenish(this):
        item.replenish(this)
        this.matrix = [True, True, True, True, True, True]
