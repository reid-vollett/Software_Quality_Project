from ezmath import *
import GlobalVariables
from Item import item
from Poly import poly

# quadShooter fires your weapon in four different directions
class quadShooter(item):
    def __init__(this, pos):
        item.__init__(this, pos, -1)
        this.life = 500
        this.powersprite = 6

    def doPower(this, event, params):
        if (this.life <= 0):
            if (this in GlobalVariables.p1.powerups):
                GlobalVariables.p1.powerups.remove(this)
            return
        if (event == 1):
            if (params.fireDelay > 0):
                this.life -= params.fireDelay
            else:
                this.life -= 1
            pammo = params.ammo
            params.ammo = 1000
            ang = math.pi / 2
            for i in range(3):
                params.fire(GlobalVariables.p1.pos, GlobalVariables.p1.angle + ang, GlobalVariables.p1.vel)
                ang += math.pi / 2
            params.ammo = pammo

    def pDraw(this):
        ang = GlobalVariables.p1.angle + math.pi / 2
        for i in range(3):
            tpos = xyComponent(ang)
            tpos = multPoint(tpos, 30)
            tpos = addPoints(tpos, GlobalVariables.p1.pos)
            tform = poly((0, 0), (1, 0), (0, 0))
            tform.scale = this.life / 30
            tform.pos = tpos
            tform.angle = ang
            tform.color = (255, 255, 0)
            tform.thickness = 2
            GlobalVariables.maincam.toDraw(tform)
            ang += math.pi / 2

    def replenish(this):
        item.replenish(this)
        this.life = 500

    def grab(this):
        item.grab(this)
        this.life = 500
