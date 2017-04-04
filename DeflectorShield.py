from ezmath import  *
import GlobalVariables
from Poly import poly
from Circ import circ
from Item import item

# deflector shield creates a matrix of projectile resistant forcefields around the player
class deflectorShield(item):
    def __init__(this, pos):
        item.__init__(this, pos, -1)
        this.matrix = [True, True, True, True, True, True]
        this.powersprite = 5

    def pUpdate(this):
        if (
        not (this.matrix[0] or this.matrix[1] or this.matrix[2] or this.matrix[3] or this.matrix[4] or this.matrix[5])):
            if (this in GlobalVariables.p1.powerups):
                GlobalVariables.p1.powerups.remove(this)

        for i in range(6):
            if (not this.matrix[i]):
                continue
            fpos = multPoint(xyComponent(math.pi * 2 * (i / 6)), 30)
            fpos = addPoints(fpos, GlobalVariables.p1.pos)
            for bullet in GlobalVariables.projectiles:
                if (bullet.friendly):
                    continue
                if (distance(bullet.pos, fpos) <= 15):
                    bullet.life = 0
                    this.matrix[i] = False
                    this.burst(fpos)
                    break

    def burst(this, pos):
        GlobalVariables.sounds[18].play()
        tform = circ(20)
        tform.pos = pos
        tform.color = (0, 255, 200)
        GlobalVariables.maincam.toDraw(tform)

    def pDraw(this):
        itr = 0
        for field in this.matrix:
            if (field):
                anginc = math.pi * 2 * (itr / 6)
                tform = poly((30, -10), (30, 10), (30, 10))
                tform.angle = anginc
                tform.pos = GlobalVariables.p1.pos
                tform.color = (0, 0, 255)
                tform.thickness = 3
                GlobalVariables.maincam.toDraw(tform)
            itr += 1

    def replenish(this):
        item.replenish(this)
        this.matrix = [True, True, True, True, True, True]
