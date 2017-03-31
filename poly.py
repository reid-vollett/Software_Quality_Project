import math
import os
import random
import sys
import time
import pygame
from ezmath import *

import shape as shape


class poly(shape):
    def __init__(this, *verts):
        '''initializes a poly object, basically polygon data that is given to the camera'''
        shape.__init__(this)
        this.verts = list()
        for v in verts:
            this.verts.append(v)

    def getAbsVerts(this):
        '''gets the world position of the poly's vertices'''
        result = list()
        for vert in this.verts:
            av = multPoint(vert, this.scale)
            result.append(transform(av, this.pos, this.angle))
        return result

    def draw(this, cam):
        '''adds the poly to the camera's draw query'''
        cam.toDraw(this)

    def circleGon(points, radius):
        '''returns a circular polygon with specified amount of points'''
        form = poly()
        form.scale = radius
        for i in range(points):
            form.verts.append(xyComponent((math.pi * 2) * (i / points)))
        return form