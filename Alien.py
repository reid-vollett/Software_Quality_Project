import math
import os
import random
import sys
import time
import pygame
from ezmath import *
from gameFunctions import *

from Enemy import enemy
from Poly import poly
from Particle import particle
from EnemyBullet import enemyBullet

class alien(enemy):
    def __init__(this, pos, p1):
        '''initializes an alien enemy'''
        enemy.__init__(this, pos)

        this.form = poly((5, 0), (3, 3), (0, 5), (-3, 5), (-4, 3), (-1, 2), (-6, 0), (-1, -2), (-4, -3), (-3, -5), (0, -5), (3, -3))
        this.form.scale = 2
        this.health = 1
        ang = direction(subtractPoints(p1.pos, this.pos)) + randRange(1, -1)
        this.vel = multPoint(xyComponent(ang), 2.5)
        this.firedelay = 60

    def update(this):
        '''handles the logic step for the current alien instance'''
        enemy.update(this)
        this.firedelay -= 1
        if (distance(subtractPoints(this.pos, p1.pos)) < 300):
            # only fires if it is within a certain distance of the player
            if (this.firedelay <= 0):
                this.fire()

    def kill(this, sounds, particles):
        '''kills the alien instance'''
        enemy.kill(this)
        sounds[10].play()
        global score
        getPoints(100)  # adds points to the player's score
        for i in range(10):
            # releases some particles to make frags more satisfying
            off = randPoint(5)
            part = particle(addPoints(this.pos, off), addPoints(this.vel, off), (255, 0, 0), 3)
            part.life = randRange(10, 25)
            if (randChance(50)):
                part.color = (150, 0, 0)
            particles.append(part)

    def fire(this, sounds, projectiles):
        '''fires a projectile at the player'''
        # resets the fire delay to a second so it doesn't fire a large amount of projectiles
        this.firedelay = 60
        sounds[15].play()
        # initializes a projectile but makes it so the alien doesn't have perfect accuracy
        proj = enemyBullet(this.pos, direction(subtractPoints(p1.pos, this.pos)) + randRange(-.3, .3), 4)
        projectiles.append(proj)
        # the alien turns in a random direction when it fires
        ang = direction(this.vel)
        mag = distance(this.vel)
        ang += randRange(1, -1)
        this.vel = multPoint(xyComponent(ang), mag)

    def draw(this, maincam):
        '''renders the alien'''
        this.form.pos = this.pos
        this.form.angle = direction(this.vel)
        this.form.fill = (100, 0, 0)
        this.form.thickness = 2
        this.form.color = (255, 0, 0)
        maincam.toDraw(this.form)