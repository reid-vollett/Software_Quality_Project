#Particle Class
import GlobalVariables
from ezmath import *


class particle:
    def __init__(this, pos, vel, color=(255, 255, 0), thickness=2):
        '''initializes a particle instance'''
        this.pos = pos
        this.vel = vel
        this.radius = 0
        this.color = color
        this.life = 10
        this.thickness = thickness
        this.damping = 1

    def update(this):
        '''handles logic for a particle instance'''
        if (this.life <= 0 or distance(GlobalVariables.p1.pos, this.pos) > 500):
            GlobalVariables.particles.remove(this)
            return

        this.vel = multPoint(this.vel, this.damping)
        this.pos = addPoints(this.pos, this.vel)
        this.life -= 1

    def draw(this, poly):
        '''handles rendering for a particle instance'''
        # particles are rendered as a line whose length is dependent upon their speed
        length = (distance(this.vel))
        # kills the particle if it is less than a pixel long
        if (length < 1):
            life = 0
        # tform is the temporary form the particle takes during renduring to give the camera an object to render
        tform = poly((0, 0), (length, 0))
        tform.pos = this.pos
        tform.angle = direction(this.vel)
        tform.color = this.color
        tform.thickness = this.thickness
        GlobalVariables.maincam.toDraw(tform)
