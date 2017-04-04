#Projectile class
import math
import os
import random
import sys
import time
import pygame
from ezmath import *

import particle
from Enemy import enemy
from Asteroid import asteroid



class projectile:
    def __init__(this, friendly, pos=(0, 0), aim=0, spd=10):
        '''initializes a projectile instance'''
        this.cck = False
        this.pos = pos
        this.vel = multPoint(xyComponent(aim), spd)
        this.radius = 10
        this.life = 100
        this.friendly = friendly
        this.damage = 1
        this.color = (255, 255, 0)
        this.thickness = 2
        this.form = None

    def update(this):
        '''handles the projectile update logic of the current instance'''
        this.cck = False
        this.pos = addPoints(this.pos, this.vel)
        this.life -= 1
        if (this.friendly):
            0
            # this.checkEnemyCollisions()
            # this.checkBogeyBulletCollisions()

    def removeCheck(this, projectiles):
        '''removes the projectile if it's time is up'''
        if (this.life <= 0):
            if (this in projectiles):
                projectiles.remove(this)

    def checkBogeyBulletCollisions(this, projectiles):
        '''handles collisions with enemy projectiles'''
        for bul in projectiles:
            if (bul.friendly):
                continue  # skips this instance if does not need to check collision
            if (collision(this, bul)):
                this.burst()
                projectiles.remove(bul)
                if (this in projectiles):
                    this.life = 0

    def checkEnemyCollisions(this, enemies):
        '''checks for collisions with enemies'''
        for en in enemies:
            if (collision(this, en)):
                this.hit(en)

    def checkAsteroidCollisions(this, enemies):
        '''checks for collisions only with asteriod objects, used for enemy bullets colliding with asteroids'''
        for ast in enemies:
            if (not type(ast) is asteroid):
                continue  # skips the instance if it is not an asteroid
            if (collision(ast, this)):
                this.hit(ast)

    def hit(this, en):
        if (not this.friendly):
            if (baseIs(en, projectile)):
                if (this.friendly == en.friendly):
                    return
                en.hit(this)
            else:
                return
        this.life = 0
        this.burst()
        if (baseIs(en, enemy)):
            this.enHit(en)

    def enHit(this, en):
        '''hits a specified enemy'''
        # damages the enemy instance it collides with
        if (en.dead()):
            return
        en.health -= this.damage
        if (en.health <= 0):
            en.kill()

    def burst(this, sounds, particles):
        '''the visual effect of the projectile's collision'''
        if (this.damage >= 1):
            sounds[12].play()
        else:
            sounds[14].play()
        for i in range(random.randrange(4, 8)):
            # add some pretty particles
            part = particle.particle(this.pos, randPoint(5), (255, 255, 0))
            part.damping = 0.9
            particles.append(part)

    def draw(this, poly, maincam, p1):
        '''adds the projectile to the main drawQuery'''
        if (this.form == None):
            # creates a temporary form to render if it has no previously defined form
            tform = poly()
            tform.color = this.color
            tform.thickness = this.thickness
            tform.verts = [(0, 0), (distance(subtractPoints(this.vel, p1.vel)), 0)]
            tform.pos = this.pos
            tform.angle = direction(subtractPoints(this.vel, p1.vel))
            maincam.toDraw(tform)
            return
        this.form.pos = this.pos
        this.form.angle = direction(this.vel)
        maincam.toDraw(this.form)

    def dead(this):
        return this.life <= 0