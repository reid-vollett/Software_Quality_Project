import math
import os
import random
import sys
import time
import pygame
from ezmath import *

# the enemy base class for all enemy type objects
class enemy:
    def __init__(this, pos):
        '''initializes an enemy object'''
        this.cck = False
        this.pos = pos
        this.vel = (0, 0)
        this.health = 1
        this.radius = 10

    def kill(this):
        '''kills the enemy instance'''
        this.itemDrop()  # handles dropping powerups
        this.health = None  # removes the enemy from the world

    def itemDrop(this):
        '''has a chance to drop an item'''
        if (len(items) > 1):
            return
        if (not randChance(5)):
            # 95% of the time nothing is dropped
            return
        # ~1 in every 20 kills an item is dropped
        power = item.randItem(this.pos)
        items.append(power)

    def update(this):
        '''handles the logic step for the current enemy instance'''
        if (this.health == None):
            return
        this.cck = False
        this.pos = addPoints(this.pos, this.vel)

    def draw(this):
        '''default rendering for an enemy base type is to not render anything'''
        0

    def hit(this, ob):
        if (baseIs(ob, projectile)):
            this.projHit(ob)

    def projHit(this, proj):
        proj.hit(this)

    def dead(this):
        return this.health == None
