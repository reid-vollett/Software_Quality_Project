import GlobalVariables
from  Item import item
from Particle import particle
from Poly import poly
from ezmath import *


# overshield creates a protective barrier around the player
class overShield(item):
    def __init__(this, pos):
        '''initializes an overshield item'''
        item.__init__(this, pos, -1)
        this.powersprite = 4

    def grab(this):
        '''gives the player an overshield'''
        item.grab(this)
        GlobalVariables.p1.health = 2
        this.life = 1

    def doPower(this, event, params):
        '''deflects the damage if the player initiates a '0' power event(takes damage)'''
        if (event == 0):
            if (this in GlobalVariables.p1.powerups):
                GlobalVariables.p1.powerups.remove(this)
                this.burst()
            len = (params.radius + GlobalVariables.p1.radius) - distance(GlobalVariables.p1.pos, params.pos)
            norm = normal(params.pos, GlobalVariables.p1.pos)
            GlobalVariables.p1.pos = addPoints(GlobalVariables.p1.pos, multPoint(norm, len))
            GlobalVariables.p1.vel = multPoint(norm, 3)
            GlobalVariables.p1.health = 1

    def pDraw(this):
        tform = poly.circleGon(8, 20)
        tform.color = (0, 100, 255)
        tform.angle = GlobalVariables.p1.angle
        tform.pos = GlobalVariables.p1.pos
        tform.thickness = 3
        GlobalVariables.maincam.toDraw(tform)

    def burst(this):
        for i in range(15):
            part = particle(this.pos, GlobalVariables.p1.vel, (0, 200, 255), 3)
            off = randCirc(10)
            part.vel = addPoints(part.vel, off)
            part.damping = 0.95
            particle.life = 100
            part.pos = addPoints(GlobalVariables.p1.pos, off * 3)
            GlobalVariables.particles.append(part)
