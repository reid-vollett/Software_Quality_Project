from ezmath import *

import item
import poly
import particle

class overShield(item):
    def __init__(this, pos):
        '''initializes an overshield item'''
        item.__init__(this, pos, -1)
        this.powersprite = 4

    def grab(this, p1):
        '''gives the player an overshield'''
        item.grab(this)
        p1.health = 2
        this.life = 1

    def doPower(this, event, params, p1):
        '''deflects the damage if the player initiates a '0' power event(takes damage)'''
        if (event == 0):
            if (this in p1.powerups):
                p1.powerups.remove(this)
                this.burst()
            len = (params.radius + p1.radius) - distance(p1.pos, params.pos)
            norm = normal(params.pos, p1.pos)
            p1.pos = addPoints(p1.pos, multPoint(norm, len))
            p1.vel = multPoint(norm, 3)
            p1.health = 1

    def pDraw(this, p1, maincam):
        tform = poly.circleGon(8, 20)
        tform.color = (0, 100, 255)
        tform.angle = p1.angle
        tform.pos = p1.pos
        tform.thickness = 3
        maincam.toDraw(tform)

    def burst(this, particles, p1):
        for i in range(15):
            part = particle.particle(this.pos, p1.vel, (0, 200, 255), 3)
            off = randCirc(10)
            part.vel = addPoints(part.vel, off)
            part.damping = 0.95
            particle.particle.life = 100
            part.pos = addPoints(p1.pos, off * 3)
            particles.append(part)